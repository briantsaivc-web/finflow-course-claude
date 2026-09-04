---
marp: true
theme: default
paginate: true
header: "FinFlow 實戰心法 | DARA 數據治理與平衡實戰"
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

<!-- 第 1 頁 -->
# 數據治理的開端

<div class="lead">不靠感覺調遊戲，用 500 局模擬逼出真相。</div>

<div class="grid">
  <div class="box"><strong>19 個技能</strong><br>成本與冷卻盤點</div>
  <div class="arrow">➔</div>
  <div class="box blue"><strong>500 局實測</strong><br>跑出真實學成率</div>
  <div class="arrow">➔</div>
  <div class="box red"><strong>浮現矛盾</strong><br>全場最痛技能無人學</div>
</div>

- **造物者視角**：跑數據不是為了寫論文，是為了看清機制盲點

---

<!-- 第 2 頁 -->
# 破除人為限制的威力

<div class="lead">限制應回歸時間與金錢，不該是人為設定的上限。</div>

<div class="grid">
  <div class="box">
    <strong>舊版枷鎖</strong><br>
    強設上限只能學 3 個<br>
    <i>高階技能學成率僅 0.1%</i>
  </div>
  <div class="arrow">➔</div>
  <div class="box blue">
    <strong>決策者裁決</strong><br>
    取消技能數上限<br>
    <i>由現金水位與輪數制衡</i>
  </div>
  <div class="arrow">➔</div>
  <div class="box red">
    <strong>落地結果</strong><br>
    高階學成率衝至 22%<br>
    <i>轉職次數從 25 飆升至 216</i>
  </div>
</div>

- 拿掉代碼裡的死規則，系統生態自然活起來

---

<!-- 第 3 頁 -->
# 量級歸位的商業常識

<div class="lead">不能讓換燈泡的手藝，變成房地產的暴利工具。</div>

| 技能項目 | 異常現象（S27 基線） | 修正裁決（S28 落地） |
| :--- | :--- | :--- |
| **基礎水電** | 房產修繕折半，狂省 22,541<br><i>（全場最高，嚴重偏離生活常識）</i> | 改為每次固定省工錢 2,000 元<br><i>（總折抵降為 3,062，量級回歸日常）</i> |
| **木作修繕** | 租金加成 8%，且沒發事件<br><i>（裝修加租背離 DIY 省錢本意）</i> | 改為每房每月固定省 1,000 元<br><i>（且每間房定期跳出省錢通知）</i> |

- **人類的責任**：檢查數值是否符合現實生活的量級邏輯

---

<!-- 第 4 頁 -->
# 生活邏輯高於工程代碼

<div class="lead">每一次數值變更，背後都必須有一套說得通的故事。</div>

<div class="grid">
  <div class="box">
    <strong>工程師草案</strong><br>
    部門團建上山開車<br>
    <i>換取永久加薪</i>
  </div>
  <div class="arrow">➔</div>
  <div class="box red">
    <strong>決策者質疑</strong><br>
    一次性出差勞務<br>
    <i>憑什麼能終身加薪？</i>
  </div>
  <div class="arrow">➔</div>
  <div class="box blue">
    <strong>商業情境修正</strong><br>
    改為接待重要外賓十天<br>
    <i>此後專屬客戶線歸你經營</i>
  </div>
</div>

- 代碼只管數字加減，真實的說服力只能由你賦予

---

<!-- 第 5 頁 -->
# 審慎看待量測工具

<div class="lead">看到數據是 0，先查是不是量尺本身壞了。</div>

- **量測盲點**：原本統計只抓現金，薪資倍率折算的價值全被算成 0
- **實體低估**：最致命的 AI 裁員風暴，在後台竟被記錄為「零損失」
- **修復對齊**：將薪資倍率折算為 24 輪實質損益，真實價差回歸第一名
- <span class="highlight">終極警惕</span>：AI 會寫程式，但也會看錯報表欄位；持續交叉驗算才是品管核心