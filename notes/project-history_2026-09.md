# 專案沿革:從「想做一個課程」到本 repo 成立

> 本檔記錄 Brian 與 Claude 在 FinFlow Project 中,關於課程/書籍的討論與決策順序。目的是讓之後接手(包括未來的自己與另一個 AI)的人,知道每個東西為什麼長成現在這樣。

## 0. 起點

Brian 想把 FinFlow(台灣在地化財商多人桌遊,S1~S20 快速疊代、多人連線、Firebase)的開發歷程,做成一個讓「沒程式基礎或基礎很低的人」也能一步一步完成自己遊戲的課程。要求:工具(AI/GitHub/Firebase)、發想方法、注意事項、最後讓讀者真的做出一個小作品建立信心。輸出先做約 100 頁簡報骨架,再擴寫成書。

## 1. 骨架演進(`outline/course-outline-134p_v1.4.md`)

| 版本 | 頁數 | 加了什麼 |
|---|---|---|
| v1.0 | 102 | 五部架構:震撼彈 / 心法 / 工具 / 實作 / 讀者實作題 + 結語 |
| v1.1 | 112 | 三大 AI 模型(ChatGPT/Gemini/Claude)白話介紹,強調免費額度夠用、不必先付費;做完專案後的方向(架構重構、卡片與引擎分離) |
| v1.2 | 120 | 「有想法就跟 AI 講,AI 幫你寫規格書」實例(用本課程大綱本身當示範)、即時互動產出(Artifact 類)功能;卡片「一層層長大」深度案例(固定金額 → 隨狀態浮動 → 技能解鎖隱藏資訊 → 更深風險),標暫定版 |
| v1.3 | 130 | UI/UX 疊代專節(視覺、功能模塊擺置、資訊隨進度揭露、記帳三級自動化),四個真實版本引用(五期方案丙、S14a v2.16.0/v2.16.1、S17 v2.22.0)已核對原文 |
| v1.4 | 134 | 過一輪待確認:卡片案例先寫暫定版;模型分工(高階寫規格、精簡模型寫碼)確認為真實做法;FinFlow 極簡版規格定案(1 人 vs 電腦、15 輪、6 職業卡、10 事件卡、1 投資決策點、比現金+未到期投資);進階方向只做方向說明 |

序(序-1~序-5)與見證(見證-1~10)插在封面與目錄之間,用獨立編號,不動 1~134 頁碼。

## 2. 逐頁細化(`outline/page-by-page-copy-and-visuals_v1.0.md`)

每一頁補「文案要點」與「圖表/視覺建議」,標「來源」者為已查證的 FinFlow 文件。細化過程新增的待確認:頁 111 十張事件卡的具體卡名數值為暫擬;會隨時間變動的資訊(AI 定價、GitHub/Firebase 介面)一律 UNKNOWN,寫書前再查。

## 3. 序:起心動念(`chapters/preface.md`)

Brian 口述起心動念(成長中發現財務情商比死板記帳重要、想寓教於樂、不會寫程式但用 AI 手刻、台灣在地情境讓玩家有共鳴),改寫成第一人稱序文,收在「如果我可以,你也可以」。

## 4. 見證(`chapters/testimonials.md`)

v1:10 則附機制對應。v2(現行):依 Brian 指示大幅縮短、去術語、改成高中~大學生的戲謔口吻、插入 2 則家長視角(「說教打不贏遊戲」「安太座」)。誠實揭露:見證 1~5 源自真實回饋改寫,6~10 為示範情境,出版時須視覺區隔。

## 5. GitHub 三步驟實戰(`chapters/github-tutorial.md`,2026-09-02)

Brian 提出:很多學員連 GitHub 在哪、Settings 在哪都找不到,要有截圖+框框;輸出分簡報/實體書/線上版三種,線上版放 GitHub 讓讀者直接複製 prompt、作者可隨時修訂。

決策(Brian 拍板):練習用 repo(不碰 `finflow-chatgpt-course`)、授權遠端操作電腦錄 CMD、線上版做 GitHub Pages 文件網站、先只做這一章當樣張。

錄製結果:在 briantsaivc-web 帳號真實建立 `github-tutorial-demo`、真實 push、Pages 真實上線;24 張加框截圖;發現 GitHub 建 repo 介面已與 Brian 原腳本不同(README 開關、下拉選單)、純 index.html 專案 Pages 應選 `main` 而非 `gh-pages`。詳見 `notes/2026-09-02_github-tutorial-recording-log.md`。

## 6. 本 repo 成立(2026-09-02)

Brian 指示正式成立專案 `finflow-course-claude`:本地資料夾 + GitHub 倉庫,放入至今所有討論成果。採「一份母版、三個輸出」架構。

## 尚未決定 / 待辦

- 線上版是否套更完整的文件主題(側邊目錄),目前用 GitHub 內建 cayman 主題,零建置
- GitHub 章在大綱裡是擴成 8-10 頁,還是獨立成附錄(原對應第 48、49、121 頁)
- 卡片深度案例(頁 23-28)待 Brian 定案真實版本後補出處
- Git for Windows 安裝精靈截圖、第一次 push 登入視窗截圖:待補
- 其餘 130 餘頁的章節內容:依骨架逐章產出

## 7. 第六部（獨立章節）「讓 AI 互相抓錯」(2026-09-08)

Brian 提問:把 AI 寫的程式交給另外兩個 AI 審查、再交回原 AI 問是否同意、來回兩輪取得共識後才改——這在原理上能否證明有效?有沒有專有名詞?能否進日常開發流程與教案?

