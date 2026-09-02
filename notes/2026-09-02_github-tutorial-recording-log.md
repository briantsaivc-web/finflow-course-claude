# GitHub 三步驟實戰:錄製紀錄(2026-09-02)

## 真實錄製環境
- GitHub 帳號 briantsaivc-web,練習 repo `github-tutorial-demo`(Public,真實建立、真實 push、Pages 真實上線:https://briantsaivc-web.github.io/github-tutorial-demo/)
- Git 2.54.0.windows.1;Windows 11;截圖日期 2026-09-02
- 網頁段:Claude in Chrome 擴充功能操作 Brian 本機 Chrome(已登入 GitHub),截圖直接存檔
- 指令段:電腦操作授權「Git CMD」,視窗以 `title 命令提示字元` 改名;截圖用 `tools/shot.ps1`(PowerShell + user32,DPI-aware,前景視窗模式)

## 誠實揭露(已寫進章節附錄)
- `git config` 那張圖只 echo 指令、未真正覆寫錄製者設定(該指令本來無輸出,畫面等同真實執行)
- 「Author identity unknown」錯誤以 `HOME=%TEMP%\fakehome` 暫時清空全域設定重現,為真實錯誤輸出,未產生 commit
- 「'git' 不是內部或外部命令」以 `set PATH=C:\Windows\System32` 暫時讓 git 找不到重現
- 未取得:Git for Windows 安裝精靈截圖(錄製機已裝)、第一次 push 的 GCM 登入視窗(已有憑證)→ 章節標【待補】【未截圖】

## 與 Brian 原腳本的差異
- GitHub 建 repo 介面:README 為 On/Off 開關、.gitignore/license 為下拉;不是勾選框
- `Branch: gh-pages` 只適用有 Actions workflow 的專案;純 index.html 專案選 `main` / `(root)`
- 第一次 commit 會撞「Author identity unknown」,教材加了 `git config` 步驟

## 重拍 SOP(介面改版時)
1. Claude in Chrome 連上 → 逐頁 screenshot(save_to_disk)→ 改名放 `tools/raw/`
2. Git CMD 段:`set SHOT=...shot.ps1 -Mode fg -Name` → 每步 `cls & echo %CD%^>指令 & 指令 & %SHOT% 檔名`(cls 會清掉打字那行,畫面只留 echo 的提示列與真實輸出)
3. 在 repo 根目錄 `python3 tools/build_images.py`(裁切/去光暈/加框,座標表在檔內)→ 檢查 → `node tools/build_pptx.js` / pandoc 重產三版

## 流程面的未預期發現
1. Playwright MCP 在 Brian 機器上是 headless,使用者看不到視窗、無法登入
2. 電腦操作的「type」走剪貼簿貼上,使用者同時複製東西會把指令換掉
3. Claude 桌面 App 重新連線後,電腦操作授權全部清空,需重新授權
4. 內建瀏覽器面板寬度受 App 視窗影響,窄時 GitHub 切手機版排版
5. Chrome 擴充功能開的分頁不一定共用原本的 GitHub 登入狀態,需在該分頁登入一次
