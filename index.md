---
layout: default
---

<style>
.nav-note{background:#eff6ff;border-left:4px solid #1d4ed8;padding:12px 18px;border-radius:0 8px 8px 0;margin:24px 0}
.start-row{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:14px;margin:22px 0 34px}
.start-card{display:block;background:#0f172a;color:#f8fafc!important;border-radius:10px;padding:16px 18px;text-decoration:none!important;transition:transform .12s}
.start-card:hover{transform:translateY(-2px)}
.start-card b{display:block;font-size:1.05rem;margin-bottom:4px}
.start-card span{font-size:.86rem;color:#94a3b8;line-height:1.5}
.deck-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:16px;margin:18px 0 34px}
.deck-card{border:1px solid #e5e7eb;border-radius:10px;padding:16px 18px;background:#fff}
.deck-card h3{margin:0 0 4px;font-size:1.02rem;border:none;padding:0}
.deck-card .sub{font-size:.8rem;color:#6b7280;margin:0 0 10px}
.deck-card ul{margin:0;padding-left:18px}
.deck-card li{margin:5px 0;font-size:.92rem;line-height:1.5}
.deck-card .pg{color:#9ca3af;font-size:.8rem}
.badge{display:inline-block;font-size:.72rem;padding:1px 8px;border-radius:999px;background:#dcfce7;color:#166534;margin-left:6px;vertical-align:middle}
.badge.extra{background:#f3f4f6;color:#6b7280}
@media (prefers-color-scheme:dark){
  .deck-card{background:#111827;border-color:#374151}
  .nav-note{background:#1e293b}
}
</style>

# 我不會寫程式，但我用 AI 做出了一套多人連線遊戲

這是本書／課程的線上版。所有範例指令與 prompt 都可以直接複製貼上；內容修訂後會直接更新在這裡，不用重新拿書。

<div class="nav-note">
<b>怎麼看：</b>下面每一張卡片是一個部，點標題進去就是投影片本身，用鍵盤 <b>← →</b> 翻頁，手機也能看。想存 PDF：瀏覽器「列印 → 另存為 PDF」。
</div>

## 從這裡開始

<div class="start-row">
  <a class="start-card" href="slides/panorama-slides.html"><b>先看地圖：全景流程圖</b><span>1 頁　一張圖看完這門課教的整套方法</span></a>
  <a class="start-card" href="slides/preface-slides.html"><b>序：起心動念</b><span>5 頁　為什麼一個不會寫程式的人要做這件事</span></a>
  <a class="start-card" href="slides/part0-shock-slides.html"><b>第零部：震撼彈</b><span>8 頁　這不是玩具，是真正能跑的軟體</span></a>
  <a class="start-card" href="slides/testimonials-slides.html"><b>見證：玩過的人怎麼說</b><span>4 頁　真實回饋與示範情境，標示清楚</span></a>
</div>

## 課程七部

<div class="deck-grid">

<div class="deck-card">
  <h3>第一部・心法</h3>
  <p class="sub">想法怎麼來，以及不准 AI 妥協的鐵律</p>
  <ul>
    <li><a href="slides/part1-mindset-slides.html">開發模式的典範轉移、靈感來源與鐵律</a> <span class="pg">頁 11–22</span></li>
    <li><a href="slides/part1-card-growth-slides.html">深度案例：一張卡片怎麼一層層長大</a> <span class="pg">頁 23–31</span></li>
  </ul>
</div>

<div class="deck-card">
  <h3>第二部・工具</h3>
  <p class="sub">地基與跟 AI 合作的方法</p>
  <ul>
    <li><a href="slides/part2-ai-partners-slides.html">認識你的 AI 夥伴：三選一就好</a> <span class="pg">頁 32–39</span></li>
    <li><a href="slides/part2-habits-and-prompts-slides.html">四個協作習慣與內容發想指令</a> <span class="pg">頁 40–46</span></li>
    <li><a href="slides/part2-git-and-techstack-slides.html">GitHub、Firebase 與單檔架構</a> <span class="pg">頁 47–53</span></li>
    <li><a href="slides/part2-advanced-tactics-slides.html">模型分工與截圖除錯</a> <span class="pg">頁 54–58</span></li>
    <li><a href="slides/part2-vscode-option-slides.html">同一件事的三種做法：命令列、VS Code、瀏覽器</a> <span class="badge extra">補充</span></li>
    <li><a href="slides/part2-ai-scope-control.html">AI 協作邊界管理：要五毛給一塊的雙面刃</a> <span class="badge extra">專題</span></li>
  </ul>
</div>

<div class="deck-card">
  <h3>第三部・實作</h3>
  <p class="sub">手把手做出第一版，含真實踩坑</p>
  <ul>
    <li><a href="slides/part3-five-days-sprint-slides.html">5 天衝刺與核心機制落地</a> <span class="pg">頁 59–66</span></li>
    <li><a href="slides/part3-debugging-and-balance-slides.html">真實踩坑排查與千局平衡實測</a> <span class="pg">頁 67–72</span></li>
    <li><a href="slides/part3-iteration-and-ui-slides.html">疊代節奏與 UI 演進：冰山水面下的 90%</a> <span class="pg">頁 73–85</span></li>
    <li><a href="slides/part3-testing-and-multiplayer-slides.html">找人測試與多人連線的決策</a> <span class="pg">頁 86–92</span></li>
    <li><a href="slides/part3-pitfalls-and-qa-slides.html">四個常見坑與你的品管習慣清單</a> <span class="pg">頁 93–101</span></li>
    <li><a href="slides/part3-shipping-and-wrap-slides.html">收尾：什麼時候能說「能分享了」</a> <span class="pg">頁 102–108</span></li>
    <li><a href="slides/part3-dara-case-study.html">DARA 數據治理實例</a> <span class="badge extra">專題</span></li>
  </ul>
</div>

<div class="deck-card">
  <h3>第四部・讀者實作題</h3>
  <p class="sub">照著做，交出你自己的極簡版</p>
  <ul>
    <li><a href="slides/part4-spec-and-prompts-slides.html">定案規格與 Step1 提示詞</a> <span class="pg">頁 109–116</span></li>
    <li><a href="slides/part4-build-and-ship-slides.html">做出來、測過、上架：四份可複製的提示詞</a> <span class="pg">頁 117–124</span></li>
  </ul>
</div>

<div class="deck-card">
  <h3>第五部・結語</h3>
  <p class="sub">帶得走的心法與資源包</p>
  <ul>
    <li><a href="slides/part5-closing-slides.html">五個心法（＋第六條）、兩個進階方向、你已經是造物者</a> <span class="pg">頁 125–134</span></li>
  </ul>
</div>

<div class="deck-card">
  <h3>第六部・讓 AI 互相抓錯</h3>
  <p class="sub">不看程式碼，也能當品管</p>
  <ul>
    <li><a href="slides/part6-ai-cross-review-slides.html">交叉審查與實證裁決</a> <span class="pg">10 頁</span></li>
  </ul>
</div>

<div class="deck-card">
  <h3>第七部・方法論</h3>
  <p class="sub">把這套流程搬到你自己的領域</p>
  <ul>
    <li><a href="slides/part7-methodology-slides.html">全景圖、兩層迴圈、卡住時怎麼辦、工具對照</a> <span class="pg">8 頁</span></li>
  </ul>
</div>

</div>

## 實作章節（圖文版，適合照著操作）

投影片適合聽，圖文版適合一邊看一邊動手。內容相同，形式不同。

- [把你的作品放上網：GitHub 三步驟實戰](chapters/github-tutorial.html) —— 建立 Repository → 用指令推上去 → 開 GitHub Pages（全程實機截圖）
- [同一件事的三種做法：命令提示字元、VS Code、瀏覽器裡的 VS Code](chapters/vscode-option.html) —— add／commit／push 三步換成三個按鈕
- [讓 AI 互相抓錯：交叉審查與實證裁決](chapters/ai-cross-review.html) —— 你不用看得懂程式，也能讓三個 AI 互相抓錯
- [序](chapters/preface.html)　·　[見證](chapters/testimonials.html)

## 幾個閱讀慣例

- 灰底的方塊是可以直接複製的指令或 prompt。
- 截圖上的紅框與編號，對應文字裡的步驟。
- 看到「⚠️」代表新手最常卡住的地方，先讀再動手。
- 投影片頁面用左右鍵翻頁；想存成 PDF，用瀏覽器的「列印 → 另存為 PDF」。

---

主體 134 頁到齊，序（5 頁）、見證（4 頁）、全景圖與第七部方法論（8 頁）已補上。線上版最後更新：2026-09-08
