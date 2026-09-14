# SlideForge · 多用途可编辑 PPT 模板库

> 脚本生成的多用途、多风格、**可编辑**且**不含正式内容**的 PowerPoint 模板库。
> MIT License · 可用 `python-pptx` 一键重建。

![风格预览](assets/previews/build-cover.svg)

## 总览

| 指标 | 数值 |
|---|---|
| 演示模板 (.pptx) | **126** 套 |
| 版面页总数 | **2268** 页 |
| 设计风格 | **25** 种 |
| 用途分类 | **24** 个 |
| 母版模板 (.potx) | **25** 套 |
| 每套版面原型 | 15 个（封面/目录/章节/要点/对比/指标/时间线/流程/图表/表格/图集/引用/团队/结尾 等） |

浏览站（GitHub Pages）：<https://fanquanpp.github.io/slide-forge/>

## 目录结构

```
slide-forge/
├─ index.html                 # GitHub Pages 浏览站，可筛选分类、预览风格、直接下载
├─ assets/previews/           # 12 种风格的矢量预览图 (SVG)
├─ templates/                 # 全部可编辑模板 (.pptx) 与索引清单
│  ├─ <分类目录>/<编号>__<风格>.pptx
│  ├─ _potx/slideforge-<风格>.potx
│  └─ index.manifest.json     # 权威清单（分类 / 风格 / 页数）
├─ generator/                 # 生成器与校验脚本 (Python + python-pptx)
│  ├─ themes.py  slidekit.py  build.py  validate.py  requirements.txt
├─ scripts/                   # 站点 / README / 索引重建脚本
├─ docs/                      # 画像报告 / 需求映射 / 安装记录 / 交接运维
├─ .github/workflows/pages.yml
└─ LICENSE  (MIT)
```

## 模板目录

| 分类 | 用途 | 设计风格数 | 套数 |
|---|---|---:|---:|
| 编程教学课件 | Programming Courseware | 5 | 5 |
| 游戏设计提案 | Game Design Proposal | 5 | 5 |
| 像素与美术作品集 | Pixel & Art Portfolio | 5 | 5 |
| 社团活动策划 | Club Event Planning | 6 | 6 |
| 项目汇报与复盘 | Project Report & Retrospective | 5 | 5 |
| 学习笔记分享 | Study Notes Sharing | 5 | 5 |
| 求职简历与自我介绍 | Resume & Self-Intro | 5 | 5 |
| 活动宣传与推广 | Event Promo | 6 | 6 |
| 数据看板与指标 | Data Dashboard | 5 | 5 |
| 内容创作提案 | Creative Pitch | 5 | 5 |
| 产品发布与介绍 | Product Launch | 6 | 6 |
| 读书会与共读分享 | Reading Club | 6 | 6 |
| 竞聘述职与答辩 | Job Competition | 5 | 5 |
| 比赛答辩与路演 | Contest Defense | 5 | 5 |
| 课程大纲与教学计划 | Course Syllabus | 5 | 5 |
| 招新宣讲与纳新 | Recruitment | 6 | 6 |
| 年度总结与规划 | Annual Review | 5 | 5 |
| 培训手册与 SOP | Training Manual | 5 | 5 |
| 用户调研与访谈 | User Research | 5 | 5 |
| 市场与竞品分析 | Market Analysis | 5 | 5 |
| 预算与财务计划 | Budget & Finance | 5 | 5 |
| 旅行与行程计划 | Travel Plan | 6 | 6 |
| 开源项目发布 | Open Source Release | 5 | 5 |
| 技术架构评审 | Tech Architecture Review | 5 | 5 |

### 各分类 · 各风格文件

- **编程教学课件**（Programming Courseware）
  - 呼吸留白极简（11 Build）· 18 页 —— `01-teaching-programming-courseware/01__build.pptx` · 母版 `_potx/slideforge-build.potx`
  - 赛博终端（08 Resn）· 18 页 —— `01-teaching-programming-courseware/01__terminal.pptx` · 母版 `_potx/slideforge-terminal.potx`
  - 柔和科技图表（17 Takram）· 18 页 —— `01-teaching-programming-courseware/01__takram.pptx` · 母版 `_potx/slideforge-takram.potx`
  - 黑板粉笔（15 Ash Thorp）· 18 页 —— `01-teaching-programming-courseware/01__chalk.pptx` · 母版 `_potx/slideforge-chalk.potx`
  - 学术严谨（04 Fathom）· 18 页 —— `01-teaching-programming-courseware/01__academic.pptx` · 母版 `_potx/slideforge-academic.potx`
