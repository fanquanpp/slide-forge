[中文](README.md) · **English**

# SlideForge · A multi-purpose, editable PowerPoint template library
> A script-generated, multi-purpose, multi-style library of PowerPoint templates that is **editable** and **contains no final content**.
> MIT License · rebuildable in one command with `python-pptx`.

![Style preview](assets/previews/build-cover.svg)

## Overview
| Metric | Value |
|---|---|
| Presentation templates (.pptx) | **126** |
| Total layout slides | **2394** |
| Design styles | **25** |
| Use-case categories | **24** |
| Master templates (.potx) | **25** |
| Layout archetypes per deck | 15 (cover / agenda / section / key points / comparison / metrics / timeline / process / chart / table / gallery / quote / team / closing, etc.) |

Browsing site (GitHub Pages): <https://fanquanpp.github.io/slide-forge/>

## Directory structure
```
slide-forge/
├─ index.html                 # GitHub Pages browsing site: filter by category, preview styles, download directly
├─ assets/previews/           # vector preview images for 12 styles (SVG)
├─ templates/                 # all editable templates (.pptx) plus the index manifest
│  ├─ <category-dir>/<number>__<style>.pptx
│  ├─ _potx/slideforge-<style>.potx
│  └─ index.manifest.json     # authoritative manifest (categories / styles / page counts)
├─ generator/                 # generator and validation scripts (Python + python-pptx)
│  ├─ themes.py  slidekit.py  build.py  validate.py  requirements.txt
├─ scripts/                   # site / README / index rebuild scripts
├─ docs/                      # profile reports / requirements mapping / install log / handoff & ops
├─ .github/workflows/pages.yml
└─ LICENSE  (MIT)
```

## Template catalogue
| Category | Use case | Design styles | Decks |
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

### Files by category and style
- **Programming Courseware**
  - Breathing Whitespace (11 Build) · 19 slides — `01-teaching-programming-courseware/01__build.pptx` · master `_potx/slideforge-build.potx`
  - Cyber Terminal (08 Resn) · 19 slides — `01-teaching-programming-courseware/01__terminal.pptx` · master `_potx/slideforge-terminal.potx`
  - Soft Tech (17 Takram) · 19 slides — `01-teaching-programming-courseware/01__takram.pptx` · master `_potx/slideforge-takram.potx`
  - Chalkboard (15 Ash Thorp) · 19 slides — `01-teaching-programming-courseware/01__chalk.pptx` · master `_potx/slideforge-chalk.potx`
  - Academic (04 Fathom) · 19 slides — `01-teaching-programming-courseware/01__academic.pptx` · master `_potx/slideforge-academic.potx`
- **Game Design Proposal**
  - Dark Neon (06 Active Theory) · 19 slides — `02-game-gdd-game-design-proposal/02__darkneon.pptx` · master `_potx/slideforge-darkneon.potx`
  - Retro Pixel (16 Territory Studio) · 19 slides — `02-game-gdd-game-design-proposal/02__retropixel.pptx` · master `_potx/slideforge-retropixel.potx`
  - Corporate Blue (09 Experimental Jetset) · 19 slides — `02-game-gdd-game-design-proposal/02__corporate.pptx` · master `_potx/slideforge-corporate.potx`
  - Isometric (02 Stamen Design) · 19 slides — `02-game-gdd-game-design-proposal/02__isometric.pptx` · master `_potx/slideforge-isometric.potx`
  - Vaporwave (06 Active Theory) · 19 slides — `02-game-gdd-game-design-proposal/02__vaporwave.pptx` · master `_potx/slideforge-vaporwave.potx`
- **Pixel & Art Portfolio**
  - Editorial (19 Irma Boom) · 19 slides — `03-portfolio-pixel-art-portfolio/03__editorial.pptx` · master `_potx/slideforge-editorial.potx`
  - Retro Pixel (16 Territory Studio) · 19 slides — `03-portfolio-pixel-art-portfolio/03__retropixel.pptx` · master `_potx/slideforge-retropixel.potx`
  - Breathing Whitespace (11 Build) · 19 slides — `03-portfolio-pixel-art-portfolio/03__build.pptx` · master `_potx/slideforge-build.potx`
  - Risograph (19 Irma Boom) · 19 slides — `03-portfolio-pixel-art-portfolio/03__risograph.pptx` · master `_potx/slideforge-risograph.potx`
  - Luxury Noir (11 Build) · 19 slides — `03-portfolio-pixel-art-portfolio/03__luxury.pptx` · master `_potx/slideforge-luxury.potx`
