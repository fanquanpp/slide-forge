# SlideForge · 多用途可编辑 PPT 模板库

> 脚本生成的多用途、多风格、**可编辑**且**不含正式内容**的 PowerPoint 模板库。
> MIT License · 可用 `python-pptx` 一键重建。

![风格预览](assets/previews/build-cover.svg)

## 总览

| 指标 | 数值 |
|---|---|
| 演示模板 (.pptx) | **30** 套 |
| 版面页总数 | **450** 页 |
| 设计风格 | **12** 种 |
| 用途分类 | **10** 个 |
| 母版模板 (.potx) | **12** 套 |
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
| 编程教学课件 | Programming Courseware | 3 | 3 |
| 游戏设计提案 | Game Design Proposal | 3 | 3 |
| 像素与美术作品集 | Pixel & Art Portfolio | 3 | 3 |
| 社团活动策划 | Club Event Planning | 3 | 3 |
| 项目汇报与复盘 | Project Report & Retrospective | 3 | 3 |
| 学习笔记分享 | Study Notes Sharing | 4 | 4 |
| 求职简历与自我介绍 | Resume & Self-Intro | 2 | 2 |
| 活动宣传与推广 | Event Promo | 3 | 3 |
| 数据看板与指标 | Data Dashboard | 3 | 3 |
| 内容创作提案 | Creative Pitch | 3 | 3 |

### 各分类 · 各风格文件

- **编程教学课件**（Programming Courseware）
  - 呼吸留白极简（11 Build）· 15 页 —— `01-teaching-programming-courseware/01__build.pptx` · 母版 `_potx/slideforge-build.potx`
  - 赛博终端（08 Resn）· 15 页 —— `01-teaching-programming-courseware/01__terminal.pptx` · 母版 `_potx/slideforge-terminal.potx`
  - 柔和科技图表（17 Takram）· 15 页 —— `01-teaching-programming-courseware/01__takram.pptx` · 母版 `_potx/slideforge-takram.potx`
- **游戏设计提案**（Game Design Proposal）
  - 暗黑霓虹（06 Active Theory）· 15 页 —— `02-game-gdd-game-design-proposal/02__darkneon.pptx` · 母版 `_potx/slideforge-darkneon.potx`
  - 复古像素（16 Territory Studio）· 15 页 —— `02-game-gdd-game-design-proposal/02__retropixel.pptx` · 母版 `_potx/slideforge-retropixel.potx`
  - 商务蓝调（09 Experimental Jetset）· 15 页 —— `02-game-gdd-game-design-proposal/02__corporate.pptx` · 母版 `_potx/slideforge-corporate.potx`
- **像素与美术作品集**（Pixel & Art Portfolio）
  - 杂志编辑（19 Irma Boom）· 15 页 —— `03-portfolio-pixel-art-portfolio/03__editorial.pptx` · 母版 `_potx/slideforge-editorial.potx`
  - 复古像素（16 Territory Studio）· 15 页 —— `03-portfolio-pixel-art-portfolio/03__retropixel.pptx` · 母版 `_potx/slideforge-retropixel.potx`
  - 呼吸留白极简（11 Build）· 15 页 —— `03-portfolio-pixel-art-portfolio/03__build.pptx` · 母版 `_potx/slideforge-build.potx`
- **社团活动策划**（Club Event Planning）
  - 孟菲斯活力（12 Sagmeister & Walsh）· 15 页 —— `04-club-event-club-event-planning/04__memphis.pptx` · 母版 `_potx/slideforge-memphis.potx`
  - 自然有机（18 Kenya Hara）· 15 页 —— `04-club-event-club-event-planning/04__organic.pptx` · 母版 `_potx/slideforge-organic.potx`
  - 呼吸留白极简（11 Build）· 15 页 —— `04-club-event-club-event-planning/04__build.pptx` · 母版 `_potx/slideforge-build.potx`