- **游戏设计提案**（Game Design Proposal）
  - 暗黑霓虹（06 Active Theory）· 18 页 —— `02-game-gdd-game-design-proposal/02__darkneon.pptx` · 母版 `_potx/slideforge-darkneon.potx`
  - 复古像素（16 Territory Studio）· 18 页 —— `02-game-gdd-game-design-proposal/02__retropixel.pptx` · 母版 `_potx/slideforge-retropixel.potx`
  - 商务蓝调（09 Experimental Jetset）· 18 页 —— `02-game-gdd-game-design-proposal/02__corporate.pptx` · 母版 `_potx/slideforge-corporate.potx`
  - 等距信息图（02 Stamen Design）· 18 页 —— `02-game-gdd-game-design-proposal/02__isometric.pptx` · 母版 `_potx/slideforge-isometric.potx`
  - 蒸汽波（06 Active Theory）· 18 页 —— `02-game-gdd-game-design-proposal/02__vaporwave.pptx` · 母版 `_potx/slideforge-vaporwave.potx`
- **像素与美术作品集**（Pixel & Art Portfolio）
  - 杂志编辑（19 Irma Boom）· 18 页 —— `03-portfolio-pixel-art-portfolio/03__editorial.pptx` · 母版 `_potx/slideforge-editorial.potx`
  - 复古像素（16 Territory Studio）· 18 页 —— `03-portfolio-pixel-art-portfolio/03__retropixel.pptx` · 母版 `_potx/slideforge-retropixel.potx`
  - 呼吸留白极简（11 Build）· 18 页 —— `03-portfolio-pixel-art-portfolio/03__build.pptx` · 母版 `_potx/slideforge-build.potx`
  - 孔版双色（19 Irma Boom）· 18 页 —— `03-portfolio-pixel-art-portfolio/03__risograph.pptx` · 母版 `_potx/slideforge-risograph.potx`
  - 轻奢金黑（11 Build）· 18 页 —— `03-portfolio-pixel-art-portfolio/03__luxury.pptx` · 母版 `_potx/slideforge-luxury.potx`
- **社团活动策划**（Club Event Planning）
  - 孟菲斯活力（12 Sagmeister & Walsh）· 18 页 —— `04-club-event-club-event-planning/04__memphis.pptx` · 母版 `_potx/slideforge-memphis.potx`
  - 自然有机（18 Kenya Hara）· 18 页 —— `04-club-event-club-event-planning/04__organic.pptx` · 母版 `_potx/slideforge-organic.potx`
  - 呼吸留白极简（11 Build）· 18 页 —— `04-club-event-club-event-planning/04__build.pptx` · 母版 `_potx/slideforge-build.potx`
  - 马卡龙柔彩（17 Takram）· 18 页 —— `04-club-event-club-event-planning/04__pastel.pptx` · 母版 `_potx/slideforge-pastel.potx`
  - 包豪斯三原色（09 Experimental Jetset）· 18 页 —— `04-club-event-club-event-planning/04__bauhaus.pptx` · 母版 `_potx/slideforge-bauhaus.potx`
  - 泡泡堂风（12 Sagmeister & Walsh）· 18 页 —— `04-club-event-club-event-planning/04__bubble.pptx` · 母版 `_potx/slideforge-bubble.potx`
- **项目汇报与复盘**（Project Report & Retrospective）
  - 数学网格功能主义（10 Müller-Brockmann）· 18 页 —— `05-project-report-project-report-retrospective/05__brockmann.pptx` · 母版 `_potx/slideforge-brockmann.potx`
  - 商务蓝调（09 Experimental Jetset）· 18 页 —— `05-project-report-project-report-retrospective/05__corporate.pptx` · 母版 `_potx/slideforge-corporate.potx`
  - 呼吸留白极简（11 Build）· 18 页 —— `05-project-report-project-report-retrospective/05__build.pptx` · 母版 `_potx/slideforge-build.potx`
  - 北欧灰蓝（03 Information Architects）· 18 页 —— `05-project-report-project-report-retrospective/05__nordic.pptx` · 母版 `_potx/slideforge-nordic.potx`
  - 学术严谨（04 Fathom）· 18 页 —— `05-project-report-project-report-retrospective/05__academic.pptx` · 母版 `_potx/slideforge-academic.potx`
