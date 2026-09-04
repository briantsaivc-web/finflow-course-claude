---
marp: true
theme: default
paginate: true
header: "FinFlow 實戰心法"
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

<!-- 第 3 頁 -->
# 重新定義造物者

<div class="lead">你不是在學寫程式，你是在學指揮工程隊。</div>

<div class="grid">
  <div class="box blue"><strong>人類決策者</strong><br>出題目・定規格・做裁決</div>
  <div class="arrow">➔</div>
  <div class="box"><strong>自然語言</strong><br>SODA 互動・白話描述</div>
  <div class="arrow">➔</div>
  <div class="box red"><strong>AI 施工隊</strong><br>刻程式・調版面・修 Bug</div>
</div>

- **核心承諾**：不懂代碼，也能獨立產出多人連線遊戲

---

<!-- 第 4 頁 -->
# 開發時程的真相

<div class="lead">小步快跑，五天完成二十次疊代。</div>

| 日期 | 里程碑 | 實質進展 |
| :--- | :--- | :--- |
| **7/16** | 一頁規格書 | 釐清核心痛點，定義玩法邊界 |
| **8/25** | 正式動工 | 核心邏輯成型，單人版試跑 |
| **8/27** | 多人同步草案 | 設計 M12 鎖步架構，待核可才動工 |
| **8/30** | S20 里程碑 | 5 天 20 次疊代，多人連線完整落地 |

---

<!-- 第 5 頁 -->
# 動手前的第一步

<div class="lead">工欲善其事，先立一頁規格書。</div>

<div class="grid">
  <div class="box"><strong>01 核心受眾</strong><br>誰在玩？有何財務痛點？</div>
  <div class="box blue"><strong>02 遊戲迴圈</strong><br>擲骰 ➔ 事件 ➔ 決策 ➔ 結算</div>
  <div class="box red"><strong>03 勝利條件</strong><br>固定 15 輪後誰資產多？</div>
</div>

- **不開設計軟體**、**不架伺服器**，一張紙就能定案

---

<!-- 第 6 頁 -->
# 疊代的節奏感

<div class="lead">沒有一次到位的神作，只有極速修正的日常。</div>

<div class="grid">
  <div class="box"><strong>S1～S5</strong><br>打底核心機制</div>
  <div class="arrow">➔</div>
  <div class="box blue"><strong>S6～S10</strong><br>除錯與數值校正</div>
  <div class="arrow">➔</div>
  <div class="box red"><strong>S11～S15</strong><br>連線同步鎖步</div>
  <div class="arrow">➔</div>
  <div class="box"><strong>S16～S20</strong><br>版面重整收尾</div>
</div>

- 每天推進 4 期，每次只攻克一個小主題

---

<!-- 第 7 頁 -->
# 協作的邊界

<div class="lead">AI 負責提供選項，人類負責下達裁決。</div>

<div class="grid">
  <div class="box"><strong>遭遇技術瓶頸</strong><br>多人同步卡死異常</div>
  <div class="arrow">➔</div>
  <div class="box blue"><strong>AI 提供 3 種解法</strong><br>方案 A / B / C 優劣比較</div>
  <div class="arrow">➔</div>
  <div class="box red"><strong class="highlight">你的裁決</strong><br>守住鐵律，拍板路線</div>
</div>

- 失去裁決權，產品走向就會被 AI 帶偏

---

<!-- 第 8 頁 -->
# 最貴的經驗

<div class="lead">不看漂亮的程式碼，只拆真實踩過的坑。</div>

<div class="grid">
  <div class="box red"><strong>數值崩潰</strong><br>面板出現 NaN<br><i>型態未檢查</i></div>
  <div class="box red"><strong>雙向卡死</strong><br>多人連線死結<br><i>狀態未同步</i></div>
  <div class="box red"><strong>排版飄移</strong><br>螢幕縮放跑版<br><i>Zoom 倍率失真</i></div>
</div>

- 真實踩坑與工程除錯紀錄，就是最核心的教學資產

---

<!-- 第 9 頁 -->
# 讀者的落地產出

<div class="lead">做出一個能跑、能玩、能發布的極簡產品。</div>

<div class="grid">
  <div class="box blue"><strong>對戰架構</strong><br>1 位人類玩家 vs 1 電腦對手</div>
  <div class="arrow">➔</div>
  <div class="box"><strong>15 輪推進</strong><br>6 職業 + 10 事件 + 1 投資點</div>
  <div class="arrow">➔</div>
  <div class="box red"><strong>勝負裁決</strong><br>比較現金與投資估值總額</div>
</div>

- 跑滿 15 輪全自動記帳，直接部署至 GitHub Pages 免費玩

---

<!-- 第 10 頁 -->
# 出發前的認知

<div class="lead">放下技術恐懼，帶上你的邏輯即可。</div>

| 你完全不需要 | 你真正需要具備 |
| :--- | :--- |
| 先買昂貴的付費帳號 | 清楚具體地描述你的需求 |
| 精通任何程式語言（JS/HTML） | 遇到異常畫面能截圖指出問題 |
| 記憶複雜的終端機 Git 指令 | 守住三條不准妥協的底線鐵律 |