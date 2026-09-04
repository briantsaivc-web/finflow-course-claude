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

<!-- 第 54 頁 -->
# 高低階模型分工的智慧

<div class="lead">不要拿牛刀削蘋果：高階模型動腦，輕量模型跑腿。</div>

<div class="grid">
  <div class="box red">
    <strong>高階旗艦模型</strong><br>
    Claude Opus / GPT-4o<br>
    <i>負責難題拆解・架構定案</i>
  </div>
  <div class="arrow">➔</div>
  <div class="box blue">
    <strong>輕量疾速模型</strong><br>
    Haiku / Flash / 4o-mini<br>
    <i>負責批量生成・文案填寫</i>
  </div>
</div>

- **成本法則**：架構思考只佔 10% 對話，90% 批量執行交給輕量模型

---

<!-- 第 55 頁 -->
# 實戰：模型分工操作範例

<div class="lead">用標準規格書做橋樑，兼顧超高精度與極低成本。</div>

| 工作階段 | 委派模型層級 | 具體執行任務 |
| :--- | :--- | :--- |
| **第一步：架構設計** | 高階旗艦模型 | 制定「品格帳本」資料結構與六大類別權重比例 |
| **第二步：產出範本** | 高階旗艦模型 | 產出 3 張符合規範的標準 JSON 示範卡牌 |
| **第三步：批量擴充** | 輕量疾速模型 | 按照範本，一口氣快速產出 100 張各職業卡片文案 |

- 思考與執行分流，Token 消耗降低 70%，速度提升 3 倍以上

---

<!-- 第 56 頁 -->
# 截圖除錯法：小白的最強武器

<div class="lead">講不清楚專有名詞沒關係，直接用眼睛看到的畫面說話。</div>

<div class="grid">
  <div class="box">
    <strong>傳統痛苦回報</strong><br>
    「那個按鈕按下去沒反應，<br>
    右邊好像變形了」
  </div>
  <div class="arrow">➔</div>
  <div class="box red">
    <strong>截圖標註三要素</strong><br>
    1. 紅圈圈出跑版位置<br>
    2. 一句話說明預期樣子<br>
    3. 附上一張 Console 報錯截圖
  </div>
</div>

- 多模態視覺能力，讓非工程師省去背誦前端 CSS 術語的痛苦

---

<!-- 第 57 頁 -->
# 實戰案例：畫面跑版一鍵修復

<div class="lead">給 AI 具體坐標，它能在 30 秒內精確鎖定錯誤行數。</div>

<div class="grid">
  <div class="box">
    <strong>上傳截圖與指令</strong><br>
    「在手機直式畫面下，<br>
    現金流總結面板被最底部的按鈕遮住了。」
  </div>
  <div class="arrow">➔</div>
  <div class="box blue">
    <strong>AI 視覺分析定位</strong><br>
    識別固定定位 (`fixed`) 缺少內距 (`padding-bottom`)
  </div>
  <div class="arrow">➔</div>
  <div class="box red">
    <strong>精準給出補丁</strong><br>
    只修正容器邊距<br>
    <i>不更動任何底層業務代碼</i>
  </div>
</div>

- **原則**：永遠拿「前後對比」驗收，改完立刻在瀏覽器刷新看結果

---

<!-- 第 58 頁 -->
# 第二部行動清單

<div class="lead">工具已備齊、習慣已建立，你的虛擬工程團隊正式開工。</div>

- [ ] **工具定位**：挑選一個主力對話工具，完成一個單檔網頁測試
- [ ] **存檔基地**：建立 GitHub 儲存庫，完成第一次 Commit & Push
- [ ] **協作默契**：記住「先要規格再寫代碼」與「截圖標註」兩大紀律

<!-- EOF: VERIFIED FULL FILE DELIVERY -->