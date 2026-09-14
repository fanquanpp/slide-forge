# -*- coding: utf-8 -*-
"""从 templates/index.manifest.json + generator/themes.py 生成 GitHub Pages 站点与风格预览图。

产出：
  index.html                     自包含浏览页（分类筛选 + 风格速览 + 下载）
  assets/previews/<style>-*.svg  每种设计风格的矢量预览缩略图
用法：python scripts/build_site.py
"""
import os, sys, json, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "generator"))
from themes import THEMES  # noqa

REPO_URL = "https://github.com/fanquanpp/slide-forge"
SITE_URL = "https://fanquanpp.github.io/slide-forge/"
REPO_BLOB = REPO_URL + "/blob/main/"
PREVIEW_SVG = ('<svg viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" '
               'style="vertical-align:-2px;margin-right:5px" fill="currentColor">'
               '<path d="M8 5.5v13l11-6.5z"/></svg>')


def load_manifest():
    with open(os.path.join(ROOT, "templates", "index.manifest.json"), encoding="utf-8") as f:
        return json.load(f)


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


CSS = """
*{box-sizing:border-box;margin:0;padding:0}
:root{--ink:#14161a;--ink2:#6b7280;--line:#e7e9ee;--bg:#fbfbfa;--accent:#2f6bff;--card:#fff}
html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--ink);font:15px/1.6 "Segoe UI","Microsoft YaHei",system-ui,sans-serif;-webkit-font-smoothing:antialiased}
a{color:inherit;text-decoration:none}
.wrap{max-width:1180px;margin:0 auto;padding:0 28px}
header.top{position:sticky;top:0;z-index:20;background:rgba(251,251,250,.86);backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}
.top .wrap{display:flex;align-items:center;justify-content:space-between;height:62px}
.brand{display:flex;align-items:center;gap:10px;font-weight:700;letter-spacing:.2px}
.mark{width:26px;height:26px;border-radius:7px;background:var(--accent);display:inline-flex;align-items:center;justify-content:center;color:#fff;font-size:13px;font-weight:800}
.top nav a{color:var(--ink2);font-size:14px;margin-left:22px}
.top nav a:hover{color:var(--accent)}
.hero{padding:74px 0 34px;border-bottom:1px solid var(--line)}
.hero h1{font-size:38px;font-weight:800;letter-spacing:-.4px;max-width:820px;line-height:1.18}
.hero p.lead{margin-top:16px;color:var(--ink2);max-width:720px;font-size:16px}
.metrics{display:grid;grid-template-columns:repeat(5,1fr);gap:14px;margin-top:34px}
.metric{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:18px 18px}
.metric b{display:block;font-size:27px;font-weight:800;letter-spacing:-.5px}
.metric span{color:var(--ink2);font-size:12.5px}
section{padding:54px 0;border-bottom:1px solid var(--line)}
h2.sec{font-size:23px;font-weight:750;letter-spacing:-.2px}
p.sub{color:var(--ink2);margin-top:8px;max-width:760px}
.filters{display:flex;flex-wrap:wrap;gap:9px;margin:26px 0 8px}
.chip{border:1px solid var(--line);background:var(--card);border-radius:999px;padding:7px 15px;font-size:13px;cursor:pointer;color:var(--ink2)}
.chip.on{background:var(--ink);color:#fff;border-color:var(--ink)}
.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:26px}
.card{background:var(--card);border:1px solid var(--line);border-radius:16px;overflow:hidden;display:flex;flex-direction:column;transition:transform .15s,box-shadow .15s}
.card:hover{transform:translateY(-3px);box-shadow:0 10px 30px rgba(20,22,26,.08)}
.card img{width:100%;display:block;background:#eef0f4}
.card .body{padding:15px 16px 16px;display:flex;flex-direction:column;gap:8px;flex:1}
.card .cat{font-size:11.5px;color:var(--accent);font-weight:700;letter-spacing:.4px;text-transform:uppercase}
.card .name{font-weight:700;font-size:15.5px}
.card .meta{color:var(--ink2);font-size:12.5px}
.card .links{margin-top:auto;display:flex;gap:8px;flex-wrap:wrap}
.btn{border:1px solid var(--line);border-radius:9px;padding:6px 12px;font-size:12.5px;color:var(--ink);background:#fff}
.btn.primary{background:var(--accent);border-color:var(--accent);color:#fff}
.btn:hover{border-color:var(--accent)}
.themegrid{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:26px}
.tcard{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:16px}
.tcard .sw{display:flex;gap:6px;margin-bottom:12px}
.tcard .sw i{width:22px;height:22px;border-radius:6px;display:block;border:1px solid rgba(0,0,0,.06)}
.tcard b{font-size:14.5px}
.tcard small{display:block;color:var(--ink2);font-size:12px;margin-top:3px}
.tcard em{display:block;color:var(--ink2);font-size:12px;font-style:normal;margin-top:8px;line-height:1.5}
.usegrid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:26px}
.ubox{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:20px}
.ubox h3{font-size:15px;margin-bottom:8px}
.ubox p,.ubox li{color:var(--ink2);font-size:13.5px}
.ubox ol{margin-left:18px;display:flex;flex-direction:column;gap:6px}
pre{background:#14161a;color:#e8ecf3;border-radius:12px;padding:16px 18px;overflow:auto;font:12.5px/1.6 Consolas,monospace;margin-top:14px}
footer{padding:40px 0 60px;color:var(--ink2);font-size:13px}
footer a{color:var(--accent)}
.tag{display:inline-block;border:1px solid var(--line);border-radius:999px;padding:3px 10px;font-size:11.5px;color:var(--ink2);margin:0 6px 6px 0}
@media(max-width:900px){.metrics{grid-template-columns:repeat(2,1fr)}.grid{grid-template-columns:1fr 1fr}.themegrid{grid-template-columns:1fr 1fr}.usegrid{grid-template-columns:1fr}.hero h1{font-size:30px}}
@media(max-width:600px){.grid,.themegrid{grid-template-columns:1fr}}
@media(prefers-color-scheme:dark){
:root{--ink:#e8ecf3;--ink2:#9aa7cc;--line:#2a3556;--bg:#10141d;--card:#171d2a;--accent:#7cc4ff;color-scheme:dark}
body{background:var(--bg);color:var(--ink)}
header.top{background:rgba(16,20,29,.88);border-bottom-color:var(--line)}
.card,.tcard,.metric,.ubox,.btn,.searchbar input[type=search]{background:var(--card);color:var(--ink)}
.chip{background:var(--card);color:var(--ink2)}
.chip.on{background:var(--accent);color:#0b1220;border-color:var(--accent)}
pre{background:#0b0f17;color:#dbe6f5}
}
.skip-link{position:absolute;left:-9999px;top:0;background:var(--accent);color:#fff;padding:8px 14px;border-radius:0 0 8px 0;z-index:99}
.skip-link:focus{left:0}
:focus-visible{outline:2px solid var(--accent);outline-offset:2px;border-radius:4px}
.searchbar{display:flex;gap:10px;align-items:center;margin:16px 0 2px;flex-wrap:wrap}
.searchbar input[type=search]{flex:1 1 260px;max-width:440px;border:1px solid var(--line);border-radius:10px;padding:9px 14px;font:14px/1.4 inherit;background:#fff;color:inherit}
.searchbar input[type=search]:focus{border-color:var(--accent);outline:none}
.count{color:var(--ink2);font-size:13px}
.empty-state{display:none;background:var(--card);border:1px dashed var(--line);border-radius:12px;padding:26px;text-align:center;color:var(--ink2);margin-top:14px}
@media(prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important;scroll-behavior:auto!important}}
.pv-btn{position:absolute;inset:0;width:100%;height:100%;border:0;background:transparent;cursor:zoom-in;opacity:0}
.card{position:relative}
.card:hover .pv-btn,.card:focus-within .pv-btn{opacity:1}
.pv-chip{position:absolute;left:10px;bottom:10px;background:rgba(20,22,26,.82);color:#fff;border-radius:999px;padding:5px 12px;font-size:12px;display:flex;gap:6px;align-items:center;pointer-events:none}
.pv-btn:focus-visible{opacity:1;outline:2px solid var(--accent)}
dialog.lightbox{border:0;border-radius:16px;padding:0;max-width:min(1100px,94vw);width:94vw;background:var(--card);color:var(--ink)}
dialog.lightbox::backdrop{background:rgba(8,10,16,.66);backdrop-filter:blur(3px)}
.lb-head{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:14px 18px;border-bottom:1px solid var(--line)}
.lb-head b{font-size:15px}
.lb-head .x{border:1px solid var(--line);background:transparent;color:inherit;border-radius:8px;padding:6px 10px;cursor:pointer;font-size:13px}
.lb-body{display:flex;gap:14px;padding:16px 18px;flex-wrap:wrap}
.lb-main{flex:2 1 520px;min-width:300px}
.lb-main img,.lb-main svg{width:100%;height:auto;display:block;border-radius:12px;border:1px solid var(--line);background:#eef0f4}
.lb-fallback{display:none;padding:22px;border:1px dashed var(--line);border-radius:12px;color:var(--ink2);font-size:13.5px}
.lb-thumb{flex:1 1 200px;min-width:180px;display:flex;flex-wrap:wrap;gap:8px;align-content:flex-start}
.lb-thumb button{border:1px solid var(--line);background:transparent;border-radius:8px;padding:0;cursor:pointer;overflow:hidden;width:calc(50% - 4px)}
.lb-thumb button[aria-current="true"]{outline:2px solid var(--accent)}
.lb-thumb img{width:100%;height:auto;display:block}
.lb-meta{padding:0 18px 18px;color:var(--ink2);font-size:13px;display:flex;gap:14px;flex-wrap:wrap}
.lb-nav{display:flex;gap:8px;padding:0 18px 18px;flex-wrap:wrap}
.lb-nav button{border:1px solid var(--line);background:transparent;color:inherit;border-radius:9px;padding:7px 12px;cursor:pointer;font-size:13px}
@media(max-width:760px){.lb-thumb{flex-basis:100%}.lb-thumb button{width:calc(25% - 6px)}}
@media print{header.top,.filters,.searchbar,.chip,.btn{display:none!important}.grid{grid-template-columns:1fr 1fr}.card{break-inside:avoid}body{background:#fff;color:#000}a{color:#000;text-decoration:none}}
"""