- **学习笔记分享**（Study Notes Sharing）
  - 柔和科技图表（17 Takram）· 18 页 —— `06-study-notes-study-notes-sharing/06__takram.pptx` · 母版 `_potx/slideforge-takram.potx`
  - 自然有机（18 Kenya Hara）· 18 页 —— `06-study-notes-study-notes-sharing/06__organic.pptx` · 母版 `_potx/slideforge-organic.potx`
  - 杂志编辑（19 Irma Boom）· 18 页 —— `06-study-notes-study-notes-sharing/06__editorial.pptx` · 母版 `_potx/slideforge-editorial.potx`
  - 学术严谨（04 Fathom）· 18 页 —— `06-study-notes-study-notes-sharing/06__academic.pptx` · 母版 `_potx/slideforge-academic.potx`
  - 单色印刷极简（03 Information Architects）· 18 页 —— `06-study-notes-study-notes-sharing/06__monochrome.pptx` · 母版 `_potx/slideforge-monochrome.potx`
- **求职简历与自我介绍**（Resume & Self-Intro）
  - 呼吸留白极简（11 Build）· 18 页 —— `07-resume-resume-self-intro/07__build.pptx` · 母版 `_potx/slideforge-build.potx`
  - 杂志编辑（19 Irma Boom）· 18 页 —— `07-resume-resume-self-intro/07__editorial.pptx` · 母版 `_potx/slideforge-editorial.potx`
  - 北欧灰蓝（03 Information Architects）· 18 页 —— `07-resume-resume-self-intro/07__nordic.pptx` · 母版 `_potx/slideforge-nordic.potx`
  - 单色印刷极简（03 Information Architects）· 18 页 —— `07-resume-resume-self-intro/07__monochrome.pptx` · 母版 `_potx/slideforge-monochrome.potx`
  - 轻奢金黑（11 Build）· 18 页 —— `07-resume-resume-self-intro/07__luxury.pptx` · 母版 `_potx/slideforge-luxury.potx`
- **活动宣传与推广**（Event Promo）
  - 孟菲斯活力（12 Sagmeister & Walsh）· 18 页 —— `08-promo-event-promo/08__memphis.pptx` · 母版 `_potx/slideforge-memphis.potx`
  - 玻璃拟态（05 Locomotive）· 18 页 —— `08-promo-event-promo/08__glass.pptx` · 母版 `_potx/slideforge-glass.potx`
  - 暗黑霓虹（06 Active Theory）· 18 页 —— `08-promo-event-promo/08__darkneon.pptx` · 母版 `_potx/slideforge-darkneon.potx`
  - 包豪斯三原色（09 Experimental Jetset）· 18 页 —— `08-promo-event-promo/08__bauhaus.pptx` · 母版 `_potx/slideforge-bauhaus.potx`
  - 马卡龙柔彩（17 Takram）· 18 页 —— `08-promo-event-promo/08__pastel.pptx` · 母版 `_potx/slideforge-pastel.potx`
  - 泡泡堂风（12 Sagmeister & Walsh）· 18 页 —— `08-promo-event-promo/08__bubble.pptx` · 母版 `_potx/slideforge-bubble.potx`
- **数据看板与指标**（Data Dashboard）
  - 商务蓝调（09 Experimental Jetset）· 18 页 —— `09-dashboard-data-dashboard/09__corporate.pptx` · 母版 `_potx/slideforge-corporate.potx`
  - 玻璃拟态（05 Locomotive）· 18 页 —— `09-dashboard-data-dashboard/09__glass.pptx` · 母版 `_potx/slideforge-glass.potx`
  - 柔和科技图表（17 Takram）· 18 页 —— `09-dashboard-data-dashboard/09__takram.pptx` · 母版 `_potx/slideforge-takram.potx`
  - 渐变流体（07 Field.io）· 18 页 —— `09-dashboard-data-dashboard/09__gradient.pptx` · 母版 `_potx/slideforge-gradient.potx`
  - 等距信息图（02 Stamen Design）· 18 页 —— `09-dashboard-data-dashboard/09__isometric.pptx` · 母版 `_potx/slideforge-isometric.potx`
