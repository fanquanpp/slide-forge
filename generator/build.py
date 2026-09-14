# -*- coding: utf-8 -*-
"""SlideForge 构建器：按「用途分类 × 设计风格」批量生成可编辑 PPT 模板并输出主清单台账。

用法:  python build.py <输出目录>
产出:  templates/<分类目录>/<编号>__<风格>.pptx   templates/_potx/*.potx
       templates/index.manifest.json（含台账字段）
"""
import os, sys, json, shutil, zipfile, hashlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from slidekit import Deck
from themes import THEMES, CATEGORIES

CAT_CONTENT = {
    "01-teaching": dict(sec=["课程目标", "核心概念", "代码演示", "练习与作业"], nodes=["环境准备", "编写代码", "运行调试", "提交作业"], quote="在此输入课程寄语或重要结论。"),
    "02-game-gdd": dict(sec=["游戏概述", "核心玩法", "美术与世界观", "开发计划"], nodes=["玩法验证", "资源制作", "系统整合", "测试调优"], quote="在此输入一句设计信条 / 立项理由。"),
    "03-portfolio": dict(sec=["作者简介", "代表作品", "创作流程", "联系方式"], nodes=["需求沟通", "草稿确认", "正式绘制", "交付源文件"], quote="在此输入一句创作感言。"),
    "04-club-event": dict(sec=["活动背景", "活动流程", "宣传与报名", "预算与分工"], nodes=["发起", "审批", "宣传", "执行"], quote="在此输入活动口号 / 宣传语。"),
    "05-project-report": dict(sec=["目标回顾", "执行过程", "结果与数据", "反思与下一步"], nodes=["计划", "执行", "检查", "改进"], quote="在此输入一条关键复盘结论。"),
    "06-study-notes": dict(sec=["为什么学", "知识地图", "重点拆解", "练习与延伸"], nodes=["阅读", "笔记", "练习", "输出"], quote="在此输入一句学习方法论。"),
    "07-resume": dict(sec=["关于我", "技能栈", "项目经历", "求职意向"], nodes=["投递", "笔试", "面试", "入职"], quote="在此输入一句个人宣言。"),
    "08-promo": dict(sec=["亮点速览", "活动内容", "参与方式", "常见问题"], nodes=["扫码", "填写", "确认", "参与"], quote="在此输入一句行动号召（CTA）。"),
    "09-dashboard": dict(sec=["总体概览", "关键指标", "趋势分析", "结论与行动"], nodes=["采集", "清洗", "分析", "展示"], quote="在此输入一条数据洞察。"),
    "10-creative-pitch": dict(sec=["创意缘起", "世界观 / 故事", "视觉与音乐", "制作计划"], nodes=["设定", "建模", "动画", "后期"], quote="在此输入一句作品主题 / 立意。"),
    "11-product-launch": dict(sec=["产品定位", "核心亮点", "演示与对比", "发布计划"], nodes=["内测", "公测", "发布", "迭代"], quote="在此输入一句产品主张。"),
    "12-reading-club": dict(sec=["书目简介", "核心观点", "金句摘录", "共读安排"], nodes=["选书", "共读", "讨论", "输出"], quote="在此输入一句读后感。"),
    "13-job-competition": dict(sec=["岗位理解", "个人优势", "工作设想", "承诺与计划"], nodes=["竞选", "陈述", "答辩", "公示"], quote="在此输入一句竞选宣言。"),
    "14-contest-defense": dict(sec=["项目背景", "方案与创新", "成果与验证", "价值与应用"], nodes=["选题", "研发", "验证", "路演"], quote="在此输入一句项目一句话介绍。"),
    "15-course-syllabus": dict(sec=["课程定位", "教学目标", "内容与周次", "考核方式"], nodes=["备课", "授课", "作业", "考核"], quote="在此输入一句教学理念。"),
    "16-recruitment": dict(sec=["社团介绍", "部门与岗位", "成长路径", "报名方式"], nodes=["宣讲", "报名", "面试", "入社"], quote="在此输入一句招新口号。"),
    "17-annual-review": dict(sec=["年度回望", "关键成果", "问题与反思", "明年规划"], nodes=["回顾", "总结", "规划", "启动"], quote="在此输入一句年度关键词。"),
    "18-training-manual": dict(sec=["适用范围", "流程步骤", "常见问题", "注意事项"], nodes=["准备", "执行", "检查", "归档"], quote="在此输入一条安全 / 规范提示。"),
    "19-user-research": dict(sec=["研究目标", "方法与样本", "关键发现", "结论与建议"], nodes=["设计问卷", "招募", "访谈", "分析"], quote="在此输入一条用户洞察。"),
    "20-market-analysis": dict(sec=["市场概览", "竞品对比", "机会与风险", "策略建议"], nodes=["调研", "对标", "分析", "决策"], quote="在此输入一条市场判断。"),
    "21-budget-plan": dict(sec=["预算总览", "分项明细", "收支平衡", "风险与预案"], nodes=["编制", "审批", "执行", "结算"], quote="在此输入一条财务原则。"),
    "22-travel-plan": dict(sec=["目的地概览", "行程安排", "预算与装备", "注意事项"], nodes=["规划", "预订", "出发", "记录"], quote="在此输入一句旅行心情。"),
    "23-open-source-release": dict(sec=["项目简介", "新特性", "安装与使用", "路线图"], nodes=["开发", "测试", "发布", "维护"], quote="在此输入一句项目口号。"),
    "24-tech-review": dict(sec=["背景与目标", "架构方案", "取舍与风险", "评审结论"], nodes=["提案", "评审", "落地", "复盘"], quote="在此输入一条架构原则。"),
}

