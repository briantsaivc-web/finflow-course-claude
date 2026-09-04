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

<!-- 第 11 頁 -->
# 開發模式的典範轉移

<div class="lead">為什麼自己指揮 AI 做，比外包等別人做更划算？</div>

| 比較維度 | 外包或等待工程團隊 | 你親自指揮 AI 疊代 |
| :--- | :--- | :--- |
| **溝通成本** | 需求文件來回往返數週 | 自然語言即時對話修正 |
| **細節掌控** | 工程師常以技術限制回絕 | 核心商業邏輯由你親自拍板 |
| **疊代週期** | 改一版耗時以月為單位 | 5 天完成 20 次版本演進[cite: 2] |

- **結論**：工具門檻消失後，領域專家的商業直覺才是最貴的資產

---

<!-- 第 12 頁 -->
# 靈感來源：真實生活痛點

<div class="lead">最好的產品需求，往往來自你最痛的真實經歷。</div>

<div class="grid">
  <div class="box">
    <strong>生活真實痛點</strong><br>
    租房惡房客・合資遊艇買單<br>
    <i>社會欠缺安全練習場</i>[cite: 2]
  </div>
  <div class="arrow">➔</div>
  <div class="box blue">
    <strong>在地土壤轉化</strong><br>
    醫師工時・健檢紅字決策<br>
    <i>摒棄脫離現實的西方教條</i>[cite: 2]
  </div>
  <div class="arrow">➔</div>
  <div class="box red">
    <strong>產品核心玩法</strong><br>
    15 輪財務情商模擬<br>
    <i>真金白銀交學費前先試錯</i>[cite: 2]
  </div>
</div>

- 不從宏大理論出發，只解決眼前具體的生活困境

---

<!-- 第 13 頁 -->
# 借鏡經典：拆解再重構

<div class="lead">借鏡不是抄襲，是拆解經典骨架並更換靈魂。</div>

| 經典機制來源 | 傳統桌遊作法 | FinFlow 的在地改造[cite: 2] |
| :--- | :--- | :--- |
| **大富翁／現金流** | 骰子回合制、固定買地收租 | 引入真實職場工時與生活意外事件[cite: 2] |
| **記帳訓練** | 紙筆手寫記帳，節奏拖沓冗長 | 記帳自動化三級制，隨熟練度解鎖[cite: 2] |
| **勝負判斷** | 單純比拚現金或累積資產 | 結合幸福感、品格帳本與健康指標[cite: 1, 2] |

- 站在前人的肩膀上，保留迴圈、重寫規則

---

<!-- 第 14 頁 -->
# 守住邊界：先砍成 MVP

<div class="lead">你腦中的完整版，永遠比第一版能做出來的大十倍。</div>

<div class="grid">
  <div class="box">
    <strong>宏大願景</strong><br>
    全功能多人線上金融帝國
  </div>
  <div class="arrow">➔</div>
  <div class="box red">
    <strong>無情揮刀</strong><br>
    砍掉商城・砍掉拍賣・砍掉連線
  </div>
  <div class="arrow">➔</div>
  <div class="box blue">
    <strong>最小可行產品 (MVP)</strong><br>
    單機可跑・數值精準・規則可驗[cite: 2]
  </div>
</div>

- **定義**：MVP 是「最小可玩」，絕不是「最小可想」[cite: 2]

---

<!-- 第 15 頁 -->
# 實戰案例：FinFlow 最初的 MVP

<div class="lead">一開始很小，小到一天就能跑完所有閉環。</div>

| 卡牌與模組類別 | MVP 最初規劃規模[cite: 2] | 設計初衷與目標[cite: 2] |
| :--- | :--- | :--- |
| **職業卡** | 6 張（含月薪與月支出）[cite: 2] | 建立基礎現金流級距差距[cite: 2] |
| **機會卡** | 小額 14 張、大額 10 張[cite: 2] | 驗證主動收入與槓桿邏輯[cite: 2] |
| **事件卡** | 生活誘惑 16 張、市場 12 張[cite: 2] | 考驗財務情商與突發應變[cite: 2] |
| **對手邏輯** | 3 種基礎 NPC 行為模式[cite: 2] | 作為數值平衡驗證的對照組[cite: 2] |

- 規模小才能極速除錯，地基穩了才准擴充

---

<!-- 第 16 頁 -->
# 定下不能被打破的原則

<div class="lead">鐵律是人類給 AI 的韁繩，不准因施工難度而妥協。</div>

<div class="grid">
  <div class="box red">
    <strong>失控的風險</strong><br>
    AI 遇到技術障礙時<br>
    <i>會擅自簡化甚至修改遊戲規則</i>
  </div>
  <div class="arrow">➔</div>
  <div class="box">
    <strong>造物者的韁繩</strong><br>
    動手前立下不能改的原則<br>
    <i>技術可以換，原則不能動</i>[cite: 2]
  </div>
  <div class="arrow">➔</div>
  <div class="box blue">
    <strong>審核底線</strong><br>
    不需懂代碼語法<br>
    <i>看懂原則是否被違背即可</i>[cite: 2]
  </div>