- **Club Event Planning**
  - Memphis Pop (12 Sagmeister & Walsh) · 19 slides — `04-club-event-club-event-planning/04__memphis.pptx` · master `_potx/slideforge-memphis.potx`
  - Organic (18 Kenya Hara) · 19 slides — `04-club-event-club-event-planning/04__organic.pptx` · master `_potx/slideforge-organic.potx`
  - Breathing Whitespace (11 Build) · 19 slides — `04-club-event-club-event-planning/04__build.pptx` · master `_potx/slideforge-build.potx`
  - Pastel (17 Takram) · 19 slides — `04-club-event-club-event-planning/04__pastel.pptx` · master `_potx/slideforge-pastel.potx`
  - Bauhaus (09 Experimental Jetset) · 19 slides — `04-club-event-club-event-planning/04__bauhaus.pptx` · master `_potx/slideforge-bauhaus.potx`
  - Bubble Pop (12 Sagmeister & Walsh) · 19 slides — `04-club-event-club-event-planning/04__bubble.pptx` · master `_potx/slideforge-bubble.potx`
- **Project Report & Retrospective**
  - Swiss Grid (10 Müller-Brockmann) · 19 slides — `05-project-report-project-report-retrospective/05__brockmann.pptx` · master `_potx/slideforge-brockmann.potx`
  - Corporate Blue (09 Experimental Jetset) · 19 slides — `05-project-report-project-report-retrospective/05__corporate.pptx` · master `_potx/slideforge-corporate.potx`
  - Breathing Whitespace (11 Build) · 19 slides — `05-project-report-project-report-retrospective/05__build.pptx` · master `_potx/slideforge-build.potx`
  - Nordic (03 Information Architects) · 19 slides — `05-project-report-project-report-retrospective/05__nordic.pptx` · master `_potx/slideforge-nordic.potx`
  - Academic (04 Fathom) · 19 slides — `05-project-report-project-report-retrospective/05__academic.pptx` · master `_potx/slideforge-academic.potx`
- **Study Notes Sharing**
  - Soft Tech (17 Takram) · 19 slides — `06-study-notes-study-notes-sharing/06__takram.pptx` · master `_potx/slideforge-takram.potx`
  - Organic (18 Kenya Hara) · 19 slides — `06-study-notes-study-notes-sharing/06__organic.pptx` · master `_potx/slideforge-organic.potx`
  - Editorial (19 Irma Boom) · 19 slides — `06-study-notes-study-notes-sharing/06__editorial.pptx` · master `_potx/slideforge-editorial.potx`
  - Academic (04 Fathom) · 19 slides — `06-study-notes-study-notes-sharing/06__academic.pptx` · master `_potx/slideforge-academic.potx`
  - Monochrome (03 Information Architects) · 19 slides — `06-study-notes-study-notes-sharing/06__monochrome.pptx` · master `_potx/slideforge-monochrome.potx`
- **Resume & Self-Intro**
  - Breathing Whitespace (11 Build) · 19 slides — `07-resume-resume-self-intro/07__build.pptx` · master `_potx/slideforge-build.potx`
  - Editorial (19 Irma Boom) · 19 slides — `07-resume-resume-self-intro/07__editorial.pptx` · master `_potx/slideforge-editorial.potx`
  - Nordic (03 Information Architects) · 19 slides — `07-resume-resume-self-intro/07__nordic.pptx` · master `_potx/slideforge-nordic.potx`
  - Monochrome (03 Information Architects) · 19 slides — `07-resume-resume-self-intro/07__monochrome.pptx` · master `_potx/slideforge-monochrome.potx`
  - Luxury Noir (11 Build) · 19 slides — `07-resume-resume-self-intro/07__luxury.pptx` · master `_potx/slideforge-luxury.potx`
