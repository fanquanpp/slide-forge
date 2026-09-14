# -*- coding: utf-8 -*-
"""SlideForge 动画引擎：逐元素分级入场动画 + 多样化切换特效。

入场 XML 结构严格照搬 pptx-animation-skill 的 oracle 模板（entr/filter_effect），
并包裹进标准 <p:timing> 时间树；切换特效使用标准 <p:transition> 子元素。
"""
from pptx.oxml.ns import qn

# ---- 入场滤镜词表（来自 oracle/filter_vocabulary，含 preset 映射）----
# filter -> (preset_id, preset_subtype)
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
# 每个主题/种子用的滤波序列（视觉上“细致且不呆板”）
FILTER_RING = [
    "fade", "wipe(right)", "circle(in)", "wipe(up)", "blinds(horizontal)",
    "checkerboard(across)", "wheel(2)", "dissolve", "strips(downRight)", "barn(inHorizontal)",
    "wipe(left)", "wedge", "randombar(horizontal)", "wheel(1)", "wipe(down)",
]

# ---- 切换特效（标准 <p:transition> 子元素）----
# (name, attr_key, attr_val, speed)
TRANSITIONS = [
    ("fade", None, None, "med"),
    ("push", "dir", "l", "med"),
    ("wipe", "dir", "u", "med"),
    ("split", "orient", "horz", "med"),
    ("blinds", "dir", "horz", "med"),
    ("circle", "dir", "in", "med"),
    ("comb", "dir", "horz", "med"),
    ("dissolve", None, None, "med"),
    ("zoom", "dir", "in", "med"),
    ("cover", "dir", "l", "med"),
    ("checker", "dir", "across", "med"),
    ("newsflash", None, None, "med"),
    ("push", "dir", "u", "med"),
    ("wipe", "dir", "d", "med"),
]

E = "{http://schemas.openxmlformats.org/presentationml/2006/main}"


def set_transition(slide, spec):
    """写入单页切换特效（在 <p:clrMapOvr> 之后）。"""
    name, key, val, spd = spec
    sld = slide._element
    for t in sld.findall(qn("p:transition")):
        sld.remove(t)
    trans = sld.makeelement(qn("p:transition"), {"spd": spd})
    child = sld.makeelement(qn("p:%s" % name), {})
    if key:
        child.set(key, val)
    trans.append(child)
    anchor = sld.find(qn("p:clrMapOvr"))
    if anchor is not None:
        anchor.addnext(trans)
    else:
        cSld = sld.find(qn("p:cSld"))
        (cSld.addnext(trans) if cSld is not None else sld.insert(0, trans))


def _effect_par(spid, filt, dur, delay, par_id, node_type):
    """按 oracle entr/filter_effect 模板生成一个入场效果 <p:par>。"""
    pid, psub = ENTRANCE.get(filt, (9, 0))
    set_bid = par_id + 1
    eff_bid = par_id * 10 + 1
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
             sb=set_bid, eb=eff_bid, spid=spid, filt=filt)


def build_timing(slide, seed, sw=13.333, sh=7.5, max_items=14, step=130):
    """为一页生成细致分级入场动画：元素按位置排序，逐个错峰入场。"""
    shapes = []
    for shp in slide.shapes:
        try:
            w, h = shp.width, shp.height
            if w is None or h is None:
                continue
            win, hin = w / 914400.0, h / 914400.0
        except Exception:
            continue
        # 跳过整页背景
        if win >= sw - 0.2 and hin >= sh - 0.2:
            continue
        if not shp.has_text_frame and shp.shape_type is None:
            continue
        shapes.append(((shp.top or 0), (shp.left or 0), shp.shape_id))
    shapes.sort()
    shapes = shapes[:max_items]
    if not shapes:
        return None
    frags = []
    pid = 5
    for i, (top, left, spid) in enumerate(shapes):
        filt = FILTER_RING[(seed + i) % len(FILTER_RING)]
        dur = 450 + ((seed + i) % 4) * 120          # 450~810ms
        delay = i * step                            # 错峰
        nt = "clickEffect" if i == 0 else "afterEffect"
        frags.append(_effect_par(spid, filt, dur, delay, pid, nt))
        pid += 2
    return (
        '<p:timing xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"><p:tnLst><p:par>'
        '<p:cTn id="1" dur="indefinite" restart="never" nodeType="tmRoot"><p:childTnLst>'
        '<p:seq concurrent="1" nextAc="seek"><p:cTn id="2" dur="indefinite" nodeType="mainSeq"><p:childTnLst>'
        '<p:par><p:cTn id="3" fill="hold"><p:stCondLst><p:cond delay="indefinite"/></p:stCondLst>'
        '<p:childTnLst>' + "".join(frags) + '</p:childTnLst></p:cTn></p:par>'
        '</p:childTnLst></p:cTn>'
        '<p:prevCondLst><p:cond evt="onPrev" delay="0"><p:tgtEl><p:sldTgt/></p:tgtEl></p:cond></p:prevCondLst>'
        '<p:nextCondLst><p:cond evt="onNext" delay="0"><p:tgtEl><p:sldTgt/></p:tgtEl></p:cond></p:nextCondLst>'
        '</p:seq></p:childTnLst></p:cTn></p:par></p:tnLst></p:timing>'
    )


def apply_to_slide(slide, seed, trans_spec, sw=13.333, sh=7.5):
    """写入切换特效 + 入场动画时间树（顺序：transition 后接 timing）。"""
    set_transition(slide, trans_spec)
    xml = build_timing(slide, seed, sw, sh)
    if not xml:
        return
    from lxml import etree
    frag = etree.fromstring(xml.encode("utf-8"))
    sld = slide._element
    for t in sld.findall(qn("p:timing")):
        sld.remove(t)
    anchor = sld.find(qn("p:transition"))
    if anchor is not None:
        anchor.addnext(frag)
    else:
        cSld = sld.find(qn("p:cSld"))
        (cSld.addnext(frag) if cSld is not None else sld.append(frag))