EXTRA = ["plans", "faq", "glossary", "compare_table", "roadmap", "stat_chart", "bignumber", "checklist", "quote_wall", "steps_vertical"]
KICK = ["Overview", "Key Points", "Process", "Data", "Appendix"]


def _seed(cat, style):
    return (CATEGORIES.index(cat) * 7 + list(THEMES.keys()).index(style)) % 9973


def build_deck(cat, style, outdir):
    t = THEMES[style]; c = CAT_CONTENT[cat["id"]]; sd = _seed(cat, style)
    sec = c["sec"]; nodes = c["nodes"]
    title = cat["name"]
    sub = "%s · 在此输入副标题 / 项目名称" % cat["name"]
    meta = "团队 / 姓名  ·  YYYY-MM-DD"
    d = Deck(t)
    d._seed = sd
    # 1 封面
    d.cover(title, sub, meta, variant=["left", "center", "split"][sd % 3])
    # 2 目录
    d.agenda(sec, variant=["num", "card"][sd % 2])
    # 3 章节页
    d.section("01", sec[0], "在此输入本章导语 · 一句话点题")
    # 4 要点页
    bl = ["在此输入「%s」的要点一" % sec[0], "在此输入「%s」的要点二" % sec[0],
          "在此输入「%s」的要点三" % sec[0], "在此输入「%s」的要点四" % sec[0]]
    d.bullets_page(KICK[0], sec[0], bl, variant=["dot", "card", "num"][sd % 3])
    # 5 左右对比
    d.two_col(KICK[1], sec[1], sec[0], sec[1],
              ["在此输入要点一", "在此输入要点二", "在此输入要点三"],
              ["在此输入要点一", "在此输入要点二", "在此输入要点三"],
              variant="vs" if sd % 2 else "compare")
    # 6 指标卡
    d.cards("Metrics", "关键数据一览", [("00", "指标一", "在此输入说明"), ("00", "指标二", "在此输入说明"),
                                      ("00", "指标三", "在此输入说明"), ("00", "指标四", "在此输入说明")])
    # 7 时间线
    d.timeline(KICK[2], "排期 / 路线图", [(sec[i], "在此输入说明") for i in range(4)])
    # 8 流程
    d.process(KICK[2], "工作流程", nodes, style="round" if sd % 2 else "chevron")
    # 9 图表
    d.chart_ph(KICK[3], "数据图表", variant=["bar", "line", "donut"][sd % 3])
    # 10 表格
    d.table_ph(KICK[3], "明细表", ["项目", "内容", "备注"],
               [["项一", "在此填内容", "在此填备注"], ["项二", "在此填内容", "在此填备注"], ["项三", "在此填内容", "在此填备注"]])
    # 11 图集
    d.gallery(KICK[1], "图集 / 案例", cols=3, rows=2)
    # 12 章节页二
    d.section("02", sec[2], "在此输入本章导语 · 一句话点题")
    # 13 引用
    d.quote(c["quote"], "— 署名 / 出处")
    # 14 团队
    d.team("Team", "团队 / 分工", [("姓名", "角色一"), ("姓名", "角色二"), ("姓名", "角色三")])
    # 15-17 三个随机附加原型（让每套结构不同，避免千篇一律）
    picks = [EXTRA[(sd + k * 3) % len(EXTRA)] for k in range(3)]
    for ext in picks:
        if ext == "plans":
            d.plans("Options", "方案对比", [("方案一", "00", ["在此输入要点", "在此输入要点", "在此输入要点"]),
                                          ("方案二", "00", ["在此输入要点", "在此输入要点", "在此输入要点"]),
                                          ("方案三", "00", ["在此输入要点", "在此输入要点", "在此输入要点"])])
        elif ext == "faq":
            d.faq("FAQ", "常见问题", [("在此输入问题一？", "在此输入回答（占位）"), ("在此输入问题二？", "在此输入回答（占位）"),
                                     ("在此输入问题三？", "在此输入回答（占位）")])
        elif ext == "glossary":
            d.glossary("Glossary", "术语表", [("术语一", "在此输入释义（占位）"), ("术语二", "在此输入释义（占位）"),
                                            ("术语三", "在此输入释义（占位）"), ("术语四", "在此输入释义（占位）")])
        elif ext == "compare_table":
            d.compare_table("Matrix", "对比矩阵", ["维度", "选项 A", "选项 B", "选项 C"],
                            [["维度一", "", "", ""], ["维度二", "", "", ""], ["维度三", "", "", ""]],
                            [[1, 1, 0], [1, 0, 1], [1, 1, 1]])
        elif ext == "roadmap":
            d.roadmap("Roadmap", "多线路线图", [("线一", [(0.6, "任务"), (0.6, "任务"), (0.6, "任务")]),
                                              ("线二", [(0.6, "任务"), (0.6, "任务")])])
        elif ext == "stat_chart":
            d.stat_chart("Highlight", "关键指标", "00%", "在此输入指标说明 · 占位文本")
        elif ext == "bignumber":
            d.bignumber(KICK[1], "00", "在此输入关键数字的含义", "在此输入补充说明（占位）")
        elif ext == "checklist":
            d.checklist("Checklist", "清单", ["在此输入待办项一", "在此输入待办项二", "在此输入待办项三", "在此输入待办项四"])
        elif ext == "quote_wall":
            d.quote_wall("Quotes", "金句墙", ["在此输入短句一", "在此输入短句二", "在此输入短句三", "在此输入短句四", "在此输入短句五"])
        else:
            d.steps_vertical("Steps", "分步说明", [(sec[i], "在此输入步骤说明（占位）") for i in range(4)])
    # 结尾
    d.closing("谢谢观看", "在此输入联系方式 / 二维码 / 致谢")

    slug = "".join(ch.lower() if ch.isalnum() or ch in "-" else ("-" if ch in " &/" else "") for ch in cat["en"])
    slug = "-".join([x for x in slug.split("-") if x])
    catdir = os.path.join(outdir, cat["id"] + "-" + slug)
    os.makedirs(catdir, exist_ok=True)
    num = cat["id"].split("-")[0]
    fname = "%s__%s.pptx" % (num, style)
    path = os.path.join(catdir, fname)
    d.save(path)
    return path, len(d.prs.slides._sldIdLst)


