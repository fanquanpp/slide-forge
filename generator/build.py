# -*- coding: utf-8 -*-
"""SlideForge 构建器：按「用途分类 × 设计风格」批量生成可编辑 PPT 模板。

用法:  python build.py <输出目录>
产出:  <输出目录>/<分类>/<分类>-<风格>.pptx  以及 index.manifest.json
所有页面仅含版式与占位示例文本，无正式内容。
"""
import os, sys, json, shutil, zipfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from slidekit import Deck
from themes import THEMES, CATEGORIES

# ---- 每个用途分类的占位内容包（全部为占位/示意文本）----
PACKS = {
    "01-teaching": dict(
        sub="第 N 讲 · 在此输入知识点标题", meta="课程名称  ·  讲师 / 学期",
        agenda=["课程目标", "核心概念", "代码演示", "练习与作业"],
        kickers=["Learning Goals", "Core Concepts", "Hands-on", "Assignment"],
        bullets=["在此输入本讲要点一（概念 / 定义）", "在此输入本讲要点二（原理 / 机制）",
                 "在此输入本讲要点三（示例 / 反例）", "在此输入本讲要点四（常见误区）"],
        two=("概念 A", "概念 B", ["特征一", "特征二", "特征三"], ["特征一", "特征二", "特征三"]),
        cards=[("01", "模块一", "在此输入说明"), ("02", "模块二", "在此输入说明"),
               ("03", "模块三", "在此输入说明"), ("04", "模块四", "在此输入说明")],
        steps=[("第 1 步", "在此输入说明"), ("第 2 步", "在此输入说明"),
               ("第 3 步", "在此输入说明"), ("第 4 步", "在此输入说明")],
        nodes=["环境准备", "编写代码", "运行调试", "提交作业"],
        table=(["阶段", "内容", "产出"], [["阶段一", "在此填内容", "在此填产出"],
                                         ["阶段二", "在此填内容", "在此填产出"],
                                         ["阶段三", "在此填内容", "在此填产出"]]),
        quote=("在此输入一段课程寄语或重要结论。", "— 课程 / 讲师"),
        members=[("姓名", "主讲"), ("姓名", "助教"), ("姓名", "助教")],
    ),
    "02-game-gdd": dict(
        sub="玩法原型提案 · 在此输入项目代号", meta="团队 / 组名  ·  YYYY-MM-DD",
        agenda=["游戏概述", "核心玩法", "美术与世界观", "开发计划"],
        kickers=["Overview", "Core Loop", "Art & World", "Roadmap"],
        bullets=["在此输入设计目标一（体验 / 情感）", "在此输入设计目标二（机制 / 循环）",
                 "在此输入设计目标三（差异点）", "在此输入设计目标四（约束 / 风险）"],
        two=("参考作品 A", "参考作品 B", ["借鉴点一", "借鉴点二", "借鉴点三"], ["借鉴点一", "借鉴点二", "借鉴点三"]),
        cards=[("核心循环", "玩法", "在此输入说明"), ("目标时长", "单局 / 单章", "在此输入说明"),
               ("美术风格", "视觉", "在此输入说明"), ("目标平台", "发布", "在此输入说明")],
        steps=[("概念", "在此输入说明"), ("原型", "在此输入说明"), ("垂直切片", "在此输入说明"), ("发布", "在此输入说明")],
        nodes=["玩法验证", "资源制作", "系统整合", "测试调优"],
        table=(["模块", "状态", "负责"], [["战斗", "在此填状态", "在此填负责"],
                                         ["关卡", "在此填状态", "在此填负责"],
                                         ["UI", "在此填状态", "在此填负责"]]),
        quote=("在此输入一句设计信条 / 立项理由。", "— 制作人"),
        members=[("姓名", "策划"), ("姓名", "程序"), ("姓名", "美术")],
    ),
    "03-portfolio": dict(
        sub="作品集 · 在此输入作者署名", meta="领域 / 风格  ·  YYYY",
        agenda=["作者简介", "代表作品", "创作流程", "联系方式"],
        kickers=["About", "Selected Works", "Process", "Contact"],
        bullets=["在此输入作品亮点一", "在此输入作品亮点二", "在此输入作品亮点三", "在此输入作品亮点四"],
        two=("作品 A", "作品 B", ["亮点一", "亮点二", "亮点三"], ["亮点一", "亮点二", "亮点三"]),
        cards=[("年份", "起始", "在此输入说明"), ("张数", "产出", "在此输入说明"),
               ("工具", "软件", "在此输入说明"), ("尺寸", "规格", "在此输入说明")],
        steps=[("构思", "在此输入说明"), ("草图", "在此输入说明"), ("细化", "在此输入说明"), ("导出", "在此输入说明")],
        nodes=["需求沟通", "草稿确认", "正式绘制", "交付源文件"],
        table=(["作品", "类型", "年份"], [["作品一", "在此填类型", "在此填年份"],
                                         ["作品二", "在此填类型", "在此填年份"],
                                         ["作品三", "在此填类型", "在此填年份"]]),
        quote=("在此输入一句创作感言。", "— 作者"),
        members=[("姓名", "像素美术"), ("姓名", "插画"), ("姓名", "动效")],
    ),
    "04-club-event": dict(
        sub="活动策划案 · 在此输入活动名称", meta="社团 / 协会  ·  YYYY-MM-DD",
        agenda=["活动背景", "活动流程", "宣传与报名", "预算与分工"],
        kickers=["Background", "Schedule", "Promotion", "Budget & Team"],
        bullets=["在此输入活动目标一", "在此输入活动目标二", "在此输入活动目标三", "在此输入活动目标四"],
        two=("往期活动 A", "往期活动 B", ["效果一", "效果二", "效果三"], ["效果一", "效果二", "效果三"]),
        cards=[("预计人数", "规模", "在此输入说明"), ("活动时长", "时间", "在此输入说明"),
               ("预算", "经费", "在此输入说明"), ("场地", "地点", "在此输入说明")],
        steps=[("报名", "在此输入说明"), ("预热", "在此输入说明"), ("举办", "在此输入说明"), ("复盘", "在此输入说明")],
        nodes=["发起", "审批", "宣传", "执行", "总结"],
        table=(["项目", "负责人", "截止"], [["场地", "在此填负责", "在此填日期"],
                                           ["物料", "在此填负责", "在此填日期"],
                                           ["宣传", "在此填负责", "在此填日期"]]),
        quote=("在此输入活动口号 / 宣传语。", "— 社团"),
        members=[("姓名", "总负责"), ("姓名", "宣传"), ("姓名", "后勤")],
    ),
    "05-project-report": dict(
        sub="项目汇报 / 复盘 · 在此输入项目名称", meta="团队 / 部门  ·  YYYY-MM-DD",
        agenda=["目标回顾", "执行过程", "结果与数据", "反思与下一步"],
        kickers=["Objectives", "Execution", "Results", "Retrospective"],
        bullets=["在此输入目标一及达成情况", "在此输入目标二及达成情况",
                 "在此输入目标三及达成情况", "在此输入目标四及达成情况"],
        two=("做得好", "待改进", ["在此输入要点一", "在此输入要点二", "在此输入要点三"],
             ["在此输入要点一", "在此输入要点二", "在此输入要点三"]),
        cards=[("达成率", "指标一", "在此输入说明"), ("数量", "指标二", "在此输入说明"),
               ("时长", "指标三", "在此输入说明"), ("成本", "指标四", "在此输入说明")],
        steps=[("立项", "在此输入说明"), ("执行", "在此输入说明"), ("验收", "在此输入说明"), ("复盘", "在此输入说明")],
        nodes=["计划", "执行", "检查", "改进"],
        table=(["指标", "目标", "实际"], [["指标一", "在此填目标", "在此填实际"],
                                         ["指标二", "在此填目标", "在此填实际"],
                                         ["指标三", "在此填目标", "在此填实际"]]),
        quote=("在此输入一条关键复盘结论。", "— 项目组"),
        members=[("姓名", "负责人"), ("姓名", "执行"), ("姓名", "协作")],
    ),
    "06-study-notes": dict(
        sub="学习笔记分享 · 在此输入主题", meta="分享人  ·  YYYY-MM-DD",
        agenda=["为什么学", "知识地图", "重点拆解", "练习与延伸"],
        kickers=["Why", "Map", "Key Points", "Practice"],
        bullets=["在此输入知识点一", "在此输入知识点二", "在此输入知识点三", "在此输入知识点四"],
        two=("容易混淆 A", "容易混淆 B", ["区别一", "区别二", "区别三"], ["区别一", "区别二", "区别三"]),
        cards=[("模块一", "概览", "在此输入说明"), ("模块二", "概览", "在此输入说明"),
               ("模块三", "概览", "在此输入说明"), ("模块四", "概览", "在此输入说明")],
        steps=[("入门", "在此输入说明"), ("进阶", "在此输入说明"), ("实战", "在此输入说明"), ("拓展", "在此输入说明")],
        nodes=["阅读", "笔记", "练习", "输出"],
        table=(["主题", "难度", "用时"], [["主题一", "在此填难度", "在此填用时"],
                                         ["主题二", "在此填难度", "在此填用时"],
                                         ["主题三", "在此填难度", "在此填用时"]]),
        quote=("在此输入一句学习方法论。", "— 分享人"),
        members=[("姓名", "主讲"), ("姓名", "补充")],
    ),
    "07-resume": dict(
        sub="自我介绍 · 在此输入姓名 / 目标岗位", meta="联系方式  ·  城市",
        agenda=["关于我", "技能栈", "项目经历", "求职意向"],
        kickers=["About", "Skills", "Projects", "Objective"],
        bullets=["在此输入个人优势一", "在此输入个人优势二", "在此输入个人优势三", "在此输入个人优势四"],
        two=("熟练技能", "了解技能", ["技能一", "技能二", "技能三"], ["技能一", "技能二", "技能三"]),
        cards=[("年", "经验", "在此输入说明"), ("个", "项目数", "在此输入说明"),
               ("项", "证书 / 奖项", "在此输入说明"), ("篇", "作品 / 文章", "在此输入说明")],
        steps=[("在校", "在此输入说明"), ("实习", "在此输入说明"), ("项目", "在此输入说明"), ("目标", "在此输入说明")],
        nodes=["投递", "笔试", "面试", "入职"],
        table=(["时间", "经历", "角色"], [["YYYY-MM", "在此填经历", "在此填角色"],
                                         ["YYYY-MM", "在此填经历", "在此填角色"],
                                         ["YYYY-MM", "在此填经历", "在此填角色"]]),
        quote=("在此输入一句个人宣言。", "— 姓名"),
        members=[("姓名", "一个身份"), ("姓名", "另一个身份")],
    ),
    "08-promo": dict(
        sub="活动宣传 · 在此输入活动名称", meta="时间地点  ·  YYYY-MM-DD",
        agenda=["亮点速览", "活动内容", "参与方式", "常见问题"],
        kickers=["Highlights", "Program", "Join Us", "FAQ"],
        bullets=["在此输入宣传点一", "在此输入宣传点二", "在此输入宣传点三", "在此输入宣传点四"],
        two=("你将获得 A", "你将获得 B", ["收益一", "收益二", "收益三"], ["收益一", "收益二", "收益三"]),
        cards=[("时间", "日程", "在此输入说明"), ("地点", "场地", "在此输入说明"),
               ("名额", "规模", "在此输入说明"), ("费用", "价格", "在此输入说明")],
        steps=[("了解", "在此输入说明"), ("报名", "在此输入说明"), ("参与", "在此输入说明"), ("收获", "在此输入说明")],
        nodes=["扫码", "填写", "支付", "确认"],
        table=(["场次", "时间", "地点"], [["第一场", "在此填时间", "在此填地点"],
                                         ["第二场", "在此填时间", "在此填地点"],
                                         ["第三场", "在此填时间", "在此填地点"]]),
        quote=("在此输入一句行动号召（CTA）。", "— 主办方"),
        members=[("姓名", "报名咨询"), ("姓名", "合作联系")],
    ),
    "09-dashboard": dict(
        sub="数据看板 · 在此输入主题", meta="周期  ·  YYYY-MM-DD",
        agenda=["总体概览", "关键指标", "趋势分析", "结论与行动"],
        kickers=["Overview", "KPIs", "Trends", "Actions"],
        bullets=["在此输入指标解读一", "在此输入指标解读二", "在此输入指标解读三", "在此输入指标解读四"],
        two=("同比", "环比", ["在此输入要点一", "在此输入要点二", "在此输入要点三"],
             ["在此输入要点一", "在此输入要点二", "在此输入要点三"]),
        cards=[("00.0%", "指标一", "在此输入说明"), ("000", "指标二", "在此输入说明"),
               ("0.00", "指标三", "在此输入说明"), ("00", "指标四", "在此输入说明")],
        steps=[("Q1", "在此输入说明"), ("Q2", "在此输入说明"), ("Q3", "在此输入说明"), ("Q4", "在此输入说明")],
        nodes=["采集", "清洗", "分析", "展示"],
        table=(["维度", "数值", "变化"], [["维度一", "在此填数值", "在此填变化"],
                                         ["维度二", "在此填数值", "在此填变化"],
                                         ["维度三", "在此填数值", "在此填变化"]]),
        quote=("在此输入一条数据洞察。", "— 分析"),
        members=[("姓名", "数据"), ("姓名", "业务")],
    ),
    "10-creative-pitch": dict(
        sub="创作提案 · 在此输入作品名称", meta="团队  ·  YYYY-MM-DD",
        agenda=["创意缘起", "世界观 / 故事", "视觉与音乐", "制作计划"],
        kickers=["Concept", "Story", "Art & Music", "Production"],
        bullets=["在此输入创意点一", "在此输入创意点二", "在此输入创意点三", "在此输入创意点四"],
        two=("风格参考 A", "风格参考 B", ["参考点一", "参考点二", "参考点三"], ["参考点一", "参考点二", "参考点三"]),
        cards=[("时长", "成片", "在此输入说明"), ("镜头", "数量", "在此输入说明"),
               ("角色", "数量", "在此输入说明"), ("周期", "排期", "在此输入说明")],
        steps=[("剧本", "在此输入说明"), ("分镜", "在此输入说明"), ("制作", "在此输入说明"), ("合成", "在此输入说明")],
        nodes=["设定", "建模", "动画", "后期"],
        table=(["环节", "工具", "负责"], [["模型", "在此填工具", "在此填负责"],
                                         ["动作", "在此填工具", "在此填负责"],
                                         ["后期", "在此填工具", "在此填负责"]]),
        quote=("在此输入一句作品主题 / 立意。", "— 创作团队"),
        members=[("姓名", "导演"), ("姓名", "美术"), ("姓名", "动画")],
    ),
}


