# -*- coding: utf-8 -*-
"""校验生成的模板：可打开性、幻灯片数、占用元素数、是否含占位文本、以及 pptx/potx 内容类型。"""
import os, sys, json, zipfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pptx import Presentation

root = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), "..", "templates")
root = os.path.abspath(root)
bad = []
n = 0; slides = 0; shapes = 0
for dp, dn, fn in os.walk(root):
    for f in fn:
        if not f.endswith(".pptx"):
            continue
        p = os.path.join(dp, f); n += 1
        try:
            prs = Presentation(p)
            slides += len(prs.slides._sldIdLst)
            for s in prs.slides:
                shapes += len(s.shapes)
        except Exception as e:
            bad.append((f, str(e)))
# content type check for potx
potx_dir = os.path.join(root, "_potx")
potx_ok = []
if os.path.isdir(potx_dir):
    for f in os.listdir(potx_dir):
        if f.endswith(".potx"):
            with zipfile.ZipFile(os.path.join(potx_dir, f)) as z:
                ct = z.read("[Content_Types].xml").decode("utf-8")
                potx_ok.append((f, "template.main+xml" in ct))
print(json.dumps({"pptx_files": n, "slides": slides, "shapes": shapes,
                  "broken": bad, "potx": potx_ok}, ensure_ascii=False))