- **内容创作提案**（Creative Pitch）
  - 杂志编辑（19 Irma Boom）· 18 页 —— `10-creative-pitch-creative-pitch/10__editorial.pptx` · 母版 `_potx/slideforge-editorial.potx`
  - 暗黑霓虹（06 Active Theory）· 18 页 —— `10-creative-pitch-creative-pitch/10__darkneon.pptx` · 母版 `_potx/slideforge-darkneon.potx`
  - 自然有机（18 Kenya Hara）· 18 页 —— `10-creative-pitch-creative-pitch/10__organic.pptx` · 母版 `_potx/slideforge-organic.potx`
  - 报纸排版（01 Pentagram）· 18 页 —— `10-creative-pitch-creative-pitch/10__newspaper.pptx` · 母版 `_potx/slideforge-newspaper.potx`
  - 蒸汽波（06 Active Theory）· 18 页 —— `10-creative-pitch-creative-pitch/10__vaporwave.pptx` · 母版 `_potx/slideforge-vaporwave.potx`
- **产品发布与介绍**（Product Launch）
  - 渐变流体（07 Field.io）· 18 页 —— `11-product-launch-product-launch/11__gradient.pptx` · 母版 `_potx/slideforge-gradient.potx`
  - 玻璃拟态（05 Locomotive）· 18 页 —— `11-product-launch-product-launch/11__glass.pptx` · 母版 `_potx/slideforge-glass.potx`
  - 轻奢金黑（11 Build）· 18 页 —— `11-product-launch-product-launch/11__luxury.pptx` · 母版 `_potx/slideforge-luxury.potx`
  - 呼吸留白极简（11 Build）· 18 页 —— `11-product-launch-product-launch/11__build.pptx` · 母版 `_potx/slideforge-build.potx`
  - 暗黑霓虹（06 Active Theory）· 18 页 —— `11-product-launch-product-launch/11__darkneon.pptx` · 母版 `_potx/slideforge-darkneon.potx`
  - 泡泡堂风（12 Sagmeister & Walsh）· 18 页 —— `11-product-launch-product-launch/11__bubble.pptx` · 母版 `_potx/slideforge-bubble.potx`
- **读书会与共读分享**（Reading Club）
  - 杂志编辑（19 Irma Boom）· 18 页 —— `12-reading-club-reading-club/12__editorial.pptx` · 母版 `_potx/slideforge-editorial.potx`
  - 自然有机（18 Kenya Hara）· 18 页 —— `12-reading-club-reading-club/12__organic.pptx` · 母版 `_potx/slideforge-organic.potx`
  - 报纸排版（01 Pentagram）· 18 页 —— `12-reading-club-reading-club/12__newspaper.pptx` · 母版 `_potx/slideforge-newspaper.potx`
  - 马卡龙柔彩（17 Takram）· 18 页 —— `12-reading-club-reading-club/12__pastel.pptx` · 母版 `_potx/slideforge-pastel.potx`
  - 单色印刷极简（03 Information Architects）· 18 页 —— `12-reading-club-reading-club/12__monochrome.pptx` · 母版 `_potx/slideforge-monochrome.potx`
  - 泡泡堂风（12 Sagmeister & Walsh）· 18 页 —— `12-reading-club-reading-club/12__bubble.pptx` · 母版 `_potx/slideforge-bubble.potx`
- **竞聘述职与答辩**（Job Competition）
  - 商务蓝调（09 Experimental Jetset）· 18 页 —— `13-job-competition-job-competition/13__corporate.pptx` · 母版 `_potx/slideforge-corporate.potx`
  - 呼吸留白极简（11 Build）· 18 页 —— `13-job-competition-job-competition/13__build.pptx` · 母版 `_potx/slideforge-build.potx`
  - 数学网格功能主义（10 Müller-Brockmann）· 18 页 —— `13-job-competition-job-competition/13__brockmann.pptx` · 母版 `_potx/slideforge-brockmann.potx`
  - 学术严谨（04 Fathom）· 18 页 —— `13-job-competition-job-competition/13__academic.pptx` · 母版 `_potx/slideforge-academic.potx`
  - 北欧灰蓝（03 Information Architects）· 18 页 —— `13-job-competition-job-competition/13__nordic.pptx` · 母版 `_potx/slideforge-nordic.potx`
