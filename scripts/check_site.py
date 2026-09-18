# -*- coding: utf-8 -*-
"""站点交付指标：解析 index.html 输出结构化 JSON 指标 + 全页快照 + HTML 配平校验。

产物（沿用既有迭代工作流）：
  docs/iterations/roundN-index-snapshot.html   当轮全页快照
  docs/iterations/roundN.json                  当轮量化指标

用法：
  python scripts/check_site.py            # 自动取下一个 round 编号
  python scripts/check_site.py --round 4  # 指定编号
仅依赖标准库。
"""
import argparse
import json
import os
import re
import shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ITER_DIR = os.path.join(ROOT, "docs", "iterations")
INDEX = os.path.join(ROOT, "index.html")

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
        "meta", "param", "source", "track", "wbr"}
TAG_RE = re.compile(r"<(/?)([a-zA-Z][a-zA-Z0-9-]*)([^>]*?)(/?)>")


def strip_inner(doc):
    """去掉 script/style 的内部内容，避免 JS/CSS 干扰标签配平。"""
    doc = re.sub(r"(<script\b[^>]*>).*?(</script>)", r"\1\2", doc, flags=re.S | re.I)
    doc = re.sub(r"(<style\b[^>]*>).*?(</style>)", r"\1\2", doc, flags=re.S | re.I)
    return doc


def tag_balance_errors(doc):
    doc = strip_inner(doc)
    stack, errors = [], []
    for mt in TAG_RE.finditer(doc):
        close, name, attrs, selfclose = mt.groups()
        name = name.lower()
        if name in VOID or selfclose:
            continue
        if close:
            if not stack:
                errors.append("stray </%s>@%d" % (name, mt.start()))
            elif stack[-1] != name:
                errors.append("mismatch: expect </%s> got </%s>@%d" % (stack[-1], name, mt.start()))
                stack.pop()
            else:
                stack.pop()
        else:
            stack.append(name)
    for name in stack:
        errors.append("unclosed <%s>" % name)
    return errors


def count(pat, doc, flags=0):
    return len(re.findall(pat, doc, flags))


