---
marp: true
theme: finflow-clean
paginate: true
header: "FinFlow 實戰心法 | 第五部・結語與資源包"
---

<!-- 第 125 頁 -->
# 五個心法，一張圖記完

<div class="lead">整本書講的東西，收斂成這五句。</div>

| | 心法 | 一句話 |
| :--- | :--- | :--- |
| ① | **鐵律先行** | 動手前先寫下不能讓步的三條 |
| ② | **MVP 優先** | 砍到剩骨架，先讓它跑起來 |
| ③ | **小步疊代** | 一次一個小主題，每次都驗收 |
| ④ | **找人測試** | 你測不出自己的 bug |
| ⑤ | **定期盤點** | 文件跟成品，定期對一次帳 |

- 五條裡面，<span class="highlight">沒有一條跟「會不會寫程式」有關</span>
- 它們也不只適用做遊戲——寫報告、辦活動、做任何專案都成立

---

<!-- 第 126 頁 -->
# 資源包：可以直接拿去用的東西

<div class="lead">全書出現過、你可以複製的模板都在這裡。</div>

<div class="grid">
  <div class="box">
    <strong>寫在動手前</strong><br>
    鐵律 worksheet（頁 115）<br>
    MVP 刀法清單（頁 14）
  </div>
  <div class="box blue">
    <strong>四份提示詞</strong><br>
    Step1 生規格書（頁 116）<br>
    Step2 生程式（頁 117）<br>
    Step3 抓 bug（頁 118）<br>
    Step4 加功能（頁 119）
  </div>
  <div class="box red">
    <strong>驗收用</strong><br>
    品管習慣七條（頁 101）<br>
    驗收清單五項（頁 120）<br>
    交叉審查三種提示詞（第六部）
  </div>
</div>

- 全部都是純文字，直接複製貼上就能用，不需要任何工具

---

<!-- 第 127 頁 -->
# 做完不是終點，是起點

<div class="lead">你已經跑完一圈完整的產品週期。接下來有兩條路可以走。</div>

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

- 接下來五頁**只講方向，不教步驟**——這是留給你的下一個學習計畫，不是本書的作業
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
- 拖住你的不是單檔本身，是**單檔長到某個大小之後**

---

<!-- 第 129 頁 -->
# 方向一，後來真的做了

<div class="lead">2026 年 9 月 1 日那次改動，把一整個大檔案拆開了。</div>

| 拆成 | 放什麼 |
| :--- | :--- |
| **引擎** | 遊戲規則怎麼算（不管畫面長怎樣） |
| **資料** | 所有卡片內容，一包一包的 JSON 檔 |
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

- FinFlow 跟方向一是**同一次改動一起做的**——它們本來就是同一件事的兩面
- 這也是第四部要你寫進鐵律的那一條：「卡片資料集中放一起，加卡片不用改邏輯」

---

<!-- 第 131 頁 -->
# 方向二的延伸：批量生成與專用工具

<div class="lead">資料獨立出來之後，才有可能一次生一批。</div>

<div class="grid">
  <div class="box">
    <strong>批量生成</strong><br>
    給 2-3 張範例卡<br>
    請 AI 抓規律生一整批<br>
    <i>再請它自己檢查一致性</i>
  </div>
  <div class="arrow">➔</div>
  <div class="box blue">
    <strong>做一個編輯器</strong><br>
    FinFlow 後來做了一個<br>
    視覺化的卡片編輯器<br>
    <i>三欄式：選卡、填表、即時預覽</i>
  </div>
</div>

- 這呼應第二部教的「內容發想指令」（頁 44-45），只是規模放大了
- 資料一旦獨立，<span class="highlight">工具就有東西可以工作</span>——這是拆分真正的紅利

---

<!-- 第 132 頁 -->
# 但是：做了，不等於做完了

<div class="lead">那個卡片編輯器，實際查證後發現有一半的卡片它編不了。</div>

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
# 新手最常問的三個問題

<div class="lead">先回答完，你就沒有不動手的理由了。</div>

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

- 三個答案的共同點：<span class="highlight">你缺的從來不是技術，是把想法講清楚的耐心</span>

---

<!-- 第 134 頁 -->
# 你已經是個造物者了

<div class="lead">你不需要會寫程式。你需要的是有想法、願意動手、願意來回修正。</div>

<div class="grid">
  <div class="box">
    <strong>你證明的事</strong><br>
    一個完整的產品週期<br>
    <i>想法 → 規格 → 實作</i><br>
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

- 這本書的案例到現在跑了 74 次疊代，而且還在跑；你跑了 1 次。**方法完全一樣，差別只在次數**
- 下一個想做的東西是什麼？<span class="highlight">現在你知道第一步該做什麼了：寫下三條鐵律。</span>
