# finflow-course-claude

《我不會寫程式,但我用 AI 做出了一套多人連線遊戲》—— 課程/書籍/線上內容的**唯一母版倉庫**。

把 FinFlow(台灣在地化財商多人桌遊,由不會寫程式的作者與 AI 協作完成)的開發歷程,整理成讓零基礎的人也能一步一步做出自己作品的教材。同一份內容產出三個版本:**簡報**(演講用)、**實體書**、**線上版**(本 repo 開 GitHub Pages 即是)。

## 目錄結構

```
finflow-course-claude/
├── README.md                ← 你正在看的這份
├── CHANGELOG.md             ← 每次修訂記一筆
├── _config.yml / index.md   ← GitHub Pages(線上版)設定與首頁
├── outline/                 ← 全書骨架與逐頁細化(內容的「設計圖」)
│   ├── course-outline-134p_v1.4.md(課程大綱 134 頁骨架 v1.4)
│   └── page-by-page-copy-and-visuals_v1.0.md(逐頁文案與圖表細化 v1.0)
├── chapters/                ← 已完稿的章節(Markdown,線上版直接渲染)
│   ├── preface.md           序:起心動念(書籍全文 + 簡報五頁版)
│   ├── testimonials.md      見證:玩家怎麼說(v2,含真實/示範揭露)
│   └── github-tutorial.md   GitHub 三步驟實戰(24 張實機截圖)
├── images/                  ← 所有加框截圖,三個版本共用;介面改版重拍時只換這裡
├── samples/                 ← 由母版產生的簡報/書籍樣張(衍生品,不要手改)
├── tools/                   ← 產生器與錄製工具
│   ├── build_images.py      raw 截圖 → 裁切/去光暈/紅框編號 → images/
│   ├── annotate.py          單張加框工具
│   ├── build_pptx.js        母版 → 簡報(pptxgenjs)
│   ├── shot.ps1             Windows 視窗截圖存檔(錄製終端機畫面用)
│   ├── shotlist.md          錄製腳本
│   ├── raw/                 未加框的原始截圖
│   └── demo-site/index.html 教學用的練習網頁
└── notes/                   ← 專案沿革、錄製紀錄、決策
```

## 三個版本怎麼產生

| 版本 | 來源 | 產生方式 |
|---|---|---|
| 線上版 | `chapters/*.md` + `images/` | 本 repo 開 GitHub Pages(Settings → Pages → Branch `main` / `(root)`),push 後自動更新 |
| 簡報 | `tools/build_pptx.js`(內容目前手寫在腳本裡,對照 `chapters/`) | 在 repo 根目錄 `node tools/build_pptx.js` → `samples/` |
| 實體書 | `chapters/*.md` | `pandoc chapters/github-tutorial.md -o samples/github-tutorial_book_sample.docx --resource-path=chapters`(字型用 reference docx 設微軟正黑體) |

**紀律**:母版只有一份(`chapters/` 與 `outline/`)。簡報與書是衍生品,內容要改就改母版再重產,不要各自手改,否則三份很快對不上。

## 修訂流程(也是本書第二步教的東西)

```
git add .
git commit -m "寫一句這次改了什麼"
git push
```

## 誠實揭露原則

- 所有「案例」引用 FinFlow 專案內可查證的變更說明/工程書,標版本號與日期,不憑印象改數字。
- 截圖標拍攝日期;錯誤畫面若是以可逆手段重現,附錄會說明。
- 見證分「真實回饋改寫」與「示範情境」,不混為一談。
- 查不到、沒拍到的東西標 UNKNOWN /【待補】,不用記憶補。

## 狀態(2026-09-02)

- 骨架 134 頁 + 序 5 頁 + 見證 10 則:定案(v1.4),待確認事項列在骨架檔末尾
- 逐頁文案與圖表建議:v1.0 完成
- GitHub 三步驟實戰章:內容完稿、三版樣張完成
- 其餘章節:尚未動工(依骨架逐章產出)
