# 前端网页迭代台账（iteration log）

> 迭代对象：SlideForge 浏览站 `index.html`（GitHub Pages）。
> **收敛标准（开工前写明）**：完成 3 轮完整「联网搜索 → 修改 → 构建验证」循环即收尾；若某轮改动后核心指标无实质提升，也提前收尾。本次按 3 轮收尾。
> 对比方式：每轮保存 `docs/iterations/roundN-index-snapshot.html` 全页快照 + `roundN.json` 量化指标；本机无浏览器截图能力，故以**可复核的结构化指标 + 全页快照 diff** 作为前后对比证据。

## 基线（Round 0）

| 指标 | 基线值 |
|---|---|
| skip_link | False |
| main_landmark | False |
| search_input | False |
| empty_state | False |
| aria_labels | 0 |
| aria_pressed_chips | 0 |
| og_tags | 0 |
| canonical | False |
| jsonld | False |
| favicon | False |
| img_dims | 0 |
| img_lazy | 126 |
| focus_visible_css | False |
| prefers_color_scheme | False |
| print_css | False |
| prefers_reduced_motion | False |
| card_count | 126 |
| bytes | 113832 |

## Round 1（2026-09-15）

**搜索依据（可点击查证）**：

- [W3C WAI — Skip Link Easy Checks](https://www.w3.org/WAI/test-evaluate/easy-checks/skip-link/)
- [WebAIM — Skip Navigation Links](https://webaim.org/techniques/skipnav/)
- [The A11Y Collective — Skip to main content best practices](https://www.a11y-collective.com/blog/skip-to-main-content/)

**改动点**：新增跳转链接、<main> 地标、nav aria-label；25 个筛选 chip 加 aria-pressed 并由 JS 同步；新增搜索框(带 role=status 计数)与空态提示；:focus-visible 焦点环；prefers-reduced-motion 降级。

**验证结果**：check_site 指标 skip_link/main/search/empty/focus-visible 全部 True；aria-pressed=24；HTML 配平 0 错误；线上 200 且含 skip-link/search/main；Pages 部署成功。

| 指标 | Round 1 | 与基线 |
|---|---|---|
| skip_link | True | False → True |
| main_landmark | True | False → True |
| search_input | True | False → True |
| empty_state | True | False → True |
| aria_labels | 3 | 0 → 3 |
| aria_pressed_chips | 24 | 0 → 24 |
| og_tags | 0 | = |
| canonical | False | = |
| jsonld | False | = |
| favicon | False | = |
| img_dims | 0 | = |
| focus_visible_css | True | False → True |
| prefers_color_scheme | False | = |
| print_css | False | = |
| card_count | 126 | = |
| bytes | 116576 | 113832 → 116576 |

## Round 2（2026-09-15）

**搜索依据（可点击查证）**：

- [web.dev — Optimize CLS（图片必须写 width/height）](https://web.dev/articles/optimize-cls)
- [Aleksandr Hovhannisyan — Set width and height on images](https://www.aleksandrhovhannisyan.com/blog/setting-width-and-height-on-images/)

**改动点**：126 张卡片图片补 width/height（消除 CLS）；新增 prefers-color-scheme 深色模式（变量级覆盖）；新增 @media print 打印样式。

**验证结果**：img_dims=126/126（与 img_lazy 一致）；prefers_color_scheme/print_css=True；HTML 配平 0 错误；体积 120,467B（+2.4%）；推送 6d11693。

| 指标 | Round 2 | 与基线 |
|---|---|---|
| skip_link | True | False → True |
| main_landmark | True | False → True |
| search_input | True | False → True |
| empty_state | True | False → True |
| aria_labels | 3 | 0 → 3 |
| aria_pressed_chips | 24 | 0 → 24 |
| og_tags | 0 | = |
| canonical | False | = |
| jsonld | False | = |
| favicon | False | = |
| img_dims | 126 | 0 → 126 |
| focus_visible_css | True | False → True |
| prefers_color_scheme | True | False → True |
| print_css | True | False → True |
| card_count | 126 | = |
| bytes | 120467 | 113832 → 120467 |

## Round 3（2026-09-15）

**搜索依据（可点击查证）**：

- [Google Search Central — Introduction to structured data（推荐 JSON-LD）](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data)
- [opengraph.io — OG Tags vs Schema](https://www.opengraph.io/og-tags-vs-schema)
- [Mintlify — SEO（meta/OG/canonical 配置）](https://www.mintlify.com/docs/optimize/seo)

**改动点**：新增 canonical、6 个 Open Graph 标签、twitter:card、JSON-LD(SoftwareSourceCode)、SVG data-URI favicon、theme-color/color-scheme；仓库新增 sitemap.xml 与 robots.txt。

**验证结果**：og_tags=6、canonical/jsonld/favicon/theme_color=True；sitemap.xml/robots.txt 已提交；HTML 配平 0 错误；推送 b129845。

| 指标 | Round 3 | 与基线 |
|---|---|---|
| skip_link | True | False → True |
| main_landmark | True | False → True |
| search_input | True | False → True |
| empty_state | True | False → True |
| aria_labels | 3 | 0 → 3 |
| aria_pressed_chips | 24 | 0 → 24 |
| og_tags | 6 | 0 → 6 |
| canonical | True | False → True |
| jsonld | True | False → True |
| favicon | True | False → True |
| img_dims | 126 | 0 → 126 |
| focus_visible_css | True | False → True |
| prefers_color_scheme | True | False → True |
| print_css | True | False → True |
| card_count | 126 | = |
| bytes | 122041 | 113832 → 122041 |

## 回滚演练记录

- 时间：2026-09-15。步骤：向 `scripts/build_site.py` 注入坏标签（`</main>`→`</maiin>`）→ 重建 → 结构校验报 `VALID=False errors=2`（stray </maiin>）→ `git checkout -- scripts/build_site.py` 恢复 → 重建 → `VALID=True errors=0` → `git status` 干净。
- 结论：回滚流程可用，恢复后页面正常。

## 收尾判定

- 3 轮闭环全部完成（每轮都有搜索依据、改动、构建与验证），达到开工前设定的收敛标准 → **收尾**。

---

# 第二次迭代：联网洞察 + 全面重构（Round 4-6，2026-09-18）

> 迭代对象不变：`index.html`（GitHub Pages）。
> **收敛标准（开工前写明）**：完成 3 轮完整「联网搜索 → 修改 → 构建验证」即收尾；本次同步完成一次**结构性全面重构**（前端源码与构建器分离）。
> 工具升级：本轮起指标由 `scripts/check_site.py` 固化产出（roundN.json + 全页快照 + HTML 配平校验），不再临时拼脚本。
> 历史口径：仓库中原有的 `round4/5-index-snapshot.html` 是灯箱功能期（d18317d → 1035b2c）的临时快照，从未配套指标 JSON；本次已被带完整指标的 Round 4-6 覆盖，灯箱期页面状态可随时经上述提交还原查阅。
> 口径说明：round3.json 的 bytes=122,041 是灯箱功能合入前的旧值；重构前 index.html 实际为 **238,235 B**，本轮对比以实际值为准。

## Round 4（2026-09-18）· 结构重构 + 渲染性能

**搜索依据（可点击查证）**：

- [web.dev — content-visibility 渲染性能](https://web.dev/articles/content-visibility)（配 [MDN contain-intrinsic-size](https://developer.mozilla.org/docs/Web/CSS/contain-intrinsic-size)、[DebugBear 2025-11 实测](https://www.debugbear.com/blog/content-visibility)）
- [web.dev — Optimize LCP](https://web.dev/articles/optimize-lcp)（LCP 图不得懒加载；`fetchpriority="high"` 提升首屏图优先级）
- [MDN — History.replaceState()](https://developer.mozilla.org/docs/Web/API/History/replaceState) 与 [Dynatrace — URL sharing guidance](https://developer.dynatrace.com)（连续输入用 replaceState、离散切换用 pushState、popstate 回放）

**改动点**：

1. **全面重构**：删除 `build_site.py` 中 117 行死代码 `build_html()`（含损坏的 `%` 格式化，误调用即崩溃）；前端源码拆分为 `scripts/site/{page.html,style.css,app.js}` 三件套，`build_site.py` 只做数据装配与 token 注入（残留 token 自检、防二次二义事故）。删除 app.js 内死选择器 `.preview` 与死变量（`data-style-label`/`mm`）。
2. **性能**：126 张卡片图全部懒加载 → 前 3 张 `loading="eager" fetchpriority="high"`，其余 lazy，全部 `decoding="async"`；`.card{content-visibility:auto;contain-intrinsic-size:auto 344px}` 跳过视口外卡片渲染；搜索改为构建期预算 `data-q` 检索串 + 120ms 防抖（不再每次键入全量扫描 textContent）。
3. **URL 可分享状态**：筛选/搜索写入 `?cat=&q=`（输入 replaceState、切分类 pushState、popstate 回放、带状态进入自动定位到列表）。
4. 顺手修复：重写中补回 `data-file`（防灯箱下载 404 复发，此为上次线上事故同款风险点）；「全部」chip 此前缺 `aria-pressed`，已补。

**验证结果**：`html_valid=True`（配平 0 错误）；75 张预览 SVG 重建后 **git 零 diff**（回归通过）；卡片 126 = 3 eager + 123 lazy 全带 decoding/dims/alt；content-visibility/url_state/search_dataq/debounce 全 True；体积 238,235B → 203,723B（**-34.5KB，-14.5%**）；`node --check` JS 语法通过。

| 指标 | Round 4 | 与重构前实际值 |
|---|---|---|
| bytes | 203,723 | 238,235 → -34,512 (-14.5%) |
| html_valid | True | True（0 错误） |
| img_eager + fetchpriority | 3 + 3 | 0 → 3 |
| img_lazy | 123 | 126 → 123（首屏改 eager） |
| content_visibility_css | True | False → True |
| url_state_js | True | False → True |
| search_dataq / search_debounce | True / True | False → True |
| aria_pressed_chips | 25 | 24 → 25（补「全部」chip） |
| 死代码 build_html / `.preview` 选择器 | 已删除 | 117 行 / 1 处 → 0 |

## Round 5（2026-09-18）· 灯箱可访问性（APG 对齐）

**搜索依据（可点击查证）**：

- [W3C WAI APG — Dialog (Modal) 模式](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/)（焦点圈闭、Esc、关闭后焦点还原、aria-modal/aria-labelledby）
- [W3C WAI APG — Listbox 模式](https://www.w3.org/WAI/ARIA/apg/patterns/listbox/)（原文明确：listbox "does not provide an accessible way to present a list of interactive elements, such as links, buttons"；可点击按钮组无需 listbox 语义）

**改动点**：缩略图容器 `role="listbox"` + 按钮 `role="option"` 属 APG 反模式 → 改为 `role="group"` + 普通按钮 + `aria-current` 指示当前项；删除无效的 `aria-selected`；dialog 显式 `aria-modal="true"`；新增 `#pv-status`（sr-only + aria-live=polite）播报「第 X 张，共 3 张」；键盘补 Home/End；触摸横滑翻页（阈值 40px，`touch-action:pan-y`）；空态新增「重置筛选」按钮（重置后焦点回搜索框）。

**验证结果**：`html_valid=True`；六项新指标全部翻转（见下表）；`node --check` 通过。

| 指标 | Round 5 | 与 Round 4 |
|---|---|---|
| listbox_misuse（反模式） | False | True → False |
| thumb_aria_group | True | False → True |
| dialog_aria_modal | True | False → True |
| aria_live_status | True | False → True |
| home_end_keys / swipe_js | True / True | False → True |
| empty_reset | True | False → True |
| bytes | 204,893 | +1,170 |

## Round 6（2026-09-18）· SEO / 分享元数据

**搜索依据（可点击查证）**：

- [Google Search Central — Carousel (ItemList) 结构化数据](https://developers.google.com/search/docs/appearance/structured-data/carousel)（汇总页用 ItemList + ListItem{position,url}，应完整列出条目）
- [MDN — meta name="theme-color"](https://developer.mozilla.org/docs/Web/HTML/Reference/Elements/meta/name/theme-color)（media 属性分别声明浅色/深色主题色）
- Open Graph 协议（[ogp.me](https://ogp.me/)）：og:image 需配 width/height/alt；**多数社交平台不支持 SVG 作 og:image**，需 PNG ≥1200×630

**改动点**：新增 ItemList JSON-LD（全量 126 项 position+url+name，与 SoftwareSourceCode 并列两个 script 块）；theme-color 拆分为 light/dark 两条 media 查询；Pillow 构建期生成 `assets/previews/og-cover.png`（1200×630）替换 SVG 作 og:image，并补 og:image:type/width/height/alt、og:locale、twitter:image、robots `max-image-preview:large`；sitemap.xml 首页补 lastmod。

**验证结果**：`html_valid=True`；两块 JSON-LD 均可 `json.loads` 解析（ItemList 126 项）；OG PNG 尺寸 1200×630；og 标签 6 → 11。

| 指标 | Round 6 | 与 Round 5 |
|---|---|---|
| jsonld / jsonld_itemlist | 2 / True | 1 / False → True |
| og_tags | 11 | 6 → 11 |
| og_image_png / og_image_dims | True / True | False → True |
| theme_color_dark | True | False → True |
| robots_meta | True | False → True |
| bytes | 230,869 | +25,976（ItemList 17KB + OG 标签，gzip 后增量更小） |

## 回滚

- 前端源码已拆分，回滚粒度更细：`git checkout <commit> -- scripts/site scripts/build_site.py` 后重跑 `python scripts/build_site.py && python scripts/check_site.py` 即可；模板文件（.pptx/.potx）不受影响。
- 构建自检：`build_site.py` 发现残留 `__TOKEN__` 会直接报错退出，防止半成品 index.html 落盘（延续上轮回滚演练的坏标签防护思路）。

## 收尾判定（第二次迭代）

- Round 4-6 三轮闭环完成，每轮均有搜索依据、改动、构建验证与量化前后对比，且完成结构性重构（前端源码/构建器分离 + 指标工具固化）→ **收尾**。
- 遗留建议（不阻塞）：GH Pages 无法自定义响应头，CSP/brotli 依赖平台；若后续引入构建链（如 Vite），可再做资源分包与压缩。
