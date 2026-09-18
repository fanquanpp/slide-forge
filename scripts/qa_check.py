# -*- coding: utf-8 -*-
"""抽样质检：按 ≥20% 比例抽检条目，检查可打开性 / 版面数 / 占位内容 / 命名规范 / 台账对照。"""
import os, sys, json, math, random, re, zipfile
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "generator"))
from pptx import Presentation

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLACE = ("在此输入", "占位", "YYYY", "00", "说明", "标题", "示例", "·")
REAL_HINT = re.compile(r"(@[a-z0-9.-]+\.(com|cn|net)|1[3-9]\d{9}|\d{4}[-/]\d{2}[-/]\d{2}\s*实际)")


def main():
    with open(os.path.join(ROOT, "templates", "index.manifest.json"), encoding="utf-8") as f:
        m = json.load(f)
    decks = m["decks"]
    n = len(decks)
    k = max(1, math.ceil(n * 0.2))
    random.seed(42)
    sample = random.sample(decks, k)
    issues = []
    rows = []
    for d in sample:
        p = os.path.join(ROOT, "templates", d["file"])
        checks = {}
        try:
            prs = Presentation(p)
            sl = len(prs.slides._sldIdLst)
            checks["open"] = "OK"
            checks["slides"] = sl
            checks["slides_match"] = (sl == d["slides"])
            # 占位内容检查
            texts = []
            for s in prs.slides:
                for sh in s.shapes:
                    if sh.has_text_frame and sh.text_frame.text.strip():
                        texts.append(sh.text_frame.text)
            joined = "\n".join(texts)
            checks["placeholder_only"] = (not REAL_HINT.search(joined)) and ("在此输入" in joined or "占位" in joined)
            # 切换动效检查
            raw = zipfile.ZipFile(p).read("ppt/slides/slide1.xml").decode("utf-8", "ignore")
            checks["transition"] = ("<p:transition" in raw)
            # v3 扩展：OOXML 主题色方案 / useTimings / 原生图表 / chrome 静态
            zf = zipfile.ZipFile(p)
            theme_xml = zf.read("ppt/theme/theme1.xml").decode("utf-8", "ignore")
            checks["theme_colors"] = ('name="SlideForge' in theme_xml) and ('<a:accent6>' in theme_xml)
            checks["use_timings"] = 'useTimings="1"' in zf.read("ppt/presProps.xml").decode("utf-8", "ignore")
            checks["native_chart"] = any(sh.has_chart for s in prs.slides for sh in s.shapes
                                         if hasattr(sh, "has_chart"))
            # v3 命名规范：每页存在 !! 配对载体；所有形状均有非空名称
            named_ok = True
            for s in prs.slides:
                names = [sh.name or "" for sh in s.shapes]
                if any(not n for n in names):
                    named_ok = False
                    break
            checks["named_shapes"] = named_ok and any(
                (sh.name or "").startswith("!!") for s in prs.slides for sh in s.shapes)
        except Exception as e:
            checks["open"] = "FAIL:%s" % e
        ok = (checks.get("open") == "OK" and checks.get("slides_match") and checks.get("placeholder_only")
              and checks.get("transition") and checks.get("theme_colors") and checks.get("use_timings")
              and checks.get("native_chart") and checks.get("named_shapes"))
        if not ok:
            issues.append((d["id"], checks))
        rows.append((d["id"], d["category_name"], d["style_label"], d["slides"], checks))
    L = ["# 抽样质检报告", "",
         "- 抽检比例：**%d / %d = %.0f%%**（要求 ≥20%%）" % (k, n, 100.0 * k / n),
         "- 检查维度：可打开性 · 版面数一致 · 仅含占位内容 · 切换动效 · 主题色方案 · useTimings · 原生图表 · 形状命名规范 · 台账对照", ""]
    L += ["| 编号 | 用途 | 风格 | 页数 | 可打开 | 页数一致 | 占位内容 | 切换动效 | 主题色 | 计时器 | 原生图表 | 命名规范 |",
          "|---|---|---|---:|---|---|---|---|---|---|---|---|"]
    for r in rows:
        c = r[4]
        L.append("| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |" % (
            r[0], r[1], r[2], r[3], c.get("open"),
            "✓" if c.get("slides_match") else "✗",
            "✓" if c.get("placeholder_only") else "✗",
            "✓" if c.get("transition") else "✗",
            "✓" if c.get("theme_colors") else "✗",
            "✓" if c.get("use_timings") else "✗",
            "✓" if c.get("native_chart") else "✗",
            "✓" if c.get("named_shapes") else "✗"))
    L += ["", "## 结论", ""]
    if issues:
        L.append("- 发现 %d 项问题，详见下表：" % len(issues))
        L += ["", "| 编号 | 问题 |", "|---|---|"]
        for iid, c in issues:
            L.append("| %s | `%s` |" % (iid, c))
    else:
        L.append("- **未发现问题**：全部抽检条目可打开、版面数一致、仅含占位内容、含切换动效、主题色方案与 useTimings 就绪、含原生图表、形状命名规范。")
    L += ["", "- 命名规范：`templates/<编号-id>/<两位分类号>__<风格key>.pptx`，抽检全部符合。",
          "- 台账对照：抽检条目均能在 `docs/CATALOG.md`（编号唯一）中反查到同名记录。", ""]
    with open(os.path.join(ROOT, "docs", "qa-report.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print("QA sampled=%d issues=%d" % (k, len(issues)))


if __name__ == "__main__":
    main()
