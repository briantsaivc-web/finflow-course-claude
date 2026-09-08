---
marp: true
theme: finflow-clean
paginate: true
header: "FinFlow 實戰心法 | 第三部・常見坑與品管習慣"
---

<!-- 第 93 頁 -->
# 常見坑一：AI 的記憶體會滿

<div class="lead">問題不是「會不會滿」，是「什麼時候滿、滿了你怎麼辦」。</div>

<div class="grid">
  <div class="box">
    <strong>你會一直塞東西進去</strong><br>
    程式檔、規格書、變更說明<br>
    <i>因為 AI 要看得到才幫得上忙</i>
  </div>
  <div class="arrow">➔</div>
  <div class="box red">
    <strong>然後某一天</strong><br>
    它跟你說寫不進去了<br>
    <i>通常挑在你最忙的時候</i>
  </div>
</div>

- 這不是意外，是**必然**。任何長期累積的專案都會走到這一步
- 先有心理準備，你就會提早訂規則，而不是等爆掉才手忙腳亂

---

<!-- 第 94 頁 -->
# 案例：離上限只剩 10%

<div class="lead">FinFlow 撞牆前的真實數字。</div>

| | 數字 |
| :--- | ---: |
| 專案知識庫上限 | 2,000,000 |
| 每一份完整程式檔約占 | 300,000 – 350,000 |
| 全部留著，撐得了幾期 | **六、七期** |
| S17 交付前實際用量 | <span class="highlight">1,792,948（89.6%）</span> |

- 89.6% 是被**三份舊版程式檔**吃掉的——每一份都是「捨不得刪」留下來的
- 變更說明那種純文字檔，一份才 5,000–10,000。**佔空間的從來不是紀錄，是舊版本**

---

<!-- 第 95 頁 -->
# 解法：一張三條規則的 SOP

<div class="lead">丟東西之前，先確定你還有另一份。</div>

<div class="grid">
  <div class="box blue">
    <strong>① 程式檔只留最新一版</strong><br>
    新版寫入、回讀核對無誤<br>
    才刪上一版<br>
    <i>順序不能顛倒</i>
  </div>
  <div class="box">
    <strong>② 文字紀錄全部保留</strong><br>
    變更說明體積很小<br>
    <i>那是你的決策軌跡，不清</i>
  </div>
  <div class="box red">
    <strong>③ 用到 70% 就示警</strong><br>
    不要等寫不進去才說<br>
    <i>留給自己反應時間</i>
  </div>
</div>

- 第 ① 條的細節才是重點：**刪之前先把舊版讀回來、交還給自己保存，確認新版真的落地了，最後才刪**
- 這套規則訂完之後，同一個專案今天查是 60.7%——<span class="highlight">規則有用，是因為它訂在爆掉之前</span>

---

<!-- 第 96 頁 -->
# 常見坑二：哪一份才是現在該聽的？

<div class="lead">戴一隻錶的人知道現在幾點；戴兩隻錶的人永遠不確定。</div>

<div class="grid">
  <div class="box red">
    <strong>你的資料夾裡</strong><br>
    規格書 v0.1（草案）<br>
    規格書 v0.2（定案）<br>
    <i>兩份都在，都沒寫誰算數</i>
  </div>
  <div class="arrow">➔</div>
  <div class="box">
    <strong>三個月後</strong><br>
    你自己也忘了<br>
    <i>AI 更不可能知道</i>
  </div>
</div>

- 解法不是刪掉舊的（歷史有價值），是**在新版裡把話講清楚**
- 一句話就夠：「本版取代前版的哪些條款；<span class="highlight">前版沒被覆寫的部分仍然有效</span>」

---

<!-- 第 97 頁 -->
# 案例：一份做對了，兩份沒做

<div class="lead">同一個專案裡，正反教材都有。</div>

