/* SlideForge 站点脚本 —— 由 scripts/build_site.py 内联进 index.html
   模块：模板筛选/搜索（URL 可分享状态） + 预览灯箱 */
(function () {
  'use strict';

  /* ---------- 模板筛选 / 搜索 ----------
     - data-q：构建期预算好的小写检索串，避免每次键入扫描 textContent
     - 输入防抖 120ms 后用 replaceState 写 URL（连续输入不刷历史），
       分类切换属离散跳转，用 pushState（可前进/后退） */
  var chips = [].slice.call(document.querySelectorAll('.chip'));
  var cards = [].slice.call(document.querySelectorAll('.card'));
  var input = document.getElementById('q');
  var empty = document.getElementById('empty');
  var count = document.getElementById('count');
  var active = 'all';
  var timer = null;

  cards.forEach(function (c) {
    c._q = (c.getAttribute('data-q') || c.textContent || '').toLowerCase();
  });

  function apply() {
    var q = ((input && input.value) || '').trim().toLowerCase();
    var shown = 0;
    cards.forEach(function (card) {
      var show = (active === 'all' || card.dataset.cat === active) && (!q || card._q.indexOf(q) > -1);
      card.style.display = show ? '' : 'none';
      if (show) shown++;
    });
    if (empty) empty.style.display = shown ? 'none' : 'block';
    if (count) count.textContent = shown + ' 套';
    chips.forEach(function (c) {
      var on = c.dataset.cat === active;
      c.classList.toggle('on', on);
      c.setAttribute('aria-pressed', on ? 'true' : 'false');
    });
  }

  function supportsUrlState() {
    return !!(window.history && history.replaceState && window.URL && window.URLSearchParams);
  }

  function writeUrl(push) {
    if (!supportsUrlState()) return;
    try {
      var u = new URL(location.href);
      u.searchParams.delete('cat');
      u.searchParams.delete('q');
      if (active !== 'all') u.searchParams.set('cat', active);
      var q = ((input && input.value) || '').trim();
      if (q) u.searchParams.set('q', q);
      history[push ? 'pushState' : 'replaceState'](null, '', u);
    } catch (err) { /* file:// 等环境忽略 */ }
  }

  function readUrl() {
    if (!supportsUrlState()) return { cat: 'all', q: '' };
    var p = new URLSearchParams(location.search);
    return { cat: p.get('cat') || 'all', q: p.get('q') || '' };
  }

  chips.forEach(function (c) {
    c.addEventListener('click', function () {
      active = c.dataset.cat;
      apply();
      writeUrl(true);
    });
  });

  var resetBtn = document.getElementById('empty-reset');
  if (resetBtn) {
    resetBtn.addEventListener('click', function () {
      active = 'all';
      if (input) { input.value = ''; input.focus(); }
      apply();
      writeUrl(true);
    });
  }

  if (input) {
    input.addEventListener('input', function () {
      clearTimeout(timer);
      timer = setTimeout(function () {
        apply();
        writeUrl(false);
      }, 120);
    });
  }

  window.addEventListener('popstate', function () {
    var s = readUrl();
    active = s.cat;
    if (input) input.value = s.q;
    apply();
  });

  /* 首次加载：从 URL 还原筛选/搜索；带状态进入（如他人分享的链接）时定位到列表 */
  (function restore() {
    var s = readUrl();
    var hasState = s.cat !== 'all' || s.q !== '';
    if (s.cat !== 'all' && !chips.some(function (c) { return c.dataset.cat === s.cat; })) s.cat = 'all';
    active = s.cat;
    if (input && s.q) input.value = s.q;
    apply();
    if (hasState) {
      var lib = document.getElementById('library');
      if (lib && lib.scrollIntoView) lib.scrollIntoView();
    }
  })();

  apply();
})();

