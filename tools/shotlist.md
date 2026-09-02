# GitHub 教學錄製腳本(內部用)

練習 repo:`github-tutorial-demo`(Owner briantsaivc-web,Public,不勾 README/.gitignore/License)
本機資料夾:`C:\Users\Carrie\Pictures\finflow-course-shots\demo\github-tutorial-demo\`(含 index.html)
截圖落地:`C:\Users\Carrie\Pictures\finflow-course-shots\raw\`

## A. GitHub 網頁段(Playwright,需已登入)
A01 github.com 首頁(登入後)——框:右上角「+」
A02 「+」下拉——框:New repository
A03 /new 空白表單——框:Owner、Repository name
A04 /new 填好——框:name=github-tutorial-demo、Public、README 未勾、.gitignore=None、License=None
A05 /new 底部——框:Create repository 按鈕
A06 建好後的空 repo 頁——框:「…or push an existing repository from the command line」那一塊、repo 網址

## B. CMD 段(Git CMD,PowerShell 全螢幕存圖後裁切)
B01 開始功能表找 Git CMD(用 Playwright 不行;改用截圖說明)→ 改為:Git CMD 空白視窗
B02 `git --version`(證明裝好了)
B03 `git config --global user.name / user.email`(第一次必做)
B04 `cd` 到資料夾 + `git init` + `git branch -M main`
B05 `git add .` + `git commit -m "..."`(顯示 1 file changed)
B06 `git remote add origin ...` + `git push -u origin main`
B07 登入視窗(Git Credential Manager 跳出瀏覽器/視窗)——若無跳出(已有憑證)則標註 UNKNOWN
B08 push 成功輸出(branch 'main' set up to track...)

## C. GitHub Pages 段(Playwright)
C01 repo 頁重新整理——框:index.html 已出現、Settings 分頁
C02 Settings 左側選單——框:Pages
C03 Pages 設定——框:Source=Deploy from a branch、Branch=main、Folder=/(root)、Save
C04 儲存後——框:「Your site is live at ...」(可能需等 1-2 分鐘,重新整理)
C05 打開成品網址 https://briantsaivc-web.github.io/github-tutorial-demo/
C06 repo 網址 vs 網站網址 並排對照(後製合成)

## 新手小心框(要配圖)
- 沒裝 Git → 「'git' 不是內部或外部命令」(B01 前,示範錯誤畫面:在一般 CMD 打 git 的錯誤;若無法錄到則用文字說明+標 UNKNOWN)
- 沒設 user.name → commit 錯誤畫面(B03 前故意先 commit 一次錄錯誤)
- 第一次 push 跳登入(B07)
- Pages 要等 Actions 跑完(C04)
- 兩個網址搞混(C06)