- **Event Promo**
  - Memphis Pop (12 Sagmeister & Walsh) · 19 slides — `08-promo-event-promo/08__memphis.pptx` · master `_potx/slideforge-memphis.potx`
  - Glassmorphism (05 Locomotive) · 19 slides — `08-promo-event-promo/08__glass.pptx` · master `_potx/slideforge-glass.potx`
  - Dark Neon (06 Active Theory) · 19 slides — `08-promo-event-promo/08__darkneon.pptx` · master `_potx/slideforge-darkneon.potx`
  - Bauhaus (09 Experimental Jetset) · 19 slides — `08-promo-event-promo/08__bauhaus.pptx` · master `_potx/slideforge-bauhaus.potx`
  - Pastel (17 Takram) · 19 slides — `08-promo-event-promo/08__pastel.pptx` · master `_potx/slideforge-pastel.potx`
  - Bubble Pop (12 Sagmeister & Walsh) · 19 slides — `08-promo-event-promo/08__bubble.pptx` · master `_potx/slideforge-bubble.potx`
- **Data Dashboard**
  - Corporate Blue (09 Experimental Jetset) · 19 slides — `09-dashboard-data-dashboard/09__corporate.pptx` · master `_potx/slideforge-corporate.potx`
  - Glassmorphism (05 Locomotive) · 19 slides — `09-dashboard-data-dashboard/09__glass.pptx` · master `_potx/slideforge-glass.potx`
  - Soft Tech (17 Takram) · 19 slides — `09-dashboard-data-dashboard/09__takram.pptx` · master `_potx/slideforge-takram.potx`
  - Gradient Flow (07 Field.io) · 19 slides — `09-dashboard-data-dashboard/09__gradient.pptx` · master `_potx/slideforge-gradient.potx`
  - Isometric (02 Stamen Design) · 19 slides — `09-dashboard-data-dashboard/09__isometric.pptx` · master `_potx/slideforge-isometric.potx`
- **Creative Pitch**
  - Editorial (19 Irma Boom) · 19 slides — `10-creative-pitch-creative-pitch/10__editorial.pptx` · master `_potx/slideforge-editorial.potx`
  - Dark Neon (06 Active Theory) · 19 slides — `10-creative-pitch-creative-pitch/10__darkneon.pptx` · master `_potx/slideforge-darkneon.potx`
  - Organic (18 Kenya Hara) · 19 slides — `10-creative-pitch-creative-pitch/10__organic.pptx` · master `_potx/slideforge-organic.potx`
  - Newspaper (01 Pentagram) · 19 slides — `10-creative-pitch-creative-pitch/10__newspaper.pptx` · master `_potx/slideforge-newspaper.potx`
  - Vaporwave (06 Active Theory) · 19 slides — `10-creative-pitch-creative-pitch/10__vaporwave.pptx` · master `_potx/slideforge-vaporwave.potx`
- **Product Launch**
  - Gradient Flow (07 Field.io) · 19 slides — `11-product-launch-product-launch/11__gradient.pptx` · master `_potx/slideforge-gradient.potx`
  - Glassmorphism (05 Locomotive) · 19 slides — `11-product-launch-product-launch/11__glass.pptx` · master `_potx/slideforge-glass.potx`
  - Luxury Noir (11 Build) · 19 slides — `11-product-launch-product-launch/11__luxury.pptx` · master `_potx/slideforge-luxury.potx`
  - Breathing Whitespace (11 Build) · 19 slides — `11-product-launch-product-launch/11__build.pptx` · master `_potx/slideforge-build.potx`
  - Dark Neon (06 Active Theory) · 19 slides — `11-product-launch-product-launch/11__darkneon.pptx` · master `_potx/slideforge-darkneon.potx`
  - Bubble Pop (12 Sagmeister & Walsh) · 19 slides — `11-product-launch-product-launch/11__bubble.pptx` · master `_potx/slideforge-bubble.potx`
- **Reading Club**
  - Editorial (19 Irma Boom) · 19 slides — `12-reading-club-reading-club/12__editorial.pptx` · master `_potx/slideforge-editorial.potx`
  - Organic (18 Kenya Hara) · 19 slides — `12-reading-club-reading-club/12__organic.pptx` · master `_potx/slideforge-organic.potx`
  - Newspaper (01 Pentagram) · 19 slides — `12-reading-club-reading-club/12__newspaper.pptx` · master `_potx/slideforge-newspaper.potx`
  - Pastel (17 Takram) · 19 slides — `12-reading-club-reading-club/12__pastel.pptx` · master `_potx/slideforge-pastel.potx`
  - Monochrome (03 Information Architects) · 19 slides — `12-reading-club-reading-club/12__monochrome.pptx` · master `_potx/slideforge-monochrome.potx`
  - Bubble Pop (12 Sagmeister & Walsh) · 19 slides — `12-reading-club-reading-club/12__bubble.pptx` · master `_potx/slideforge-bubble.potx`
