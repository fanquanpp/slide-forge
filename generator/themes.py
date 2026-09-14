# -*- coding: utf-8 -*-
"""SlideForge 主题库 —— 每种主题是一套可替换的视觉系统（配色 / 字体 / 形状语言）。

仅包含版式与占位示例文本，不含任何正式业务内容。
"""

# 字体族：latin 与 east-asian 分开设置，保证中英文都清晰
FONT_SANS = "Segoe UI"
FONT_SANS_EA = "微软雅黑"
FONT_SERIF = "Georgia"
FONT_SERIF_EA = "宋体"
FONT_MONO = "Consolas"
FONT_MONO_EA = "等线"

THEMES = {
    # 11 Build —— 呼吸留白极简
    "build": dict(
        label="呼吸留白极简", en="Breathing Whitespace", preset="11 Build",
        philosophy="大量留白 + 单一强调色，克制中性，便于替换成任意品牌色。",
        bg="FBFBFA", surface="FFFFFF", ink="1A1A1A", ink2="8A8A8A",
        accent="2F6BFF", accent2="1A1A1A", line="E6E6E6",
        title_font=(FONT_SANS, FONT_SANS_EA), body_font=(FONT_SANS, FONT_SANS_EA),
        radius=0.10, decor="min",
    ),
    # 10 Müller-Brockmann —— 数学网格功能主义
    "brockmann": dict(
        label="数学网格功能主义", en="Swiss Grid", preset="10 Müller-Brockmann",
        philosophy="严格网格与对齐，双色体系，适合数据、计划与结构化汇报。",
        bg="FFFFFF", surface="F7F7F5", ink="111111", ink2="6B6B6B",
        accent="E2231A", accent2="111111", line="D8D8D4",
        title_font=(FONT_SANS, FONT_SANS_EA), body_font=(FONT_SANS, FONT_SANS_EA),
        radius=0.0, decor="grid",
    ),
    # 17 Takram —— 柔和科技图表
    "takram": dict(
        label="柔和科技图表", en="Soft Tech", preset="17 Takram",
        philosophy="圆角、柔影与图表即艺术，适合作品集、产品提案与数据看板。",
        bg="F5F3EF", surface="FFFFFF", ink="2B2B2B", ink2="9A9A93",
        accent="3FA88C", accent2="E2A03F", line="E4E0D8",
        title_font=(FONT_SANS, FONT_SANS_EA), body_font=(FONT_SANS, FONT_SANS_EA),
        radius=0.24, decor="soft",
    ),
    # 商务蓝调
    "corporate": dict(
        label="商务蓝调", en="Corporate Blue", preset="09 Experimental Jetset",
        philosophy="沉稳海军蓝 + 金色点缀，适合汇报、方案与数据看板。",
        bg="FFFFFF", surface="F2F5FA", ink="10233F", ink2="5B6B82",
        accent="1E5FBF", accent2="C9A227", line="D7E0EE",
        title_font=(FONT_SANS, FONT_SANS_EA), body_font=(FONT_SANS, FONT_SANS_EA),
        radius=0.06, decor="band",
    ),
    # 暗黑霓虹
    "darkneon": dict(
        label="暗黑霓虹", en="Dark Neon", preset="06 Active Theory",
        philosophy="深空底色 + 霓虹青/品红，适合游戏提案、发布与科技主题。",
        bg="0B0F1A", surface="151B2B", ink="EAF2FF", ink2="94A3C4",
        accent="22D3EE", accent2="F472B6", line="26314B",
        title_font=(FONT_SANS, FONT_SANS_EA), body_font=(FONT_SANS, FONT_SANS_EA),
        radius=0.08, decor="glow",
    ),
    # 复古像素
    "retropixel": dict(
        label="复古像素", en="Retro Pixel", preset="16 Territory Studio",
        philosophy="暗紫底 + 糖果色块，呼应像素美术与独立游戏审美。",
        bg="1B1B2F", surface="262647", ink="F4F4F8", ink2="A6A6C9",
        accent="FF6B6B", accent2="FFD93D", line="3B3B63",
        title_font=(FONT_MONO, FONT_MONO_EA), body_font=(FONT_SANS, FONT_SANS_EA),
        radius=0.0, decor="pixel",
    ),
    # 杂志编辑
    "editorial": dict(
        label="杂志编辑", en="Editorial", preset="19 Irma Boom",
        philosophy="暖纸底 + 砖红点缀，衬线标题，适合作品集与深度叙事。",
        bg="FAF6F0", surface="FFFFFF", ink="1C1B19", ink2="7A756C",
        accent="B23A2E", accent2="2A2A28", line="E7DFD2",
        title_font=(FONT_SERIF, FONT_SERIF_EA), body_font=(FONT_SANS, FONT_SANS_EA),
        radius=0.0, decor="rule",
    ),
    # 孟菲斯
    "memphis": dict(
        label="孟菲斯活力", en="Memphis Pop", preset="12 Sagmeister & Walsh",
        philosophy="高饱和撞色 + 几何形状，适合活动宣传与轻松场景。",
        bg="FFFFFF", surface="FFF7F2", ink="111111", ink2="6E6E6E",
        accent="FF4D6D", accent2="2EC4B6", line="F0D9E0",
        title_font=(FONT_SANS, FONT_SANS_EA), body_font=(FONT_SANS, FONT_SANS_EA),
        radius=0.14, decor="pop", decor3="FFB703",
    ),
    # 玻璃拟态
    "glass": dict(
        label="玻璃拟态", en="Glassmorphism", preset="05 Locomotive",
        philosophy="深色渐变 + 半透明卡片，适合产品发布与科技展示。",
        bg="101826", surface="1B2A44", ink="F2F6FF", ink2="9FB2D0",
        accent="7CC4FF", accent2="A78BFA", line="33456B",
        title_font=(FONT_SANS, FONT_SANS_EA), body_font=(FONT_SANS, FONT_SANS_EA),
        radius=0.12, decor="glass",
    ),
    # 赛博终端
    "terminal": dict(
        label="赛博终端", en="Cyber Terminal", preset="08 Resn",
        philosophy="黑底绿字等宽，命令行气质，适合技术教学与极客分享。",
        bg="0A0E0A", surface="111711", ink="C8FACC", ink2="6F9E78",
        accent="38D39F", accent2="E2E23F", line="1E2A1E",
        title_font=(FONT_MONO, FONT_MONO_EA), body_font=(FONT_MONO, FONT_MONO_EA),
        radius=0.0, decor="term",
    ),
    # 自然有机
    "organic": dict(
        label="自然有机", en="Organic", preset="18 Kenya Hara",
        philosophy="暖砂底 + 植物绿/陶土色，柔和圆角，适合笔记与生活方式主题。",
        bg="F3EFE6", surface="FFFFFF", ink="33352E", ink2="8C8A78",
        accent="6B8E5A", accent2="C98A5E", line="E3DCCB",
        title_font=(FONT_SANS, FONT_SANS_EA), body_font=(FONT_SANS, FONT_SANS_EA),
        radius=0.22, decor="organic",
    ),
    # 学术严谨
    "academic": dict(
        label="学术严谨", en="Academic", preset="04 Fathom",
        philosophy="冷静灰蓝 + 严谨结构，适合研究、课件与数据报告。",
        bg="FFFFFF", surface="F4F6F8", ink="22252A", ink2="6B7280",
        accent="34508C", accent2="B4552D", line="DDE3EA",
        title_font=(FONT_SERIF, FONT_SERIF_EA), body_font=(FONT_SANS, FONT_SANS_EA),
        radius=0.03, decor="rule",
    ),
}