/* ---------- 预览灯箱 ---------- */
(function () {
  'use strict';
  var dlg = document.getElementById('pv');
  if (!dlg) return;
  var stage = document.getElementById('pv-stage');
  var thumbs = document.getElementById('pv-thumbs');
  var meta = document.getElementById('pv-meta');
  var title = document.getElementById('pv-title');
  var dl = document.getElementById('pv-dl');
  var fallback = document.getElementById('pv-fallback');
  var cur = 0, items = [], lastFocus = null, curMeta = {};
  var VARIANTS = ['cover', 'content', 'data'];
  var status = document.getElementById('pv-status');

  function labelOf(i) {
    var v = VARIANTS[i % 3];
    return v === 'cover' ? '封面' : (v === 'content' ? '内容页' : '数据页');
  }

  function render(i) {
    if (!items.length) return;
    cur = (i + items.length) % items.length;
    var it = items[cur];
    stage.innerHTML = '';
    var img = new Image();
    img.alt = it.name + ' · ' + labelOf(cur);
    img.onload = function () { fallback.style.display = 'none'; };
    img.onerror = function () { fallback.style.display = 'block'; };
    img.src = it.src;
    stage.appendChild(img);
    if (it.file) dl.setAttribute('href', 'templates/' + it.file);
    title.textContent = it.name;
    meta.innerHTML = '<span>用途：' + (curMeta.cat || '—') + '</span><span>版面：' + (curMeta.slides || '—') + ' 页</span>'
      + '<span>风格：' + (curMeta.style || '—') + '</span><span>当前：' + labelOf(cur) + '</span>';
    if (status) status.textContent = '第 ' + (cur + 1) + ' 张，共 ' + items.length + ' 张：' + labelOf(cur);
    [].slice.call(thumbs.children).forEach(function (b, k) {
      b.setAttribute('aria-current', k === cur ? 'true' : 'false');
    });
  }

  function open(card) {
    lastFocus = document.activeElement;
    var f = card.getAttribute('data-file');
    var name = (card.querySelector('.name') || { textContent: '模板预览' }).textContent;
    var catName = (card.querySelector('.cat') || { textContent: '' }).textContent;
    var styleKey = card.getAttribute('data-style') || 'build';
    var slides = card.getAttribute('data-slides') || '';
    items = VARIANTS.map(function (v) {
      return { src: 'assets/previews/' + styleKey + '-' + v + '.svg', name: name, file: f };
    });
    curMeta = { cat: catName, slides: slides, style: name };
    thumbs.innerHTML = '';
    items.forEach(function (it, i) {
      /* APG：普通可点击按钮组即可，勿套 listbox/option 语义（option 不支持内含交互控件） */
      var b = document.createElement('button');
      b.type = 'button';
      b.innerHTML = '<img src="' + it.src + '" alt="' + labelOf(i) + ' 缩略图">';
      b.addEventListener('click', function () { render(i); });
      thumbs.appendChild(b);
    });
    render(0);
    try {
      if (typeof dlg.showModal === 'function') { dlg.showModal(); }
      else { dlg.setAttribute('open', ''); }
    } catch (err) { dlg.setAttribute('open', ''); } /* 任何环境下都保证打开 */
  }

  /* 事件委托：点击卡片图上的热区按钮打开灯箱 */
  document.addEventListener('click', function (e) {
    var btn = e.target && e.target.closest ? e.target.closest('.pv-btn') : null;
    if (!btn) return;
    var card = btn.closest('.card');
    if (card) open(card);
  });

  document.getElementById('pv-close').addEventListener('click', function () {
    try { dlg.close ? dlg.close() : dlg.removeAttribute('open'); }
    catch (err) { dlg.removeAttribute('open'); }
  });
  document.getElementById('pv-prev').addEventListener('click', function () { render(cur - 1); });
  document.getElementById('pv-next').addEventListener('click', function () { render(cur + 1); });
  document.getElementById('pv-fs').addEventListener('click', function () {
    if (document.fullscreenElement) { document.exitFullscreen(); }
    else if (dlg.requestFullscreen) { dlg.requestFullscreen().catch(function () {}); }
  });

  dlg.addEventListener('keydown', function (e) {
    if (e.key === 'ArrowLeft') { render(cur - 1); }
    else if (e.key === 'ArrowRight') { render(cur + 1); }
    else if (e.key === 'Home') { render(0); }
    else if (e.key === 'End') { render(items.length - 1); }
  });

  /* 触摸滑动翻页（横滑阈值 40px；touch-action:pan-y 不影响纵向滚动） */
  var touchX = null;
  stage.style.touchAction = 'pan-y';
  stage.addEventListener('pointerdown', function (e) { touchX = e.clientX; });
  stage.addEventListener('pointerup', function (e) {
    if (touchX === null) return;
    var dx = e.clientX - touchX;
    touchX = null;
    if (Math.abs(dx) > 40) render(dx < 0 ? cur + 1 : cur - 1);
  });

  dlg.addEventListener('close', function () {
    if (lastFocus && lastFocus.focus) lastFocus.focus();
  });
})();