- **Job Competition**
  - Corporate Blue (09 Experimental Jetset) · 19 slides — `13-job-competition-job-competition/13__corporate.pptx` · master `_potx/slideforge-corporate.potx`
  - Breathing Whitespace (11 Build) · 19 slides — `13-job-competition-job-competition/13__build.pptx` · master `_potx/slideforge-build.potx`
  - Swiss Grid (10 Müller-Brockmann) · 19 slides — `13-job-competition-job-competition/13__brockmann.pptx` · master `_potx/slideforge-brockmann.potx`
  - Academic (04 Fathom) · 19 slides — `13-job-competition-job-competition/13__academic.pptx` · master `_potx/slideforge-academic.potx`
  - Nordic (03 Information Architects) · 19 slides — `13-job-competition-job-competition/13__nordic.pptx` · master `_potx/slideforge-nordic.potx`
- **Contest Defense**
  - Swiss Grid (10 Müller-Brockmann) · 19 slides — `14-contest-defense-contest-defense/14__brockmann.pptx` · master `_potx/slideforge-brockmann.potx`
  - Gradient Flow (07 Field.io) · 19 slides — `14-contest-defense-contest-defense/14__gradient.pptx` · master `_potx/slideforge-gradient.potx`
  - Corporate Blue (09 Experimental Jetset) · 19 slides — `14-contest-defense-contest-defense/14__corporate.pptx` · master `_potx/slideforge-corporate.potx`
  - Dark Neon (06 Active Theory) · 19 slides — `14-contest-defense-contest-defense/14__darkneon.pptx` · master `_potx/slideforge-darkneon.potx`
  - Blueprint (14 Raven Kwok) · 19 slides — `14-contest-defense-contest-defense/14__blueprint.pptx` · master `_potx/slideforge-blueprint.potx`
- **Course Syllabus**
  - Academic (04 Fathom) · 19 slides — `15-course-syllabus-course-syllabus/15__academic.pptx` · master `_potx/slideforge-academic.potx`
  - Soft Tech (17 Takram) · 19 slides — `15-course-syllabus-course-syllabus/15__takram.pptx` · master `_potx/slideforge-takram.potx`
  - Nordic (03 Information Architects) · 19 slides — `15-course-syllabus-course-syllabus/15__nordic.pptx` · master `_potx/slideforge-nordic.potx`
  - Chalkboard (15 Ash Thorp) · 19 slides — `15-course-syllabus-course-syllabus/15__chalk.pptx` · master `_potx/slideforge-chalk.potx`
  - Isometric (02 Stamen Design) · 19 slides — `15-course-syllabus-course-syllabus/15__isometric.pptx` · master `_potx/slideforge-isometric.potx`
- **Recruitment**
  - Memphis Pop (12 Sagmeister & Walsh) · 19 slides — `16-recruitment-recruitment/16__memphis.pptx` · master `_potx/slideforge-memphis.potx`
  - Pastel (17 Takram) · 19 slides — `16-recruitment-recruitment/16__pastel.pptx` · master `_potx/slideforge-pastel.potx`
  - Bauhaus (09 Experimental Jetset) · 19 slides — `16-recruitment-recruitment/16__bauhaus.pptx` · master `_potx/slideforge-bauhaus.potx`
  - Glassmorphism (05 Locomotive) · 19 slides — `16-recruitment-recruitment/16__glass.pptx` · master `_potx/slideforge-glass.potx`
  - Vaporwave (06 Active Theory) · 19 slides — `16-recruitment-recruitment/16__vaporwave.pptx` · master `_potx/slideforge-vaporwave.potx`
  - Bubble Pop (12 Sagmeister & Walsh) · 19 slides — `16-recruitment-recruitment/16__bubble.pptx` · master `_potx/slideforge-bubble.potx`
- **Annual Review**
  - Newspaper (01 Pentagram) · 19 slides — `17-annual-review-annual-review/17__newspaper.pptx` · master `_potx/slideforge-newspaper.potx`
  - Editorial (19 Irma Boom) · 19 slides — `17-annual-review-annual-review/17__editorial.pptx` · master `_potx/slideforge-editorial.potx`
  - Corporate Blue (09 Experimental Jetset) · 19 slides — `17-annual-review-annual-review/17__corporate.pptx` · master `_potx/slideforge-corporate.potx`
  - Monochrome (03 Information Architects) · 19 slides — `17-annual-review-annual-review/17__monochrome.pptx` · master `_potx/slideforge-monochrome.potx`
  - Gradient Flow (07 Field.io) · 19 slides — `17-annual-review-annual-review/17__gradient.pptx` · master `_potx/slideforge-gradient.potx`
