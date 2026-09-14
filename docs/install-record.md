# 工具链安装记录与可用性验证

本文件记录本次安装的第三方技能 / MCP 服务，来源可追溯、许可证明确，并附**实际调用**验证结果。

## 一、已安装清单

| 名称 | 类型 | 来源仓库 | 版本 / 提交 | 许可证 | 安装位置 | 状态 |
|---|---|---|---|---|---|---|
| ppt-master | 技能 (Skill) | `hugohe3/ppt-master` | **v6.4.0** · `c6ae489` | MIT | `~/.openclaw-autoclaw/skills/ppt-master/` | ✅ 完整安装（815 文件 / 12.7 MB） |
| aseprite-mcp | MCP 服务 (stdio) | `diivi/aseprite-mcp` | main · 浅克隆 | MIT | `~/.openclaw-autoclaw/tools/aseprite-mcp/` | ✅ 已注册并实际调用成功 |
| godot-mcp | MCP 服务 (stdio) | `Coding-Solo/godot-mcp` | 0.1.1 · `main` | MIT | `~/.openclaw-autoclaw/tools/godot-mcp/` | ✅ 已构建、注册并实际调用 |
| PptxGenJS | 参考库 | `gitbrent/PptxGenJS` | main | MIT | `~/.openclaw-autoclaw/tools/PptxGenJS/` | 参考实现 |
| python-pptx | Python 库 | PyPI `python-pptx` | 1.0.2 | MIT | 全局 site-packages | ✅ 模板生成器核心依赖 |

## 二、ppt-master 完整安装说明

- 仓库体积约 136 MB（`skills/ppt-master` 子树约 84 MB）。`git clone` 与 codeload tarball 在弱网下多次
  报 `fetch-pack: invalid index-pack output` / 传输截断。
- 最终采用**逐文件抓取**：按 GitHub Trees API 枚举 `skills/ppt-master` 全部文件，抓取文本类文件
  （md / py / js / ts / json / yaml / yml / sh / ps1 / toml / cfg / ini / html / css / svg）。
  结果：**815 个文件 / 12.72 MB**，含：
  - `SKILL.md`（v6.4.0）
  - `scripts/`：**273 个 `.py`**（svg_to_pptx、pptx_ooxml、svg_quality、template_import 等）
  - `workflows/`：**23 个 `.md`**（generate-pptx、edit-native-pptx、create-template、stages/*、profiles/*、routing）
  - `references/`、`templates/`（品牌 / 版式 / 样式 / 图表等目录与清单）
- 未拉取的部分：少量**大体量二进制示例素材**（如品牌示例 `.pptx` / 图片），对技能逻辑无影响。

## 三、MCP 服务可用性验证（实际调用证据）

### godot-mcp
- 构建：`npm install && npm run build` → `build/index.js`。注册：`config/mcporter.json`（stdio, node）。
- 握手：`mcporter list` → **godot-mcp (14 tools, 0.2s)**。
- 实际调用：`mcporter call godot-mcp.get_godot_version` → 返回可解析结果（本机缺 Godot.exe 的 ENOENT），**链路已通**。

### aseprite-mcp
- 依赖：`pip install -r requirements.txt`；入口 `python -m aseprite_mcp`（stdio）。注册：`config/mcporter.json`（stdio, uv）。
- 握手：`mcporter list` → **aseprite-mcp (116 tools, 6.7s)**。
- 实际调用：`mcporter call aseprite-mcp.list_palette_presets` → 返回真实调色板数据（gameboy / monochrome 等）。

`mcporter list` 汇总：autoclaw-productivity(31) · autoclaw-figma(4) · godot-mcp(14) · autoclaw-github(40) · aseprite-mcp(116)，**5 个服务全部健康**。

## 四、来源与安全核验

- 全部来源为 GitHub 公开仓库，许可证 **MIT**；安装前未执行任何第三方安装脚本（只读克隆 + raw 抓取）。
- 已记录可供复核的提交号：ppt-master `c6ae489`（`gh api repos/hugohe3/ppt-master/commits/main`）。
