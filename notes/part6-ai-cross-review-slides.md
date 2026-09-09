---
marp: true
theme: finflow-clean
paginate: true
header: "FinFlow 實戰心法 | 第六部・讓 AI 互相抓錯"
---

<!-- 第 135 頁 -->
# 一個真實的下午：兩個 AI 交手、五個 bug

<div class="lead">2026 年 9 月 5 日，FinFlow v2.49.0。我把整套遊戲交給 Gemini 除錯。</div>

<div class="grid">
  <div class="box">
    <strong>Gemini 交出報告</strong><br>
    5 個 bug、5 段修改碼<br>
    <i>「已在沙盒實際執行」</i>
  </div>
  <div class="arrow">➔</div>
  <div class="box blue">
    <strong>Claude 逐條覆驗</strong><br>
    在我的電腦上實跑 24,000 局<br>
    <i>不是再讀一次，是真的跑</i>
  </div>
  <div class="arrow">➔</div>
  <div class="box red">
    <strong>結果</strong><br>
    3 真・1 半真・1 機制寫錯<br>
    <i>修改碼 4 段不能照抄</i>
  </div>
</div>

- **那個數字是怎麼來的**：AI 寫一支自動跑局的測試腳本，我在自己電腦上執行，跑完它自己印出統計。<span class="highlight">腳本要留在專案裡，這個數字才回查得到</span>——下一頁 Gemini 出問題的地方，正是這一點
- 我一行程式都沒看懂，但我能判斷誰對——因為我要求每一方拿出證據
- 這做法叫**交叉審查**，跟銀行的「四眼原則」一樣：重要的事，要兩雙眼睛看過

---

<!-- 第 136 頁 -->
# AI 會錯在哪：不是不會寫，是「看起來對」

<div class="lead">Gemini 五個 bug 的判定（出處：S42 前置驗證，2026-09-05）</div>

| 編號 | Gemini 說 | 實跑後 | 修改碼 |
| :--- | :--- | :--- | :--- |
| BUG-01/02 | 借還款金額 NaN 會污染帳本 | **真**，但 UI 正常操作碰不到 | 可用 |
| BUG-03 | 買進度先記錄再驗資，會造成多人失步 | **半真**：記錄屬實，失步推論錯 | 漏了技能折扣 |
| BUG-04 | 壞職業代號開局白屏 | **真** | 變數名寫錯，貼上就報錯 |
| BUG-05 | 破產急售查錯人，死結 | **真且更廣**，但機制寫錯 | 漏了外圈同型入口 |
| P2-1 | 房貸成數除以零 | 形式為真、目前不可達 | <span class="highlight">整行換掉，會把房貸邏輯改壞</span> |

- 它引用的測試腳本，repo 裡當時**根本不存在**——「已實跑」無法回查

---

<!-- 第 137 頁 -->
# 多一雙眼睛有用——但 AI 常常一起錯

<div class="lead">三個各七成準的人投票，比一個人準。前提是他們<b>各自想</b>，不是抄同一份答案。</div>

<div class="grid">
  <div class="box blue">
    <strong>各自想</strong><br>
    1 個人 70% 準<br>
    <i>3 個人投票 → 約 78%</i>
  </div>
  <div class="arrow">➔</div>
  <div class="box red">
    <strong>但 AI 讀的是同一本書</strong><br>
    不同模型的訓練資料高度重疊<br>
    <i>兩個都答錯時，很常<br>錯得一模一樣</i>
  </div>
  <div class="arrow">➔</div>
  <div class="box">
    <strong>所以</strong><br>
    「三個 AI 都同意」<br>
    <i>不算證據，它們可能一起錯</i>
  </div>
</div>

- 多找幾個 AI 看是對的，但**不能只靠投票**——先看下一頁的第二個坑，真正的解方在頁 139：**實跑**

---

<!-- 第 138 頁 -->
# 第二個坑：AI 會順著你

<div class="lead">你問「同不同意」，AI 多半會說同意——尤其你的問法已經透露你站哪邊。</div>

<div class="grid">
  <div class="box red">
    <strong>真實案例</strong><br>
    Gemini 對齊書開頭一整段<br>
    <i>「Claude 展示了極高水準的逆向工程能力…」</i>
  </div>
  <div class="arrow">➔</div>
  <div class="box">
    <strong>問題</strong><br>
    稱讚不是驗證<br>
    <i>它「完全認同」的五段修法，四段有錯</i>
  </div>
  <div class="arrow">➔</div>
  <div class="box blue">
    <strong>解法</strong><br>
    不問「同不同意」、不透露你站哪邊<br>
    <i>問「逐條核對原始碼，說對或不對、附行數」</i>
  </div>
</div>

- 問法決定答案的品質——這是你不寫程式也能控制的變數

---

<!-- 第 139 頁 -->
# 真正有效的那一步：實跑

<div class="lead">多人看＝抓得多；實跑＝抓得準。兩個都要。</div>

<div class="grid">
  <div class="box red">
    <strong>只有多人看</strong><br>
    假警報一堆<br>
    <i>大家一起錯，還以為是共識</i>
  </div>
  <div class="box red">
    <strong>只有實跑</strong><br>
    跑到的都準<br>
    <i>但沒人想到的問題就漏了</i>
  </div>
  <div class="box blue">
    <strong>兩個都有</strong><br>
    錯誤現形<br>
    <i>假警報被剔除</i>
  </div>