- **项目汇报与复盘**（Project Report & Retrospective）
  - 数学网格功能主义（10 Müller-Brockmann）· 15 页 —— `05-project-report-project-report-retrospective/05__brockmann.pptx` · 母版 `_potx/slideforge-brockmann.potx`
  - 商务蓝调（09 Experimental Jetset）· 15 页 —— `05-project-report-project-report-retrospective/05__corporate.pptx` · 母版 `_potx/slideforge-corporate.potx`
  - 呼吸留白极简（11 Build）· 15 页 —— `05-project-report-project-report-retrospective/05__build.pptx` · 母版 `_potx/slideforge-build.potx`
- **学习笔记分享**（Study Notes Sharing）
  - 柔和科技图表（17 Takram）· 15 页 —— `06-study-notes-study-notes-sharing/06__takram.pptx` · 母版 `_potx/slideforge-takram.potx`
  - 自然有机（18 Kenya Hara）· 15 页 —— `06-study-notes-study-notes-sharing/06__organic.pptx` · 母版 `_potx/slideforge-organic.potx`
  - 杂志编辑（19 Irma Boom）· 15 页 —— `06-study-notes-study-notes-sharing/06__editorial.pptx` · 母版 `_potx/slideforge-editorial.potx`
  - 学术严谨（04 Fathom）· 15 页 —— `06-study-notes-study-notes-sharing/06__academic.pptx` · 母版 `_potx/slideforge-academic.potx`
- **求职简历与自我介绍**（Resume & Self-Intro）
  - 呼吸留白极简（11 Build）· 15 页 —— `07-resume-resume-self-intro/07__build.pptx` · 母版 `_potx/slideforge-build.potx`
  - 杂志编辑（19 Irma Boom）· 15 页 —— `07-resume-resume-self-intro/07__editorial.pptx` · 母版 `_potx/slideforge-editorial.potx`
- **活动宣传与推广**（Event Promo）
  - 孟菲斯活力（12 Sagmeister & Walsh）· 15 页 —— `08-promo-event-promo/08__memphis.pptx` · 母版 `_potx/slideforge-memphis.potx`
  - 玻璃拟态（05 Locomotive）· 15 页 —— `08-promo-event-promo/08__glass.pptx` · 母版 `_potx/slideforge-glass.potx`
  - 暗黑霓虹（06 Active Theory）· 15 页 —— `08-promo-event-promo/08__darkneon.pptx` · 母版 `_potx/slideforge-darkneon.potx`
- **数据看板与指标**（Data Dashboard）
  - 商务蓝调（09 Experimental Jetset）· 15 页 —— `09-dashboard-data-dashboard/09__corporate.pptx` · 母版 `_potx/slideforge-corporate.potx`
  - 玻璃拟态（05 Locomotive）· 15 页 —— `09-dashboard-data-dashboard/09__glass.pptx` · 母版 `_potx/slideforge-glass.potx`
  - 柔和科技图表（17 Takram）· 15 页 —— `09-dashboard-data-dashboard/09__takram.pptx` · 母版 `_potx/slideforge-takram.potx`
- **内容创作提案**（Creative Pitch）
  - 杂志编辑（19 Irma Boom）· 15 页 —— `10-creative-pitch-creative-pitch/10__editorial.pptx` · 母版 `_potx/slideforge-editorial.potx`
  - 暗黑霓虹（06 Active Theory）· 15 页 —— `10-creative-pitch-creative-pitch/10__darkneon.pptx` · 母版 `_potx/slideforge-darkneon.potx`
  - 自然有机（18 Kenya Hara）· 15 页 —— `10-creative-pitch-creative-pitch/10__organic.pptx` · 母版 `_potx/slideforge-organic.potx`

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

- [本机与 U 盘目录画像报告](docs/inventory-profile.md)（仅聚合统计，不含隐私）
- [需求 → 模板映射表](docs/need-template-mapping.md)
- [工具链安装记录](docs/install-record.md)
- [交接与运维手册](docs/handoff-ops.md)

## 许可

本项目以 **MIT License** 发布，可自由用于个人与商业用途，详见 [LICENSE](LICENSE)。

模板内**不含**任何真实业务数据、客户信息或受版权保护的第三方素材；字体依赖系统字体，
如需替换为商用字体，请自行确认授权。

---

由 `python-pptx` 脚本生成 · SlideForge · https://github.com/fanquanpp/slide-forge