</div>

- 沒有鐵律的協作，產品最終會淪為 AI 便宜行事的拼裝車

---

<!-- 第 17 頁 -->
# FinFlow 的三條鐵律

<div class="lead">動手寫代碼前，先定三條不可動搖的基石。</div>

- **鐵律一：引擎與 UI 徹底分離**
  規則計算是引擎，畫面長相是外殼；改版面絕不准動到數值邏輯[cite: 2]
- **鐵律二：資料驅動 (Data-Driven)**
  卡片數值全為獨立資料表，非寫死在邏輯中；增刪卡片免改引擎[cite: 2]
- **鐵律三：每筆金錢變動必產生日記帳**
  每一塊錢流向皆有分錄可查，帳目對不上直接退回重寫[cite: 2]

---

<!-- 第 18 頁 -->
# 為什麼小白更需要鐵律？

<div class="lead">你不用會修車，但你必須知道煞車絕不能拔掉。</div>

<div class="grid">
  <div class="box">
    <strong>工程師的把關方式</strong><br>
    逐行檢查程式碼架構與語法
  </div>
  <div class="arrow">➔</div>
  <div class="box blue">
    <strong>你的把關方式</strong><br>
    拿「三條鐵律」作為退件標準[cite: 2]
  </div>
  <div class="arrow">➔</div>
  <div class="box red">
    <strong>下達指令話術</strong><br>
    「這個改動動到了引擎，退回重做」
  </div>
</div>

- 鐵律是小白面對黑盒子技術時，唯一的最高裁決依據[cite: 2]

---

<!-- 第 19 頁 -->
# 難度分期的智慧

<div class="lead">先把地基打牢，進階複雜功能刻意延後。</div>

<div class="grid">
  <div class="box blue"><strong>第 1 階段</strong><br>單機規則閉環</div>
  <div class="arrow">➔</div>
  <div class="box blue"><strong>第 2 階段</strong><br>數值驗證平衡</div>
  <div class="arrow">➔</div>
  <div class="box"><strong>第 3 階段</strong><br>介面拋光重整</div>
  <div class="arrow">➔</div>
  <div class="box red"><strong>第 4 階段</strong><br>多人同步連線</div>
</div>

- 任何過早引入的多人連線或複雜後端，都是專案腰斬的元兇

---

<!-- 第 20 頁 -->
# 實戰案例：多人連線的管制

<div class="lead">連你自己都要簽字，AI 才能動手施工。</div>

<div class="grid">
  <div class="box red">
    <strong>高風險架構</strong><br>
    M12 多人連線鎖步機制[cite: 2]
  </div>
  <div class="arrow">➔</div>
  <div class="box">
    <strong>工程書文件標註</strong><br>
    「v1.0 草案，待 Brian 核可後動工」[cite: 2]
  </div>
  <div class="arrow">➔</div>
  <div class="box blue">
    <strong>造物者意志</strong><br>
    單機版 100% 穩定之前<br>
    絕不准提前開工多人同步[cite: 2]
  </div>
</div>

- 規範寫得越死，專案進度就越安全[cite: 2]

---

<!-- 第 21 頁 -->
# 點子難度分級工作表

<div class="lead">動手之前，先將你的構想無情歸類。</div>

| 分級類別 | 判定標準 | 具體功能處置策略 |
| :--- | :--- | :--- |
| **現在做 (MVP)** | 沒有它，核心遊戲迴圈無法運作 | 職業基本盤、固定輪數、買賣結算[cite: 2] |
| **之後做 (Next)** | 有它更豐富，但沒有也能玩得通 | 技能樹深度、特殊事件、自動升級[cite: 1, 2] |
| **也許不做 (Never)** | 開發成本極高，邊際效益未知 | 即時語音聊天、自定義換裝、複雜拍賣 |

- 隨時拿著這張表，砍掉 AI 試圖為你塞入的過度設計

---

<!-- 第 22 頁 -->
# 想法如何越滾越大？

<div class="lead">版本擴充不是失控膨脹，是有秩序地生長。</div>

<div class="grid">
  <div class="box">
    <strong>草案初生 (v0.1)</strong><br>
    6 張職業卡跑通原型[cite: 2]
  </div>
  <div class="arrow">➔</div>
  <div class="box blue">
    <strong>規則拓展 (v1.0)</strong><br>
    規劃 20 張職業光譜草案[cite: 2]
  </div>
  <div class="arrow">➔</div>
  <div class="box red">
    <strong>代碼落地 (基線驗收)</strong><br>
    20 張職業全數解析入庫[cite: 2]
  </div>
</div>

- 容許想法長大，但必須透過版本記錄逐一核對落差[cite: 2]

<!-- EOF: VERIFIED FULL FILE DELIVERY -->