# -*- coding: utf-8 -*-
"""从 templates/index.manifest.json 生成：主清单台账 / 覆盖矩阵 / 逐条使用说明 / 统计。"""
import os, sys, json, csv, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "generator"))
from themes import THEMES  # noqa

REPO = "https://github.com/fanquanpp/slide-forge"
HUGO = "https://github.com/fanquanpp/slide-forge/tree/main/templates/"


def load():
    with open(os.path.join(ROOT, "templates", "index.manifest.json"), encoding="utf-8") as f:
        return json.load(f)


def catalog(m):
    rows = []
    for d in m["decks"]:
        rows.append({
            "编号": d["id"], "名称": "%s · %s" % (d["category_name"], d["style_label"]),
            "类型": d["type"], "用途场景": d["purpose"], "状态": d["status"], "版本": d["version"],
            "来源": d["source"], "最后更新": d["updated"], "页数": d["slides"], "文件": d["file"],
        })
    os.makedirs(os.path.join(ROOT, "docs"), exist_ok=True)
    with open(os.path.join(ROOT, "docs", "catalog.csv"), "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)
    L = ["# SlideForge 主清单台账", "",
         "> 共 **%d** 条成品条目。字段：编号 / 名称 / 类型 / 用途场景 / 状态 / 版本 / 来源 / 最后更新 / 页数 / 文件。"
         % len(rows),
         "> 任取一条可定位到文件（`templates/<文件>`）；任取一个文件可反查本表。", "",
         "| 编号 | 名称 | 类型 | 用途场景 | 状态 | 版本 | 来源 | 最后更新 | 页数 | 文件 |",
         "|---|---|---|---|---|---|---|---|---:|---|"]
    for r in rows:
        L.append("| %s | %s | %s | %s | %s | %s | %s | %s | %d | `%s` |" % (
            r["编号"], r["名称"], r["类型"], r["用途场景"], r["状态"], r["版本"], r["来源"], r["最后更新"], r["页数"], r["文件"]))
    with open(os.path.join(ROOT, "docs", "CATALOG.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    return rows


def coverage(m):
    cats = m["categories"]; styles = list(m["themes"].keys())
    have = {}
    for d in m["decks"]:
        have[(d["category"], d["style"])] = d
    # md
    L = ["# 类型 × 用途 覆盖矩阵", "",
         "行为用途分类（24），列为设计风格（24）；`●` 表示存在对应模板，`编号` 为台账 ID。", "",
         "| 用途 \\ 风格 | " + " | ".join(THEMES[s]["label"][:4] for s in styles) + " |",
         "|" + "---|" * (len(styles) + 1)]
    for c in cats:
        cells = []
        for s in styles:
            d = have.get((c["id"], s))
            cells.append(d["id"][-3:] if d else "·")
        L.append("| %s | %s |" % (c["name"], " | ".join(cells)))
    # per-style totals
    L.append("")
    L.append("## 各风格使用次数（类型分布）")
    L.append("")
    L.append("| 风格 | 次数 | 占比 |")
    L.append("|---|---:|---:|")
    total = len(m["decks"])
    for s, n in sorted(m["stats"]["style_distribution"].items(), key=lambda kv: -kv[1]):
        L.append("| %s | %d | %.1f%% |" % (THEMES[s]["label"], n, 100.0 * n / total))
    L.append("")
    L.append("## 各用途条目数")
    L.append("")
    L.append("| 用途场景 | 条目数 |")
    L.append("|---|---:|")
    for c in cats:
        L.append("| %s | %d |" % (c["name"], len(c["decks"])))
    with open(os.path.join(ROOT, "docs", "coverage-matrix.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    # html (self-contained)
    th = "".join('<th>%s</th>' % html.escape(THEMES[s]["label"][:4]) for s in styles)
    trs = []
    for c in cats:
        tds = []
        for s in styles:
            d = have.get((c["id"], s))
            tds.append('<td class="on">%s</td>' % d["id"][-3:] if d else '<td class="off">·</td>')
        trs.append('<tr><th class="rowh">%s</th>%s</tr>' % (html.escape(c["name"]), "".join(tds)))
    style_rows = "".join('<tr><td>%s</td><td>%d</td><td>%.1f%%</td></tr>' % (html.escape(THEMES[s]["label"]), n, 100.0*n/total)
                         for s, n in sorted(m["stats"]["style_distribution"].items(), key=lambda kv: -kv[1]))
    doc = """<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>类型 × 用途 覆盖矩阵 · SlideForge</title>
<style>
*{box-sizing:border-box;margin:0;padding:0}body{background:#fbfbfa;color:#14161a;font:14px/1.6 "Segoe UI","Microsoft YaHei",system-ui,sans-serif}
.wrap{max-width:1180px;margin:0 auto;padding:56px 26px 80px}.kicker{color:#2f6bff;font-weight:700;font-size:12px;letter-spacing:.8px;text-transform:uppercase}
h1{font-size:30px;font-weight:800;margin:10px 0 12px}.lead{color:#6b7280;max-width:820px}
h2{font-size:19px;font-weight:750;margin:38px 0 12px}
table{border-collapse:collapse;font-size:11.5px;background:#fff;border:1px solid #e7e9ee}
td,th{border:1px solid #eef0f4;padding:4px 6px;text-align:center;white-space:nowrap}
th{background:#f4f6f8}.rowh{text-align:left;background:#fafbfc;position:sticky;left:0}
.on{color:#2f6bff;font-weight:700}.off{color:#dfe3ea}
.scroll{overflow:auto;margin-top:12px;border-radius:10px}
.m{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin:22px 0}
.metric{background:#fff;border:1px solid #e7e9ee;border-radius:12px;padding:16px}.metric b{display:block;font-size:24px;font-weight:800}.metric span{color:#6b7280;font-size:12.5px}
footer{margin-top:40px;color:#6b7280;font-size:12.5px}
</style></head><body><div class="wrap">
<div class="kicker">Coverage Matrix</div><h1>类型 × 用途 覆盖矩阵</h1>
<p class="lead">行为 24 个用途分类，列为 24 种设计风格；格子内为对应模板的台账编号后三位（`·` 表示该组合未配置）。</p>
<div class="m">
<div class="metric"><b>__DECKS__</b><span>成品条目</span></div>
<div class="metric"><b>__CATS__</b><span>用途场景</span></div>
<div class="metric"><b>__THEMES__</b><span>设计风格（类型）</span></div>
<div class="metric"><b>__MAXPCT__</b><span>单一类型最高占比</span></div>
</div>
<div class="scroll"><table><tr><th class="rowh">用途 \\ 风格</th>__TH__</tr>__TRS__</table></div>
<h2>各风格使用次数（类型分布）</h2>
<div class="scroll"><table><tr><th>风格</th><th>次数</th><th>占比</th></tr>__STYLE__</table></div>
<footer>SlideForge · 覆盖矩阵 · 与 index.manifest.json 一致 · MIT License</footer>
</div></body></html>"""
    maxpct = max(100.0 * n / total for n in m["stats"]["style_distribution"].values())
    doc = (doc.replace("__DECKS__", str(total)).replace("__CATS__", str(len(cats))).replace("__THEMES__", str(len(styles)))
              .replace("__MAXPCT__", "%.1f%%" % maxpct).replace("__TH__", th).replace("__TRS__", "".join(trs))
              .replace("__STYLE__", style_rows))
    with open(os.path.join(ROOT, "docs", "coverage-matrix.html"), "w", encoding="utf-8") as f:
        f.write(doc)
    return maxpct


def usage(m):
    L = ["# 逐条使用说明（120 条）", "",
         "每条说明：适用场景 · 输入前提 · 使用方法 · 注意事项。文件路径相对 `templates/`。", ""]
    for c in m["categories"]:
        for d in c["decks"]:
            L += ["## %s — %s · %s" % (d["id"], c["name"], THEMES[d["style"]]["label"]), "",
                  "- **适用场景**：%s" % c["needs"],
                  "- **设计风格**：%s（%s，锚点 %s）——%s" % (THEMES[d["style"]]["label"], THEMES[d["style"]]["en"], THEMES[d["style"]]["preset"], THEMES[d["style"]]["philosophy"]),
                  "- **输入前提**：无需外部素材；打开即可编辑（PowerPoint / WPS / Keynote / LibreOffice）。",
                  "- **使用方法**：替换标题与正文占位文本 → 按需删除多余版面 → 批量替换主题色换成品牌色 → 用「插入-图片」替换图片占位框 → 需要时用「设计-幻灯片大小」保持 16:9。",
                  "- **注意事项**：字体依赖系统字体（微软雅黑 / Segoe UI 等），如需商用字体请自行确认授权；模板不含正式内容。",
                  "- **文件**：`%s`（%d 页）" % (d["file"], d["slides"]), ""]
    with open(os.path.join(ROOT, "docs", "USAGE.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")


def main():
    m = load()
    rows = catalog(m)
    maxpct = coverage(m)
    usage(m)
    stats = m["stats"]; stats["max_type_pct"] = round(maxpct, 2)
    with open(os.path.join(ROOT, "docs", "stats.json"), "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=1)
    print("OK catalog=%d entries; max_type_pct=%.1f%%" % (len(rows), maxpct))


if __name__ == "__main__":
    main()