- **Training Manual**
  - Monochrome (03 Information Architects) · 19 slides — `18-training-manual-training-manual/18__monochrome.pptx` · master `_potx/slideforge-monochrome.potx`
  - Nordic (03 Information Architects) · 19 slides — `18-training-manual-training-manual/18__nordic.pptx` · master `_potx/slideforge-nordic.potx`
  - Academic (04 Fathom) · 19 slides — `18-training-manual-training-manual/18__academic.pptx` · master `_potx/slideforge-academic.potx`
  - Isometric (02 Stamen Design) · 19 slides — `18-training-manual-training-manual/18__isometric.pptx` · master `_potx/slideforge-isometric.potx`
  - Chalkboard (15 Ash Thorp) · 19 slides — `18-training-manual-training-manual/18__chalk.pptx` · master `_potx/slideforge-chalk.potx`
- **User Research**
  - Soft Tech (17 Takram) · 19 slides — `19-user-research-user-research/19__takram.pptx` · master `_potx/slideforge-takram.potx`
  - Nordic (03 Information Architects) · 19 slides — `19-user-research-user-research/19__nordic.pptx` · master `_potx/slideforge-nordic.potx`
  - Academic (04 Fathom) · 19 slides — `19-user-research-user-research/19__academic.pptx` · master `_potx/slideforge-academic.potx`
  - Organic (18 Kenya Hara) · 19 slides — `19-user-research-user-research/19__organic.pptx` · master `_potx/slideforge-organic.potx`
  - Monochrome (03 Information Architects) · 19 slides — `19-user-research-user-research/19__monochrome.pptx` · master `_potx/slideforge-monochrome.potx`
- **Market Analysis**
  - Corporate Blue (09 Experimental Jetset) · 19 slides — `20-market-analysis-market-analysis/20__corporate.pptx` · master `_potx/slideforge-corporate.potx`
  - Swiss Grid (10 Müller-Brockmann) · 19 slides — `20-market-analysis-market-analysis/20__brockmann.pptx` · master `_potx/slideforge-brockmann.potx`
  - Gradient Flow (07 Field.io) · 19 slides — `20-market-analysis-market-analysis/20__gradient.pptx` · master `_potx/slideforge-gradient.potx`
  - Newspaper (01 Pentagram) · 19 slides — `20-market-analysis-market-analysis/20__newspaper.pptx` · master `_potx/slideforge-newspaper.potx`
  - Glassmorphism (05 Locomotive) · 19 slides — `20-market-analysis-market-analysis/20__glass.pptx` · master `_potx/slideforge-glass.potx`
- **Budget & Finance**
  - Swiss Grid (10 Müller-Brockmann) · 19 slides — `21-budget-plan-budget-finance/21__brockmann.pptx` · master `_potx/slideforge-brockmann.potx`
  - Corporate Blue (09 Experimental Jetset) · 19 slides — `21-budget-plan-budget-finance/21__corporate.pptx` · master `_potx/slideforge-corporate.potx`
  - Isometric (02 Stamen Design) · 19 slides — `21-budget-plan-budget-finance/21__isometric.pptx` · master `_potx/slideforge-isometric.potx`
  - Monochrome (03 Information Architects) · 19 slides — `21-budget-plan-budget-finance/21__monochrome.pptx` · master `_potx/slideforge-monochrome.potx`
  - Nordic (03 Information Architects) · 19 slides — `21-budget-plan-budget-finance/21__nordic.pptx` · master `_potx/slideforge-nordic.potx`