def make_potx(pptx_path, potx_path):
    tmp = potx_path + ".tmp"
    with zipfile.ZipFile(pptx_path, "r") as zin, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == "[Content_Types].xml":
                txt = data.decode("utf-8").replace(
                    "application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml",
                    "application/vnd.openxmlformats-officedocument.presentationml.template.main+xml")
                data = txt.encode("utf-8")
            zout.writestr(item, data)
    shutil.move(tmp, potx_path)
    return potx_path


def main():
    outdir = sys.argv[1] if len(sys.argv) > 1 else "templates"
    os.makedirs(outdir, exist_ok=True)
    date = "2026-09-14"
    manifest = {"generated_at": date, "version": "2.0",
                "themes": {k: {"label": v["label"], "en": v["en"], "preset": v["preset"], "philosophy": v["philosophy"]} for k, v in THEMES.items()},
                "categories": [], "decks": [], "potx": []}
    total_slides = 0; sf = 0; style_count = {}
    for cat in CATEGORIES:
        ce = {"id": cat["id"], "name": cat["name"], "en": cat["en"], "needs": cat["needs"], "decks": []}
        for style in cat["styles"]:
            path, ns = build_deck(cat, style, outdir)
            total_slides += ns; sf += 1
            style_count[style] = style_count.get(style, 0) + 1
            rel = os.path.relpath(path, outdir).replace("\\", "/")
            entry = {"id": "SF-%03d" % sf, "category": cat["id"], "category_name": cat["name"], "style": style,
                     "style_label": THEMES[style]["label"], "type": THEMES[style]["en"], "purpose": cat["name"],
                     "file": rel, "slides": ns, "status": "active", "version": "2.0",
                     "source": "SlideForge generator", "updated": date}
            manifest["decks"].append(entry)
            ce["decks"].append({"id": entry["id"], "style": style, "label": THEMES[style]["label"], "file": rel, "slides": ns})
        manifest["categories"].append(ce)
    # potx：每种风格一套
    potx_dir = os.path.join(outdir, "_potx"); os.makedirs(potx_dir, exist_ok=True)
    first = {}
    for dk in manifest["decks"]:
        first.setdefault(dk["style"], dk["file"])
    for i, style in enumerate(THEMES.keys(), 1):
        rel = first.get(style)
        if not rel:
            continue
        src = os.path.join(outdir, rel); dst = os.path.join(potx_dir, "slideforge-%s.potx" % style)
        if os.path.exists(src):
            make_potx(src, dst)
            manifest["potx"].append({"id": "POTX-%02d" % i, "style": style, "file": os.path.relpath(dst, outdir).replace("\\", "/")})
    manifest["stats"] = {"decks": len(manifest["decks"]), "slides_total": total_slides, "categories": len(CATEGORIES),
                         "themes": len(THEMES), "potx": len(manifest["potx"]),
                         "style_distribution": style_count}
    with open(os.path.join(outdir, "index.manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=1)
    print("OK decks=%d slides=%d categories=%d themes=%d potx=%d" %
          (manifest["stats"]["decks"], total_slides, len(CATEGORIES), len(THEMES), len(manifest["potx"])))
    print("style_distribution min=%d max=%d styles_used=%d" %
          (min(style_count.values()), max(style_count.values()), len(style_count)))


if __name__ == "__main__":
    main()
