---
marp: true
theme: finflow-clean
paginate: true
header: "FinFlow 實戰心法 | 第五部・結語與資源包"
---

<!-- 第 125 頁 -->
<!-- _class: dense -->
# 五個心法，一張圖記完

<div class="lead">整本書最常用的基本功，收斂成這五句——而且每一句都住在全景圖的某一格（<b>全景圖在第七部</b>，這裡先記住對應關係就好）。</div>

| | 心法 | 一句話 | 住在全景圖哪一格 |
| :--- | :--- | :--- | :--- |
| ① | **鐵律先行** | 動手前先寫下不能讓步的三條 | 規格書：**不做什麼** |
| ② | **MVP 優先** | 砍到剩骨架，先讓它跑起來 | 規格書：**做什麼** |
| ③ | **小步疊代** | 一次一個小主題，每次都驗收 | 執行 ⇄ 優化 那個迴圈 |
| ④ | **找人測試** | 你測不出自己的 bug | 成品・上線：**別人自己會用** |
| ⑤ | **定期盤點** | 文件跟成品，定期對一次帳 | 四道閘門：**落地驗證** |

- 五條裡面，<span class="highlight">沒有一條跟「會不會寫程式」有關</span>
- 這五條是**一開始就用得上**的基本功；還有第六條要撞到牆才用得上，下一頁講
- 它們也不只適用做遊戲——<b>第七部</b>把同一張流程換成「寫一份產業研究報告」，一格都沒改

---

<!-- 第 125b 頁 -->
<!-- _class: dense -->
# 第六條：五個心法沒教你的那一招

<div class="lead">前五條讓你把事情做完。這一條讓你在做不下去的時候，還走得下去。</div>

<div class="grid">
  <div class="box red">
    <strong>五個心法管得到的</strong><br>
    範圍失控 ➔ ① 鐵律<br>
    做太大 ➔ ② MVP<br>
    改一次全垮 ➔ ③ 小步<br>
    自己看不見 ➔ ④ 找人測<br>
    文件脫節 ➔ ⑤ 盤點
  </div>
  <div class="arrow">➔</div>
  <div class="box">
    <strong>管不到的那一種</strong><br>
    五條都做了，<br>
    <b>迴圈就是轉不動</b><br>
    <i>每次都要重講規矩</i><br>
    <i>AI 說做好了其實沒有</i><br>
    <i>修 A 順手動壞 B</i>
  </div>
  <div class="arrow">➔</div>
  <div class="box blue">
    <strong>⑥ 借鏡專業</strong><br>
    不要問「這個怎麼修」<br>
    要問<b>「這件事，專業的<br>團隊是怎麼分工的？」</b><br>
    <i>第七部整頁講這一招</i>
  </div>
</div>

- 這一條是<span class="highlight">作者把 FinFlow 做到第 26 批（S26）才學會的</span>——前五條寫得出來，是因為它們一開始就用得上；第六條要撞到牆才用得上

---

<!-- 第 126 頁 -->
# 資源包：可以直接拿去用的東西

<div class="lead">全書出現過、可以直接複製的模板，索引都在這裡。</div>

<div class="grid">
  <div class="box">
    <strong>寫在動手前</strong><br>
    三條鐵律 ＋ 不做清單（頁 115）<br>
    MVP 刀法（頁 14）<br>
    點子難度分級表（頁 21）
  </div>
  <div class="box blue">
    <strong>四份提示詞</strong><br>
    提示詞 1 生規格書（頁 116）<br>
    提示詞 2 生程式（頁 117）<br>
    提示詞 3 抓 bug（頁 118）<br>
    提示詞 4 加功能（頁 119）
  </div>
  <div class="box red">
    <strong>驗收用</strong><br>
    品管習慣七條（頁 101）<br>
    驗收清單五項（頁 120）<br>
    交叉審查三種提示詞（第六部頁 142）
  </div>
</div>

- 提示詞全部是純文字，直接複製貼上就能用；驗收清單是給你自己逐條打勾的
- 另外兩張要印下來貼牆上的：<b>全景圖</b>與<b>工具對照表</b>，都在<span class="highlight">第七部</span>

---

<!-- 第 127 頁 -->
# 做完不是終點，是起點

