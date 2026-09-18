# 交接与运维手册

面向后续维护者：如何新增模板、重建索引、发布与回滚，以及常见异常处理。

## 1. 环境准备

```bash
pip install -r generator/requirements.txt     # python-pptx / XlsxWriter / Pillow
```

要求 Python ≥ 3.9。本机使用 Python 3.13。

## 2. 新增一种「设计风格」

1. 打开 `generator/themes.py`，在 `THEMES` 中新增一个条目（复制现有条目改配色/字体/圆角/装饰）。
2. 在 `CATEGORIES` 中把新风格 key 加入目标分类的 `styles` 列表（每类建议 ≥ 2 种风格）。
3. 如新增了装饰类型，在 `generator/slidekit.py` 的 `Deck.decor()` 中补充对应分支。

## 3. 新增一种「用途分类」

1. 在 `generator/themes.py` 的 `CATEGORIES` 追加分类（`id / name / en / needs / styles`）。
2. 在 `generator/build.py` 的 `PACKS` 中为同 `id` 添加内容包（全部使用占位文本）。
3. 重新生成（见下节）。

## 4. 重新生成全部产物

```bash
python generator/build.py templates     # 覆盖生成模板 + index.manifest.json + _potx
python generator/validate.py templates  # 校验：可打开性 / 页数 / 形状数 / .potx 内容类型
python scripts/build_site.py            # 重建 index.html 与 assets/previews/*.svg（含 og-cover.png）
python scripts/check_site.py            # 交付指标：docs/iterations/roundN.json + 全页快照 + HTML 配平校验
python scripts/build_readme.py          # 重建 README.md
```

> 注意：`build.py` 是**覆盖写入**，不需要先删除 `templates/`。若需清理，请在确认无他人在用后手动删除。

### 4.1 前端源码结构（改页面请改这里，不要手改 index.html）

- `scripts/site/page.html` —— 页面骨架，`__TOKEN__` 占位符由构建器注入；残留 token 会使构建报错退出。
- `scripts/site/style.css` / `scripts/site/app.js` —— 全部样式与脚本，构建期内联进 index.html（内联是刻意选择：静态单页省请求）。
- `scripts/build_site.py` —— 数据装配器：读 manifest → 生成卡片/筛选/JSON-LD/OG 封面 → 写 index.html 与预览图。
- `scripts/check_site.py` —— 站点指标（口径见 docs/iterations/roundN.json），迭代时每轮跑一次留档。

## 5. 发布到 GitHub Pages

- 仓库：<https://github.com/fanquanpp/slide-forge>
- Pages 由 `.github/workflows/pages.yml`（GitHub Actions）从 `main` 分支根目录发布。
- 手动发布：`git add -A && git commit -m "..." && git push`，随后在仓库 Settings → Pages 确认 Source 为
  「GitHub Actions」或 `main / (root)`。

## 6. 回滚

- 模板是**纯生成物**：任意版本都可用 `git checkout <commit> -- templates` 还原，再 `git push`。
- 若误改了生成器，用 `git revert <commit>` 回退生成器与产物，然后重跑第 4 节命令复核。
- 建议每次发布前打 tag：`git tag -a vX.Y -m "..."`。

## 7. 常见异常处理

| 现象 | 原因 | 处理 |
|---|---|---|
| `ModuleNotFoundError: No module named 'slidekit'` | Python 精简分发未把脚本目录加入 `sys.path` | `build.py` 已内置 `sys.path.insert(...)`；自定义脚本请同样处理 |
| PowerShell 写文件出现中文乱码 | 控制台编码非 UTF-8 | 用 `[System.IO.File]::WriteAllText(..., UTF8Encoding($false))` 或 `Out-File -Encoding utf8` |
| `.potx` 无法作为模板打开 | 内容类型未修正 | `build.py` 的 `make_potx()` 已把主文档类型改为 `template.main+xml`，`validate.py` 会校验 |
| 生成很慢 / 卡住 | 一次性生成全部 30 套属正常（约数秒~数十秒） | 如只需单类，可临时缩小 `CATEGORIES` 后运行 |
| GitHub clone 失败 | 大仓库 + 弱网 | 用 `--depth 1 --filter=blob:none --sparse`，或只取所需文件 |

## 8. 敏感信息约定

`templates/`、`docs/`、`index.html` 均为生成/撰写产物，**不得**写入任何原始文件名、绝对路径、
个人信息或令牌。发布前执行一次排查：

```bash
git grep -nE "[A-Z]:\\Users|[A-Za-z0-9_-]{32,}|gho_|ghp_|BEGIN (RSA|OPENSSH) PRIVATE KEY" -- . || echo "clean"
```
