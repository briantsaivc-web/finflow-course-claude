---
marp: true
theme: default
paginate: true
header: "FinFlow 實戰心法 | 第二部・地基與工具"
style: |
  section {
    background: #ffffff;
    color: #111827;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang TC", sans-serif;
    padding: 50px 70px;
    font-size: 26px;
  }
  h1 {
    font-size: 2rem;
    color: #111827;
    border-bottom: 2px solid #e5e7eb;
    padding-bottom: 8px;
    margin-bottom: 16px;
  }
  .lead {
    font-size: 1.3rem;
    color: #1d4ed8;
    font-weight: 700;
    margin-bottom: 24px;
  }
  .highlight { color: #b91c1c; font-weight: bold; }
  .grid {
    display: flex;
    gap: 16px;
    margin: 24px 0;
    align-items: center;
  }
  .box {
    flex: 1;
    border: 2px solid #111827;
    padding: 16px;
    text-align: center;
    border-radius: 6px;
    background: #ffffff;
  }
  .box.blue { border-color: #1d4ed8; background: #eff6ff; }
  .box.red { border-color: #b91c1c; background: #fef2f2; }
  .arrow { font-size: 24px; font-weight: bold; color: #1d4ed8; }
  table { width: 100%; border-collapse: collapse; margin-top: 16px; font-size: 22px; }
  th { border-bottom: 2px solid #111827; text-align: left; padding: 10px; }
  td { border-bottom: 1px solid #e5e7eb; padding: 10px; }
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
    <strong>改壞時一鍵還原</strong><br>
    隨時回到穩定版本<br>
    <i>徹底消除改爛代碼的恐懼</i>
  </div>
</div>

- 不怕改錯、不怕檔案遺失，每一步推進都有跡可循

---

<!-- 第 48 頁 -->
# GitHub 極速上手：建立儲存庫

<div class="lead">三步建立你的雲端基地，Repository 就是專案資料夾。</div>

- **步驟 1：申請免費帳號**
  註冊單一帳號，終身免費使用核心版控功能
- **步驟 2：新增 Repository (儲存庫)**
  點擊 New，為你的遊戲專案命名（如 `finflow-mini`）
- **步驟 3：設定公開或私有**
  剛動工可選 Private，準備給朋友玩時隨時一鍵切換 Public

---

<!-- 第 49 頁 -->
# 核心兩招：Commit 與 Push

<div class="lead">日常版控只有兩個動作：寫下說明存檔、推上雲端備份。</div>

<div class="grid">
  <div class="box blue">
    <strong>Commit（認可存檔）</strong><br>
    幫這次變更寫一句話白話說明<br>
    <i>例如：修復房產修繕折抵邏輯</i>
  </div>
  <div class="arrow">➔</div>
  <div class="box red">
    <strong>Push（推送同步）</strong><br>
    將本機存檔同步到 GitHub 雲端<br>
    <i>換一台電腦隨時拉下來繼續做</i>
  </div>
</div>

- 每次叫 AI 改完一版，就執行一次 Commit & Push 建立存檔點

---

<!-- 第 50 頁 -->
# 白話認識 Firebase：多人即時同步

<div class="lead">單機遊戲完全不需要，要做多人同桌才需要它。</div>

<div class="grid">
  <div class="box">
    <strong>單機對戰模式</strong><br>
    瀏覽器本機運算即可<br>
    <i>完全不需要伺服器與資料庫</i>
  </div>
  <div class="arrow">➔</div>
  <div class="box blue">
    <strong>多人跨裝置連線</strong><br>
    需要即時同步每位玩家的動作<br>
    <i>此時才引入 Firebase 雲端資料庫</i>
  </div>
</div>

- **架構原則**：單機版沒有測穩定前，絕對不要過早引入 Firebase

---

<!-- 第 51 頁 -->
# 實戰案例：連基礎架設都請 AI 寫指南

<div class="lead">小白不用自己研究文件，讓 AI 幫你產出操作 SOP。</div>

- **真實痛點**：Firebase 後台設定複雜，權限與金鑰容易卡關
- **造物者指令**：
  > 「請為一個非工程師，寫一份 Firebase 即時資料庫的設定指南，告訴我每一步該點哪個按鈕。」
- **落地成果**：產出圖文步驟手冊，按部就班 10 分鐘完成基礎建設
- **心法**：連環境設定都能外包給 AI，不要讓技術名詞嚇退你

---

<!-- 第 52 頁 -->
# 為什麼單一 HTML 檔案最友善？

<div class="lead">零環境配置、隨開即玩、隨時分享：極致的低門檻。</div>

| 傳統軟體開發 | 單一 HTML 檔案架構 |
| :--- | :--- |
| 安裝 Node.js、編譯工具、本地伺服器 | **完全不裝任何軟體**，雙擊瀏覽器直接開跑 |
| 套件版本衝突，換台電腦就報錯 | **一份檔案包辦全部**，結構極度單純透明 |
| 部署需要雲端主機與複雜網址設定 | **LINE 傳一個檔案**或貼到免費用戶端就能玩 |

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
    雲端存檔與免費用戶端<br>
    <i>存檔點與成果發布基地</i>
  </div>
</div>

- 不需要昂貴軟體，這三樣免費工具就能支撐做出完整遊戲

<!-- EOF: VERIFIED FULL FILE DELIVERY -->