- **比赛答辩与路演**（Contest Defense）
  - 数学网格功能主义（10 Müller-Brockmann）· 18 页 —— `14-contest-defense-contest-defense/14__brockmann.pptx` · 母版 `_potx/slideforge-brockmann.potx`
  - 渐变流体（07 Field.io）· 18 页 —— `14-contest-defense-contest-defense/14__gradient.pptx` · 母版 `_potx/slideforge-gradient.potx`
  - 商务蓝调（09 Experimental Jetset）· 18 页 —— `14-contest-defense-contest-defense/14__corporate.pptx` · 母版 `_potx/slideforge-corporate.potx`
  - 暗黑霓虹（06 Active Theory）· 18 页 —— `14-contest-defense-contest-defense/14__darkneon.pptx` · 母版 `_potx/slideforge-darkneon.potx`
  - 工程蓝图（14 Raven Kwok）· 18 页 —— `14-contest-defense-contest-defense/14__blueprint.pptx` · 母版 `_potx/slideforge-blueprint.potx`
- **课程大纲与教学计划**（Course Syllabus）
  - 学术严谨（04 Fathom）· 18 页 —— `15-course-syllabus-course-syllabus/15__academic.pptx` · 母版 `_potx/slideforge-academic.potx`
  - 柔和科技图表（17 Takram）· 18 页 —— `15-course-syllabus-course-syllabus/15__takram.pptx` · 母版 `_potx/slideforge-takram.potx`
  - 北欧灰蓝（03 Information Architects）· 18 页 —— `15-course-syllabus-course-syllabus/15__nordic.pptx` · 母版 `_potx/slideforge-nordic.potx`
  - 黑板粉笔（15 Ash Thorp）· 18 页 —— `15-course-syllabus-course-syllabus/15__chalk.pptx` · 母版 `_potx/slideforge-chalk.potx`
  - 等距信息图（02 Stamen Design）· 18 页 —— `15-course-syllabus-course-syllabus/15__isometric.pptx` · 母版 `_potx/slideforge-isometric.potx`
- **招新宣讲与纳新**（Recruitment）
  - 孟菲斯活力（12 Sagmeister & Walsh）· 18 页 —— `16-recruitment-recruitment/16__memphis.pptx` · 母版 `_potx/slideforge-memphis.potx`
  - 马卡龙柔彩（17 Takram）· 18 页 —— `16-recruitment-recruitment/16__pastel.pptx` · 母版 `_potx/slideforge-pastel.potx`
  - 包豪斯三原色（09 Experimental Jetset）· 18 页 —— `16-recruitment-recruitment/16__bauhaus.pptx` · 母版 `_potx/slideforge-bauhaus.potx`
  - 玻璃拟态（05 Locomotive）· 18 页 —— `16-recruitment-recruitment/16__glass.pptx` · 母版 `_potx/slideforge-glass.potx`
  - 蒸汽波（06 Active Theory）· 18 页 —— `16-recruitment-recruitment/16__vaporwave.pptx` · 母版 `_potx/slideforge-vaporwave.potx`
  - 泡泡堂风（12 Sagmeister & Walsh）· 18 页 —— `16-recruitment-recruitment/16__bubble.pptx` · 母版 `_potx/slideforge-bubble.potx`
- **年度总结与规划**（Annual Review）
  - 报纸排版（01 Pentagram）· 18 页 —— `17-annual-review-annual-review/17__newspaper.pptx` · 母版 `_potx/slideforge-newspaper.potx`
  - 杂志编辑（19 Irma Boom）· 18 页 —— `17-annual-review-annual-review/17__editorial.pptx` · 母版 `_potx/slideforge-editorial.potx`
  - 商务蓝调（09 Experimental Jetset）· 18 页 —— `17-annual-review-annual-review/17__corporate.pptx` · 母版 `_potx/slideforge-corporate.potx`
  - 单色印刷极简（03 Information Architects）· 18 页 —— `17-annual-review-annual-review/17__monochrome.pptx` · 母版 `_potx/slideforge-monochrome.potx`
  - 渐变流体（07 Field.io）· 18 页 —— `17-annual-review-annual-review/17__gradient.pptx` · 母版 `_potx/slideforge-gradient.potx`