JS = """
(function(){
  var chips=[].slice.call(document.querySelectorAll('.chip'));
  var cards=[].slice.call(document.querySelectorAll('.card'));
  var input=document.getElementById('q');
  var empty=document.getElementById('empty');
  var count=document.getElementById('count');
  var active='all';
  function apply(){
    var q=(input&&input.value||'').trim().toLowerCase();
    var shown=0;
    cards.forEach(function(card){
      var okCat=(active==='all'||card.dataset.cat===active);
      var okQ=!q||((card.textContent||'').toLowerCase().indexOf(q)>-1);
      var show=okCat&&okQ;
      card.style.display=show?'':'none';
      if(show)shown++;
    });
    if(empty)empty.style.display=shown?'none':'block';
    if(count)count.textContent=shown+' 套';
    chips.forEach(function(c){c.setAttribute('aria-pressed', c.dataset.cat===active?'true':'false');});
  }
  chips.forEach(function(c){
    c.addEventListener('click',function(){
      active=c.dataset.cat;
      chips.forEach(function(x){x.classList.remove('on');});
      c.classList.add('on');
      apply();
    });
  });
  if(input)input.addEventListener('input',apply);
  apply();
})();

/* ---------- 预览灯箱 ---------- */
(function(){
  var dlg=document.getElementById('pv');
  if(!dlg)return;
  var stage=document.getElementById('pv-stage');
  var thumbs=document.getElementById('pv-thumbs');
  var meta=document.getElementById('pv-meta');
  var title=document.getElementById('pv-title');
  var dl=document.getElementById('pv-dl');
  var fallback=document.getElementById('pv-fallback');
  var cur=0, items=[], lastFocus=null, curMeta={};
  var VARIANTS=['cover','content','data'];
  function labelOf(i){var v=VARIANTS[i%3];return v==='cover'?'封面':(v==='content'?'内容页':'数据页');}
  function render(i){
    if(!items.length)return;
    cur=(i+items.length)%items.length;
    var it=items[cur];
    stage.innerHTML='';
    var img=new Image();
    img.alt=it.name+' · '+labelOf(cur);
    img.onload=function(){fallback.style.display='none';};
    img.onerror=function(){fallback.style.display='block';};
    img.src=it.src;
    stage.appendChild(img);
    if(it.file){dl.setAttribute('href','templates/'+it.file);}
    title.textContent=it.name;
    meta.innerHTML='<span>用途：'+(curMeta.cat||'—')+'</span><span>版面：'+(curMeta.slides||'—')+' 页</span>'
      +'<span>风格：'+(curMeta.style||'—')+'</span><span>当前：'+labelOf(cur)+'</span>';
    [].slice.call(thumbs.children).forEach(function(b,k){
      b.setAttribute('aria-current', k===cur?'true':'false');
      b.setAttribute('aria-selected', k===cur?'true':'false');
    });
  }
  function open(card){
    lastFocus=document.activeElement;
    var f=card.getAttribute('data-file');
    var name=(card.querySelector('.name')||{textContent:'模板预览'}).textContent;
    var catName=(card.querySelector('.cat')||{textContent:''}).textContent;
    var styleKey=card.getAttribute('data-style')||'build';
    var slides=card.getAttribute('data-slides')||'';
    items=VARIANTS.map(function(v){return {src:'assets/previews/'+styleKey+'-'+v+'.svg',name:name,file:f};});
    curMeta={cat:catName,slides:slides,style:name};
    thumbs.innerHTML='';
    items.forEach(function(it,i){
      var b=document.createElement('button');
      b.setAttribute('role','option');
      b.innerHTML='<img src="'+it.src+'" alt="'+labelOf(i)+' 缩略图">';
      b.addEventListener('click',function(){render(i);});
      thumbs.appendChild(b);
    });
    render(0);
    try{
      if(typeof dlg.showModal==='function'){dlg.showModal();}
      else{dlg.setAttribute('open','');}
    }catch(err){dlg.setAttribute('open','');} /* 任何环境下都保证打开 */
  }
  document.addEventListener('click',function(e){
    var btn=e.target&&e.target.closest?e.target.closest('.pv-btn,.preview'):null;
    if(!btn)return;
    var card=btn.closest('.card');
    if(!card)return;
    card.setAttribute('data-style-label', (card.querySelector('.meta')||{}).textContent||'');
    var mm=(card.querySelector('.meta').textContent.split(' 个版面')[0]||'');
    open(card);
  });
  document.getElementById('pv-close').addEventListener('click',function(){try{dlg.close?dlg.close():dlg.removeAttribute('open');}catch(err){dlg.removeAttribute('open');}});
  document.getElementById('pv-prev').addEventListener('click',function(){render(cur-1);});
  document.getElementById('pv-next').addEventListener('click',function(){render(cur+1);});
  document.getElementById('pv-fs').addEventListener('click',function(){
    var el=dlg;
    if(document.fullscreenElement){document.exitFullscreen();}
    else if(el.requestFullscreen){el.requestFullscreen().catch(function(){});}
  });
  dlg.addEventListener('keydown',function(e){
    if(e.key==='ArrowLeft'){render(cur-1);}
    else if(e.key==='ArrowRight'){render(cur+1);}
  });
  dlg.addEventListener('close',function(){
    if(lastFocus&&lastFocus.focus)lastFocus.focus();
  });
})();
"""