def metrics(doc):
    css = re.search(r"<style>(.*?)</style>", doc, re.S)
    js = re.findall(r"<script>(.*?)</script>", doc, re.S)
    body = strip_inner(doc)  # 计 DOM 类指标时排除脚本/样式内部
    head = doc[:doc.find("</head>")]
    css_b = len(css.group(1).encode("utf-8")) if css else 0
    js_b = sum(len(b.encode("utf-8")) for b in js)
    errs = tag_balance_errors(doc)
    m = {
        "bytes": len(doc.encode("utf-8")),
        "lang_attr": '<html lang="zh-CN">' in doc,
        "meta_description": 'name="description"' in doc,
        "viewport_meta": 'name="viewport"' in doc,
        "charset_first": doc.find('charset="utf-8"') > -1 and doc.find('charset="utf-8"') < doc.find("<title>"),
        "og_tags": count(r'property="og:', doc),
        "og_image_png": 'property="og:image" content="https://fanquanpp.github.io/slide-forge/assets/previews/og-cover.png"' in doc,
        "og_image_dims": 'property="og:image:width"' in doc and 'property="og:image:height"' in doc,
        "twitter_card": 'name="twitter:card"' in doc,
        "canonical": 'rel="canonical"' in doc,
        "jsonld": count(r'application/ld\+json', doc),
        "jsonld_itemlist": '"@type":"ItemList"' in doc,
        "favicon": 'rel="icon"' in doc,
        "theme_color": 'name="theme-color"' in doc,
        "theme_color_dark": bool(re.search(r'name="theme-color"[^>]*media="\(prefers-color-scheme: dark\)"', doc)),
        "robots_meta": 'name="robots"' in doc,
        "skip_link": "skip-link" in doc,
        "main_landmark": "<main" in doc,
        "nav_landmark": "<nav" in doc,
        "footer_landmark": "<footer" in doc,
        "h1_count": count(r"<h1[\s>]", body),
        "h2_count": count(r"<h2[\s>]", body),
        "img_total": count(r"<img\b", body),
        "img_lazy": count(r'loading="lazy"', body),
        "img_eager": count(r'loading="eager"', body),
        "img_fetchpriority": count(r"fetchpriority=", body),
        "img_decoding": count(r"decoding=", body),
        "img_dims": count(r"<img[^>]*width=", body),
        "img_alt": count(r"<img[^>]*alt=", body),
        "aria_labels": count(r"aria-label=", body),
        "aria_pressed_chips": count(r'aria-pressed="(?:true|false)"', body),
        "search_input": 'type="search"' in doc,
        "search_dataq": 'data-q="' in body,
        "search_debounce": "setTimeout" in doc,
        "url_state_js": "pushState" in doc and "popstate" in doc,
        "empty_state": 'id="empty"' in doc,
        "empty_reset": 'id="empty-reset"' in doc,
        "focus_visible_css": ":focus-visible" in doc,
        "prefers_reduced_motion": "prefers-reduced-motion" in doc,
        "prefers_color_scheme": "prefers-color-scheme" in doc,
        "print_css": "@media print" in doc,
        "content_visibility_css": "content-visibility" in doc,
        "card_count": count(r'class="card"', body),
        "chip_count": count(r'class="chip', body),
        "dialog_landmark": "<dialog" in doc,
        "dialog_aria_modal": 'aria-modal="true"' in doc,
        # True = 反模式仍在（APG：option 内不得含交互按钮）；匹配渲染值与 JS setAttribute 两种形态
        "listbox_misuse": 'role="option"' in doc or "'role', 'option'" in doc,
        "thumb_aria_group": 'id="pv-thumbs" role="group"' in body,
        "aria_live_status": 'id="pv-status"' in body,
        "swipe_js": "pointerdown" in doc,
        "home_end_keys": "'Home'" in doc,
        "defer_or_async_script": False,  # 内联脚本为刻意选择（首屏无额外请求），保留键位做连续对比
        "svg_inline": bool(re.search(r"<body[^>]*>[^<]*<svg", body)),
        "html_valid": not errs,
        "html_errors": errs,
        "css_bytes": css_b,
        "js_bytes": js_b,
    }
    return m


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--round", type=int, default=0, help="round 编号（默认自动递增）")
    args = ap.parse_args()

    with open(INDEX, encoding="utf-8") as f:
        doc = f.read()
    m = metrics(doc)

    os.makedirs(ITER_DIR, exist_ok=True)
    rnd = args.round
    if not rnd:
        existing = [int(x[5:-5]) for x in os.listdir(ITER_DIR)
                    if re.fullmatch(r"round\d+\.json", x)]
        rnd = max(existing) + 1 if existing else 0

    out_json = os.path.join(ITER_DIR, "round%d.json" % rnd)
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(m, f, ensure_ascii=False, indent=1)
    shutil.copyfile(INDEX, os.path.join(ITER_DIR, "round%d-index-snapshot.html" % rnd))

    # 与上一轮对比
    prev_path = os.path.join(ITER_DIR, "round%d.json" % (rnd - 1))
    lines = ["round %d  bytes=%d  html_valid=%s" % (rnd, m["bytes"], m["html_valid"])]
    if m["html_errors"]:
        lines += ["  ERRORS: " + "; ".join(m["html_errors"][:8])]
    if os.path.exists(prev_path):
        with open(prev_path, encoding="utf-8") as f:
            prev = json.load(f)
        lines.append("changed vs round%d:" % (rnd - 1))
        for k in m:
            if k in prev and prev[k] != m[k] and k not in ("html_errors",):
                lines.append("  %-24s %s -> %s" % (k, prev[k], m[k]))
    print("\n".join(lines))


if __name__ == "__main__":
    main()
