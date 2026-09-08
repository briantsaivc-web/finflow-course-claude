---
marp: true
theme: finflow-clean
paginate: true
header: "FinFlow 實戰心法 | 第三部・找人測試與多人連線"
---

<!-- 第 86 頁 -->
# Step4：你測不出自己的 bug

<div class="lead">魚是最後一個發現水的。你太熟悉自己的產品了。</div>

<div class="grid">
  <div class="box">
    <strong>你玩的時候</strong><br>
    每一步都照「正確用法」<br>
    <i>因為那是你設計的</i>
  </div>
  <div class="arrow">➔</div>
  <div class="box red">
    <strong>別人玩的時候</strong><br>
    他不知道什麼叫正確用法<br>
    <i>所以他會走到你沒走過的路</i>
  </div>
</div>

- 你會不自覺避開容易出問題的操作——<span class="highlight">不是故意的，是你的手已經學會繞過去了</span>
- 所以找人測試不是「禮貌上讓別人看一下」，是**唯一能走到那些路的方法**

---

<!-- 第 87 頁 -->
# 案例：三個人玩一局，抓出五個 bug

<div class="lead">而且其中最嚴重的那個，一個人玩<b>永遠</b>不會出現。</div>

<div class="grid">
  <div class="box red">
    <strong>那個 bug</strong><br>
    借款畫面寫死了「第 1 個玩家」<br>
    <i>一個人玩時你就是第 1 個</i><br>
    <i>所以永遠正確</i>
  </div>
  <div class="arrow">➔</div>
  <div class="box">
    <strong>三個人玩</strong><br>
    第 2、3 個人打開借款畫面<br>
    看到的是<b>別人的額度</b><br>
    <i>按下去當然借不到</i>
  </div>
</div>

- 這種「單機剛好是對的」最可怕：**它不是壞掉，它是巧合地對**
- 玩家還看到滿螢幕的 `NO_CAPACITY`。後來也改了：<span class="highlight">錯誤訊息要說人話</span>——「信用額度不足，借不到這個金額」

---

<!-- 第 88 頁 -->
# 五個抱怨，其實是同一個病

<div class="lead">使用者告訴你的是<b>症狀</b>，不是病因。這是你的工作。</div>

| 他們回報的 | 實際上 |
| :--- | :--- |
| 「玩到一半卡住了」 | ← |
| 「某個人的可借金額怪怪的」 | ← 同一條根因鏈的三個症狀 |
| 「合資邀請有問題」 | ← |
| 「借款拉桿拉不到滿」 | 另一個獨立問題 |
| 「商城在別人回合也能買」 | 另一個獨立問題 |

- 不要照回報的條數去修。<span class="highlight">先問「這幾件事會不會是同一件事？」</span>
- 這句話你可以直接丟給 AI：「這幾個回報有沒有可能是同一個根因？請往回追。」

---

<!-- 第 89 頁 -->
# 回饋怎麼轉成 AI 聽得懂的話

<div class="lead">病人說哪裡不舒服，醫生決定要照哪裡。你是那個醫生。</div>

<div class="grid">
  <div class="box red">
    <strong>① 原話（很情緒）</strong><br>
    「這個超難用欸」
  </div>
  <div class="arrow">➔</div>
  <div class="box">
    <strong>② 你追問</strong><br>
    哪個畫面？按了什麼？<br>
    你以為會發生什麼？<br>
    <i>實際發生了什麼？</i>
  </div>
  <div class="arrow">➔</div>
  <div class="box blue">
    <strong>③ 轉成 bug 描述</strong><br>
    照 Step2 的公式<br>
    <i>再丟給 AI</i>
  </div>
</div>

- 追問的四個問題就是全部了。<span class="highlight">問完再丟給 AI，命中率天差地遠</span>
- 「這個超難用」丟給 AI，它只能猜；補上這四項，它可以直接去找

---

<!-- 第 90 頁 -->
# Step5（選修）：要不要做多人連線？

<div class="lead">先問「要不要」，再問「怎麼做」。這一步不是每個作品都需要。</div>

<div class="grid">
  <div class="box blue">
    <strong>需要</strong><br>
    不同的人<br>
    在<b>不同的裝置上</b><br>
    同時互動
  </div>
  <div class="box">
    <strong>不需要</strong><br>
    一台裝置輪流玩<br>
    或單人對電腦<br>
    <i>那就別碰這一步</i>
  </div>
</div>

- 多人連線是整個專案裡最貴的一塊。<span class="highlight">不需要卻做了，等於自找兩週的麻煩</span>
- FinFlow 需要，因為它的教育場景就是「一家人各自拿平板一起玩」

---

<!-- 第 91 頁 -->
# 大改動之前：先寫工程書，核可才動工

<div class="lead">「凡事豫則立，不豫則廢。」——《中庸》</div>

FinFlow 的多人連線工程書，標題就寫著<b>「草案，待核可後動工」</b>。裡面有三段特別值得抄：

<div class="grid">
  <div class="box blue">
    <strong>你拍板的事</strong><br>
    用什麼後端、幾個人、<br>斷線怎麼辦<br>
    <i>四項，先寫清楚</i>
  </div>
  <div class="box">
    <strong>這次<b>不做</b>什麼</strong><br>
    帳號系統、排行榜、<br>聊天、防作弊<br>
    <i>寫下來才不會偷偷長大</i>
  </div>
  <div class="box red">
    <strong>誰驗收哪一項</strong><br>
    哪些 AI 能自己驗<br>
    哪些一定要你本機測<br>
    <i>先講好，不要事後才發現</i>
  </div>
</div>

- 中間那格最容易被跳過，也最重要：**「非目標」清單是防止範圍失控的唯一工具**

---

<!-- 第 92 頁 -->
# 白話版：多人連線在解決什麼問題

<div class="lead">不是把畫面傳給大家看，是<b>大家照同一份譜各自演奏</b>。</div>

<div class="grid">
  <div class="box">
    <strong>一本共同的動作紀錄</strong><br>
    誰在第幾步做了什麼<br>
    <i>只能往後加，不能改</i>
  </div>
  <div class="arrow">➔</div>
  <div class="box blue">
    <strong>每台裝置各自重算</strong><br>
    同一份紀錄、同一顆亂數種子<br>
    <i>算出來保證一樣</i>
  </div>
  <div class="arrow">➔</div>
  <div class="box red">
    <strong>斷線重連＝補放</strong><br>
    把落後的動作補算一次<br>
    <i>就追上了</i>
  </div>
</div>

- 這個做法叫**鎖步同步**。你不需要會做，只需要聽得懂 AI 在講什麼
- 而且你的角色沒變：<span class="highlight">決定要不要做、什麼時候做。技術方案讓 AI 提，你對照鐵律與時程判斷</span>