def build_html(m):
    themes = m["themes"]
    potx_by_style = {p["style"]: p["file"] for p in m.get("potx", [])}
    st = m["stats"]

    cards = []
    for cat in m["categories"]:
        for dk in cat["decks"]:
            style = dk["style"]
            f = dk["file"]
            fname = os.path.basename(f)
            potx = potx_by_style.get(style)
            pv = ('<button class="btn preview" data-cat="%s" data-file="%s" '
                  'aria-label="预览 %s">%s预览 %d 页</button>'
                  % (html.escape(cat["id"]), f, html.escape(cat["name"] + " · " + themes[style]["label"]),
                     PREVIEW_SVG, dk["slides"]))
            links = ['<a class="btn primary" href="templates/%s" download>下载 .pptx</a>' % f,
                     pv,
                     '<a class="btn" href="%s" target="_blank" rel="noopener">GitHub 源码</a>' % (REPO_BLOB + "templates/" + f)]
            if potx:
                links.insert(2, '<a class="btn" href="templates/%s" download>.potx 母版</a>' % potx)
            cards.append(
                '<article class="card" data-cat="%s">'
                '<img loading="lazy" width="640" height="360" src="assets/previews/%s-cover.svg" alt="%s %s 预览">'
                '<div class="body"><div class="cat">%s</div><div class="name">%s</div>'
                '<div class="meta">%s · %d 个版面</div>'
                '<div class="links">%s</div></div></article>' % (
                    html.escape(cat["id"]), style, html.escape(cat["name"]), html.escape(themes[style]["label"]),
                    html.escape(cat["name"]), html.escape(themes[style]["label"]),
                    html.escape(cat["en"]), dk["slides"], "".join(links)))

    chips = ['<button class="chip on" data-cat="all">全部 %d 套</button>' % st["decks"]]
    for cat in m["categories"]:
        chips.append('<button class="chip" data-cat="%s" aria-pressed="false">%s</button>' % (html.escape(cat["id"]), html.escape(cat["name"])))

    tcards = []
    for k, v in themes.items():
        s = THEMES[k]
        sw = "".join('<i style="background:#%s"></i>' % c for c in (s["bg"], s["accent"], s["accent2"], s["ink"]))
        tcards.append('<div class="tcard"><div class="sw">%s</div><b>%s</b><small>%s · %s</small><em>%s</em></div>'
                      % (sw, html.escape(v["label"]), html.escape(v["en"]), html.escape(v["preset"]), html.escape(v["philosophy"])))

    cats = "".join('<span class="tag">%s</span>' % html.escape(c["name"]) for c in m["categories"])

    doc = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>SlideForge · 多用途可编辑 PPT 模板库</title>
