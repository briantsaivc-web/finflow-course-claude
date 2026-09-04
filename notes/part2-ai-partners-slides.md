---
marp: true
theme: default
paginate: true
header: "FinFlow 實戰心法 | 第一部・想法怎麼來"
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

<!-- 第 23 頁 -->
# 深度案例：卡片的演進

<div class="lead">同一張卡片，可以隨玩家的能力逐步長出深度。</div>

<div class="grid">
  <div class="box">
    <strong>初階單純版</strong><br>
    固定報酬數字<br>
    <i>先讓迴圈跑得通</i>
  </div>
  <div class="arrow">➔</div>
  <div class="box blue">
    <strong>動態連動版</strong><br>
    報酬隨狀態浮動<br>
    <i>個人財務槓桿連動</i>
  </div>
  <div class="arrow">➔</div>
  <div class="box red">
    <strong>技能解鎖版</strong><br>
    隱藏長尾與隱性風險<br>
    <i>特定手藝才看得見</i>
  </div>
</div>

- **核心原則**：不要試圖在第 1 輪把卡片規則寫到極致

---

<!-- 第 24 頁 -->
# 第一層：固定的回報

<div class="lead">先求能玩能算，初期全部寫死固定數字。</div>

<div class="grid">
  <div class="box">
    <strong>卡面名稱</strong><br>
    市區套房投資案
  </div>
  <div class="box blue">
    <strong>投資成本</strong><br>
    自備款 20 萬 / 貸款 80 萬
  </div>
  <div class="box red">
    <strong>每月淨現金流</strong><br>
    固定 +8,000 元
  </div>
</div>

- **初學者心法**：第一版不要管通膨、空租或修繕，跑順規則最優先

---

<!-- 第 25 頁 -->
# 第二層：與玩家狀態連動

<div class="lead">同一張機會卡，對不同財務體質的人意義完全不同。</div>

| 玩家狀態條件 | 實際承擔與結果 | 遊戲機制教你的事 |
| :--- | :--- | :--- |
| **高現金儲備** | 利率一般，每月穩定收租 +8,000 元 | 現金多是談判籌碼 |
| **高負債槓桿** | 銀行信用調降，利息支出增加 3,000 元 | 負債會侵蝕實質報酬 |
| **已持有修繕手藝** | 自行維護免請師傅，每房每月再省工錢 | 技能可以直接折現 |

- 同一份資料卡片，因為玩家狀態不同而產生策略分歧

---

<!-- 第 26 頁 -->
# 第三層：資訊隱藏機制

<div class="lead">只有具備特定技能的人，才能看穿表面報酬下的風險。</div>

<div class="grid">
  <div class="box">
    <strong>普通玩家看見的</strong><br>
    表面投報率 8%<br>
    <i>看起來是一門好生意</i>
  </div>
  <div class="arrow">➔</div>
  <div class="box red">
    <strong>解鎖「財務分析」技能</strong><br>
    看穿未來 5 輪隱性支出<br>
    <i>惡意欠租率 30%・管線老化修繕</i>
  </div>
</div>

- 讓玩家主動想進修技能，而不是被動堆疊數值

---

<!-- 第 27 頁 -->
# 第四層：長尾與結構風險

<div class="lead">更高階的視野，看見的是十年後的宏觀週期。</div>

<div class="grid">
  <div class="box red">
    <strong>隱藏陷阱</strong><br>
    該商圈屬於人口外移區<br>
    <i>第 10 輪後資產面臨跌價腰斬</i>
  </div>
  <div class="arrow">➔</div>
  <div class="box blue">
    <strong>高階合規/治理技能</strong><br>
    提前發出週期預警提示<br>
    <i>避開長尾資產歸零風險</i>
  </div>
</div>

- 商業遊戲的深度，在於將真實世界的「認知落差」做成機制

---

<!-- 第 28 頁 -->
# 卡片演進給造物者的啟示

<div class="lead">誘因設計讓學習成為必需，而非無聊的數值加成。</div>

- **不用一次到位**：這四層是玩過多輪測試後才逐步疊上去的
- **以問題驅動升級**：玩家被騙過一次，才會懂得在遊戲裡學法律與審計
- <span class="highlight">造物者鐵律</span>：機制負責製造痛點，技能負責提供解方

---

<!-- 第 29 頁 -->
# 順序抉擇：機制優先還是內容優先？

<div class="lead">先有骨架再填肉，絕不為尚未成型的規則寫大量卡片。</div>

<div class="grid">
  <div class="box blue">
    <strong>第一步：機制先跑通 (80%)</strong><br>
    只做 6 張卡，驗證金流迴圈與勝負結算
  </div>
  <div class="arrow">➔</div>
  <div class="box">
    <strong>第二步：大量填入內容 (20%)</strong><br>
    機制驗證無誤後，指揮 AI 批量擴充 100 張卡
  </div>
</div>

- **致命錯誤**：一開始就寫滿 300 張卡片，改一次規則全盤作廢

---

<!-- 第 30 頁 -->
# 最常踩的陷阱：完美主義

<div class="lead">想清楚全部細節才動手，等於永遠不會動手。</div>

| 失敗者的思考迴圈 | 造物者的實戰節奏 |
| :--- | :--- |
| 一定要把全台灣所有稅制都塞進去 | 先抓出最常見的薪資與買賣情境 |
| 畫面一定要畫得跟 3A 大作一樣精緻 | 簡單方框與表格能跑就先測 |
| 必須支援八人即時語音連線 | 先做單人對決電腦，把規則測乾淨 |

- **座右銘**：完成遠勝於完美，先求上線、再求豐富

---

<!-- 第 31 頁 -->
# 第一部行動清單

<div class="lead">動手之前，請在紙上寫下這三件事。</div>

- [ ] **一句話痛點**：你要為玩家提供什麼生活財務的練習場？
- [ ] **三條底線鐵律**：列出絕對不准 AI 擅自妥協的原則
- [ ] **MVP 刀法**：挑出 6 張核心卡片與 1 個勝利條件

<!-- EOF: VERIFIED FULL FILE DELIVERY -->