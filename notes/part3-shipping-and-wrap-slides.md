---
marp: true
theme: finflow-clean
paginate: true
header: "FinFlow 實戰心法 | 第三部・收尾與本部小結"
---

<!-- 第 102 頁 -->
# Step6：什麼時候可以說「能分享了」？

<div class="lead">判斷標準不是「我做完了嗎」，是<b>「我可以離開房間了嗎」</b>。</div>

<div class="grid">
  <div class="box">
    <strong>① 鐵律都沒被違反</strong><br>
    那三條你一開始寫下的<br>
    <i>回頭對一次</i>
  </div>
  <div class="box blue">
    <strong>② 核心流程玩得通</strong><br>
    從開始到結束跑一遍<br>
    <i>中間不會卡死</i>
  </div>
  <div class="box red">
    <strong>③ 陌生人自己玩得動</strong><br>
    你不用坐在旁邊解釋<br>
    <i>這條最難，也最重要</i>
  </div>
</div>

- 第 ③ 條是唯一的真考驗：<span class="highlight">如果每次都要你在旁邊講，那說明書就是你本人</span>
- 三條同時成立，才叫「能分享」。不是三缺一，是三缺零

---

<!-- 第 103 頁 -->
# 案例：最後那四期，一個新功能都沒做

<div class="lead">S17 到 S20 做的全是「讓別人能自己上手」的收尾工程。</div>

| 期別 | 做了什麼 | 為了解決 |
| :--- | :--- | :--- |
| S17 | 主畫面三欄重整 | 操作區要捲才按得到；四人的卡片排成 3＋1 很醜 |
| S18 | 通知分類 | 訊息太吵，重要的被淹沒 |
| S19 | 三人實測，修五個 bug | 自己測不出來的那些 |
| S20 | 互動教學 | 新玩家不用問人就會玩 |

- 這四期的共同點：<span class="highlight">功能一個都沒加，但產品從「我能玩」變成「別人能玩」</span>
- 沒有這四期，前面十幾期做的東西沒有人拿得起來用

---

<!-- 第 104 頁 -->
# 收尾階段，要換一顆腦袋

<div class="lead">「知識的詛咒」：你一旦懂了，就再也想不起來不懂是什麼感覺。</div>

<div class="grid">
  <div class="box">
    <strong>開發階段你在問</strong><br>
    「這個功能<br>做不做得出來？」<br>
    <i>看的是可行性</i>
  </div>
  <div class="arrow">➔</div>
  <div class="box red">
    <strong>收尾階段要問</strong><br>
    「一個完全不懂的人<br>能不能自己搞懂？」<br>
    <i>看的是別人的視角</i>
  </div>
</div>

- 這兩個問題會給你**完全相反的待辦清單**，所以不能同時做
- 實務上最有效的解法很簡單：**找一個真的不懂的人來玩，然後閉嘴看他操作**

---

<!-- 第 105 頁 -->
# 一張圖：整個第三部在講什麼

<div class="lead">從鐵律開始，繞一圈回到鐵律。</div>

| | 步驟 | 對應的坑 |
| :--- | :--- | :--- |
| **起點** | Step0 寫鐵律與 MVP 清單 | 一開始就想做完整版 |
| ① | Step1 先要規格書，你審核 | 直接要程式，錯了才發現 |
| ② | Step2 拿到程式先玩過 | 沒玩就說完成 |
| ③ | Step3 小步快跑疊代 | 一次做太多，壞了找不到 |
| ④ | Step4 找人測試 | 你測不出自己的 bug |
| ⑤ | Step5（選修）多人連線 | 不需要卻做了 |
| ⑥ | Step6 判斷能不能分享 | 自己覺得好就上線 |

- 走到 ⑥ 之後不是結束，是<span class="highlight">帶著新的想法回到 Step0，開始下一輪</span>

---

<!-- 第 106 頁 -->
# 三個最常被問的問題

<div class="lead">先回答，免得你卡在這裡不敢動手。</div>

<div class="grid">
  <div class="box">
    <strong>Q：一定要照順序走完六步？</strong><br>
    不用。Step5 本來就是選修，<br>
    Step4 找不到人可以先跳過<br>
    <i>但 Step1 和 Step2 不要跳</i>
  </div>
  <div class="box blue">
    <strong>Q：卡在某一步很久怎麼辦？</strong><br>
    把那一步再切小一點<br>
    <i>卡住通常是因為那一步太大</i>
  </div>
  <div class="box red">
    <strong>Q：找不到人幫忙測試？</strong><br>
    家人朋友就可以<br>
    重點不是他懂不懂，<br>
    <i>是他沒看過你怎麼做的</i>
  </div>
</div>

- 補充一句：<span class="highlight">Step1 跳過的代價最大</span>——沒有規格書，你就沒有審核點，只能等程式出來才發現方向錯

---

<!-- 第 107 頁 -->
# 走完這一部，你手上會有這些東西

<div class="lead">對照一下。缺哪一項，回頭補。</div>

- ☐ **一份鐵律**：三條，寫在紙上或檔案裡都行
- ☐ **至少一份規格書**：AI 生的，你逐項看過並改過
- ☐ **一串變更說明**：每次交付一份，含「未預期發現」
- ☐ **一份測試心得**：別人玩過之後你記下來的
- ☐ **一個真的能跑的東西**：不是投影片，是可以打開來玩的

- 前四項是過程，第五項是結果。<span class="highlight">但真正讓你能做出第五項的，是前四項</span>

---

<!-- 第 108 頁 -->
# 本部小結

<div class="lead">疊代不是把事情做對一次，是<b>每次都比上一次好一點</b>。</div>

<div class="grid">
  <div class="box">
    <strong>你學到的</strong><br>
    六個步驟、四個坑、<br>
    七條品管習慣<br>
    <i>沒有一條需要你會寫程式</i>
  </div>
  <div class="arrow">➔</div>
  <div class="box blue">
    <strong>接下來</strong><br>
    第四部：<br>
    <b>換你做一個</b><br>
    <i>規格已經幫你定好了</i>
  </div>
</div>

- 前面所有案例都是別人的專案。**下一部開始，做的是你自己的**
