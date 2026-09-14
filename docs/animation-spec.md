# 动效规范（Animation Spec）

> 全部 126 套 / 2268 页均注入了**逐元素分级入场动画**与**逐页切换特效**；本文件登记规则与清单。

## 一、入场动画规则

- **分级顺序**：元素按页面坐标 `(top, left)` 排序入场 —— 先背景装饰块，再标题主体，最后标注与页脚，形成「背景 → 主体 → 标注 → 强调」的层次。
- **触发方式**：每页首个元素为 `clickEffect`（点击触发），其余元素为 `afterEffect` 自动串播，无需逐一点击。
- **错峰延时**：相邻元素间隔 **130 ms**，避免同时出现造成呆板。
- **时长区间**：单个元素入场 **450–810 ms**，随主题/种子变化。
- **效果多样性**：使用 **15** 种入场滤镜循环（见下表），同一页内相邻元素效果不同。
- **XML 依据**：入场结构严格采用 `pptx-animation-skill` 的 oracle 模板（`entr/filter_effect`），已通过其官方 `validate.py` 校验为 **oracle-clean（无死路径）**。

## 二、切换特效规则

- **不单一**：使用 **12** 类切换（fade/push/wipe/split/blinds/circle/comb/dissolve/zoom/cover/checker/newsflash）。
- **相邻必不同**：切换表按「相邻类型不同」的环排序，逐页轮换；校验结果：相邻重复 = **0**。
- **方向多样**：push/wipe/cover 使用不同方向（l/u/d），避免整篇同一种平移。

| # | 切换 | 方向/参数 | 速度 |
|---|---|---|---|
| 1 | fade | — | med |
| 2 | push | dir=l | med |
| 3 | wipe | dir=u | med |
| 4 | split | orient=horz | med |
| 5 | blinds | dir=horz | med |
| 6 | circle | dir=in | med |
| 7 | comb | dir=horz | med |
| 8 | dissolve | — | med |
| 9 | zoom | dir=in | med |
| 10 | cover | dir=l | med |
| 11 | checker | dir=across | med |
| 12 | newsflash | — | med |
| 13 | push | dir=u | med |
| 14 | wipe | dir=d | med |

## 三、入场滤镜清单（25 种）

| 滤镜 | preset | 说明 |
|---|---|---|
| `fade` | 9/0 | 淡入 |
| `dissolve` | 10/0 | 溶解 |
| `wipe(down)` | 22/4 | 向下擦除 |
| `wipe(up)` | 22/1 | 向上擦除 |
| `wipe(left)` | 22/8 | 向左擦除 |
| `wipe(right)` | 22/2 | 向右擦除 |
| `wedge` | 37/0 | 楔形展开 |
| `wheel(1)` | 21/1 | 1 叶时钟擦除 |
| `wheel(2)` | 21/2 | 2 叶时钟擦除 |
| `wheel(3)` | 21/3 | 3 叶时钟擦除 |
| `wheel(4)` | 21/4 | 4 叶时钟擦除 |
| `circle(in)` | 18/12 | 圆形由内展开 |
| `circle(out)` | 19/12 | 圆形由外收拢 |
| `strips(downLeft)` | 25/0 | 斜条展开 |
| `strips(downRight)` | 25/1 | 斜条展开 |
| `strips(upLeft)` | 25/2 | 斜条展开 |
| `strips(upRight)` | 25/3 | 斜条展开 |
| `blinds(horizontal)` | 42/10 | 横向百叶 |
| `blinds(vertical)` | 42/5 | 纵向百叶 |
| `checkerboard(across)` | 43/0 | 棋盘横向 |
| `checkerboard(down)` | 43/1 | 棋盘纵向 |
| `barn(inVertical)` | 45/0 | 纵向谷仓门 |
| `barn(inHorizontal)` | 45/1 | 横向谷仓门 |
| `randombar(horizontal)` | 52/0 | 随机横条 |
| `randombar(vertical)` | 52/1 | 随机竖条 |

## 四、逐套模板动效概览