- **培训手册与 SOP**（Training Manual）
  - 单色印刷极简（03 Information Architects）· 18 页 —— `18-training-manual-training-manual/18__monochrome.pptx` · 母版 `_potx/slideforge-monochrome.potx`
  - 北欧灰蓝（03 Information Architects）· 18 页 —— `18-training-manual-training-manual/18__nordic.pptx` · 母版 `_potx/slideforge-nordic.potx`
  - 学术严谨（04 Fathom）· 18 页 —— `18-training-manual-training-manual/18__academic.pptx` · 母版 `_potx/slideforge-academic.potx`
  - 等距信息图（02 Stamen Design）· 18 页 —— `18-training-manual-training-manual/18__isometric.pptx` · 母版 `_potx/slideforge-isometric.potx`
  - 黑板粉笔（15 Ash Thorp）· 18 页 —— `18-training-manual-training-manual/18__chalk.pptx` · 母版 `_potx/slideforge-chalk.potx`
- **用户调研与访谈**（User Research）
  - 柔和科技图表（17 Takram）· 18 页 —— `19-user-research-user-research/19__takram.pptx` · 母版 `_potx/slideforge-takram.potx`
  - 北欧灰蓝（03 Information Architects）· 18 页 —— `19-user-research-user-research/19__nordic.pptx` · 母版 `_potx/slideforge-nordic.potx`
  - 学术严谨（04 Fathom）· 18 页 —— `19-user-research-user-research/19__academic.pptx` · 母版 `_potx/slideforge-academic.potx`
  - 自然有机（18 Kenya Hara）· 18 页 —— `19-user-research-user-research/19__organic.pptx` · 母版 `_potx/slideforge-organic.potx`
  - 单色印刷极简（03 Information Architects）· 18 页 —— `19-user-research-user-research/19__monochrome.pptx` · 母版 `_potx/slideforge-monochrome.potx`
- **市场与竞品分析**（Market Analysis）
  - 商务蓝调（09 Experimental Jetset）· 18 页 —— `20-market-analysis-market-analysis/20__corporate.pptx` · 母版 `_potx/slideforge-corporate.potx`
  - 数学网格功能主义（10 Müller-Brockmann）· 18 页 —— `20-market-analysis-market-analysis/20__brockmann.pptx` · 母版 `_potx/slideforge-brockmann.potx`
  - 渐变流体（07 Field.io）· 18 页 —— `20-market-analysis-market-analysis/20__gradient.pptx` · 母版 `_potx/slideforge-gradient.potx`
  - 报纸排版（01 Pentagram）· 18 页 —— `20-market-analysis-market-analysis/20__newspaper.pptx` · 母版 `_potx/slideforge-newspaper.potx`
  - 玻璃拟态（05 Locomotive）· 18 页 —— `20-market-analysis-market-analysis/20__glass.pptx` · 母版 `_potx/slideforge-glass.potx`
- **预算与财务计划**（Budget & Finance）
  - 数学网格功能主义（10 Müller-Brockmann）· 18 页 —— `21-budget-plan-budget-finance/21__brockmann.pptx` · 母版 `_potx/slideforge-brockmann.potx`
  - 商务蓝调（09 Experimental Jetset）· 18 页 —— `21-budget-plan-budget-finance/21__corporate.pptx` · 母版 `_potx/slideforge-corporate.potx`
  - 等距信息图（02 Stamen Design）· 18 页 —— `21-budget-plan-budget-finance/21__isometric.pptx` · 母版 `_potx/slideforge-isometric.potx`
  - 单色印刷极简（03 Information Architects）· 18 页 —— `21-budget-plan-budget-finance/21__monochrome.pptx` · 母版 `_potx/slideforge-monochrome.potx`
  - 北欧灰蓝（03 Information Architects）· 18 页 —— `21-budget-plan-budget-finance/21__nordic.pptx` · 母版 `_potx/slideforge-nordic.potx`
- **旅行与行程计划**（Travel Plan）
  - 自然有机（18 Kenya Hara）· 18 页 —— `22-travel-plan-travel-plan/22__organic.pptx` · 母版 `_potx/slideforge-organic.potx`
  - 马卡龙柔彩（17 Takram）· 18 页 —— `22-travel-plan-travel-plan/22__pastel.pptx` · 母版 `_potx/slideforge-pastel.potx`
  - 杂志编辑（19 Irma Boom）· 18 页 —— `22-travel-plan-travel-plan/22__editorial.pptx` · 母版 `_potx/slideforge-editorial.potx`
  - 孔版双色（19 Irma Boom）· 18 页 —— `22-travel-plan-travel-plan/22__risograph.pptx` · 母版 `_potx/slideforge-risograph.potx`
  - 蒸汽波（06 Active Theory）· 18 页 —— `22-travel-plan-travel-plan/22__vaporwave.pptx` · 母版 `_potx/slideforge-vaporwave.potx`
  - 泡泡堂风（12 Sagmeister & Walsh）· 18 页 —— `22-travel-plan-travel-plan/22__bubble.pptx` · 母版 `_potx/slideforge-bubble.potx`
