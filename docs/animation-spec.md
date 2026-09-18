# 动效规范（Animation Spec）· v3

> 全部 126 套 / 2394 页均注入**角色化切换特效**、**内容元素分级入场动画**与**大数字强调动画**；本文件登记规则与清单。
> v3 依据：ppt-master `references/animations.md` / `scripts/docs/pptx-transitions.md` 契约 + 2026 演示设计趋势调研（purposeful motion，chrome 静态化）。

## 一、入场动画规则

- **只动内容**：动画时间树仅收录内容元素；`chrome:*`（背景/页脚/装饰）与 `!!*`（Morph 配对载体）命名形状**保持静态**——「chrome stays static」，避免整页齐动的 AI 模板感，页面节奏更快。
- **分级顺序**：内容元素按页面坐标 `(top, left)` 排序入场（主体 → 标注）。
- **触发方式**：每页首个内容元素为 `clickEffect`（点击触发），其余 `afterEffect` 自动串播。
- **错峰延时**：相邻元素间隔 **130 ms**；单元素入场 **450–810 ms**。
- **效果多样性**：**25** 种入场滤镜循环（见 §四），同页相邻元素效果不同。
- **强调动画**：`motion:hero` 命名的大数字（bignumber / stat_chart / kpi 首瓦片）入场后追加一次 **grow/shrink（presetID 6, presetClass=emph）**，放大至 108% 收住；全库共 **96** 处。
- **XML 依据**：入场结构沿用 oracle 模板（`entr/filter_effect`），oracle-clean 无死路径。

## 二、切换特效规则（v3 核心变化）

**按页面角色（相邻页关系）选族，不再机械轮换**——「choose from the relationship between adjacent pages, not gallery coverage」：

| 页面角色 | 关系诊断 | 切换族 |
|---|---|---|
| cover 封面 | 开场边界、状态标记 | reveal / split / circle |
| section 章节 | 主题节拍 | flash / reveal / wipe |
| flow 流程（时间线/流程/路线图/金字塔/分步） | 方向性推进 | push（l/u）/ wipe(r) |
| data 数据（图表/表格/指标卡/漏斗/矩阵/看板） | 几何化揭示 | ripple / circle(in) / wheel(1) |
| collect 集合（图集/团队/金句墙） | 集合在空间中轮换 | pan / gallery / conveyor |
| content 正文 | 普通延续 → 克制基线 | fade |
| closing 结尾 | 收束 | fade |

- **现代主题升级**：darkneon / glass / vaporwave / gradient / luxury / bubble 六个现代主题的 data、collect 族升级为 glitter / vortex / switch / flip；并在**连续阅读页（content/flow 相邻）使用真 Morph**。
- **确定性 Morph 配对**：品牌规线 `!!brand-band`、页脚线 `!!footer-rule` 跨页同名（PowerPoint `!!` 命名配对约定），`<p159:morph option="byObject"/>` 补间载体；全库共 **95** 处 Morph。封面/章节/结尾边界不 morph。
- **MCE 降级**：p14/p159 特效一律 `mc:AlternateContent` 载体 + `<p:fade/>` Fallback，Choice/Fallback 的 `spd/advClick/advTm` 同步——旧版 Office 自动降级淡入，不丢驻留时长。
- **驻留分级**：封面/章节 **6s**，正文/流程 **8s**，数据/集合 **10s**（信息越密停留越久）；`presProps.xml` 显式 `useTimings="1"`（包级硬规则：写 advTm 必须声明使用计时器）。

### 现代切换使用量（全库 2394 页）

| 键 | 载体 | 次数 |
|---|---|---:|
| morph（byObject） | p159 + fade 降级 | 95 |
| reveal / flash / ripple / pan / gallery / conveyor / glitter / vortex / switch / flip | p14 + fade 降级 | 741 |
| 经典 p: 族（fade/push/wipe/split/circle/wheel…） | 直接载体 | 其余全部 |

## 三、逐套模板动效概览

126 套逐页登记见构建产物：切换按「角色 × 主题（classic/modern）× 种子」确定，同分类同风格的套件计划一致、可复现。抽样明细由 `scripts/qa_check.py` 出具（见 `docs/qa-report.md`）。

## 四、入场滤镜清单（25 种）

| 滤镜 | preset | 滤镜 | preset |
|---|---|---|---|
| `fade` | 9/0 | `strips(downRight)` | 25/1 |
| `dissolve` | 10/0 | `strips(upLeft)` | 25/2 |
| `wipe(down)` | 22/4 | `strips(upRight)` | 25/3 |
| `wipe(up)` | 22/1 | `blinds(horizontal)` | 42/10 |
| `wipe(left)` | 22/8 | `blinds(vertical)` | 42/5 |
| `wipe(right)` | 22/2 | `checkerboard(across)` | 43/0 |
| `wedge` | 37/0 | `checkerboard(down)` | 43/1 |
| `wheel(1)` | 21/1 | `barn(inVertical)` | 45/0 |
| `wheel(2)` | 21/2 | `barn(inHorizontal)` | 45/1 |
| `wheel(3)` | 21/3 | `randombar(horizontal)` | 52/0 |
| `wheel(4)` | 21/4 | `randombar(vertical)` | 52/1 |
| `circle(in)` | 18/12 | `circle(out)` | 19/12 |
| `strips(downLeft)` | 25/0 | | |

## 五、设计取舍记录

- **p15 纸张类切换（page_curl/origami 等）未采用**：语义最娱乐化，与 24 个正式用途分类的匹配度低；若后续引入「创意/活动」专属包再评估。
- **声音未启用**：模板库默认静音（sound 是可选提示，不是能力展示）。
- **入场不做全页覆盖**：单页最多 14 个动画目标（保护性能），超出的装饰天然被 chrome 静态规则排除。