Claude 回答並經 Brian 定案:有名字(IV&V、四眼原則、Fagan 審查、N 版本程式設計、多智能體辯論);原理上成立(孔多塞陪審團定理)但兩個前提在 AI 上有坑(Knight & Leveson 1986 錯在同處;Sharma 2023 趨同偏誤);真正有效的核心是「實證裁決」不是「共識」。案例全部取自 S42(Gemini 五項)與 S43(ChatGPT 四項,含 ChatGPT 糾正 Claude 兩點)。

決策:先做獨立最後章節,不併入 134 頁主骨架,Brian 整理時再 merge;TA 程式小白、全章無程式碼;AI 用真名;文獻僅查出處確認,不做文獻探討。

產出:`outline/part6-ai-cross-review_outline_v1.0.md`(12 頁骨架,暫編 135-146)、`notes/part6-ai-cross-review-slides.md`(Marp 12 頁)、`chapters/ai-cross-review.md`(書籍版全文)、`samples/part6-ai-cross-review_slides_sample.pptx`(Marp CLI 渲染)。

## 8. 第二部補充「同一件事的三種做法」(2026-09-08)

Brian 看到 Claude 交付 zip 後問:用 VS Code 會不會比 cmd 的 add/commit/push 更有效率?Claude 答會(看得到差異、Marp 預覽、AI 直接寫進資料夾),Brian 決定把「原始作法 vs 協作作法」加進課程,讓有興趣的學員知道有這個選項,並加上雲端(github.com 改 github.dev)與本機兩種開法的差異。

事實查證(2026-09-08):GitHub Docs「The github.dev web-based editor」(改網址或按 `.`、可 commit/push、無終端機、僅 web extensions、未 commit 修改存於瀏覽器);marp-team Discussion #169(網頁版可預覽、不可匯出 pptx)。

產出:`outline/part2-supplement-vscode_outline_v1.0.md`(8 頁,S2-1~S2-8)、`notes/part2-vscode-option-slides.md`、`chapters/vscode-option.md`、`samples/part2-vscode-option_slides_sample.pptx`、`images/VSC-01-restricted-mode.png`(Brian 電腦截圖,未加框,【待補】加框版與 Source Control 面板截圖)。

## 9. 第六部外部審閱與精簡（2026-09-08）
- 另兩個 AI 對第六部投影片提出四項勘誤：孔多塞數字精度／IV&V 誤寫成盲審／sycophancy 過度延伸與「找錯」提示詞／136 表頭 2 欄。
- 查證結果：二、三成立（IV&V 的獨立是組織／管理／預算獨立；Sharma 2023 研究的是迎合人類使用者，未測模型對模型）；一為捨入問題；四不成立（repo 原始檔本就 4 欄）。對方引 Zhou 2022 支持「找錯 prompt 誘發假警報」不成立，該文未談此事。
- Brian 重申課程三原則（不是學術研討；小白看得懂做得到；性價比高才放），據此重盤：12 頁→10 頁。砍「這件事有名字」整頁；孔多塞＋Knight & Leveson 合為一頁並改用 Kim et al. 2025（ICML，350+ 模型、兩者都錯時約 60% 相同）當例子；去掉 sycophancy 一詞；反向質詢提示詞改中立核對版；「標 UNKNOWN」改「寫進待辦」。文獻只留章節 md 附錄。
- 檔案：notes/part6-ai-cross-review-slides.md、chapters/ai-cross-review.md、outline/part6-ai-cross-review_outline_v1.0.md（各留 .backup.20260908）、samples pptx 重渲 10 頁。

## 10. 第二部補充 v1.1：五張實機截圖與換行符號假差異（2026-09-08）
- Brian 第一次用 VS Code 推 VS Code 補充章節，過程截圖五張（Changes 清單、沒 staged 的對話框、空訊息 COMMIT_EDITMSG、staged＋訊息、Sync 對話框），裁切後放進 images/VSC-02～06，新增 S2-2b、S2-2c、S2-7b 三頁，8 頁→11 頁；S2-7 踩坑表加兩列。
- 查本機：main 與 origin/main 同步（29d4c5e），第六部 v1.0 與 VS Code 補充皆已上 GitHub。6 個檔顯示 M 但忽略空白後 diff 為 0——前 45～48 行被改成 CRLF。加 .gitattributes（* text=auto eol=lf）並 renormalize。
- 第六部 v1.1 五個檔同批寫入。

## 11. 投影片樣板系統化：四套主題，全課程採用 A（2026-09-08）
- 原本 14 份 slides md 各自在 frontmatter 內嵌一段一模一樣的 CSS（1,139 字元，13 份雜湊完全相同；deck-test.md 另有 appendix／highlight 兩條）。改動樣式要改 14 個檔。
- 改成 Marp 主題檔：`themes/finflow-clean.css`（A 白板筆記）、`finflow-card.css`（B 桌遊卡牌）、`finflow-dark.css`（C 夜間終端機）、`finflow-bold.css`（D 雜誌雙色）。`.vscode/settings.json` 登記四套，VS Code 預覽即時吃到。
- 14 份 md 的 frontmatter 移除內嵌 style、改為 `theme: finflow-clean`；Brian 選定 A。deck-test.md 原本 `.highlight` 是藍色，統一為紅色（紅＝警示）；`section.appendix` 併入主題保留。
- 換樣板＝改一行 `theme:`。`themes/README.md` 記錄四套差異、頁面寫法（`_class: title`／`appendix`、lead／grid／box／highlight）與匯出指令。
- 驗證：part1-mindset、part3-five-days、deck-test 逐頁渲染確認；part2 與 part6 的 pptx 用 `--theme-set themes` 重渲（11／10 頁）。備份於 `_backup_theme_20260908/`。
