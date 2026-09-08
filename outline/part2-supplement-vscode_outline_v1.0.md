# 第二部補充（獨立小節）・同一件事的三種做法：命令提示字元、VS Code、瀏覽器裡的 VS Code（8 頁）

> 狀態：獨立補充 v1.0（2026-09-08），接在第二部第 49 頁「commit、push」之後或 GitHub 三步驟實戰章之後皆可；Brian 整理時再 merge。
> 定位：不是要學員換工具，是讓「有興趣」的人知道有這個選項，以及三種做法在做的是同一件事。
> TA：程式小白。截圖為 Brian 電腦 2026-09-08 實機畫面（VS Code 開啟 finflow-course-claude）。

## 一句話
add／commit／push 三步在 VS Code 裡變成「打勾／Commit／Sync」三個按鈕；底下還是同一套 git，觀念不用重學。

## 頁面骨架
S2-1. **你已經會的三步**——命令提示字元版：`git add .` → `git commit -m "…"` → `git push`（回顧第 49 頁與 GitHub 章）
S2-2. **同一件事，換一個介面**——VS Code 的 Source Control 面板：改了哪些檔一目了然、點一下看逐行紅綠差異、打勾＝add、輸入訊息按 Commit＝commit、Sync＝push（＋pull）
S2-3. **三種做法對照表**——命令提示字元／本機 VS Code／瀏覽器 VS Code（github.dev）：要不要安裝、能不能看差異、能不能執行程式、能不能預覽投影片、能不能匯出 pptx、適合誰
S2-4. **瀏覽器版怎麼開**——在 repo 網址把 `github.com` 改成 `github.dev`，或在 repo 頁面按 `.` 鍵；不用安裝、手機平板也能改文字；限制：沒有終端機、不能執行程式、只能用網頁版擴充功能、**沒 commit 前的修改只存在瀏覽器裡**
S2-5. **本機版怎麼開**——安裝 VS Code → File → Open Folder 選 repo 資料夾 → 第一次會問「信任這個資料夾嗎」要按 Trust（截圖：Restricted Mode 藍條）→ 左側 Source Control
S2-6. **為什麼對這個課程特別有用**——三個實質好處：改前先看差異（就是第六部「動手門檻」的實作）；Marp 擴充功能預覽投影片 md、本機版可直接匯出 pptx；跟 AI 協作時 AI 把檔案寫進資料夾、你在面板看到變更再決定送不送
S2-7. **踩坑提醒**——Restricted Mode 下 git 功能是關的；github.dev 沒存就關分頁會不見；Sync 會先 pull 再 push，遠端有人改過會跳合併；第一次 push 會跳 GitHub 登入視窗（與 GitHub 章的第一次 push 相同）
S2-8. **要不要裝？**——決策表：只改文字、偶爾改 → 瀏覽器版就夠；會常改、想看差異、想匯出簡報 → 本機版；想跑程式（`npm run build`、跑測試）→ 本機版＋終端機（VS Code 內建，Ctrl+`），或維持命令提示字元

## 圖表／視覺
- S2-2：三步對照圖（左：三行指令；右：面板三個按鈕），箭頭一對一
- S2-3：對照表（6 列 × 3 欄）
- S2-4：網址改法示意（`github.com/…` → `github.dev/…`）＋「按 `.` 鍵」
- S2-5：截圖 `images/VSC-01-restricted-mode.png`（Brian 電腦，2026-09-08），紅框標 Manage／Trust 與 Source Control 圖示【待補：加框版】
- S2-8：決策流程圖

## 事實查證（2026-09-08，會變動，正式出版前再查）
- github.dev 開啟方式（改網址／按 `.`）、能編輯 commit push 開分支、無 compute 無終端機、僅 web extensions、未 commit 的修改存於瀏覽器本機——GitHub Docs「The github.dev web-based editor」
- Marp for VS Code 有網頁版擴充功能：github.dev／vscode.dev 可預覽，**匯出 pptx／pdf 不行**（瀏覽器無 Node）——marp-team Discussion #169（2021-09／10 公告，2026-09 仍適用；擴充功能版本 3.3.0）
- 免費額度、Codespaces 方案：UNKNOWN，不寫死

## 待確認（Brian）
- 是否要補「本機 VS Code 的 Source Control 面板」加框截圖（S2-2、S2-5 各一張）；目前只有一張 Restricted Mode 畫面
- 放在第二部第 49 頁後（8 頁）或當 GitHub 章附錄