def build_deck(cat, style, outdir):
    t = THEMES[style]
    p = PACKS[cat["id"]]
    d = Deck(t)
    # 1 封面
    d.cover(p["deck"] if "deck" in p else cat["name"], p["sub"], p["meta"])
    # 2 目录
    d.agenda(p["agenda"])
    # 3 章节页
    d.section("01", p["agenda"][0], "在此输入本章导语 · 一句话点题")
    # 4 要点页
    d.bullets_page(p["kickers"][0], p["agenda"][0], p["bullets"], variant="dot")
    # 5 左右对比
    d.two_col(p["kickers"][0], p["two"][0] + " / " + p["two"][1], p["two"][0], p["two"][1], p["two"][2], p["two"][3], variant="vs")
    # 6 卡片指标
    d.cards("Metrics", "关键数据一览", p["cards"])
    # 7 时间线
    d.timeline(p["kickers"][2], "排期 / 路线图", p["steps"])
    # 8 流程
    d.process(p["kickers"][2], "工作流程", p["nodes"])
    # 9 图表
    d.chart_ph(p["kickers"][2], "数据图表", variant="bar" if style not in ("glass",) else "line")
    # 10 表格
    d.table_ph(p["kickers"][3], "明细表", p["table"][0], p["table"][1])
    # 11 图片网格
    d.gallery(p["kickers"][1], "图集 / 案例", cols=3)
    # 12 章节页二
    d.section("02", p["agenda"][2], "在此输入本章导语 · 一句话点题")
    # 13 引用
    d.quote(p["quote"][0], p["quote"][1])
    # 14 团队
    d.team(p["kickers"][3], "团队 / 分工", p["members"])
    # 15 结尾
    d.closing("谢谢观看", "在此输入联系方式 / 二维码 / 致谢")

    slug = "".join(ch.lower() if ch.isalnum() or ch in "-" else ("-" if ch in " &/" else "") for ch in cat["en"])
    slug = "-".join([x for x in slug.split("-") if x])
    catdir = os.path.join(outdir, cat["id"] + "-" + slug)
    os.makedirs(catdir, exist_ok=True)
    fname = "%s__%s.pptx" % (cat["id"].split("-")[0], style)
    path = os.path.join(catdir, fname)
    d.save(path)
    return path, len(d.prs.slides._sldIdLst), catdir