# 用途分类 → 设计风格（每类至少两种不同设计）
CATEGORIES = [
    dict(
        id="01-teaching", name="编程教学课件", en="Programming Courseware",
        needs="来自 04-代码实践 / 05-编程学习资料 / 08-其他笔记，适用于讲课、培训、知识点串讲。",
        styles=["build", "terminal", "takram"],
    ),
    dict(
        id="02-game-gdd", name="游戏设计提案", en="Game Design Proposal",
        needs="来自 04-代码实践/Godot、godot-engine、深空之眼，适用于 GDD、玩法提案、立项。",
        styles=["darkneon", "retropixel", "corporate"],
    ),
    dict(
        id="03-portfolio", name="像素与美术作品集", en="Pixel & Art Portfolio",
        needs="来自 06-创作素材、Aseprite、MMD、Blender，适用于作品展示、约稿、投稿。",
        styles=["editorial", "retropixel", "build"],
    ),
    dict(
        id="04-club-event", name="社团活动策划", en="Club Event Planning",
        needs="来自 07-个人文档/社团活动、软工协会总章程、活动策划，适用于策划、申报、竞聘。",
        styles=["memphis", "organic", "build"],
    ),
    dict(
        id="05-project-report", name="项目汇报与复盘", en="Project Report & Retrospective",
        needs="来自代码实践与课程项目，适用于阶段汇报、结项、复盘总结。",
        styles=["brockmann", "corporate", "build"],
    ),
    dict(
        id="06-study-notes", name="学习笔记分享", en="Study Notes Sharing",
        needs="来自 08-其他笔记、网络技术资料、编程大礼包，适用于知识分享、读书会。",
        styles=["takram", "organic", "editorial", "academic"],
    ),
    dict(
        id="07-resume", name="求职简历与自我介绍", en="Resume & Self-Intro",
        needs="学生身份与作品积累，适用于简历、自我介绍、面试展示。",
        styles=["build", "editorial"],
    ),
    dict(
        id="08-promo", name="活动宣传与推广", en="Event Promo",
        needs="社团招新、活动预热、作品发布，适用于海报式宣讲与报名引导。",
        styles=["memphis", "glass", "darkneon"],
    ),
    dict(
        id="09-dashboard", name="数据看板与指标", en="Data Dashboard",
        needs="比赛/项目数据、社团统计，适用于指标展示、季度数据、看板大屏。",
        styles=["corporate", "glass", "takram"],
    ),
    dict(
        id="10-creative-pitch", name="内容创作提案", en="Creative Pitch",
        needs="来自 06-创作素材/剧本大纲、Stage、MMD-Motion，适用于动画/剧本/视频提案。",
        styles=["editorial", "darkneon", "organic"],
    ),
]
