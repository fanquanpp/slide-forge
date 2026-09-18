# -*- coding: utf-8 -*-
"""SlideForge 动画引擎 v3：角色化切换 + 确定性 Morph 配对 + chrome 静态入场 + 强调动画。

规范来源：ppt-master references/animations.md 与 scripts/docs/pptx-transitions.md
- 切换按「页面角色（关系）」选族，不再机械轮换：封面=reveal/split、流程=push、
  数据=ripple/circle/clock、集合=pan/gallery/conveyor、正文=fade（克制基线）。
- p14/p15/morph 特效一律 mc:AlternateContent 载体 + fade Fallback，Choice/Fallback
  的 spd/advClick/advTm 保持同步。
- Morph 仅用于现代主题连续阅读页（封面/章节/结尾边界不 morph），以 !!key 命名
  跨页持久载体（品牌规线/页脚线）实现确定性配对（p159:morph option=byObject）。
- 入场动画只作用于内容元素；chrome:* 与 !!* 命名的形状保持静态。
- motion:hero 命名形状（大数字）入场后追加一次 grow 强调（presetClass="emph"）。
"""
from pptx.oxml.ns import qn

# ---- 命名空间（与 ppt-master pptx_transitions.py 一致）----
P14_NS = "http://schemas.microsoft.com/office/powerpoint/2010/main"
P15_NS = "http://schemas.microsoft.com/office/powerpoint/2012/main"
P159_NS = "http://schemas.microsoft.com/office/powerpoint/2015/09/main"
MC_NS = "http://schemas.openxmlformats.org/markup-compatibility/2006"
PML_NS = "http://schemas.openxmlformats.org/presentationml/2006/main"

EXT_NS = {"p14": P14_NS, "p15": P15_NS, "p159": P159_NS}

# ---- 入场滤镜词表（filter -> presetID, presetSubtype）----
ENTRANCE = {
    "fade": (9, 0), "dissolve": (10, 0),
    "wipe(down)": (22, 4), "wipe(up)": (22, 1), "wipe(left)": (22, 8), "wipe(right)": (22, 2),
    "wedge": (37, 0), "wheel(1)": (21, 1), "wheel(2)": (21, 2), "wheel(3)": (21, 3), "wheel(4)": (21, 4),
    "circle(in)": (18, 12), "circle(out)": (19, 12),
    "strips(downLeft)": (25, 0), "strips(downRight)": (25, 1), "strips(upLeft)": (25, 2), "strips(upRight)": (25, 3),
    "blinds(horizontal)": (42, 10), "blinds(vertical)": (42, 5),
    "checkerboard(across)": (43, 0), "checkerboard(down)": (43, 1),
    "barn(inVertical)": (45, 0), "barn(inHorizontal)": (45, 1),
    "randombar(horizontal)": (52, 0), "randombar(vertical)": (52, 1),
}
FILTER_RING = [
    "fade", "wipe(right)", "circle(in)", "wipe(up)", "blinds(horizontal)",
    "checkerboard(across)", "wheel(2)", "dissolve", "strips(downRight)", "barn(inHorizontal)",
    "wipe(left)", "wedge", "randombar(horizontal)", "wheel(1)", "wipe(down)",
]

