---
marp: true
theme: default
paginate: true
header: "FinFlow 實戰心法 | AI 協作邊界管理"
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

<!-- 案例第 1 頁 -->
# AI 協作的超展開現象

<div class="lead">你只要五毛，AI 往往會主動熱情地塞給你一塊。</div>

<div class="grid">
  <div class="box">
    <strong>人類原始指令</strong><br>
    數位資產做四點微調<br>
    <i>改動詞・區分長尾・補 AI 卡</i>
  </div>
  <div class="arrow">➔</div>
  <div class="box blue">
    <strong>AI 主動加碼</strong><br>
    覆寫引擎衰減演算法<br>
    <i>順手排查舊通知漏網之魚</i>
  </div>
  <div class="arrow">➔</div>
  <div class="box red">
    <strong>延伸發散提案</strong><br>
    「要不要順便做外包系統？」<br>
    <i>從改卡片演變成大架構重構</i>
  </div>
</div>

- **正面是極度省心**，**負面是若無約束，專案將瞬間失控發散**

---

<!-- 案例第 2 頁 -->
# 「要五毛給一塊」的雙面刃

<div class="lead">享受驚喜紅利，但絕不能任由對話與代碼無限膨脹。</div>

| 合作維度 | 正面效益（省心紅利） | 負面風險（失控代價） |
| :--- | :--- | :--- |
| **機制深度** | 主動將商業邏輯刻入代碼（如 AI 生成成本低，爆紅機率自動降至 8%） | 偷改底層引擎核心，改動範圍遠超原本預期 |
| **排錯敏銳度** | 動新卡順手抓出隱藏的多餘通知 | 隨意放大測試容忍度，破壞原有測試基線 |
| **資源消耗** | 一次對話解決多個隱性問題 | 忘記煞車時對話脈絡與 Token 瞬間燒爆 |

- **造物者心態**：允許 AI 給建議，但開工權限永遠捏在自己手裡

---

<!-- 案例第 3 頁 -->
# 實戰示範：把 AI 的發散收攏回待辦

<div class="lead">最優秀的工程師，是懂得主動把野心放進待辦清單。</div>

<div class="grid">
  <div class="box red">
    <strong>AI 的強烈衝動</strong><br>
    「我想做一人公司外包機制，<br>
    讓資產不用親自顧也不衰減！」
  </div>
  <div class="arrow">➔</div>
  <div class="box blue">
    <strong>自我克制底線</strong><br>
    「這需要新機制而不是新卡，<br>
    我不塞進這批，記進待辦。」
  </div>
  <div class="arrow">➔</div>
  <div class="box">
    <strong>版本乾淨交付</strong><br>
    S29 準時落地驗收<br>
    <i>450 項回歸測試乾淨全過</i>
  </div>
</div>

- **金句**：不要在修屋頂時，順便把地基挖開重鋪

---

<!-- 案例第 4 頁 -->
# 駕馭主動型 AI 的三條韁繩

<div class="lead">學會這三句話，把 AI 的超常發揮鎖在安全範圍。</div>

- **韁繩一：定死當期範圍（Scope Locking）**
  「今天只改資料層與數值，不准動任何既有引擎邏輯。」
- **韁繩二：善用待辦抽屜（Backlog Parking）**
  「這個點子非常好，先寫進待辦清單，本期一概不准動工。」
- **韁繩三：用回歸測試當照妖鏡**
  「不管你順便修了什麼，交付時必須證明既有測試全數通過。」

<!-- EOF: VERIFIED FULL FILE DELIVERY -->