- **开源项目发布**（Open Source Release）
  - 赛博终端（08 Resn）· 18 页 —— `23-open-source-release-open-source-release/23__terminal.pptx` · 母版 `_potx/slideforge-terminal.potx`
  - 工程蓝图（14 Raven Kwok）· 18 页 —— `23-open-source-release-open-source-release/23__blueprint.pptx` · 母版 `_potx/slideforge-blueprint.potx`
  - 暗黑霓虹（06 Active Theory）· 18 页 —— `23-open-source-release-open-source-release/23__darkneon.pptx` · 母版 `_potx/slideforge-darkneon.potx`
  - 单色印刷极简（03 Information Architects）· 18 页 —— `23-open-source-release-open-source-release/23__monochrome.pptx` · 母版 `_potx/slideforge-monochrome.potx`
  - 渐变流体（07 Field.io）· 18 页 —— `23-open-source-release-open-source-release/23__gradient.pptx` · 母版 `_potx/slideforge-gradient.potx`
- **技术架构评审**（Tech Architecture Review）
  - 工程蓝图（14 Raven Kwok）· 18 页 —— `24-tech-review-tech-architecture-review/24__blueprint.pptx` · 母版 `_potx/slideforge-blueprint.potx`
  - 等距信息图（02 Stamen Design）· 18 页 —— `24-tech-review-tech-architecture-review/24__isometric.pptx` · 母版 `_potx/slideforge-isometric.potx`
  - 数学网格功能主义（10 Müller-Brockmann）· 18 页 —— `24-tech-review-tech-architecture-review/24__brockmann.pptx` · 母版 `_potx/slideforge-brockmann.potx`
  - 赛博终端（08 Resn）· 18 页 —— `24-tech-review-tech-architecture-review/24__terminal.pptx` · 母版 `_potx/slideforge-terminal.potx`
  - 单色印刷极简（03 Information Architects）· 18 页 —— `24-tech-review-tech-architecture-review/24__monochrome.pptx` · 母版 `_potx/slideforge-monochrome.potx`

## 设计风格

