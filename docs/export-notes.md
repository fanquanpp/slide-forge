# 导出、回滚与交接说明

## 一、源文件与播放

- 主交付：`templates/` 下的 **120 套 .pptx**（保留可编辑图层与动画时间轴）+ `_potx/` 下 **24 套母版**。
- 目标播放环境：**Microsoft PowerPoint**（Windows / macOS）。切换与入场动画均为标准 OOXML，PowerPoint 原生播放。
- Google Slides / Keynote 对部分切换（如 newsflash/comb）支持有限，会降级为淡入，属预期差异。

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
git checkout v2-animated -- templates    # 回到带完整动效的版本
```
- 或整体重建：`python generator/build.py templates`（生成器在 `generator/`）。

## 五、常见播放问题排查

| 现象 | 原因 | 处理 |
|---|---|---|
| 动画不播放 | 以「阅读视图」打开 / 「动画窗格」被关闭 | 用「幻灯片放映」并开启动画 |
| 切换被自动跳过 | 设置了「设置自动换片时间」 | 幻灯片放映→设置幻灯片放映→勾选手动 |
| 字体变形 | 目标机缺字体 | 安装字体或「替换字体」 |
| 部分元素无动画 | 该页元素超过 14 个上限（保护性能） | 在「动画」中手动补加 |
| 纹理/图形错位 | 跨软件打开（Keynote） | 以 PowerPoint 为准；或导出 PDF |
