# -*- coding: utf-8 -*-
"""从 templates/index.manifest.json + scripts/site/ 前端源码生成 GitHub Pages 站点。

产出：
  index.html                     自包含浏览页（分类筛选 + 搜索 + URL 状态 + 预览灯箱 + 下载）
  assets/previews/<style>-*.svg  每种设计风格的矢量预览缩略图

结构：
  scripts/site/page.html   页面骨架（__TOKEN__ 占位符）
  scripts/site/style.css   全部样式（构建期内联）
  scripts/site/app.js      全部脚本（构建期内联）
  scripts/build_site.py    数据装配器：manifest → 卡片/筛选/风格卡 HTML → token 注入

用法：python scripts/build_site.py
"""
import os, sys, json, html, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "generator"))
from themes import THEMES  # noqa

SITE_DIR = os.path.join(ROOT, "scripts", "site")
REPO_URL = "https://github.com/fanquanpp/slide-forge"
SITE_URL = "https://fanquanpp.github.io/slide-forge/"
REPO_BLOB = REPO_URL + "/blob/main/"
PREVIEW_SVG = ('<svg viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" '
               'style="vertical-align:-2px;margin-right:5px" fill="currentColor">'
               '<path d="M8 5.5v13l11-6.5z"/></svg>')
EAGER_FIRST_N = 3  # 首屏前 N 张卡片图 eager + fetchpriority=high（web.dev：LCP 图不得懒加载）


def load_manifest():
    with open(os.path.join(ROOT, "templates", "index.manifest.json"), encoding="utf-8") as f:
        return json.load(f)


def read_site_asset(name):
    with open(os.path.join(SITE_DIR, name), encoding="utf-8") as f:
        return f.read()


# ---------------------------------------------------------------- 预览 SVG
def svg_preview(style, variant="cover"):
    t = THEMES[style]
    bg, ink, ink2, ac, ac2 = t["bg"], t["ink"], t["ink2"], t["accent"], t["accent2"]
    s = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 360" width="640" height="360">']
    s.append('<rect width="640" height="360" rx="10" fill="#%s"/>' % bg)
    if variant == "cover":
        if t.get("decor") in ("glow", "glass"):
            s.append('<circle cx="540" cy="60" r="150" fill="#%s" opacity="0.20"/>' % ac)
        s.append('<rect x="56" y="150" width="70" height="8" rx="4" fill="#%s"/>' % ac)
        s.append('<rect x="56" y="176" width="330" height="26" rx="6" fill="#%s"/>' % ink)
        s.append('<rect x="56" y="212" width="250" height="14" rx="5" fill="#%s" opacity="0.55"/>' % ink2)
        s.append('<rect x="56" y="292" width="150" height="9" rx="4" fill="#%s" opacity="0.5"/>' % ink2)
    elif variant == "content":
        s.append('<rect x="56" y="46" width="120" height="8" rx="4" fill="#%s"/>' % ac)
        s.append('<rect x="56" y="66" width="280" height="20" rx="6" fill="#%s"/>' % ink)
        s.append('<rect x="56" y="96" width="60" height="6" rx="3" fill="#%s"/>' % ac)
        for i in range(4):
            s.append('<circle cx="66" cy="%d" r="5" fill="#%s"/>' % (140 + i * 34, ac))
            s.append('<rect x="84" y="%d" width="%d" height="12" rx="4" fill="#%s" opacity="0.7"/>'
                     % (134 + i * 34, 330 - i * 30, ink))
        s.append('<rect x="430" y="120" width="156" height="150" rx="12" fill="#%s" opacity="0.35"/>' % ac)
    else:  # data
        s.append('<rect x="56" y="46" width="120" height="8" rx="4" fill="#%s"/>' % ac)
        s.append('<rect x="56" y="66" width="220" height="20" rx="6" fill="#%s"/>' % ink)
        cw = 132
        for i in range(4):
            x = 56 + i * (cw + 14)
            s.append('<rect x="%d" y="120" width="%d" height="120" rx="12" fill="#%s" opacity="0.10"/>' % (x, cw, ink))
            s.append('<rect x="%d" y="146" width="46" height="26" rx="6" fill="#%s"/>' % (x + 16, ac if i % 2 == 0 else ac2))
            s.append('<rect x="%d" y="186" width="80" height="10" rx="4" fill="#%s" opacity="0.7"/>' % (x + 16, ink))
            s.append('<rect x="%d" y="204" width="60" height="8" rx="4" fill="#%s" opacity="0.4"/>' % (x + 16, ink2))
    s.append("</svg>")
    return "\n".join(s)