<div class="grid">
  <div class="box blue">
    <strong>✓ 做對的：自由圈</strong><br>
    v0.1 草案（7/24）<br>
    v0.2 定案（8/26）<br>
    <i>v0.2 文件內明文寫著：</i><br>
    <i>「取代 v0.1 對應條款，</i><br>
    <i>v0.1 未覆寫者仍有效」</i>
  </div>
  <div class="box red">
    <strong>✕ 沒做的：職業系統、品格帳本</strong><br>
    只有 v0.1 草案<br>
    <b>沒有定案版</b><br>
    <i>但程式裡早就做完了</i><br>
    <i>變成「文件沒升版，</i><br>
    <i>內容卻已生效」的懸空狀態</i>
  </div>
</div>

- 右邊那種最麻煩：**文件說的是舊的，程式跑的是新的，而沒有人記得這件事**

---

<!-- 第 98 頁 -->
# 常見坑三：規劃的數字跟做出來的對不上

<div class="lead">地圖不等於實際的地形。文件也不等於程式。</div>

<div class="grid">
  <div class="box">
    <strong>規劃時說</strong><br>
    人生百態卡 300 張<br>
    六類各 50 張
  </div>
  <div class="arrow">➔</div>
  <div class="box red">
    <strong>實際解析出來</strong><br>
    302 張<br>
    <i>六類分布不均</i><br>
    <i>「衣」只有 26 張</i>
  </div>
</div>

- 有落差是正常的。**重點不是避免落差，是有辦法把落差查出來**
- 查的方式也很關鍵：<span class="highlight">直接解析程式裡的資料，不是翻文件回想、也不是問 AI「我們做了幾張」</span>

---

<!-- 第 99 頁 -->
# 常見坑四：它不會說「我不確定」

<div class="lead">AI 沒有「我好像漏掉了什麼」這個表情。它的語氣永遠一樣肯定。</div>

<div class="grid">
  <div class="box red">
    <strong>它會說</strong><br>
    「已完成，全部 300 張都已實作」<br>
    <i>語氣非常有把握</i>
  </div>
  <div class="arrow">➔</div>
  <div class="box blue">
    <strong>你要做的</strong><br>
    「請直接解析程式碼<br>把實際數量列給我」<br>
    <i>不是再問一次「真的做完了嗎」</i>
  </div>
</div>

- 再問一次「真的嗎」，只會得到更肯定的「真的」。<span class="highlight">要換成「拿證據給我」</span>
- 這不是它在騙你——它是真的以為做完了。**信心不等於正確，人也一樣**

---

<!-- 第 100 頁 -->
# 定期「現況盤點」：跟自己的專案對帳

<div class="lead">帳要定期對，專案也是。</div>

<div class="grid">
  <div class="box">
    <strong>拿出來對的兩邊</strong><br>
    左：文件說的<br>
    右：程式裡實際有的
  </div>
  <div class="arrow">➔</div>
  <div class="box blue">
    <strong>怎麼對</strong><br>
    請 AI 直接解析程式資料<br>
    <i>逐項清點，不是憑印象</i>
  </div>
  <div class="arrow">➔</div>
  <div class="box red">
    <strong>對出來的落差</strong><br>
    有些能當場解決<br>
    <i>有些只能標「待確認」</i>
  </div>
</div>

- FinFlow 那次盤點列出五項落差：**四項當場用程式解析解決，第五項寫明「無法用程式碼回答，仍待確認」**
- 那句「仍待確認」是這份盤點最誠實、也最有用的地方

---

<!-- 第 101 頁 -->
# 你的品管習慣清單

<div class="lead">外科醫師靠一張清單降低併發症——不是因為不會，是因為人會漏。</div>

- ☐ **寫下鐵律**：三條就好，寫下絕不讓步的原則
- ☐ **先要規格書再要程式**：你看得懂文字，這是你的審核點
- ☐ **玩過再驗收**：不玩過就說完成，等於沒驗
- ☐ **每次交付都有變更說明**：含「未預期發現」那一段
- ☐ **版本要編號**：看得出先後就夠
- ☐ **找人測試**：你測不出自己的 bug
- ☐ **定期現況盤點**：文件跟程式對一次帳

<span class="highlight">七條裡面，沒有一條需要你會寫程式。</span>
