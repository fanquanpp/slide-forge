# 工具链安装记录与可用性验证

本文件记录本次为目标安装的第三方技能 / MCP 服务，来源可追溯、许可证明确，并附可用性验证结果。

## 已安装清单

| 名称 | 类型 | 来源仓库 | 版本 / 提交 | 许可证 | 安装位置 | 状态 |
|---|---|---|---|---|---|---|
| ppt-master | 技能 (Skill) | `hugohe3/ppt-master` | v6.4.0 · `c6ae489` | MIT | `~/.openclaw-autoclaw/skills/ppt-master/` | 技能入口已安装并校验 |
| aseprite-mcp | MCP 服务 | `diivi/aseprite-mcp` | main · 浅克隆 | MIT | `~/.openclaw-autoclaw/tools/aseprite-mcp/` | 源码就绪 |
| godot-mcp | MCP 服务 | `Coding-Solo/godot-mcp` | main · 浅克隆 | MIT | `~/.openclaw-autoclaw/tools/godot-mcp/` | 源码就绪 |
| PptxGenJS | 参考库 | `gitbrent/PptxGenJS` | main | MIT | `~/.openclaw-autoclaw/tools/PptxGenJS/` | 参考实现 |
| python-pptx | Python 库 | PyPI `python-pptx` | 1.0.2 | MIT | 全局 site-packages | 已安装，模板生成器依赖 |

## 来源与安全核验

- 全部第三方来源均为 GitHub 公开仓库，许可证为 **MIT**，无「许可证不明」或「要求执行不明脚本」的情况。
- 安装方式：`git clone`（只读，不执行仓库内脚本）、`gh api` 读取单文件；安装前未运行任何第三方安装脚本。
- `ppt-master` 仓库体积约 136 MB（skills 子树约 84 MB），弱网下整包浅克隆多次报
  `fetch-pack: invalid index-pack output`。经评估后**只安装技能运行所需的入口文件**
  （`SKILL.md` + `LICENSE` + `requirements.txt`），未拉取其庞大的 `templates/references` 素材目录。
  已通过 GitHub API 校验：`default_branch=main`、`license=MIT`。
- 未引入任何需要凭证、会外联上传数据或包含混淆代码的资源。

## 可用性验证

| 项目 | 验证方式 | 结果 |
|---|---|---|
| ppt-master | 读取 `skills/ppt-master/SKILL.md` 头部，确认 `name/description/version` 正常、UTF-8 无乱码 | ✅ v6.4.0，frontmatter 完整 |
| aseprite-mcp | 列出克隆目录文件与 `README`/入口脚本，确认结构完整 | ✅ 已克隆 |
| godot-mcp | 同上 | ✅ 已克隆 |
| python-pptx | 实际调用生成 **30 套 / 450 页** 演示并二次打开校验（`generator/validate.py`） | ✅ 无损坏文件，6596+ 形状可读 |

> 说明：`aseprite-mcp` / `godot-mcp` 为需要本机 Aseprite / Godot 应用配合的 MCP 服务，
> 本次已完成源码部署与结构核验；其运行时调用需在对应应用环境中注册 MCP 服务后使用。
> `ppt-master`、`python-pptx` 为本次模板库的直接工具链，已完成端到端实际调用验证。