| 编号 | 文件 | 页数 | 动效页数 | 切换 |
|---|---|---:|---:|---|
| SF-001 | `01-teaching-programming-courseware/01__build.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-002 | `01-teaching-programming-courseware/01__terminal.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-003 | `01-teaching-programming-courseware/01__takram.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-004 | `01-teaching-programming-courseware/01__chalk.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-005 | `01-teaching-programming-courseware/01__academic.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-006 | `02-game-gdd-game-design-proposal/02__darkneon.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-007 | `02-game-gdd-game-design-proposal/02__retropixel.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-008 | `02-game-gdd-game-design-proposal/02__corporate.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-009 | `02-game-gdd-game-design-proposal/02__isometric.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-010 | `02-game-gdd-game-design-proposal/02__vaporwave.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-011 | `03-portfolio-pixel-art-portfolio/03__editorial.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-012 | `03-portfolio-pixel-art-portfolio/03__retropixel.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-013 | `03-portfolio-pixel-art-portfolio/03__build.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-014 | `03-portfolio-pixel-art-portfolio/03__risograph.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-015 | `03-portfolio-pixel-art-portfolio/03__luxury.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-016 | `04-club-event-club-event-planning/04__memphis.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-017 | `04-club-event-club-event-planning/04__organic.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-018 | `04-club-event-club-event-planning/04__build.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-019 | `04-club-event-club-event-planning/04__pastel.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-020 | `04-club-event-club-event-planning/04__bauhaus.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-021 | `04-club-event-club-event-planning/04__bubble.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-022 | `05-project-report-project-report-retrospective/05__brockmann.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-023 | `05-project-report-project-report-retrospective/05__corporate.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-024 | `05-project-report-project-report-retrospective/05__build.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-025 | `05-project-report-project-report-retrospective/05__nordic.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-026 | `05-project-report-project-report-retrospective/05__academic.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-027 | `06-study-notes-study-notes-sharing/06__takram.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-028 | `06-study-notes-study-notes-sharing/06__organic.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-029 | `06-study-notes-study-notes-sharing/06__editorial.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-030 | `06-study-notes-study-notes-sharing/06__academic.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-031 | `06-study-notes-study-notes-sharing/06__monochrome.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-032 | `07-resume-resume-self-intro/07__build.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-033 | `07-resume-resume-self-intro/07__editorial.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-034 | `07-resume-resume-self-intro/07__nordic.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-035 | `07-resume-resume-self-intro/07__monochrome.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-036 | `07-resume-resume-self-intro/07__luxury.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-037 | `08-promo-event-promo/08__memphis.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-038 | `08-promo-event-promo/08__glass.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-039 | `08-promo-event-promo/08__darkneon.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-040 | `08-promo-event-promo/08__bauhaus.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-041 | `08-promo-event-promo/08__pastel.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-042 | `08-promo-event-promo/08__bubble.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-043 | `09-dashboard-data-dashboard/09__corporate.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-044 | `09-dashboard-data-dashboard/09__glass.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-045 | `09-dashboard-data-dashboard/09__takram.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-046 | `09-dashboard-data-dashboard/09__gradient.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-047 | `09-dashboard-data-dashboard/09__isometric.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-048 | `10-creative-pitch-creative-pitch/10__editorial.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-049 | `10-creative-pitch-creative-pitch/10__darkneon.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-050 | `10-creative-pitch-creative-pitch/10__organic.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-051 | `10-creative-pitch-creative-pitch/10__newspaper.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-052 | `10-creative-pitch-creative-pitch/10__vaporwave.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-053 | `11-product-launch-product-launch/11__gradient.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-054 | `11-product-launch-product-launch/11__glass.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-055 | `11-product-launch-product-launch/11__luxury.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-056 | `11-product-launch-product-launch/11__build.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-057 | `11-product-launch-product-launch/11__darkneon.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-058 | `11-product-launch-product-launch/11__bubble.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-059 | `12-reading-club-reading-club/12__editorial.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-060 | `12-reading-club-reading-club/12__organic.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-061 | `12-reading-club-reading-club/12__newspaper.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-062 | `12-reading-club-reading-club/12__pastel.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-063 | `12-reading-club-reading-club/12__monochrome.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-064 | `12-reading-club-reading-club/12__bubble.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-065 | `13-job-competition-job-competition/13__corporate.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-066 | `13-job-competition-job-competition/13__build.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-067 | `13-job-competition-job-competition/13__brockmann.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-068 | `13-job-competition-job-competition/13__academic.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-069 | `13-job-competition-job-competition/13__nordic.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-070 | `14-contest-defense-contest-defense/14__brockmann.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-071 | `14-contest-defense-contest-defense/14__gradient.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-072 | `14-contest-defense-contest-defense/14__corporate.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-073 | `14-contest-defense-contest-defense/14__darkneon.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-074 | `14-contest-defense-contest-defense/14__blueprint.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-075 | `15-course-syllabus-course-syllabus/15__academic.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-076 | `15-course-syllabus-course-syllabus/15__takram.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-077 | `15-course-syllabus-course-syllabus/15__nordic.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-078 | `15-course-syllabus-course-syllabus/15__chalk.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-079 | `15-course-syllabus-course-syllabus/15__isometric.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-080 | `16-recruitment-recruitment/16__memphis.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-081 | `16-recruitment-recruitment/16__pastel.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-082 | `16-recruitment-recruitment/16__bauhaus.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-083 | `16-recruitment-recruitment/16__glass.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-084 | `16-recruitment-recruitment/16__vaporwave.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-085 | `16-recruitment-recruitment/16__bubble.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-086 | `17-annual-review-annual-review/17__newspaper.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-087 | `17-annual-review-annual-review/17__editorial.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-088 | `17-annual-review-annual-review/17__corporate.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-089 | `17-annual-review-annual-review/17__monochrome.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-090 | `17-annual-review-annual-review/17__gradient.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-091 | `18-training-manual-training-manual/18__monochrome.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-092 | `18-training-manual-training-manual/18__nordic.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-093 | `18-training-manual-training-manual/18__academic.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-094 | `18-training-manual-training-manual/18__isometric.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-095 | `18-training-manual-training-manual/18__chalk.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-096 | `19-user-research-user-research/19__takram.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-097 | `19-user-research-user-research/19__nordic.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-098 | `19-user-research-user-research/19__academic.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-099 | `19-user-research-user-research/19__organic.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-100 | `19-user-research-user-research/19__monochrome.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-101 | `20-market-analysis-market-analysis/20__corporate.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-102 | `20-market-analysis-market-analysis/20__brockmann.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-103 | `20-market-analysis-market-analysis/20__gradient.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-104 | `20-market-analysis-market-analysis/20__newspaper.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-105 | `20-market-analysis-market-analysis/20__glass.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-106 | `21-budget-plan-budget-finance/21__brockmann.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-107 | `21-budget-plan-budget-finance/21__corporate.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-108 | `21-budget-plan-budget-finance/21__isometric.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-109 | `21-budget-plan-budget-finance/21__monochrome.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-110 | `21-budget-plan-budget-finance/21__nordic.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-111 | `22-travel-plan-travel-plan/22__organic.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-112 | `22-travel-plan-travel-plan/22__pastel.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-113 | `22-travel-plan-travel-plan/22__editorial.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-114 | `22-travel-plan-travel-plan/22__risograph.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-115 | `22-travel-plan-travel-plan/22__vaporwave.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-116 | `22-travel-plan-travel-plan/22__bubble.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-117 | `23-open-source-release-open-source-release/23__terminal.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-118 | `23-open-source-release-open-source-release/23__blueprint.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-119 | `23-open-source-release-open-source-release/23__darkneon.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-120 | `23-open-source-release-open-source-release/23__monochrome.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-121 | `23-open-source-release-open-source-release/23__gradient.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-122 | `24-tech-review-tech-architecture-review/24__blueprint.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-123 | `24-tech-review-tech-architecture-review/24__isometric.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-124 | `24-tech-review-tech-architecture-review/24__brockmann.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-125 | `24-tech-review-tech-architecture-review/24__terminal.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
| SF-126 | `24-tech-review-tech-architecture-review/24__monochrome.pptx` | 18 | 18 | 逐页轮换（相邻不同） |
