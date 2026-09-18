# 导出、回滚与交接说明（v3）

## 一、源文件与播放

- 主交付：`templates/` 下的 **126 套 .pptx**（保留可编辑图层与动画时间轴）+ `_potx/` 下 **25 套母版**。
- 目标播放环境：**Microsoft PowerPoint**（Windows / macOS）。切换与入场动画均为标准 OOXML，PowerPoint 原生播放。
- **现代切换（v3）**：现代主题使用 Morph（p159）与 p14 特效（reveal/ripple/pan/gallery 等），均带
  `mc:AlternateContent` + fade 降级——**PowerPoint 2016 以下 / Google Slides / Keynote 自动降级为淡入**，驻留时长不受影响。
- **Morph 播放条件**：PowerPoint 2019+/Microsoft 365；每套的连续内容页以 `!!brand-band`（品牌规线）与
  `!!footer-rule`（页脚线）确定性配对，改名或删除这两个形状后 Morph 退化为启发式匹配。
- **一键换肤（v3）**：每套已注入 OOXML 主题色方案——PowerPoint「设计 → 变体 → 颜色」可直接切换/自定义品牌色，
  新插入的形状、图表会自动继承本套配色。
- **原生图表**：每套图表页均为原生可编辑图表（柱状/折线/环形，按种子轮换），右键「编辑数据」替换数值。

## 二、成品导出（PDF / MP4）

> 本机未安装 PowerPoint / LibreOffice 渲染引擎，**未随包提供 PDF 与 MP4 成品**（无法离线渲染）。
> 请在本机 Office 环境按下列方式导出，或安装 LibreOffice 后使用命令导出 PDF：

```powershell
# 方案 A：PowerPoint 手动导出——文件 → 导出 → 创建 PDF/XPS；动画演示用 文件→导出→创建视频(MP4)
# 方案 B：安装 LibreOffice 后批量导出 PDF
#   winget install TheDocumentFoundation.LibreOffice
Get-ChildItem templates -Recurse -Filter *.pptx | ForEach-Object {
  soffice --headless --convert-to pdf --outdir out_pdf $_.FullName }
```

## 三、字体与素材

- 字体依赖系统字体（微软雅黑 / Segoe UI / Georgia / Consolas 等）；缺失时 PowerPoint 会替换，建议在目标机器确认字体或用「替换字体」统一。
- 素材全部为程序绘制的形状与占位框，不含第三方版权素材。

## 四、回滚

- 优化前版本已用 git 记录；回滚命令：

```bash
git checkout v1-static -- templates      # 回到加入动画前的静态版本
git checkout v2-animated -- templates    # 回到带经典轮换动效的版本（2268 页）
git checkout <v3 提交> -- templates       # 回到 v3：角色化切换 + Morph + 主题色（2394 页）
```
- 或整体重建：`python generator/build.py templates`（生成器在 `generator/`）。

## 五、常见播放问题排查

| 现象 | 原因 | 处理 |
|---|---|---|
| 动画不播放 | 以「阅读视图」打开 / 「动画窗格」被关闭 | 用「幻灯片放映」并开启动画 |
| 切换被自动跳过 | 设置了「设置自动换片时间」 | 幻灯片放映→设置幻灯片放映→勾选「使用计时器」（本库已预置 useTimings=1） |
| Morph 无补间效果 | PowerPoint 版本低于 2019 / 删除或改名了 `!!` 形状 | 用 Microsoft 365 / PowerPoint 2019+；保留 `!!brand-band`、`!!footer-rule` |
| 现代切换变成淡入 | 旧版 Office / Google Slides / Keynote | 预期降级行为（fade Fallback） |
| 字体变形 | 目标机缺字体 | 安装字体或「替换字体」 |
| 部分元素无动画 | 该页内容元素超过 14 个上限（保护性能）；页脚/装饰为刻意静态 | 属预期设计；需要时在「动画」中手动补加 |