def make_potx(pptx_path, potx_path):
    """由 pptx 生成 .potx：复制包并修正 [Content_Types].xml 的演示文稿内容类型。"""
    tmp = potx_path + ".tmp"
    with zipfile.ZipFile(pptx_path, "r") as zin, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == "[Content_Types].xml":
                txt = data.decode("utf-8")
                txt = txt.replace(
                    "application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml",
                    "application/vnd.openxmlformats-officedocument.presentationml.template.main+xml")
                data = txt.encode("utf-8")
            zout.writestr(item, data)
    shutil.move(tmp, potx_path)
    return potx_path


def main():
    outdir = sys.argv[1] if len(sys.argv) > 1 else "templates"
    os.makedirs(outdir, exist_ok=True)
    manifest = {"themes": {k: {"label": v["label"], "en": v["en"], "preset": v["preset"],
                                "philosophy": v["philosophy"]} for k, v in THEMES.items()},
                "categories": [], "decks": []}
    total_slides = 0
    for cat in CATEGORIES:
        catentry = {"id": cat["id"], "name": cat["name"], "en": cat["en"], "needs": cat["needs"], "decks": []}
        for style in cat["styles"]:
            path, nslides, catdir = build_deck(cat, style, outdir)
            total_slides += nslides
            rel = os.path.relpath(path, outdir).replace("\\", "/")
            catentry["decks"].append({"style": style, "file": rel, "slides": nslides,
                                      "theme_label": THEMES[style]["label"]})
            manifest["decks"].append({"category": cat["id"], "style": style, "file": rel, "slides": nslides})
        manifest["categories"].append(catentry)
    # 生成 .potx 母版模板：每种设计风格各一套
    potx_dir = os.path.join(outdir, "_potx")
    os.makedirs(potx_dir, exist_ok=True)
    made = []
    first_by_style = {}
    for dk in manifest["decks"]:
        first_by_style.setdefault(dk["style"], dk["file"])
    for style in THEMES.keys():
        rel = first_by_style.get(style)
        if not rel:
            continue
        src = os.path.join(outdir, rel)
        dst = os.path.join(potx_dir, "slideforge-%s.potx" % style)
        if os.path.exists(src):
            make_potx(src, dst)
            made.append({"style": style, "file": os.path.relpath(dst, outdir).replace("\\", "/")})
    manifest["potx"] = made
    manifest["stats"] = {"decks": len(manifest["decks"]), "slides_total": total_slides,
                         "categories": len(manifest["categories"]), "themes": len(THEMES),
                         "potx": len(made)}
    with open(os.path.join(outdir, "index.manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=1)
    print("OK decks=%d slides=%d categories=%d themes=%d potx=%d"
          % (manifest["stats"]["decks"], total_slides, manifest["stats"]["categories"],
             manifest["stats"]["themes"], len(made)))


if __name__ == "__main__":
    main()