- **Travel Plan**
  - Organic (18 Kenya Hara) · 19 slides — `22-travel-plan-travel-plan/22__organic.pptx` · master `_potx/slideforge-organic.potx`
  - Pastel (17 Takram) · 19 slides — `22-travel-plan-travel-plan/22__pastel.pptx` · master `_potx/slideforge-pastel.potx`
  - Editorial (19 Irma Boom) · 19 slides — `22-travel-plan-travel-plan/22__editorial.pptx` · master `_potx/slideforge-editorial.potx`
  - Risograph (19 Irma Boom) · 19 slides — `22-travel-plan-travel-plan/22__risograph.pptx` · master `_potx/slideforge-risograph.potx`
  - Vaporwave (06 Active Theory) · 19 slides — `22-travel-plan-travel-plan/22__vaporwave.pptx` · master `_potx/slideforge-vaporwave.potx`
  - Bubble Pop (12 Sagmeister & Walsh) · 19 slides — `22-travel-plan-travel-plan/22__bubble.pptx` · master `_potx/slideforge-bubble.potx`
- **Open Source Release**
  - Cyber Terminal (08 Resn) · 19 slides — `23-open-source-release-open-source-release/23__terminal.pptx` · master `_potx/slideforge-terminal.potx`
  - Blueprint (14 Raven Kwok) · 19 slides — `23-open-source-release-open-source-release/23__blueprint.pptx` · master `_potx/slideforge-blueprint.potx`
  - Dark Neon (06 Active Theory) · 19 slides — `23-open-source-release-open-source-release/23__darkneon.pptx` · master `_potx/slideforge-darkneon.potx`
  - Monochrome (03 Information Architects) · 19 slides — `23-open-source-release-open-source-release/23__monochrome.pptx` · master `_potx/slideforge-monochrome.potx`
  - Gradient Flow (07 Field.io) · 19 slides — `23-open-source-release-open-source-release/23__gradient.pptx` · master `_potx/slideforge-gradient.potx`
- **Tech Architecture Review**
  - Blueprint (14 Raven Kwok) · 19 slides — `24-tech-review-tech-architecture-review/24__blueprint.pptx` · master `_potx/slideforge-blueprint.potx`
  - Isometric (02 Stamen Design) · 19 slides — `24-tech-review-tech-architecture-review/24__isometric.pptx` · master `_potx/slideforge-isometric.potx`
  - Swiss Grid (10 Müller-Brockmann) · 19 slides — `24-tech-review-tech-architecture-review/24__brockmann.pptx` · master `_potx/slideforge-brockmann.potx`
  - Cyber Terminal (08 Resn) · 19 slides — `24-tech-review-tech-architecture-review/24__terminal.pptx` · master `_potx/slideforge-terminal.potx`
  - Monochrome (03 Information Architects) · 19 slides — `24-tech-review-tech-architecture-review/24__monochrome.pptx` · master `_potx/slideforge-monochrome.potx`

