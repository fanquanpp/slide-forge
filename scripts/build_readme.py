# -*- coding: utf-8 -*-
"""从 templates/index.manifest.json 生成 README.md（保证目录与真实产物一致）。"""
import os, sys, json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "generator"))
from themes import THEMES  # noqa

REPO = "https://github.com/fanquanpp/slide-forge"


def main():
    with open(os.path.join(ROOT, "templates", "index.manifest.json"), encoding="utf-8") as f:
        m = json.load(f)
    st = m["stats"]; themes = m["themes"]
    potx_by_style = {p["style"]: p["file"] for p in m.get("potx", [])}
    L = []
    A = L.append
    A("# SlideForge · 多用途可编辑 PPT 模板库")
    A("")
    A("> 脚本生成的多用途、多风格、**可编辑**且**不含正式内容**的 PowerPoint 模板库。")
    A("> MIT License · 可用 `python-pptx` 一键重建。")
    A("")
    A("![风格预览](assets/previews/build-cover.svg)")
    A("")
    A("## 总览")
    A("")
    A("| 指标 | 数值 |")
    A("|---|---|")
    A("| 演示模板 (.pptx) | **%d** 套 |" % st["decks"])
    A("| 版面页总数 | **%d** 页 |" % st["slides_total"])
    A("| 设计风格 | **%d** 种 |" % st["themes"])
    A("| 用途分类 | **%d** 个 |" % st["categories"])
    A("| 母版模板 (.potx) | **%d** 套 |" % st["potx"])
    A("| 每套版面原型 | 15 个（封面/目录/章节/要点/对比/指标/时间线/流程/图表/表格/图集/引用/团队/结尾 等） |")
    A("")
    A("浏览站（GitHub Pages）：<https://fanquanpp.github.io/slide-forge/>")
    A("")
    A("## 目录结构")
    A("")
    A("```")
    A("slide-forge/")
    A("├─ index.html                 # GitHub Pages 浏览站，可筛选分类、预览风格、直接下载")
    A("├─ assets/previews/           # 12 种风格的矢量预览图 (SVG)")
    A("├─ templates/                 # 全部可编辑模板 (.pptx) 与索引清单")
    A("│  ├─ <分类目录>/<编号>__<风格>.pptx")
    A("│  ├─ _potx/slideforge-<风格>.potx")
    A("│  └─ index.manifest.json     # 权威清单（分类 / 风格 / 页数）")
    A("├─ generator/                 # 生成器与校验脚本 (Python + python-pptx)")
    A("│  ├─ themes.py  slidekit.py  build.py  validate.py  requirements.txt")
    A("├─ scripts/                   # 站点 / README / 索引重建脚本")
    A("├─ docs/                      # 画像报告 / 需求映射 / 安装记录 / 交接运维")
    A("├─ .github/workflows/pages.yml")
    A("└─ LICENSE  (MIT)")
    A("```")
    A("")
    A("## 模板目录")
    A("")
    A("| 分类 | 用途 | 设计风格数 | 套数 |")
    A("|---|---|---:|---:|")
    for c in m["categories"]:
        A("| %s | %s | %d | %d |" % (c["name"], c["en"], len(c["decks"]), len(c["decks"])))
    A("")
    A("### 各分类 · 各风格文件")
    A("")
    for c in m["categories"]:
        A("- **%s**（%s）" % (c["name"], c["en"]))
        for dk in c["decks"]:
            t = themes[dk["style"]]
            A("  - %s（%s）· %d 页 —— `%s`%s" % (
                t["label"], t["preset"], dk["slides"], dk["file"],
                (" · 母版 `%s`" % potx_by_style[dk["style"]]) if dk["style"] in potx_by_style else ""))
    A("")
    A("## 设计风格")
    A("")
    A("| 风格 | 英文 | 审美锚点 | 说明 |")
    A("|---|---|---|---|")
    for k, v in themes.items():
        A("| %s | %s | %s | %s |" % (v["label"], v["en"], v["preset"], v["philosophy"]))
    A("")
    A("## 使用指南")
    A("")
    A("1. **直接编辑**：下载 `.pptx`，用 PowerPoint / WPS / Keynote / LibreOffice 打开。文本、形状、")
    A("   配色、图片占位框均可直接修改，不破坏版式。`.potx` 放入模板目录后可直接「新建」。")
    A("2. **换配色 / 字体**：页面颜色写在各形状上，批量替换主题色即可全局换肤；")
    A("   标题 / 正文字体在 `generator/themes.py` 的 `title_font / body_font` 定义。")
    A("3. **重新生成**：")
    A("")
    A("```bash")
    A("pip install -r generator/requirements.txt")
    A("python generator/build.py templates     # 生成全部模板 + index.manifest.json")
    A("python generator/validate.py templates  # 校验可打开性 / 版面数 / 内容类型")
    A("python scripts/build_site.py            # 重建 index.html 与风格预览图")
    A("python scripts/build_readme.py          # 重建本 README")
    A("```")
    A("")
    A("## 文档")
    A("")
    A("> 隐私说明：本仓库**不包含**任何本机 / U 盘目录清单、扫描结果或个人报告；模板与文档均为通用产物。")
    A("- [需求 → 模板映射表](docs/need-template-mapping.md)")
    A("- [工具链安装记录](docs/install-record.md)")
    A("- [主清单台账](docs/CATALOG.md) · [覆盖矩阵](docs/coverage-matrix.md) · [逐条使用说明](docs/USAGE.md)")
    A("- [抽样质检报告](docs/qa-report.md) · [异常与回滚](docs/rollback.md) · [交接文档](docs/handoff.md) · [验收汇总](docs/acceptance-summary.md)")
    A("- [交接与运维手册](docs/handoff-ops.md)")
    A("- [动效规范](docs/animation-spec.md) · [导出与回滚说明](docs/export-notes.md) · [设计/演示/动画 Skills 调研](docs/research-skills.md)")
    A("")
    A("## 许可")
    A("")
    A("本项目以 **MIT License** 发布，可自由用于个人与商业用途，详见 [LICENSE](LICENSE)。")
    A("")
    A("模板内**不含**任何真实业务数据、客户信息或受版权保护的第三方素材；字体依赖系统字体，")
    A("如需替换为商用字体，请自行确认授权。")
    A("")
    A("---")
    A("")
    A("由 `python-pptx` 脚本生成 · SlideForge · %s" % REPO)
    with open(os.path.join(ROOT, "README.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print("OK README.md (%d lines)" % len(L))


if __name__ == "__main__":
    main()
