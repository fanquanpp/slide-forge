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