## Design styles
| Style | English | Aesthetic anchor | Description |
|---|---|---|---|
| 呼吸留白极简 | Breathing Whitespace | 11 Build | Generous whitespace + a single accent colour; restrained and neutral, easy to swap for any brand colour. |
| 数学网格功能主义 | Swiss Grid | 10 Müller-Brockmann | A strict grid and alignment, a two-colour system; suited to data, plans and structured reporting. |
| 柔和科技图表 | Soft Tech | 17 Takram | Rounded corners, soft shadows and charts-as-art; suited to portfolios, product pitches and dashboards. |
| 商务蓝调 | Corporate Blue | 09 Experimental Jetset | Steady navy blue + gold accents; suited to reports, proposals and dashboards. |
| 暗黑霓虹 | Dark Neon | 06 Active Theory | A deep-space ground + neon cyan/magenta; suited to game pitches, launches and tech themes. |
| 复古像素 | Retro Pixel | 16 Territory Studio | A dark purple ground + candy-coloured blocks, echoing pixel art and indie-game aesthetics. |
| 杂志编辑 | Editorial | 19 Irma Boom | A warm paper ground + brick-red accents and serif headings; suited to portfolios and long-form narrative. |
| 孟菲斯活力 | Memphis Pop | 12 Sagmeister & Walsh | High-saturation clashing colours + geometric shapes; suited to event promos and light-hearted settings. |
| 玻璃拟态 | Glassmorphism | 05 Locomotive | Dark gradients + translucent cards; suited to product launches and tech showcases. |
| 赛博终端 | Cyber Terminal | 08 Resn | Green monospace on black, with a command-line feel; suited to technical teaching and geeky sharing. |
| 自然有机 | Organic | 18 Kenya Hara | A warm sand ground + plant green/terracotta, soft rounded corners; suited to notes and lifestyle themes. |
| 学术严谨 | Academic | 04 Fathom | Cool grey-blue + rigorous structure; suited to research, courseware and data reports. |
| 单色印刷极简 | Monochrome | 03 Information Architects | Three steps of black, white and grey, hierarchy carried by type size and whitespace; extremely restrained. |
| 工程蓝图 | Blueprint | 14 Raven Kwok | A deep blue ground + white line art and grids, in an engineering/architecture register. |
| 马卡龙柔彩 | Pastel | 17 Takram | Low-saturation pastels + rounded corners; light and approachable, suited to teaching and lifestyle themes. |
| 轻奢金黑 | Luxury Noir | 11 Build | A near-black ground + champagne-gold hairlines; a premium feel, suited to brand and high-end proposals. |
| 蒸汽波 | Vaporwave | 06 Active Theory | Purple-pink-cyan gradients + neon; retro-futurist, suited to trend and entertainment themes. |
| 孔版双色 | Risograph | 19 Irma Boom | Two-colour misregistration overprinting with a paper texture; suited to portfolios and independent publishing. |
| 包豪斯三原色 | Bauhaus | 09 Experimental Jetset | Red, yellow and blue + black and white, geometric composition; a strong sense of form. |
| 北欧灰蓝 | Nordic | 03 Information Architects | Cool grey-blue + off-white; quiet and restrained, suited to research and explanatory content. |
| 等距信息图 | Isometric | 02 Stamen Design | Isometric grids and blocky shapes, information turned into imagery; suited to process and structure explanations. |
| 渐变流体 | Gradient Flow | 07 Field.io | Soft gradients and flowing colour fields with a modern product feel; suited to launches and introductions. |
| 报纸排版 | Newspaper | 01 Pentagram | Multi-column dense setting + serif headings + hairline rules; high information density, suited to roundups and annuals. |
| 黑板粉笔 | Chalkboard | 15 Ash Thorp | A dark ink-green chalkboard + chalk white and yellow, with a classroom feel; suited to teaching and explanation. |
| 泡泡堂风 | Bubble Pop | 12 Sagmeister & Walsh | A minimal ground + candy-coloured bubbles and springy motion; bright and rounded, with strong interactive playfulness. |

## Usage guide
1. **Edit directly**: download a `.pptx` and open it in PowerPoint / WPS / Keynote / LibreOffice. Text, shapes,
   colours and picture placeholders can all be edited directly without breaking the layout. Drop a `.potx` into
   your template folder and it is available straight from "New".
2. **Change the colour scheme / fonts**: page colours are written onto each shape, so batch-replacing the theme
   colours reskins everything; the heading and body fonts are defined by `title_font / body_font` in
   `generator/themes.py`.
3. **Regenerate**:

```bash
pip install -r generator/requirements.txt
python generator/build.py templates     # generate all templates + index.manifest.json
python generator/validate.py templates  # validate openability / layout count / content types
python scripts/build_site.py            # rebuild index.html and the style preview images
python scripts/build_readme.py          # rebuild this README
```

## Documentation
> Privacy note: this repository **contains no** local-machine or USB-drive directory listings, scan results or personal reports; the templates and documents are all generic artefacts.
- [Requirements → template mapping](docs/need-template-mapping.md)
- [Toolchain install log](docs/install-record.md)
- [Master catalogue](docs/CATALOG.md) · [Coverage matrix](docs/coverage-matrix.md) · [Item-by-item usage guide](docs/USAGE.md)
- [Sampling QA report](docs/qa-report.md) · [Exceptions and rollback](docs/rollback.md) · [Handoff document](docs/handoff.md) · [Acceptance summary](docs/acceptance-summary.md)
- [Handoff and operations manual](docs/handoff-ops.md)
- [Motion specification](docs/animation-spec.md) · [Export and rollback notes](docs/export-notes.md) · [Design/presentation/animation skills research](docs/research-skills.md)
- [Front-end iteration log](docs/iteration-log.md) · [Pre-delivery review checklist](docs/review-checklist.md)
- [Advanced features](docs/export-notes.md) — native editable charts / 8s auto-advance / speaker notes / full-screen preview lightbox

## License
This project is released under the **MIT License** and may be used freely for personal and commercial purposes; see [LICENSE](LICENSE).

The templates contain **no** real business data, customer information or copyrighted third-party assets; fonts rely on system fonts, and if you replace them with commercial fonts, please confirm the licensing yourself.

---

Generated by `python-pptx` scripts · SlideForge · https://github.com/fanquanpp/slide-forge