| 风格 | 英文 | 审美锚点 | 说明 |
|---|---|---|---|
| 呼吸留白极简 | Breathing Whitespace | 11 Build | 大量留白 + 单一强调色，克制中性，便于替换成任意品牌色。 |
| 数学网格功能主义 | Swiss Grid | 10 Müller-Brockmann | 严格网格与对齐，双色体系，适合数据、计划与结构化汇报。 |
| 柔和科技图表 | Soft Tech | 17 Takram | 圆角、柔影与图表即艺术，适合作品集、产品提案与数据看板。 |
| 商务蓝调 | Corporate Blue | 09 Experimental Jetset | 沉稳海军蓝 + 金色点缀，适合汇报、方案与数据看板。 |
| 暗黑霓虹 | Dark Neon | 06 Active Theory | 深空底色 + 霓虹青/品红，适合游戏提案、发布与科技主题。 |
| 复古像素 | Retro Pixel | 16 Territory Studio | 暗紫底 + 糖果色块，呼应像素美术与独立游戏审美。 |
| 杂志编辑 | Editorial | 19 Irma Boom | 暖纸底 + 砖红点缀，衬线标题，适合作品集与深度叙事。 |
| 孟菲斯活力 | Memphis Pop | 12 Sagmeister & Walsh | 高饱和撞色 + 几何形状，适合活动宣传与轻松场景。 |
| 玻璃拟态 | Glassmorphism | 05 Locomotive | 深色渐变 + 半透明卡片，适合产品发布与科技展示。 |
| 赛博终端 | Cyber Terminal | 08 Resn | 黑底绿字等宽，命令行气质，适合技术教学与极客分享。 |
| 自然有机 | Organic | 18 Kenya Hara | 暖砂底 + 植物绿/陶土色，柔和圆角，适合笔记与生活方式主题。 |
| 学术严谨 | Academic | 04 Fathom | 冷静灰蓝 + 严谨结构，适合研究、课件与数据报告。 |
| 单色印刷极简 | Monochrome | 03 Information Architects | 黑白灰三阶，靠字号与留白分级，极致克制。 |
| 工程蓝图 | Blueprint | 14 Raven Kwok | 深蓝底 + 白色线稿与网格，工程/架构语境。 |
| 马卡龙柔彩 | Pastel | 17 Takram | 低饱和柔彩 + 圆角，轻盈亲和，适合教学与生活主题。 |
| 轻奢金黑 | Luxury Noir | 11 Build | 近黑底 + 香槟金细线，高端质感，适合品牌与高端方案。 |
| 蒸汽波 | Vaporwave | 06 Active Theory | 紫粉青渐变 + 霓虹，复古未来感，适合潮流与娱乐主题。 |
| 孔版双色 | Risograph | 19 Irma Boom | 双色错版叠加，纸张质感，适合作品集与独立出版。 |
| 包豪斯三原色 | Bauhaus | 09 Experimental Jetset | 红黄蓝 + 黑白，几何构成，强形式感。 |
| 北欧灰蓝 | Nordic | 03 Information Architects | 冷灰蓝 + 米白，安静克制，适合调研与说明类内容。 |
| 等距信息图 | Isometric | 02 Stamen Design | 等距网格与块状图形，信息图像化，适合流程与结构说明。 |
| 渐变流体 | Gradient Flow | 07 Field.io | 柔和渐变与流形色块，现代产品感，适合发布与介绍。 |
| 报纸排版 | Newspaper | 01 Pentagram | 多栏密排 + 衬线标题 + 细规线，信息密度高，适合综述与年鉴。 |
| 黑板粉笔 | Chalkboard | 15 Ash Thorp | 深墨绿黑板 + 粉笔白黄，课堂气质，适合教学与讲解。 |
| 泡泡堂风 | Bubble Pop | 12 Sagmeister & Walsh | 极简底色 + 糖果色气泡与弹性动效，明快圆润、强互动趣味。 |

## 使用指南

1. **直接编辑**：下载 `.pptx`，用 PowerPoint / WPS / Keynote / LibreOffice 打开。文本、形状、
   配色、图片占位框均可直接修改，不破坏版式。`.potx` 放入模板目录后可直接「新建」。
2. **换配色 / 字体**：页面颜色写在各形状上，批量替换主题色即可全局换肤；
   标题 / 正文字体在 `generator/themes.py` 的 `title_font / body_font` 定义。
3. **重新生成**：

```bash
pip install -r generator/requirements.txt
python generator/build.py templates     # 生成全部模板 + index.manifest.json
python generator/validate.py templates  # 校验可打开性 / 版面数 / 内容类型
python scripts/build_site.py            # 重建 index.html 与风格预览图
python scripts/build_readme.py          # 重建本 README
```

## 文档

> 隐私说明：本仓库**不包含**任何本机 / U 盘目录清单、扫描结果或个人报告；模板与文档均为通用产物。
- [需求 → 模板映射表](docs/need-template-mapping.md)
- [工具链安装记录](docs/install-record.md)
- [主清单台账](docs/CATALOG.md) · [覆盖矩阵](docs/coverage-matrix.md) · [逐条使用说明](docs/USAGE.md)
- [抽样质检报告](docs/qa-report.md) · [异常与回滚](docs/rollback.md) · [交接文档](docs/handoff.md) · [验收汇总](docs/acceptance-summary.md)
- [交接与运维手册](docs/handoff-ops.md)
- [动效规范](docs/animation-spec.md) · [导出与回滚说明](docs/export-notes.md) · [设计/演示/动画 Skills 调研](docs/research-skills.md)
- [前端迭代台账](docs/iteration-log.md) · [交付前复核清单](docs/review-checklist.md)

## 许可

本项目以 **MIT License** 发布，可自由用于个人与商业用途，详见 [LICENSE](LICENSE)。

模板内**不含**任何真实业务数据、客户信息或受版权保护的第三方素材；字体依赖系统字体，
如需替换为商用字体，请自行确认授权。

---

由 `python-pptx` 脚本生成 · SlideForge · https://github.com/fanquanpp/slide-forge