<meta name="description" content="SlideForge —— 30 套多用途、多风格、可编辑且不含正式内容的 PPT 模板库，MIT 协议，可用 python-pptx 脚本一键重建。">
<style>%s</style>
</head>
<body>
<header class="top"><div class="wrap">
  <a class="brand" href="#top"><span class="mark">SF</span> SlideForge</a>
  <nav><a href="#library">模板库</a><a href="#styles">设计风格</a><a href="#usage">使用指南</a><a href="%s" target="_blank" rel="noopener">GitHub</a></nav>
</div></header>

<div id="top"></div>
<div class="hero"><div class="wrap">
  <h1>多用途 · 多风格 · 可编辑的 PPT 模板库</h1>
  <p class="lead">SlideForge 由脚本生成：覆盖 %(cats)d 个用途分类、%(themes)d 种设计风格，每套含 15 个可复用版面原型。
  全部页面只含版式骨架与占位文本，<b>不含任何正式内容</b>，可以直接替换成你自己的文案、配色与图片。</p>
  <div class="metrics">
    <div class="metric"><b>%(decks)d</b><span>套演示模板 (.pptx)</span></div>
    <div class="metric"><b>%(slides)d</b><span>个版面页</span></div>
    <div class="metric"><b>%(themes_count)d</b><span>种设计风格</span></div>
    <div class="metric"><b>%(cats)d</b><span>个用途分类</span></div>
    <div class="metric"><b>%(potx)d</b><span>套 .potx 母版</span></div>
  </div>
