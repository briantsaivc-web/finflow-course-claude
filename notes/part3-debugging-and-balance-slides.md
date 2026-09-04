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

<!-- 第 67 頁 -->
# 實戰踩坑：S10 怪符號根治

<div class="lead">不要被亂碼嚇退，畫面上的怪符號往往只是字串污染。</div>

<div class="grid">
  <div class="box red">
    <strong>現象：畫面冒出怪字</strong><br>
    卡片標題後方黏著殘留標籤<br>
    <i>排版錯亂、美觀全毀</i>
  </div>
  <div class="arrow">➔</div>
  <div class="box blue">
    <strong>排查：定位污染源</strong><br>
    AI 引用標籤或編碼外洩<br>
    <i>字串未經清洗直接注入 DOM</i>
  </div>
  <div class="arrow">➔</div>
  <div class="box">
    <strong>根治：建立清洗過濾</strong><br>
    在渲染最前端強制防呆正則<br>
    <i>一次性防堵所有類似格式漏洞</i>
  </div>
</div>

- **品管守則**：及時發現錯、及時要求 AI 給出徹底解法，絕不手動逐一苦改

---

<!-- 第 68 頁 -->
# 第五天：數值平衡不是靠猜的

<div class="lead">不靠個人主觀感覺，用千局自動化模擬的數據說話。</div>

| 傳統遊戲調平衡 | FinFlow 的 DARA 治理模式 |
| :--- | :--- |
| 自己玩兩把，覺得太難就隨便改大數字 | 跑 1,000 局自動化無人模擬，產出統計報表 |
| 往往改好一個職業，弄壞另外三個職業 | 監控全職業勝率分布，任何異常波動無所遁形 |
| 玩家抱怨時不知道問題出在機制還是運氣 | 數據精確指出：究竟是第幾輪出現系統性卡關 |

- 機器能在 30 秒內跑完你玩三年的局數，讓數據替你做主

---

<!-- 第 69 頁 -->
# 實戰驗證：千局模擬三項硬指標

<div class="lead">合格的商業模型，數值必須收斂在安全區間內。</div>

<div class="grid">
  <div class="box blue">
    <strong>財務自由率</strong><br>
    目標區間 75% ~ 85%<br>
    <i>太高無挑戰，太低挫折感過重</i>
  </div>
  <div class="box red">
    <strong>非自願破產率</strong><br>
    目標壓在 1.0% ~ 2.0%<br>
    <i>避免極端運氣導致不可逆崩潰</i>
  </div>
  <div class="box">
    <strong>通關平均輪數</strong><br>
    穩定落在 11 ~ 13 輪<br>
    <i>確保單局 20 分鐘完賽節奏</i>
  </div>
</div>

- **S29 實戰成果**：創投派自由率 82.4%、破產率 1.0%，門檻乾淨收口

---

<!-- 第 70 頁 -->
# 實戰案例：測試放大而不是放寬門檻

<div class="lead">當數據出現異常時，先懷疑樣本數，絕不隨意妥協標準。</div>

<div class="grid">
  <div class="box red">
    <strong>S29 測試紅字報警</strong><br>
    T-58「電腦買到新創」失敗<br>
    <i>新卡加入導致牌堆亂數偏移</i>
  </div>
  <div class="arrow">➔</div>
  <div class="box">
    <strong>工程師的錯誤直覺</strong><br>
    「既然買不到，<br>
    我們把測試成功門檻降低？」
  </div>
  <div class="arrow">➔</div>
  <div class="box blue">
    <strong>造物者的科學處置</strong><br>
    樣本從 12 局擴大至 30 局<br>
    <i>實測 60 局成功 20 次，機制完全正常</i>
  </div>
</div>

- **金句**：不要為了讓測試變綠，而動手把度量衡縮水

---

<!-- 第 71 頁 -->
# 面對改壞代碼的終極武器：Git 降落傘

<div class="lead">當 AI 把功能越修越爛時，果斷放棄並一鍵還原。</div>

<div class="grid">
  <div class="box red">
    <strong>陷入死胡同的陷阱</strong><br>
    為修一個小 bug 改動十處<br>
    <i>對話越來越長，代碼徹底失控崩潰</i>
  </div>
  <div class="arrow">➔</div>
  <div class="box blue">
    <strong>Git 還原（Reset）</strong><br>
    按下還原鍵，1 秒退回前一版<br>
    <i>回到 15 分鐘前測試全過的健康狀態</i>
  </div>
</div>

- 每次 Commit 就是你的安全氣囊，學會及時停損重啟對話

---

<!-- 第 72 頁 -->
# 第三部行動清單

<div class="lead">5 天衝刺收工，你已經跨過了從空想到產品的鴻溝。</div>

- [ ] **跑通單機閉環**：確保骰子、薪資、破產判定無死角運作
- [ ] **完成三級記帳**：讓每筆資產買賣均有會計日記帳可追溯
- [ ] **千局回歸守門**：建立數值基準線，卡片再多也不怕平衡崩塌

<!-- EOF: VERIFIED FULL FILE DELIVERY -->