# ---- 页面角色 -> 切换族 ----
# (effect, prefix, element, attrs)；prefix None = 标准 p: 直接载体
FAMILIES = {
    "cover": [
        ("reveal", "p14", "reveal", {"dir": "l"}),
        ("split", None, "split", {"orient": "horz", "dir": "out"}),
        ("circle", None, "circle", {"dir": "in"}),
    ],
    "section": [
        ("flash", "p14", "flash", {}),
        ("reveal", "p14", "reveal", {"dir": "r"}),
        ("wipe", None, "wipe", {"dir": "l"}),
    ],
    "flow": [
        ("push", None, "push", {"dir": "l"}),
        ("push", None, "push", {"dir": "u"}),
        ("wipe", None, "wipe", {"dir": "r"}),
    ],
    "data": [
        ("ripple", "p14", "ripple", {}),
        ("circle", None, "circle", {"dir": "in"}),
        ("wheel", None, "wheel", {"spokes": "1"}),
    ],
    "collect": [
        ("pan", "p14", "pan", {"dir": "l"}),
        ("gallery", "p14", "gallery", {"dir": "r"}),
        ("conveyor", "p14", "conveyor", {"dir": "r"}),
    ],
    "content": [
        ("fade", None, "fade", {}),
    ],
    "closing": [
        ("fade", None, "fade", {}),
    ],
}
MODERN_SWAP = {  # modern 主题的数据/集合族升级为更具电影感的键
    "data": [("glitter", "p14", "glitter", {"dir": "l"}), ("vortex", "p14", "vortex", {"dir": "l"})],
    "collect": [("switch", "p14", "switch", {"dir": "l"}), ("flip", "p14", "flip", {"dir": "r"})],
}
MORPH_THEMES = {"darkneon", "glass", "vaporwave", "gradient", "luxury", "bubble"}
MORPH_FLOW_ROLES = {"content", "flow"}

# 角色 -> 自动换片驻留毫秒（未列出的角色 8000）
ROLE_DWELL = {"cover": 6000, "section": 6000, "data": 10000, "collect": 10000}

STATIC_PREFIX = ("chrome:", "!!")  # 时间树跳过：chrome 与 morph 配对载体


def _carrier_attrs(dwell):
    return ' spd="med" advClick="1" advTm="%d"' % dwell


def _effect_el(prefix, elem, attrs):
    a = "".join(' %s="%s"' % kv for kv in attrs.items())
    return "<%s:%s%s/>" % (prefix, elem, a)


def transition_xml(spec, dwell):
    """按 ppt-master MCE 契约生成切换载体 XML（False=直接 p:transition）。"""
    name, prefix, elem, attrs = spec
    ser_prefix = prefix or "p"  # 标准特效直接用 p: 前缀
    inner = _effect_el(ser_prefix, elem, attrs)
    if prefix is None:
        return False, ('<p:transition xmlns:p="%s"%s>%s</p:transition>'
                       % (PML_NS, _carrier_attrs(dwell), inner))
    xml = (
        '<mc:AlternateContent xmlns:mc="%(mc)s" xmlns:p="%(p)s">'
        '<mc:Choice xmlns:%(px)s="%(ns)s" Requires="%(px)s">'
        '<p:transition%(at)s>%(inner)s</p:transition>'
        '</mc:Choice>'
        '<mc:Fallback>'
        '<p:transition%(at)s><p:fade/></p:transition>'
        '</mc:Fallback>'
        '</mc:AlternateContent>'
    ) % dict(mc=MC_NS, p=PML_NS, px=prefix, ns=EXT_NS[prefix], at=_carrier_attrs(dwell), inner=inner)
    return True, xml


def plan_transition(role, prev_role, theme_key, i):
    """角色 -> 切换 spec；现代主题连续阅读页用 morph（byObject）。"""
    modern = theme_key in MORPH_THEMES
    if modern and prev_role is not None and prev_role in MORPH_FLOW_ROLES and role in MORPH_FLOW_ROLES:
        return ("morph", "p159", "morph", {"option": "byObject"})
    fam = list(FAMILIES.get(role, FAMILIES["content"]))
    if modern and role in MODERN_SWAP:
        fam = MODERN_SWAP[role] + fam
    return fam[i % len(fam)]


def dwell_of(role):
    return ROLE_DWELL.get(role, 8000)


MC_AC = "{%s}AlternateContent" % MC_NS  # python-pptx nsmap 无 mc 前缀，手工构造


