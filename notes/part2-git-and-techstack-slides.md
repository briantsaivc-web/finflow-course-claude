---
marp: true
theme: finflow-clean
paginate: true
header: "FinFlow 實戰心法 | 第二部・地基與工具"
---

<!-- 第 47 頁 -->
# 白話認識 GitHub：專案的時光機

<div class="lead">不用懂底層版本控制原理，把它當作無限存檔點。</div>

<div class="grid">
  <div class="box">
    <strong>存檔點一 (v1.0)</strong><br>
    單機可玩原型
  </div>
  <div class="arrow">➔</div>
  <div class="box blue">
    <strong>存檔點二 (v2.0)</strong><br>
    擴充至 20 個職業
  </div>
  <div class="arrow">➔</div>
  <div class="box red">
    <strong>改壞時抓回舊版</strong><br>
    每個存檔點都留著，隨時翻回去<br>
    <i>不是有一個「還原」按鈕，<br>是舊版本一直都在</i>
  </div>
</div>

- 不怕改錯、不怕檔案遺失，每一步推進都有跡可循

---

<!-- 第 48 頁 -->
# GitHub 極速上手：建立儲存庫

<div class="lead">三步建立你的雲端基地，Repository 就是專案資料夾。</div>

- **步驟 1：申請免費帳號**
  註冊一個帳號，存檔與發布的功能終身免費
- **步驟 2：新增 Repository (儲存庫)**
  點擊 New，為你的遊戲專案命名（如 `finflow-mini`）
- **步驟 3：設定公開或私有**
  剛動工可選 Private，準備給朋友玩時隨時切換 Public
  <b>建立時記得勾選「Add a README file」</b>，否則會是一個空庫，網頁上沒東西可點
- **建好之後**：畫面上有 `Add file` → `Upload files`，把 AI 給你的 `index.html` 拖進去就行

---

<!-- 第 49 頁 -->
# 核心一招：Commit（蓋一個存檔點）

<div class="lead">全程在 GitHub 網頁上做，不用裝任何軟體。</div>

<div class="grid">
  <div class="box blue">
    <strong>1. 把新檔案放上去</strong><br>
    <code>Add file</code> → <code>Upload files</code><br>
    <i>把 AI 給你的檔案拖進去</i>
  </div>
  <div class="arrow">➔</div>
  <div class="box blue">
    <strong>2. 寫一句說明</strong><br>
    下方的訊息框打一行字<br>
    <i>例如：修好房產修繕折抵</i>
  </div>
  <div class="arrow">➔</div>
  <div class="box red">
    <strong>3. 按 Commit changes</strong><br>
    存檔點成立<br>
    <i>這一版永遠留著</i>
  </div>
</div>

- 每次叫 AI 改完一版，就上傳一次、寫一句話、按一次 Commit
- 你會在別的地方看到 **Push** 這個字——那是<b>在自己電腦上裝了 Git 之後</b>才會用到的動作。本部走純網頁路線，用不到；想用的話，第二部補充章節有教

---

<!-- 第 50 頁 -->
# 白話認識 Firebase：多人即時同步

<div class="lead">單機遊戲完全不需要，要做多人同桌才需要它。</div>

<div class="grid">
  <div class="box">
    <strong>單機對戰模式</strong><br>
    所有計算都在你自己的電腦上跑<br>
    <i>不需要任何額外服務</i>
  </div>
  <div class="arrow">➔</div>
  <div class="box blue">
    <strong>多人跨裝置連線</strong><br>
    每個人的動作要即時傳給對方<br>
    <i>這時才需要 Firebase 這種「共用記事本」</i>
  </div>
</div>

- **架構原則**：單機版沒有測穩定前，絕對不要過早引入 Firebase

---

<!-- 第 51 頁 -->
# 實戰案例：連基礎架設都請 AI 寫指南

<div class="lead">小白不用自己研究文件，讓 AI 幫你產出操作 SOP。</div>

- **真實痛點**：Firebase 後台設定複雜，權限與那串連線密碼（金鑰）容易卡關
- **造物者指令**：
  > 「請為一個非工程師，寫一份 Firebase 即時資料庫的設定指南，告訴我每一步該點哪個按鈕。」
- **落地成果**：它給出一份逐步的文字操作清單（畫面截圖要自己對照），照著點完就通
- **心法**：連環境設定都能外包給 AI，不要讓技術名詞嚇退你

---

<!-- 第 52 頁 -->
# 為什麼單一 HTML 檔案最友善？

<div class="lead">零環境配置、隨開即玩、隨時分享：極致的低門檻。</div>

| 傳統軟體開發 | 單一 HTML 檔案架構 |
| :--- | :--- |
| 要先裝好幾套看不懂的開發工具 | **完全不裝任何軟體**，雙擊就用瀏覽器打開 |
| 各種元件版本相衝，換台電腦就跑不動 | **一份檔案包辦全部**，結構極度單純透明 |
| 上線需要租主機、設定網址 | **LINE 傳一個檔案**，或丟到 GitHub Pages 就有網址 |

- 降低技術複雜度，才能把精力集中在「玩法與數值」

---

<!-- 第 53 頁 -->
# 極簡工具箱：你真正需要的只有三樣

<div class="lead">砍掉 90% 的工程工具，留下最輕量的三件套。</div>

<div class="grid">
  <div class="box">
    <strong>一個瀏覽器</strong><br>
    Chrome / Edge<br>
    <i>即時運行與預覽作品</i>
  </div>
  <div class="box blue">
    <strong>一個 AI 對話框</strong><br>
    Claude / ChatGPT / Gemini<br>
    <i>你的全天候虛擬工程團隊</i>
  </div>
  <div class="box red">
    <strong>一個 GitHub 帳號</strong><br>
    雲端存檔＋免費網頁空間<br>
    <i>存檔點與成果發布基地</i>
  </div>
</div>

- 不需要昂貴軟體，這三樣免費工具就能支撐做出完整遊戲

<!-- EOF: VERIFIED FULL FILE DELIVERY -->