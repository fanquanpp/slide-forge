# 交接文档

目标：让一个不了解背景的人，能独立完成 **① 新增条目 ② 更新台账 ③ 执行复核** 三件事。

## 一、目录结构

```
ppt-template-hub/
├─ templates/                     # 全部成品条目（120 套 .pptx）
│  ├─ <编号-id>/<两位分类号>__<风格key>.pptx
│  ├─ _potx/slideforge-<风格key>.potx     # 24 套母版
│  └─ index.manifest.json         # 主清单台账（权威数据源）
├─ generator/                     # 生成器
│  ├─ themes.py     # 24 风格 + 24 用途定义（改这里扩风格/用途）
│  ├─ slidekit.py   # 24 种版面原型 + 切换动效
│  ├─ build.py      # 构建全部模板 + 台账
│  ├─ validate.py   # 校验可打开性/页数/potx 内容类型
│  └─ requirements.txt
├─ scripts/                       # build_site.py / build_readme.py / build_ledger.py / qa_check.py
├─ docs/                          # 台账 CATALOG.md、覆盖矩阵、USAGE.md、质检、回滚、交接
├─ assets/previews/               # 风格预览 SVG
├─ index.html                     # Pages 站点
├─ README.md · LICENSE(MIT) · .github/workflows/pages.yml
```

## 二、命名规范

| 对象 | 规则 | 示例 |
|---|---|---|
| 分类目录 | `<两位分类号>-<英文名 slug>` | `01-teaching-programming-courseware` |
| 模板文件 | `<两位分类号>__<风格key>.pptx` | `01__build.pptx` |
| 母版文件 | `slideforge-<风格key>.potx` | `slideforge-darkneon.potx` |
| 台账编号 | `SF-` + 三位序号 | `SF-001` |
| 母版编号 | `POTX-` + 两位序号 | `POTX-01` |
| 风格 key | 小写英文 | `build` / `darkneon` / `retrogrid`… |

## 三、任务一 · 新增条目

**加一种设计风格**：在 `generator/themes.py` 的 `THEMES` 增加一个条目（配色/字体/圆角/装饰/`transition`），
再把它的中文标签加入目标分类的 `styles` 列表即可。

**加一个用途分类**：在 `themes.py` 的 `_CATS` 追加一行（id/中文名/英文名/来源说明/风格标签列表），
并在 `generator/build.py` 的 `CAT_CONTENT` 加同名 id 的内容包（`sec`/`nodes`/`quote`，全部占位文本）。

然后执行第四节的重建流程。

## 四、任务二 · 更新台账（重建全套）

```bash
pip install -r generator/requirements.txt
python generator/build.py templates     # 重建模板 + index.manifest.json
python generator/validate.py templates  # 校验
python scripts/build_ledger.py          # 重建 CATALOG.md / catalog.csv / coverage-matrix / USAGE.md / stats.json
python scripts/build_site.py            # 重建 index.html + 预览图
python scripts/build_readme.py          # 重建 README.md
```

> 全部命令都只读 `templates/index.manifest.json` 派生其它文档，确保台账与文件始终一致。

## 五、任务三 · 执行复核

```bash
python generator/validate.py templates   # 文件侧：可打开性、页数、potx 内容类型
python scripts/qa_check.py               # 抽检 ≥20%：占位内容、命名、台账对照、动效
```

判定标准：`validate.py` 的 `broken` 为空、`potx` 全为 `true`；`qa_check.py` 的 `issues=0`。

## 六、发布

```bash
git add -A && git commit -m "..." && git push
```

Pages 由 `.github/workflows/pages.yml` 自动从 `main` 发布（也可在仓库 Settings → Pages 选 `main / (root)`）。
回滚与异常处理见 `docs/rollback.md`。

## 七、限制与注意事项

- 模板字体依赖系统字体（微软雅黑 / Segoe UI / Consolas 等）；替换商用字体请自行确认授权。
- 模板只含占位内容，**不得**写入真实业务数据或个人信息。
- `generator/build.py` 是覆盖写入，无需先删目录；若需清理请人工确认后再操作。