</div>

- 這次判定 Gemini 哪段機制寫錯，靠的不是「再讀一次」，是在我電腦上**用同一份引擎實跑**
- 共識只是證據攤開後的自然結果，不是目標

---

<!-- 第 140 頁 -->
# AI 也會糾正 AI——而且糾正的是「最強的那個」

<div class="lead">2026 年 9 月 7 日，ChatGPT 抓到四個 bug，交給 Claude 覆驗。</div>

<div class="grid">
  <div class="box">
    <strong>Claude 第一輪判定</strong><br>
    四項都真，但「缺資料會當機」<br>
    只有 7 種、單機存檔不受影響
  </div>
  <div class="arrow">➔</div>
  <div class="box red">
    <strong>ChatGPT 反駁</strong><br>
    「你只在開局狀態測，<br>
    進入決策後有 15 種」<br>
    「單機存檔就是重放，一樣受影響」
  </div>
  <div class="arrow">➔</div>
  <div class="box blue">
    <strong>Claude 實跑後</strong><br>
    兩點都承認、修正做法<br>
    <i>「我之前憑印象沒查，錯了」</i>
  </div>
</div>

- 沒有哪個 AI 永遠對。流程的價值就在**讓每一方都可能被推翻**

---

<!-- 第 141 頁 -->
# 七步流程（可以直接抄）

<div class="lead">把「多問幾個 AI」變成有停損、有證據門檻的固定程序。</div>

| 步 | 做什麼 | 關鍵 |
| :--- | :--- | :--- |
| 1 作者產出 | AI 寫程式＋自己的測試 | — |
| 2 盲審 | 兩個 AI 各自審，**不給彼此結果** | 每項附重現步驟，否則只算「疑似」 |
| 3 實證裁決 | 逐條實跑，分真／半真／假 | 機制寫錯的要指出 |
| 4 反向質詢 | 交回審查者 | 問「逐條核對」，不問「同意」 |
| 5 停損 | <span class="highlight">最多兩輪</span> | 沒共識的由人裁，或寫進待辦、這批不碰 |
| 6 人的三件事 | 定範圍、裁分歧、決定動手 | 你不寫程式，但這三件是你的 |
| 7 動手門檻 | 共識＋可重現測試＋備份＋全套回歸綠 | 四個缺一不動 |

---

<!-- 第 142 頁 -->
# 三種提示詞（複製就能用）

<div class="lead">問法決定答案品質。三個階段三種問法。</div>

<div class="grid">
  <div class="box blue">
    <strong>① 盲審</strong><br>
    「請審查這份程式。每個問題附：嚴重度、<b>第三者能照做的重現步驟</b>、出問題的位置、一句話修法。不確定的另列『疑似』。<b>不要改檔</b>。」
  </div>
  <div class="box">
    <strong>② 裁決</strong><br>
    「這是 A 的審查報告。<b>逐條實際執行</b>驗證，分真／半真／假；機制描述錯的指出來；它的修法能不能直接用。附你的執行紀錄。」
  </div>
  <div class="box red">
    <strong>③ 反向質詢</strong><br>
    「這是 B 的覆驗結論。<b>不要告訴我你同不同意</b>。請核對原始碼，<b>逐條說它對或不對</b>，附行數和理由；對的就明說對，漏掉的補上。」
  </div>
</div>

- 三句共同的底線：附證據、不改檔、不確定就說不確定

---

<!-- 第 143 頁 -->
# 什麼時候值得用：成本要誠實講

<div class="lead">這套流程不便宜。S43 用了三個模型、兩天；一個人做可能半天。</div>

<div class="grid">
  <div class="box blue">
    <strong>值得</strong><br>
    遊戲引擎、多人同步、<br>金錢計算、存檔格式<br>
    <i>錯了難回頭、影響所有人</i>
  </div>
  <div class="box">
    <strong>看情況</strong><br>
    新功能、平衡調整<br>
    <i>有自動化測試蓋著就可以少一輪</i>
  </div>
  <div class="box red">
    <strong>不值得</strong><br>
    改文案、調顏色、<br>加一張卡片<br>
    <i>回歸測試綠就好</i>
  </div>
</div>

- 判斷標準一句話：**改錯了要花多少力氣才回得來？** 回不來的才上這套

---

<!-- 第 144 頁 -->
# 你的角色：品管不是看懂程式，是要求證據

<div class="lead">整個過程我沒看懂任何一行程式碼，但每個決定都是我做的。</div>

<div class="grid">
  <div class="box">
    <strong>定範圍</strong><br>
    這批修什麼、不修什麼<br>
    <i>「F-1 另案，這批不碰」</i>
  </div>
  <div class="box blue">
    <strong>裁分歧</strong><br>
    兩個 AI 吵不完時<br>
    <i>「按你建議，他只是幫忙檢查」</i>
  </div>
  <div class="box red">
    <strong>決定動手</strong><br>
    證據齊了才說 go<br>
    <i>改前備份、全套測試綠、自己 push</i>
  </div>
</div>

- 你不需要成為工程師。你需要成為那個**不接受沒有證據的答案**的人