</div></div>

<section id="library"><div class="wrap">
  <h2 class="sec">模板库</h2>
  <p class="sub">按用途分类浏览，每个分类包含多种不同设计风格；点击即可下载可编辑的 .pptx，或跳转仓库查看源码。</p>
  <div class="filters">%(chips)s</div>
  <div class="grid">%(cards)s</div>
</div></section>

<section id="styles"><div class="wrap">
  <h2 class="sec">设计风格</h2>
  <p class="sub">每种风格是一套独立的视觉系统（配色 / 字体 / 形状语言），来自 AutoClaw 审美预设库的跨流派锚定。</p>
  <div class="themegrid">%(tcards)s</div>
</div></section>

<section id="usage"><div class="wrap">
  <h2 class="sec">使用指南</h2>
  <div class="usegrid">
    <div class="ubox"><h3>1 · 直接编辑</h3><p>下载 .pptx 用 PowerPoint / WPS / Keynote / LibreOffice 打开，文本框、形状、配色、图片位均可直接改，不破坏版式。.potx 可放入模板目录后直接「新建」。</p></div>
    <div class="ubox"><h3>2 · 换配色与字体</h3><p>每个页面的颜色都写在各形状上，批量替换主题色即可全局换肤；标题 / 正文字体分别在 <code>generator/themes.py</code> 的 <code>title_font / body_font</code> 定义。</p></div>
    <div class="ubox"><h3>3 · 重新生成</h3><ol><li><code>pip install -r generator/requirements.txt</code></li><li><code>python generator/build.py templates</code></li><li><code>python scripts/build_site.py</code></li></ol></div>
  </div>
  <pre>python generator/build.py templates     # 生成全部模版与 index.manifest.json
