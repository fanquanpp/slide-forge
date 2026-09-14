# 设计 / 演示 / 动画类 Skills 调研清单

> 联网检索 GitHub 得到，并说明其**可复用度与落地方式**。许可证均为 MIT（除个别标注）。

## 一、本次已安装（可直接复用）

| 名称 | 来源 | ★ | 许可 | 用途 / 落地方式 |
|---|---|---:|---|---|
| **pptx-animation-skill** | `BramAlkema/pptx-animation-skill` | 1 | 见仓库 | 生成**真正能播放**的 PowerPoint 动画 XML（含 oracle 校验与死路径清单）。→ 本项目的 `generator/anim.py` 直接采用其 `entr/filter_effect` oracle 模板；用其 `scripts/validate.py` 校验，结果 oracle-clean。 |
| **slide-design-skill** | `SlideSpeak/slide-design-skill` | 22 | 见仓库 | 描述需求即产出 1920×1080 的 HTML 幻灯片（含图表/表格/图片）。→ 作为 HTML 版 deck 的设计参考与风格锚点。 |
| **marp-slides** | `robonuggets/marp-slides` | 305 | 见仓库 | Marp（Markdown→幻灯片）技能，含 22 套示例 deck、SVG 图表、深浅色主题、看板组件。→ 作为 Markdown 驱动演示的模板与组件参考。 |

安装位置：`~/.openclaw-autoclaw/skills/{pptx-animation-skill,slide-design-skill,marp-slides}`。

## 二、检索到的其它相关资源（备选 / 参考）

| 名称 | 来源 | ★ | 适用场景 | 可复用度 |
|---|---|---:|---|---|
| Slidev | `slidevjs/slidev` | 48.7k | 开发者向 HTML 幻灯片框架，内置转场与代码动画 | 高（需 Node 工程） |
| Slidev Themes | `slidevjs/themes` | 217 | Slidev 官方主题集 | 中 |
| visual-cognition-slides | `edu-ai-builders/visual-cognition-slides` | 83 | 基于认知科学的 HTML slides | 中（教学场景） |
| pptxgenjs-animation | `anmism/pptxgenjs-animation` | 5 | PptxGenJS + 动画（JS 侧生成） | 中 |
| pptx-animation-splitter | `lucasrqt/pptx-animation-splitter` | 0 | 拆分 PPTX 动画便于导出 PDF | 低 |

## 三、「泡泡堂」类活泼泡泡风格的落地

「泡泡堂」= 明快、圆润、卡通气泡、高饱和糖果色、强互动趣味。落地措施：

1. **新增设计主题 `泡泡堂风 / Bubble Pop`**（审美锚点 `12 Sagmeister & Walsh`）：极简暖白底 + 糖果色气泡（品红 `#FF5FA2` / 天蓝 `#3EC6FF` / 明黄 `#FFD24D`），大圆角、气泡装饰、弹性动效。
2. **挂载到 6 个用途分类**：社团活动策划、活动宣传、招新宣讲、产品发布、读书会、旅行计划（共 +6 套模板）。
3. **动效**：泡泡主题使用 `morph` 切换 + 弹性入场错峰，契合轻快气质。

> 说明：若「泡泡堂」实际指向具体品牌（如泡泡玛特），其商标与官方素材需你提供授权后方可使用；当前按「活泼泡泡风格」方向实现，未使用任何品牌素材。