def set_transition(slide, spec, dwell=8000):
    """写入单页切换载体（位置：p:clrMapOvr 之后、p:timing 之前）。"""
    is_alt, xml = transition_xml(spec, dwell)
    from lxml import etree
    frag = etree.fromstring(xml.encode("utf-8"))
    sld = slide._element
    for old in sld.findall(qn("p:transition")):
        sld.remove(old)
    for old in sld.findall(MC_AC):
        sld.remove(old)
    anchor = sld.find(qn("p:clrMapOvr"))
    if anchor is not None:
        anchor.addnext(frag)
    else:
        cSld = sld.find(qn("p:cSld"))
        (cSld.addnext(frag) if cSld is not None else sld.insert(0, frag))


def _entrance_par(spid, filt, dur, delay, par_id, node_type):
    """oracle entr/filter_effect 结构（v2 起经官方校验器验证无死路径）。"""
    pid, psub = ENTRANCE.get(filt, (9, 0))
    return (
        '<p:par><p:cTn id="%(id)d" dur="%(dur)d" fill="hold" nodeType="%(nt)s" grpId="0" '
        'presetID="%(pid)d" presetClass="entr" presetSubtype="%(psub)d">'
        '<p:stCondLst><p:cond delay="%(delay)d"/></p:stCondLst>'
        '<p:childTnLst>'
        '<p:set><p:cBhvr><p:cTn id="%(sb)d" dur="1" fill="hold">'
        '<p:stCondLst><p:cond delay="0"/></p:stCondLst></p:cTn>'
        '<p:tgtEl><p:spTgt spid="%(spid)d"/></p:tgtEl>'
        '<p:attrNameLst><p:attrName>style.visibility</p:attrName></p:attrNameLst></p:cBhvr>'
        '<p:to><p:strVal val="visible"/></p:to></p:set>'
        '<p:animEffect transition="in" filter="%(filt)s"><p:cBhvr>'
        '<p:cTn id="%(eb)d" dur="%(dur)d"/><p:tgtEl><p:spTgt spid="%(spid)d"/></p:tgtEl></p:cBhvr></p:animEffect>'
        '</p:childTnLst></p:cTn></p:par>'
    ) % dict(id=par_id, dur=dur, nt=node_type, pid=pid, psub=psub, delay=delay,
             sb=par_id + 1, eb=par_id * 10 + 1, spid=spid, filt=filt)


def _emph_grow_par(spid, delay, par_id):
    """强调：grow/shrink（presetID=6, presetClass=emph），放大至 108% 后收住。"""
    return (
        '<p:par><p:cTn id="%(id)d" dur="500" fill="hold" nodeType="afterEffect" grpId="0" '
        'presetID="6" presetClass="emph" presetSubtype="0">'
        '<p:stCondLst><p:cond delay="%(delay)d"/></p:stCondLst>'
        '<p:childTnLst>'
        '<p:animScale><p:cBhvr>'
        '<p:cTn id="%(cb)d" dur="500" fill="hold"/>'
        '<p:tgtEl><p:spTgt spid="%(spid)d"/></p:tgtEl>'
        '</p:cBhvr><p:by x="108000" y="108000"/></p:animScale>'
        '</p:childTnLst></p:cTn></p:par>'
    ) % dict(id=par_id, delay=delay, cb=par_id * 10 + 1, spid=spid)