<div class="lead">你已經走完第一輪 MVP 的主幹：想法、規格書、實作、測試、上線、收回饋。接下來有兩條路可以走。</div>

<div class="grid">
  <div class="box blue">
    <strong>方向一</strong><br>
    把一個大檔案<br>
    <b>拆成模組化結構</b><br>
    <i>引擎、資料、畫面分開放</i>
  </div>
  <div class="box red">
    <strong>方向二</strong><br>
    讓卡片內容<br>
    <b>跟程式邏輯脫鉤</b><br>
    <i>加卡片不用碰邏輯</i>
  </div>
</div>

- 接下來五頁（頁 128–132）是**畢業後的選修**：只講原理與方向，不做完整教學。不影響你完成本書，也不需要現在動手
- 但有一件事值得先講：<span class="highlight">這兩個方向，FinFlow 後來真的都做了</span>

---

<!-- 第 128 頁 -->
# 方向一：為什麼「一個大檔案」後來會拖住你

<div class="lead">一個抽屜塞所有東西，找一支筆要翻十分鐘。</div>

<div class="grid">
  <div class="box">
    <strong>一開始很爽</strong><br>
    一個 HTML 檔<br>
    點兩下就打開<br>
    <i>不用裝任何東西</i>
  </div>
  <div class="arrow">➔</div>
  <div class="box red">
    <strong>後來很痛</strong><br>
    卡片、規則、畫面全混在一起<br>
    改一張卡要在巨大的檔案裡找位置<br>
    <i>檔案越大，AI 跟你都越難掌握全貌</i>
  </div>
</div>

- 這不是一開始做錯了。<span class="highlight">單檔在起步階段是對的選擇</span>——它讓你快速跑起來
- 就算你照第四部的鐵律二把卡片集中在檔案最上方，**檔案長到幾千行之後，你跟 AI 一樣掌握不了全貌**
- 拖住你的不是單檔本身，是**單檔長到某個大小之後**

---

<!-- 第 129 頁 -->
# 方向一，後來真的做了

<div class="lead">2026 年 9 月 1 日那次改動，把一整個大檔案拆開了。</div>

| 拆成四塊 | 各自負責什麼 |
| :--- | :--- |
| **引擎** | 遊戲規則怎麼算（不管畫面長怎樣） |
| **資料** | 所有卡片內容，一包一包的 JSON 檔（頁 55、61 講過：一種電腦看得懂的表格寫法） |
| **畫面** | 怎麼顯示、按鈕在哪裡 |
| **建置** | 一道指令把三邊組回成一個 HTML 檔 |

- 關鍵在最後一列：**拆開是為了好維護，最後還是組回單一檔案給玩家用**
- 玩家拿到的東西沒變，變的是<span class="highlight">你跟 AI 修改它的難易度</span>

---

<!-- 第 130 頁 -->
# 方向二：食譜跟廚房要分開

<div class="lead">想加一道菜，不應該要重蓋一次廚房。</div>

<div class="grid">
  <div class="box red">
    <strong>混在一起的時候</strong><br>
    卡片寫在程式裡<br>
    加一張卡＝改程式<br>
    <i>改完整套邏輯都要重測</i>
  </div>
  <div class="arrow">➔</div>
  <div class="box blue">
    <strong>分開之後</strong><br>
    卡片是獨立的資料檔<br>
    加卡片只改資料，跑一次建置<br>
    <i>邏輯一行都不用動</i>
  </div>
</div>

- 方向二跟方向一，FinFlow 是**同一次改動一起做的**——它們本來就是同一件事的兩面
- 這也呼應第四部鐵律二：<b>卡片資料集中放一起，加卡片不用動遊戲邏輯</b>

---

<!-- 第 131 頁 -->
# 方向二的延伸：批量生成與專用工具

<div class="lead">資料獨立出來之後，一次生一批才真的好管理、好檢查。</div>

<div class="grid">
  <div class="box">
    <strong>批量生成</strong><br>
    給 2～3 張範例卡<br>
    請 AI 抓規律生一整批<br>
    <i>再請它自己檢查一致性</i>
  </div>
  <div class="arrow">➔</div>
  <div class="box blue">
    <strong>做一個編輯器</strong><br>
    作者後來替 FinFlow 做了一個<br>
    內部用的網頁小工具<br>
    <i>三欄式：選卡、填表、即時預覽</i>
  </div>
