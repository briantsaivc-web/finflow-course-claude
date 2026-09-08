# 投影片樣板（Marp 主題）

本課程所有投影片（`notes/*-slides.md`）共用同一套樣板。要換樣板，只改每個檔案最上面那一行 `theme:`，不需要動內容。

目前全部使用 **A 白板筆記** `finflow-clean`。

| 檔案 | 名稱 | 長相 | 適合 |
|---|---|---|---|
| `finflow-clean.css` | A 白板筆記 | 白底、深灰字、藍色重點、紅色警示 | 目前採用。教室投影最保險，列印也清楚 |
| `finflow-card.css` | B 桌遊卡牌 | 米色桌布、圓角卡片、藍籌／紅籌／金 | 想呼應「財商桌遊」主題、對年輕聽眾 |
| `finflow-dark.css` | C 夜間終端機 | 深藍底、薄荷綠與琥珀色 | 暗室投影好看；列印不適合 |
| `finflow-bold.css` | D 雜誌雙色 | 白底、粗黑大標、橘色強調、左側色帶 | 遠看最清楚、最有記憶點 |

## 怎麼換

1. 打開任一 `notes/xxx-slides.md`，第 3 行 `theme: finflow-clean` 改成別的名字（例如 `finflow-bold`）。
2. VS Code 的 Marp 預覽會立刻變。整份課程都要換，就把 14 個檔案都改（或請 AI 一次改完）。

## 頁面寫法（四套通用）

- `<!-- _class: title -->` 放在頁首 → 章名頁（大標、置中）
- `<!-- _class: appendix -->` → 附錄頁（灰底）
- `<div class="lead">…</div>` → 標題下的一句引言
- `<div class="grid"><div class="box">…</div><div class="arrow">➔</div><div class="box blue">…</div></div>` → 並排方塊，`box blue` 是重點、`box red` 是警示
- `<span class="highlight">…</span>` → 紅色強調
- 表格、清單、`程式碼`、> 引言 直接用 Markdown 寫即可

## VS Code 設定

`.vscode/settings.json` 已登記這四套主題。第一次打開 repo 若預覽沒吃到樣板，重開 VS Code 一次即可。

## 匯出 pptx

VS Code：Ctrl+Shift+P → `Marp: Export Slide Deck` → 選 pptx。
命令列：`npx @marp-team/marp-cli --theme-set themes --allow-local-files notes/xxx-slides.md --pptx -o samples/xxx.pptx`