def build_timing(slide, seed, sw=13.333, sh=7.5, max_items=14, step=130):
    """内容元素分级入场；motion:hero 形状入场后追加 grow 强调；chrome/!! 载体静态。"""
    shapes = []
    for shp in slide.shapes:
        try:
            w, h = shp.width, shp.height
            if w is None or h is None:
                continue
            win, hin = w / 914400.0, h / 914400.0
        except Exception:
            continue
        if win >= sw - 0.2 and hin >= sh - 0.2:
            continue  # 整页背景
        if (shp.name or "").startswith(STATIC_PREFIX):
            continue  # chrome / morph 载体
        if not shp.has_text_frame and shp.shape_type is None:
            continue
        shapes.append(((shp.top or 0), (shp.left or 0), shp))
    shapes.sort(key=lambda t: (t[0], t[1]))
    shapes = shapes[:max_items]
    if not shapes:
        return None
    frags = []
    nid = 4  # tmRoot=1 mainSeq=2 wrapper=3；后续唯一小 id 从 4 起
    for i, (top, left, shp) in enumerate(shapes):
        filt = FILTER_RING[(seed + i) % len(FILTER_RING)]
        dur = 450 + ((seed + i) % 4) * 120
        delay = i * step
        nt = "clickEffect" if i == 0 else "afterEffect"
        frags.append(_entrance_par(shp.shape_id, filt, dur, delay, nid, nt))
        nid += 2  # 本 par 消耗 nid(主) + nid+1(set)
        if (shp.name or "").startswith("motion:hero"):
            frags.append(_emph_grow_par(shp.shape_id, delay + dur, nid))
            nid += 1
    return (
        '<p:timing xmlns:p="%s" xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">'
        '<p:tnLst><p:par>'
        '<p:cTn id="1" dur="indefinite" restart="never" nodeType="tmRoot"><p:childTnLst>'
        '<p:seq concurrent="1" nextAc="seek"><p:cTn id="2" dur="indefinite" nodeType="mainSeq"><p:childTnLst>'
        '<p:par><p:cTn id="3" fill="hold"><p:stCondLst><p:cond delay="indefinite"/></p:stCondLst>'
        '<p:childTnLst>' + "".join(frags) + '</p:childTnLst></p:cTn></p:par>'
        '</p:childTnLst></p:cTn>'
        '<p:prevCondLst><p:cond evt="onPrev" delay="0"><p:tgtEl><p:sldTgt/></p:tgtEl></p:cond></p:prevCondLst>'
        '<p:nextCondLst><p:cond evt="onNext" delay="0"><p:tgtEl><p:sldTgt/></p:tgtEl></p:cond></p:nextCondLst>'
        '</p:seq></p:childTnLst></p:cTn></p:par></p:tnLst></p:timing>'
    ) % PML_NS


def apply_to_slide(slide, seed, trans_spec, dwell, sw=13.333, sh=7.5):
    """切换载体 + 入场/强调时间树（顺序：transition → timing）。"""
    set_transition(slide, trans_spec, dwell)
    xml = build_timing(slide, seed, sw, sh)
    if not xml:
        return
    from lxml import etree
    frag = etree.fromstring(xml.encode("utf-8"))
    sld = slide._element
    for t in sld.findall(qn("p:timing")):
        sld.remove(t)
    anchor = sld.find(qn("p:transition"))
    if anchor is None:
        anchor = sld.find(MC_AC)
    if anchor is not None:
        anchor.addnext(frag)
    else:
        cSld = sld.find(qn("p:cSld"))
        (cSld.addnext(frag) if cSld is not None else sld.append(frag))


def set_use_timings(prs):
    """ppt-master 包级硬规则：写 advTm 必须显式 presProps.xml showPr useTimings=1。"""
    try:
        for part in prs.part.package.iter_parts():
            if str(part.partname) != "/ppt/presProps.xml":
                continue
            el = getattr(part, "_element", None)
            if el is not None:  # XmlPart：直接改树，保存时序列化
                show = el.find(qn("p:showPr"))
                if show is None:
                    show = el.makeelement(qn("p:showPr"), {})
                    el.insert(0, show)
                show.set("useTimings", "1")
                return True
            from lxml import etree
            root = etree.fromstring(part.blob)
            show = root.find(qn("p:showPr"))
            if show is None:
                show = root.makeelement(qn("p:showPr"), {})
                root.insert(0, show)
            show.set("useTimings", "1")
            part._blob = etree.tostring(root, xml_declaration=True,
                                        encoding="UTF-8", standalone=True)
            return True
    except Exception:
        pass
    return False