</div>

- 這呼應第二部教的「內容發想指令」（頁 44～45），只是規模放大了
- 資料一旦獨立，<span class="highlight">工具就有東西可以工作</span>——這是拆分真正的紅利
- 沒拆之前也能請 AI 一次生一批，只是**生完難匯入、難檢查、難換掉**

---

<!-- 第 132 頁 -->
# 但是：做了，不等於做完了

<div class="lead">那個卡片編輯器，實際查證後發現好幾類卡片它根本編不完整。</div>

<div class="grid">
  <div class="box red">
    <strong>查出來的限制</strong><br>
    有一包卡片沒出現在選單裡<br>
    有個篩選器的條件寫錯，選了會是空的<br>
    最重要的欄位（教育意義、效果、二選一選項）<br>
    表單上根本沒有<br>
    <i>所以人生事件卡實質上編不了</i>
  </div>
  <div class="arrow">➔</div>
  <div class="box blue">
    <strong>怎麼發現的</strong><br>
    不是用起來覺得怪<br>
    是<b>回頭做了一次現況盤點</b><br>
    <i>把文件說的跟程式實際有的對一次</i>
  </div>
</div>

- 重構完成之後，它自己也要疊代——<span class="highlight">你在第三部學的那一整套，在這裡照樣適用</span>
- 這兩個方向是「畢業後的選修課」，不是本書的作業。想做，它們就是你的下一個專案

---

<!-- 第 133 頁 -->
# 最後補三個新手常見疑問

<div class="lead">一路做到這裡，心裡如果還留著這三個擔心，最後一次把答案講清楚。</div>

<div class="grid">
  <div class="box">
    <strong>Q：我英文很爛</strong><br>
    全程用中文跟 AI 講就好<br>
    程式裡的英文你不用看懂<br>
    <i>本書所有提示詞都是中文</i>
  </div>
  <div class="box blue">
    <strong>Q：程式錯了我看不懂</strong><br>
    你本來就不用看懂<br>
    把畫面截圖丟回去<br>
    <i>用頁 118 的三句話公式</i>
  </div>
  <div class="box red">
    <strong>Q：我對 3C 沒概念</strong><br>
    你需要的是「會用瀏覽器」<br>
    加上「說得清楚自己要什麼」<br>
    <i>後面那個比前面重要</i>
  </div>
</div>

- 三個答案的共同點：<span class="highlight">你不需要先會寫程式</span>。需要的是基本操作，加上把想法與錯誤現象講清楚的耐心

---

<!-- 第 134 頁 -->
# 你已經是個造物者了

<div class="lead">你不需要會寫程式。你需要的是有想法、願意動手、願意來回修正。</div>

<div class="grid">
  <div class="box">
    <strong>你證明的事</strong><br>
    第一輪 MVP 完整走完<br>
    <i>想法 → 規格書 → 實作</i><br>
    <i>→ 測試 → 上線</i>
  </div>
  <div class="arrow">➔</div>
  <div class="box blue">
    <strong>你學會的角色</strong><br>
    你是決策者與品管<br>
    <i>AI 是工程師</i>
  </div>
  <div class="arrow">➔</div>
  <div class="box red">
    <strong>接下來</strong><br>
    把這次當起點<br>
    <i>不是特例</i>
  </div>
</div>

- 這本書的案例到現在跑了 74 次疊代，而且還在跑；你完成的是第 1 次。**底層流程相通**——差別在專案長大之後，會再長出新的驗證與分工（第六條心法就是第 26 批才學會的）
- 下一個想做的東西是什麼？<span class="highlight">現在你知道第一步該做什麼了：寫下三條鐵律。</span>
- **後面還有三部，不是附錄**：<b>第六部</b>（頁 135–144）教你在專案變大、AI 開始「看起來對」的時候，怎麼讓幾個 AI 互相抓錯；<b>第七部</b>把整套流程收成一張全景圖；<b>第八部</b>是那張圖的證據——同一套流程，被拿來審這本書自己
- 如果那個東西<b>不是遊戲</b>——第七部最後有一張對照表，把全景圖的每一格換成別的領域，一格都不用改