python generator/validate.py templates  # 校验可打开性 / 版面数 / 内容类型
python scripts/build_site.py            # 重建本站点与风格预览图</pre>
</div></section>

<section id="license"><div class="wrap">
  <h2 class="sec">许可</h2>
  <p class="sub">本项目以 <b>MIT License</b> 发布，可自由用于个人与商业用途。<br>
  模板内不含任何真实业务数据、客户信息或受版权保护的第三方素材；字体依赖系统字体，替换商用字体时请自行确认授权。</p>
  <p class="sub" style="margin-top:14px">分类：%(cats)s</p>
</div></section>

<footer><div class="wrap">
  SlideForge · 由 python-pptx 脚本生成 · MIT License · <a href="%s" target="_blank" rel="noopener">GitHub 仓库</a>
</div></footer>
<script>%(js)s</script>
</body></html>""" % dict(
        cats=st["categories"], themes=st["themes"], decks=st["decks"], slides=st["slides_total"],
        themes_count=st["themes"], potx=st["potx"], chips="".join(chips), cards="".join(cards),
        tcards="".join(tcards), js=JS, **{"chips": "".join(chips)})

    # 修正 %(cats)s 二义：上面 dict 里 cats 同时用于 badge 与数字，这里用字符串格式化后替换
    doc = doc % ()
    return doc, cats


def main():
    m = load_manifest()
    n = write_previews()
    # 手工组装（避免 % 转义问题）
    themes = m["themes"]
    st = m["stats"]
    potx_by_style = {p["style"]: p["file"] for p in m.get("potx", [])}
    cards = []
    for cat in m["categories"]:
        for dk in cat["decks"]:
            style = dk["style"]; f = dk["file"]; potx = potx_by_style.get(style)
            pv = ('<button class="btn preview" data-cat="%s" data-file="%s" '
                  'aria-label="预览 %s">%s预览 %d 页</button>'
                  % (html.escape(cat["id"]), f, html.escape(cat["name"] + " · " + themes[style]["label"]),
                     PREVIEW_SVG, dk["slides"]))
            links = ['<a class="btn primary" href="templates/%s" download>下载 .pptx</a>' % f,
                     pv,
                     '<a class="btn" href="%s" target="_blank" rel="noopener">GitHub 源码</a>' % (REPO_BLOB + "templates/" + f)]
            if potx:
                links.insert(2, '<a class="btn" href="templates/%s" download>.potx 母版</a>' % potx)
            img_tag = ('<img loading="lazy" width="640" height="360" '
                       'src="assets/previews/%s-cover.svg" alt="%s · %s 预览">'
                       % (style, html.escape(cat["name"]), html.escape(themes[style]["label"])))
            hot = ('<button class="pv-btn" data-cat="%s" data-file="%s" aria-label="放大预览 %s">'
                   '<span class="pv-chip">%s 预览 %d 页</span></button>'
                   % (html.escape(cat["id"]), html.escape(f),
                      html.escape(cat["name"] + " · " + themes[style]["label"]),
                      PREVIEW_SVG, dk["slides"]))
            meta = '<div class="meta">%s · %d 个版面</div>' % (html.escape(cat["en"]), dk["slides"])
            body = ('<div class="body"><div class="cat">%s</div><div class="name">%s</div>%s'
                    '<div class="links">%s</div></div>'
                    % (html.escape(cat["name"]), html.escape(themes[style]["label"]),
                       meta, "".join(links)))
            cards.append('<article class="card" data-cat="%s" data-file="%s" data-slides="%d" data-style="%s">%s%s</article>'
                         % (html.escape(cat["id"]), html.escape(f), dk["slides"], style, img_tag, hot + body))
    chips = ['<button class="chip on" data-cat="all">全部 %d 套</button>' % st["decks"]]
    for cat in m["categories"]:
        chips.append('<button class="chip" data-cat="%s" aria-pressed="false">%s</button>' % (html.escape(cat["id"]), html.escape(cat["name"])))
    tcards = []
    for k, v in themes.items():
        s = THEMES[k]
        sw = "".join('<i style="background:#%s"></i>' % c for c in (s["bg"], s["accent"], s["accent2"], s["ink"]))
        tcards.append('<div class="tcard"><div class="sw">%s</div><b>%s</b><small>%s · %s</small><em>%s</em></div>'
                      % (sw, html.escape(v["label"]), html.escape(v["en"]), html.escape(v["preset"]), html.escape(v["philosophy"])))
    cat_tags = "".join('<span class="tag">%s</span>' % html.escape(c["name"]) for c in m["categories"])

    doc = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>SlideForge · 多用途可编辑 PPT 模板库</title>
<meta name="description" content="SlideForge —— __DECKS__ 套多用途、多风格、可编辑且不含正式内容的 PPT 模板库，MIT 协议。">
<link rel="canonical" href="__SITE__">
<meta name="theme-color" content="#2f6bff">
<meta name="color-scheme" content="light dark">
<meta property="og:site_name" content="SlideForge">
<meta property="og:type" content="website">
<meta property="og:title" content="SlideForge · 多用途可编辑 PPT 模板库">
<meta property="og:description" content="__DECKS__ 套多用途、多风格、可编辑且不含正式内容的 PPT 模板库（MIT）。">
<meta property="og:url" content="__SITE__">
<meta property="og:image" content="__SITE__assets/previews/slideforge-styles.svg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='8' fill='%232f6bff'/%3E%3Ctext x='16' y='21' font-family='Segoe UI,sans-serif' font-size='13' font-weight='700' fill='white' text-anchor='middle'%3ESF%3C/text%3E%3C/svg%3E">
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"SoftwareSourceCode","name":"SlideForge","description":"多用途、多风格、可编辑且不含正式内容的 PPT 模板库","url":"__SITE__","codeRepository":"https://github.com/fanquanpp/slide-forge","license":"https://opensource.org/licenses/MIT","programmingLanguage":"Python","keywords":"pptx, powerpoint, templates, python-pptx, design","author":{"@type":"Organization","name":"SlideForge Contributors"}}
</script>
<style>__CSS__</style>
</head>
<body>
<a class="skip-link" href="#library">跳到模板列表</a>
<header class="top"><div class="wrap">
  <a class="brand" href="#top"><span class="mark">SF</span> SlideForge</a>
  <nav aria-label="站点导航"><a href="#library">模板库</a><a href="#styles">设计风格</a><a href="#usage">使用指南</a><a href="__REPO__" target="_blank" rel="noopener">GitHub</a></nav>
</div></header>
<main id="main">
<div id="top"></div>
<div class="hero"><div class="wrap">
  <h1>多用途 · 多风格 · 可编辑的 PPT 模板库</h1>
  <p class="lead">SlideForge 由脚本生成：覆盖 __CATS__ 个用途分类、__THEMES__ 种设计风格，每套含 15 个可复用版面原型。全部页面只含版式骨架与占位文本，<b>不含任何正式内容</b>，可直接替换成你自己的文案、配色与图片。</p>
  <div class="metrics">
    <div class="metric"><b>__DECKS__</b><span>套演示模板 (.pptx)</span></div>
    <div class="metric"><b>__SLIDES__</b><span>个版面页</span></div>
    <div class="metric"><b>__THEMES__</b><span>种设计风格</span></div>
    <div class="metric"><b>__CATS__</b><span>个用途分类</span></div>
    <div class="metric"><b>__POTX__</b><span>套 .potx 母版</span></div>
  </div>
</div></div>
<section id="library" aria-labelledby="lib-h"><div class="wrap">
  <h2 class="sec" id="lib-h">模板库</h2>
  <p class="sub">按用途分类浏览，每个分类包含多种不同设计风格；点击即可下载可编辑的 .pptx，或跳转仓库查看源码。</p>
  <div class="searchbar">
    <input type="search" id="q" placeholder="搜索模板名称 / 风格 / 用途…" aria-label="搜索模板" autocomplete="off">
    <span class="count" id="count" role="status" aria-live="polite">__DECKS__ 套</span>
  </div>
  <div class="filters" role="group" aria-label="按用途筛选模板">__CHIPS__</div>
  <div class="grid">__CARDS__</div>
  <p class="empty-state" id="empty">没有匹配的模板 —— 换个关键词，或选择「全部」再试。</p>
</div></section>
<section id="styles"><div class="wrap">
  <h2 class="sec">设计风格</h2>
  <p class="sub">每种风格是一套独立的视觉系统（配色 / 字体 / 形状语言），来自 AutoClaw 审美预设库的跨流派锚定。</p>
  <div class="themegrid">__TCARDS__</div>
</div></section>
<section id="usage"><div class="wrap">
  <h2 class="sec">使用指南</h2>
  <div class="usegrid">
    <div class="ubox"><h3>1 · 直接编辑</h3><p>下载 .pptx 用 PowerPoint / WPS / Keynote / LibreOffice 打开，文本框、形状、配色、图片位均可直接改，不破坏版式。.potx 可放入模板目录后直接「新建」。</p></div>
    <div class="ubox"><h3>2 · 换配色与字体</h3><p>页面颜色都写在各形状上，批量替换主题色即可全局换肤；标题 / 正文字体在 <code>generator/themes.py</code> 的 <code>title_font / body_font</code> 定义。</p></div>
    <div class="ubox"><h3>3 · 重新生成</h3><ol><li><code>pip install -r generator/requirements.txt</code></li><li><code>python generator/build.py templates</code></li><li><code>python scripts/build_site.py</code></li></ol></div>
  </div>
  <pre>python generator/build.py templates     # 生成全部模版与 index.manifest.json
python generator/validate.py templates  # 校验可打开性 / 版面数 / 内容类型
python scripts/build_site.py            # 重建本站点与风格预览图</pre>
</div></section>
<section id="license"><div class="wrap">
  <h2 class="sec">许可</h2>
  <p class="sub">本项目以 <b>MIT License</b> 发布，可自由用于个人与商业用途。模板内不含任何真实业务数据、客户信息或受版权保护的第三方素材；字体依赖系统字体，替换商用字体时请自行确认授权。</p>
  <p class="sub" style="margin-top:14px">分类：__CATTAGS__</p>
</div></section>
<dialog class="lightbox" id="pv" aria-labelledby="pv-title">
  <div class="lb-head"><b id="pv-title">模板预览</b>
    <div style="display:flex;gap:8px">
      <a class="btn primary" id="pv-dl" href="#" download>下载 .pptx</a>
      <button class="x" id="pv-close" autofocus>关闭 (Esc)</button>
    </div>
  </div>
  <div class="lb-body">
    <div class="lb-main"><div id="pv-stage"></div>
      <noscript><p class="lb-fallback" style="display:block">浏览器禁用了脚本：请直接在卡片上点「下载 .pptx」，或到 GitHub 源码页查看。</p></noscript>
      <div class="lb-fallback" id="pv-fallback">预览图暂时无法加载 —— 你仍可直接下载 .pptx，或打开 GitHub 源码页查看该模板。</div>
    </div>
    <div class="lb-thumb" id="pv-thumbs" role="listbox" aria-label="切换预览图"></div>
  </div>
  <div class="lb-meta" id="pv-meta"></div>
  <div class="lb-nav">
    <button id="pv-prev">‹ 上一张</button>
    <button id="pv-next">下一张 ›</button>
    <button id="pv-fs">全屏放映</button>
  </div>
</dialog>
</main>
<footer><div class="wrap">SlideForge · 由 python-pptx 脚本生成 · MIT License · <a href="__REPO__" target="_blank" rel="noopener">GitHub 仓库</a></div></footer>
<script>__JS__</script>
</body></html>"""
    doc = (doc.replace("__CSS__", CSS).replace("__JS__", JS).replace("__REPO__", REPO_URL).replace("__SITE__", SITE_URL)
              .replace("__DECKS__", str(st["decks"])).replace("__SLIDES__", str(st["slides_total"]))
              .replace("__THEMES__", str(st["themes"])).replace("__CATS__", str(st["categories"]))
              .replace("__POTX__", str(st["potx"])).replace("__CHIPS__", "".join(chips))
              .replace("__CARDS__", "".join(cards)).replace("__TCARDS__", "".join(tcards))
              .replace("__CATTAGS__", cat_tags))
    with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
        f.write(doc)
    print("OK site: index.html + %d previews" % n)


if __name__ == "__main__":
    main()

