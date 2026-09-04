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

<!-- 第 40 頁 -->
# 習慣一：需求寫清楚

<div class="lead">寫清楚不等於寫很長，是寫到 AI 不用猜。</div>

| 模糊的需求（AI 容易失控） | 寫清楚的需求（標準示範） |
| :--- | :--- |
| 「幫我做幾張投資卡，要有賺有賠。」 | 「生成 3 張小額房產卡，自備款 20-30 萬、每月淨現金流 +5,000 到 +8,000，遵守資料驅動鐵律。」 |
| 「遊戲畫面好像有點擠，改一下。」 | 「將三欄佈局的右側操作面板寬度固定為 320px，中間主盤面維持 1:1 正方形。」 |

- **黃金三要素**：目標是什麼、邊界限制是什麼、希望怎麼交付

---

<!-- 第 41 頁 -->
# 習慣二：先要規格，再要程式

<div class="lead">規格書是最高防線，在文字階段喊停成本最低。</div>

<div class="grid">
  <div class="box">
    <strong>1. 提出構想</strong><br>
    描述功能與商業規則
  </div>
  <div class="arrow">➔</div>
  <div class="box blue">
    <strong>2. 審查規格書</strong><br>
    人類把關確認邏輯<br>
    <i>不合預期直接退回</i>
  </div>
  <div class="arrow">➔</div>
  <div class="box red">
    <strong>3. 動手寫代碼</strong><br>
    AI 照定案規格施工<br>
    <i>零認知偏差</i>
  </div>
</div>

- 看懂中文規格書人人做得到，等代碼寫完才發現做錯最昂貴

---

<!-- 第 42 頁 -->
# 習慣三：每次交付必附變更說明

<div class="lead">變更說明不是繁文縟節，是寫給未來的除錯地圖。</div>

- **做過什麼**：精確記錄新增了哪些卡片、修改了哪些數值
- **為什麼這樣改**：記錄背後的商業裁決與動機
- **未預期發現**：誠實寫下施工中抓到的關聯錯誤與潛在破綻
- <span class="highlight">核心價值</span>：半年後回頭查帳與排錯，全靠這份交付履歷

---

<!-- 第 43 頁 -->
# 習慣四：版本必須要有編號

<div class="lead">不用懂語意化版本號，看得出先後順序就夠用。</div>

<div class="grid">
  <div class="box">
    <strong>S1～S5</strong><br>
    單機機制骨架搭建
  </div>
  <div class="arrow">➔</div>
  <div class="box blue">
    <strong>S10～S14</strong><br>
    盤面重整與符號根治
  </div>
  <div class="arrow">➔</div>
  <div class="box red">
    <strong>S20～S29</strong><br>
    平衡實測與系統盤點
  </div>
</div>

- 每次疊代推進一個版號，出問題隨時知道該退回哪一個存檔點

---

<!-- 第 44 頁 -->
# 批量內容發想指令設計

<div class="lead">給範例、抓規律、自檢查：三步產出高質感卡片。</div>

<div class="grid">
  <div class="box">
    <strong>步驟 1：給定標竿</strong><br>
    餵入 2～3 張數值合理的既有卡片
  </div>
  <div class="arrow">➔</div>
  <div class="box blue">
    <strong>步驟 2：提煉規律</strong><br>
    讓 AI 分析級距、投入產出比
  </div>
  <div class="arrow">➔</div>
  <div class="box red">
    <strong>步驟 3：批量生成+自檢</strong><br>
    生成後必須自查是否超出邊界
  </div>
</div>

- 不要讓 AI 憑空發揮，規範坐標系才能產出穩定內容

---

<!-- 第 45 頁 -->
# 實戰案例：職業卡光譜生成

<div class="lead">讓 20 種職業的薪資與支出維持嚴密的數學手感。</div>

| 職業階層範例 | 月收入 | 月支出 | 儲蓄率手感與策略挑戰 |
| :--- | :--- | :--- | :--- |
| **基層起步**（超商店員、外送員） | 25k ~ 35k | 20k ~ 24k | 儲蓄極薄，抗風險能力極低 |
| **中堅專業**（軟體工程師、護理師） | 50k ~ 70k | 30k ~ 35k | 現金流穩健，首選穩健資產累積 |
| **高壓高薪**（主治醫師、業務經理） | 85k ~ 150k | 50k ~ 90k | 收入極高但支出沉重，轉身成本大 |

- 用真實社會結構給 AI 錨定數值，避免跑出脫離現實的荒謬卡片

---

<!-- 第 46 頁 -->
# 規劃與落地的落差排查

<div class="lead">不要相信文件宣稱的數字，直接解析代碼裡的真相。</div>

<div class="grid">
  <div class="box">
    <strong>企劃文件宣稱</strong><br>
    品格帳本收錄 300 張卡片<br>
    <i>六大生活類別均勻分佈</i>
  </div>
  <div class="arrow">➔</div>
  <div class="box red">
    <strong>代碼實體盤點</strong><br>
    腳本解析實際為 302 張<br>
    <i>「衣」類僅 26 張（嚴重偏低）</i>
  </div>
</div>

- **品管金句**：規劃歸規劃、落歸落地，真實差距只能靠代碼盤點

<!-- EOF: VERIFIED FULL FILE DELIVERY -->