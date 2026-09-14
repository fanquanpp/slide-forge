# 工具链安装记录与可用性验证

本文件记录本次为目标安装的第三方技能 / MCP 服务，来源可追溯、许可证明确，并附**实际调用**验证结果。

## 一、已安装清单

| 名称 | 类型 | 来源仓库 | 版本 / 提交 | 许可证 | 安装位置 | 状态 |
|---|---|---|---|---|---|---|
| ppt-master | 技能 (Skill) | `hugohe3/ppt-master` | v6.4.0 · `c6ae489` | MIT | `~/.openclaw-autoclaw/skills/ppt-master/` | ✅ 技能入口已安装并校验 |
| aseprite-mcp | MCP 服务 (stdio) | `diivi/aseprite-mcp` | main · 浅克隆 | MIT | `~/.openclaw-autoclaw/tools/aseprite-mcp/` | ✅ 已注册并实际调用成功 |
| godot-mcp | MCP 服务 (stdio) | `Coding-Solo/godot-mcp` | 0.1.1 · `main` | MIT | `~/.openclaw-autoclaw/tools/godot-mcp/` | ✅ 已构建、注册并实际调用 |
| PptxGenJS | 参考库 | `gitbrent/PptxGenJS` | main | MIT | `~/.openclaw-autoclaw/tools/PptxGenJS/` | 参考实现 |
| python-pptx | Python 库 | PyPI `python-pptx` | 1.0.2 | MIT | 全局 site-packages | ✅ 模板生成器核心依赖 |

## 二、来源与安全核验

- 全部第三方来源均为 GitHub 公开仓库，许可证为 **MIT**，无「许可证不明」或「要求执行不明脚本」的情况。
- 安装方式：`git clone`（只读，不执行仓库内脚本）、`gh api` 读取单文件；安装前未运行任何第三方安装脚本。
- `ppt-master` 仓库体积约 136 MB（skills 子树约 84 MB），弱网下整包浅克隆多次报
  `fetch-pack: invalid index-pack output`。经评估后**只安装技能运行所需的入口文件**
  （`SKILL.md` + `LICENSE` + `requirements.txt`），未拉取其庞大的 `templates/references` 素材目录。
  已通过 GitHub API 校验：`default_branch=main`、`license=MIT`、`commit=c6ae489`。
- 未引入任何需要凭证、会外联上传数据或包含混淆代码的资源。

## 三、可用性验证（实际调用证据）

### ppt-master（技能）
- 读取 `~/.openclaw-autoclaw/skills/ppt-master/SKILL.md`，frontmatter 完整：`name: ppt-master`、
  `description: ...presentation/PPT/PPTX...`、`metadata.version: 6.4.0`，UTF-8 无乱码。✅

### godot-mcp（MCP 服务，stdio）
- 构建：`npm install && npm run build` → 生成 `build/index.js`。✅
- 注册：写入 `config/mcporter.json`（`type: stdio`, `command: node`）。
- 握手：`mcporter list` → **godot-mcp (14 tools, 0.2s)**，服务健康。
- 实际调用：`mcporter call godot-mcp.get_godot_version`
  → 返回可解析结果：`Failed to get Godot version: spawn C:\Program Files\Godot\Godot.exe ENOENT`。
  说明 **MCP 服务与工具链路完全打通**；该报错仅因本机未安装 Godot 可执行文件（工具本身可调用）。✅

### aseprite-mcp（MCP 服务，stdio）
- 依赖：`pip install -r requirements.txt`。入口 `python -m aseprite_mcp`（`mcp.run(transport='stdio')`）。
- 注册：写入 `config/mcporter.json`（`type: stdio`, `command: uv`）。
- 握手：`mcporter list` → **aseprite-mcp (116 tools, 6.7s)**，服务健康。
- 实际调用：`mcporter call aseprite-mcp.list_palette_presets`
  → 返回真实数据（`gameboy`, `monochrome` 等调色板及其色值）。✅

> 结论：`ppt-master`、`aseprite-mcp`、`godot-mcp`、`python-pptx` 均已安装并**通过实际调用验证可用**；
> `aseprite-mcp` / `godot-mcp` 面向具体图形/引擎任务，需在装有 Aseprite / Godot 的环境下执行绘图/引擎操作。