def write_previews():
    out = os.path.join(ROOT, "assets", "previews")
    os.makedirs(out, exist_ok=True)
    n = 0
    for style in THEMES:
        for v in ("cover", "content", "data"):
            with open(os.path.join(out, "%s-%s.svg" % (style, v)), "w", encoding="utf-8") as f:
                f.write(svg_preview(style, v))
            n += 1
    return n


# ---------------------------------------------------------------- 数据装配
def esc(s):
    return html.escape(s, quote=True)


def search_haystack(cat, deck, theme):
    """构建期预算的检索串（页面上不展示，供前端 data-q 使用，写入时统一小写）。"""
    parts = [cat["name"], cat["en"], cat["id"], theme["label"], theme["en"],
             deck["style"], deck["id"], os.path.basename(deck["file"])]
    return " ".join(parts).lower()


def build_cards(m):
    themes = m["themes"]
    potx_by_style = {p["style"]: p["file"] for p in m.get("potx", [])}
    cards = []
    idx = 0
    for cat in m["categories"]:
        for dk in cat["decks"]:
            style = dk["style"]
            f = dk["file"]
            idx += 1
            eager = idx <= EAGER_FIRST_N
            loading = 'loading="eager" fetchpriority="high"' if eager else 'loading="lazy"'
            img = ('<img %s decoding="async" width="640" height="360" '
                   'src="assets/previews/%s-cover.svg" alt="%s %s 预览">'
                   % (loading, style, esc(cat["name"]), esc(themes[style]["label"])))
            hot = ('<button type="button" class="pv-btn" aria-label="放大预览 %s">'
                   '<span class="pv-chip">%s 预览 %d 页</span></button>'
                   % (esc(cat["name"] + " · " + themes[style]["label"]), PREVIEW_SVG, dk["slides"]))
            links = ['<a class="btn primary" href="templates/%s" download>下载 .pptx</a>' % f]
            if potx_by_style.get(style):
                links.append('<a class="btn" href="templates/%s" download>.potx 母版</a>' % potx_by_style[style])
            links.append('<a class="btn" href="%s" target="_blank" rel="noopener">GitHub 源码</a>'
                         % (REPO_BLOB + "templates/" + f))
            body = ('<div class="body"><div class="cat">%s</div><div class="name">%s</div>'
                    '<div class="meta">%s · %d 个版面</div><div class="links">%s</div></div>'
                    % (esc(cat["name"]), esc(themes[style]["label"]), esc(cat["en"]), dk["slides"],
                       "".join(links)))
            cards.append('<article class="card" data-cat="%s" data-file="%s" data-slides="%d" data-style="%s" data-q="%s">%s%s</article>'
                         % (esc(cat["id"]), esc(f), dk["slides"], style,
                            esc(search_haystack(cat, dk, themes[style])), img, hot + body))
    return cards


def build_chips(m):
    chips = ['<button type="button" class="chip on" data-cat="all" aria-pressed="true">全部 %d 套</button>'
             % m["stats"]["decks"]]
    for cat in m["categories"]:
        chips.append('<button type="button" class="chip" data-cat="%s" aria-pressed="false">%s</button>'
                     % (esc(cat["id"]), esc(cat["name"])))
    return chips


def build_tcards(m):
    tcards = []
    for k, v in m["themes"].items():
        s = THEMES[k]
        sw = "".join('<i style="background:#%s"></i>' % c for c in (s["bg"], s["accent"], s["accent2"], s["ink"]))
        tcards.append('<div class="tcard"><div class="sw">%s</div><b>%s</b><small>%s · %s</small><em>%s</em></div>'
                      % (sw, esc(v["label"]), esc(v["en"]), esc(v["preset"]), esc(v["philosophy"])))
    return tcards


def build_jsonld(m):
    def dump(data):
        # JSON 内联进 <script> 时转义 "</"，防止提前闭合脚本标签
        return json.dumps(data, ensure_ascii=False).replace("</", "<\\/")

    blocks = [dump({
        "@context": "https://schema.org",
        "@type": "SoftwareSourceCode",
        "name": "SlideForge",
        "description": "多用途、多风格、可编辑且不含正式内容的 PPT 模板库",
        "url": SITE_URL,
        "codeRepository": REPO_URL,
        "license": "https://opensource.org/licenses/MIT",
        "programmingLanguage": "Python",
        "keywords": "pptx, powerpoint, templates, python-pptx, design",
        "author": {"@type": "Organization", "name": "SlideForge Contributors"},
    })]

    # 列表页结构化数据：全量 126 项（Google：汇总页应完整列出用户可见条目）
    items = []
    pos = 0
    for cat in m["categories"]:
        for dk in cat["decks"]:
            pos += 1
            items.append({
                "@type": "ListItem",
                "position": pos,
                "name": "%s · %s" % (cat["name"], m["themes"][dk["style"]]["label"]),
                "url": SITE_URL + "templates/" + dk["file"],
            })
    blocks.append(dump({
        "@context": "https://schema.org",
        "@type": "ItemList",
        "name": "SlideForge 模板库",
        "numberOfItems": pos,
        "itemListElement": items,
    }))

    return "\n".join('<script type="application/ld+json">\n%s\n</script>' % b for b in blocks)


