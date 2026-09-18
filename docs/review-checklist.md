# 交付前复核清单

| # | 验收标准 | 证据 | 结论 |
|---|---|---|---|
| 1 | 每轮迭代都有联网搜索依据 | iteration-log.md 三轮各列 2-3 条可点击来源；页面改动与结论一一对应 | ✅ |
| 2 | 完成完整迭代闭环 | 3 轮「搜索→修改→构建验证」，每轮结束站点可运行（HTML 配平 0 错误 + 线上 200） | ✅ |
| 3 | 迭代台账可追踪 | docs/iteration-log.md + docs/iterations/round{0-3}.json + 全页快照 | ✅ |
| 4 | 每轮页面可构建可打开 | 每轮 build_site 成功、validate_html VALID=True、Pages 部署 success、线上 200 | ✅ |
| 5 | 改进有前后对比证据 | round0-3 指标对比表 + 全页快照（无浏览器截图能力，已改用可复核指标+快照） | ✅（方式替代） |
| 6 | 按收敛标准收尾 | 台账开头写明收敛标准，3 轮后收尾 | ✅ |
| 7 | 异常可回滚 | 回滚演练：注入坏标签→校验失败→git checkout 恢复→VALID=True | ✅ |
| 8 | 最终版本可访问、可交接 | https://fanquanpp.github.io/slide-forge/ 200；docs/handoff.md 说明结构与迭代方法 | ✅ |
| 9 | 交付前逐项复核 | 本清单 | ✅ |
| 10 | 更新仓库文档信息 | README 链接迭代台账；docs/iteration-log.md、iterations/ 快照与指标入库 | ✅ |

**结论**：10 项全部通过，判定任务完成。

---

# 第二次迭代（联网洞察 + 全面重构，Round 4-6）复核清单

| # | 验收标准 | 证据 | 结论 |
|---|---|---|---|
| 1 | 每轮有联网搜索依据 | Round 4：web.dev content-visibility / Optimize LCP / MDN replaceState；Round 5：W3C APG Dialog + Listbox（原文引用）；Round 6：Google Carousel(ItemList) / MDN theme-color / ogp.me | ✅ |
| 2 | 结构性全面重构完成 | 删除 117 行死代码 `build_html()` 与死选择器；前端源码拆分 `scripts/site/{page.html,style.css,app.js}`；`build_site.py` 只做装配，残留 token 自检 | ✅ |
| 3 | 完整迭代闭环 | 3 轮「搜索→修改→构建验证」，每轮 `html_valid=True`（配平 0 错误） | ✅ |
| 4 | 可复现量化验证 | `scripts/check_site.py` 自动产出 docs/iterations/round{4-6}.json + 全页快照，含与上轮 diff | ✅ |
| 5 | 性能有前后对比 | 238,235B → 203,723B（-14.5%）；首屏 3 图 eager+fetchpriority；content-visibility；data-q 预算 + 防抖 | ✅ |
| 6 | 无障碍对齐 APG | listbox 反模式 True→False；aria-modal/aria-live/Home+End/滑动/重置按钮六项指标翻转 | ✅ |
| 7 | SEO/分享元数据补全 | ItemList JSON-LD（126 项，可解析）；OG PNG 1200×630；双 theme-color；og 标签 6→11；sitemap lastmod | ✅ |
| 8 | 回归无破坏 | 75 张预览 SVG 重建零 diff；`data-file` 修复（防灯箱下载 404 复发）；`node --check` 通过 | ✅ |
| 9 | 回滚可用 | 粒度细化到 `scripts/site` + 构建器；构建期 token 残留即报错退出 | ✅ |

**结论**：9 项全部通过。
