---
marp: true
theme: default
paginate: true
header: "FinFlow 實戰心法 | 第三部・5 天衝刺實作"
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

<!-- 第 59 頁 -->
# 五天衝刺：從零到可玩原型

<div class="lead">每天只守一個主戰場，不把今天的精力預支給明天。</div>

| 衝刺時程 | 當日核心任務 | 造物者的把關重點 |
| :--- | :--- | :--- |
| **Day 1** | 核心閉環（S1～S5） | 骰子、移動、薪資、破產判定跑得通 |
| **Day 2** | 資料注入（S6～S10） | 擴充 20 張職業與基礎機會卡 |
| **Day 3** | 機制深化（S11～S16） | 引入三級記帳制與財務分錄 |
| **Day 4** | 體驗重構（S17～S22） | 介面拋光、排查通知與跑版 |
| **Day 5** | 數值收斂（S23～S30） | 千局模擬測試、平衡性收口 |

- 節奏勝於速度，每一步都踏在可驗證的代碼基線上

---

<!-- 第 60 頁 -->
# 第一天：跑通單機最小閉環

<div class="lead">不求精美，只要「擲骰、扣錢、走完一圈」沒有報錯。</div>

<div class="grid">
  <div class="box">
    <strong>S1: 基礎盤面</strong><br>
    畫出 24 格環形棋盤<br>
    <i>方塊能隨骰子點數移動</i>
  </div>
  <div class="arrow">➔</div>
  <div class="box blue">
    <strong>S3: 薪資與結算</strong><br>
    經過起點發薪水<br>
    <i>每月固定扣除生活支出</i>
  </div>
  <div class="arrow">➔</div>
  <div class="box red">
    <strong>S5: 破產與勝利</strong><br>
    現金歸零出局<br>
    <i>達成被動收入大於支出勝出</i>
  </div>
</div>

- **第一天驗收標準**：全手動玩一局，確認迴圈可以正常結束

---

<!-- 第 61 頁 -->
# 第二天：資料驅動的威力

<div class="lead">卡片是卡片、規則是規則，加卡片絕不動遊戲引擎。</div>

<div class="grid">
  <div class="box">
    <strong>傳統硬寫陷阱</strong><br>
    把卡片效果寫死在 if-else 代碼中<br>
    <i>加一張新卡就要重寫整個遊戲</i>
  </div>
  <div class="arrow">➔</div>
  <div class="box blue">
    <strong>資料驅動架構</strong><br>
    卡片只是一張純資料表 (JSON)<br>
    <i>「名稱、成本、月收益、技能需求」</i>
  </div>
  <div class="arrow">➔</div>
  <div class="box red">
    <strong>極速擴充成果</strong><br>
    半小時內灌入 20 張在地職業<br>
    <i>引擎核心代碼一字未動</i>
  </div>
</div>

- 這正是為什麼不會寫程式的人，也能指揮 AI 輕鬆擴展遊戲內容

---

<!-- 第 62 頁 -->
# 第三天：財務手感的深度雕琢

<div class="lead">將真實生活中的財務習慣，無縫轉化為遊戲規則。</div>

<div class="grid">
  <div class="box">
    <strong>現實困境</strong><br>
    手寫記帳耗時拖沓<br>
    全自動又失去體感
  </div>
  <div class="arrow">➔</div>
  <div class="box blue">
    <strong>三級記帳制</strong><br>
    新手手動記 ➔ 熟練解鎖半自動<br>
    <i>後期晉升投資人全自動記帳</i>
  </div>
  <div class="arrow">➔</div>
  <div class="box red">
    <strong>情商指標</strong><br>
    高壓工作扣健康指標<br>
    <i>有錢但健康歸零依然失敗</i>
  </div>
</div>

- 好玩的本質，是讓機制懲罰現實中的投機、獎勵好習慣

---

<!-- 第 63 頁 -->
# 重構示範：每筆金錢變動必產生日記帳

<div class="lead">會計分錄是底線，每一塊錢流向都必須說得出由來。</div>

| 玩家動作 | 傳統遊戲作法（容易對不上） | FinFlow 鐵律作法（會計日記帳） |
| :--- | :--- | :--- |
| **買進出租套房** | 現金直接扣 20 萬，結束 | 借：不動產資產 100 萬 / 貸：現金 20 萬、銀行借款 80 萬 |
| **每月發薪日** | 現金加 5 萬、扣 3 萬 | 產生薪資收入分錄 +5 萬、生活雜支分錄 -3 萬 |
| **年終結算** | 現金只看剩餘總額 | 資產負債表與現金流量表即時連動配平 |

- 當代碼帳目對不上時，日記帳就是最好的除錯對帳單

---

<!-- 第 64 頁 -->
# 你在哪裡把關：人類決策者的職責

<div class="lead">AI 負責提供技術解法，你負責定奪商業邏輯對不對。</div>

<div class="grid">
  <div class="box">
    <strong>AI 提出的妥協提案</strong><br>
    「日記帳牽涉到底層結構，<br>
    不如我們先用變數直接加減？」
  </div>
  <div class="arrow">➔</div>
  <div class="box red">
    <strong>人類造物者的把關</strong><br>
    「不行。三條鐵律不能碰，<br>
    架構麻煩也要把日記帳做完整。」
  </div>
</div>

- 不會寫程式不代表沒有主導權；堅守商業常識就是最好的品管

---

<!-- 第 65 頁 -->
# 第四天：體驗重構與介面拋光

<div class="lead">功能做完只是 60 分，資訊層級分明才能稱為作品。</div>

<div class="grid">
  <div class="box">
    <strong>資訊超載盤面</strong><br>
    狀態、卡片、對話框擠成一團<br>
    <i>玩家找不到該按哪裡</i>
  </div>
  <div class="arrow">➔</div>
  <div class="box blue">
    <strong>三欄經典佈局</strong><br>
    左側個人面板・中間主遊戲盤<br>
    <i>右側永遠只留當前回合決策區</i>
  </div>
  <div class="arrow">➔</div>
  <div class="box red">
    <strong>乾淨視覺交付</strong><br>
    把背景雜訊轉移為彙總抽屜<br>
    <i>主視覺聚焦在關鍵數字</i>
  </div>
</div>

- 介面設計的重點不是畫圖好看，是「引導玩家做決策」

---

<!-- 第 66 頁 -->
# 階段回顧：前四天建立的資產

<div class="lead">此時你手上的不是空想，而是一個隨點隨玩的實體軟體。</div>

- **穩固骨架**：完成單機 15 輪財務模擬，勝利條件嚴密收口
- **豐富內容**：20 個職業、數十張機會與意外卡片全數入庫
- **無價歷程**：累積了數十個 Git 存檔點，隨時能說出每個機制的演進由來

<!-- EOF: VERIFIED FULL FILE DELIVERY -->