def write_og_cover(path, decks, themes, cats):
    """1200×630 OG 封面 PNG（svg 作 og:image 在多数平台不生效）。Pillow 缺失时跳过。"""
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        return False
    W, H = 1200, 630
    BG, CARD, INK, SUB, AC = "#10141d", "#171d2a", "#e8ecf3", "#9aa7cc", "#2f6bff"

    def font(names, size):
        for n in names:
            for p in (os.path.join(os.environ.get("WINDIR", r"C:\Windows"), "Fonts", n), n):
                try:
                    return ImageFont.truetype(p, size)
                except Exception:
                    pass
        return ImageFont.load_default()

    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W, 10], fill=AC)
    # 右侧三张「幻灯片」示意卡
    for ox, oy, w in [(760, 150, 360), (830, 265, 330), (900, 380, 300)]:
        d.rounded_rectangle([ox, oy, ox + w, oy + 150], 16, fill=CARD, outline="#2a3556", width=2)
        d.rounded_rectangle([ox + 24, oy + 28, ox + 90, oy + 38], 5, fill=AC)
        d.rounded_rectangle([ox + 24, oy + 56, ox + w - 60, oy + 76], 7, fill="#3a4666")
        d.rounded_rectangle([ox + 24, oy + 92, ox + w - 120, oy + 106], 6, fill="#2a3556")
    t1 = font(["msyhbd.ttc", "msyh.ttc", "arialbd.ttf"], 88)
    t2 = font(["msyh.ttc", "arialbd.ttf"], 40)
    t3 = font(["msyh.ttc", "arial.ttf"], 30)
    d.text((80, 150), "SlideForge", font=t1, fill=INK)
    d.rounded_rectangle([80, 268, 92, 330], 4, fill=AC)
    d.text((112, 272), "%d 套可编辑 PPT 模板库" % decks, font=t2, fill=INK)
    d.text((80, 380), "%d 种设计风格 · %d 个用途分类 · python-pptx 生成" % (themes, cats), font=t3, fill=SUB)
    d.text((80, 440), "MIT License · 多用途 · 可编辑 · 不含正式内容", font=t3, fill=SUB)
    img.save(path, "PNG", optimize=True)
    return True


# ---------------------------------------------------------------- 渲染
TOKEN_RE = re.compile(r"__[A-Z][A-Z0-9_]+__")


def render_page(tokens):
    doc = read_site_asset("page.html")
    for k, v in tokens.items():
        doc = doc.replace("__%s__" % k, v)
    leftover = sorted(set(TOKEN_RE.findall(doc)))
    if leftover:
        raise SystemExit("build_site: 未替换的 token：%s" % ", ".join(leftover))
    return doc


def main():
    m = load_manifest()
    n = write_previews()
    og = write_og_cover(os.path.join(ROOT, "assets", "previews", "og-cover.png"),
                        m["stats"]["decks"], m["stats"]["themes"], m["stats"]["categories"])
    st = m["stats"]

    title = "SlideForge · 多用途可编辑 PPT 模板库"
    desc = "SlideForge —— %d 套多用途、多风格、可编辑且不含正式内容的 PPT 模板库，MIT 协议。" % st["decks"]
    doc = render_page({
        "TITLE": esc(title),
        "DESC": esc(desc),
        "OGDESC": esc("%d 套多用途、多风格、可编辑且不含正式内容的 PPT 模板库（MIT）。" % st["decks"]),
        "SITE": SITE_URL,
        "REPO": REPO_URL,
        "JSONLD": build_jsonld(m),
        "CSS": read_site_asset("style.css"),
        "JS": read_site_asset("app.js"),
        "DECKS": str(st["decks"]),
        "SLIDES": str(st["slides_total"]),
        "THEMES": str(st["themes"]),
        "CATS": str(st["categories"]),
        "POTX": str(st["potx"]),
        "CHIPS": "".join(build_chips(m)),
        "CARDS": "".join(build_cards(m)),
        "TCARDS": "".join(build_tcards(m)),
        "CATTAGS": "".join('<span class="tag">%s</span>' % esc(c["name"]) for c in m["categories"]),
    })
    with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
        f.write(doc)
    print("OK site: index.html (%d bytes) + %d previews%s"
          % (len(doc.encode("utf-8")), n, " + og-cover.png" if og else " (og-cover 未生成：无 Pillow)"))


if __name__ == "__main__":
    main()
