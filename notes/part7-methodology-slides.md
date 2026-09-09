---
marp: true
theme: finflow-clean
paginate: true
header: "FinFlow 實戰心法 | 第七部・方法論"
---

<!-- 七-1 -->
<!-- _class: dense -->
# 全景圖：這門課教的其實是一套流程

<div class="lead">上排是「一個東西怎麼走完」，中框是「每一步內部怎麼跟 AI 來回」，下排是從頭到尾都在的三件事。</div>

<div style="width:100%">
<svg viewBox="0 0 1240 600" xmlns="http://www.w3.org/2000/svg" font-family="'Noto Sans TC','PingFang TC','Microsoft JhengHei',sans-serif">
  <defs>
    <marker id="ah" markerWidth="9" markerHeight="9" refX="7" refY="3.2" orient="auto"><path d="M0,0 L7,3.2 L0,6.4 z" fill="#64748b"/></marker>
    <marker id="ahb" markerWidth="9" markerHeight="9" refX="7" refY="3.2" orient="auto"><path d="M0,0 L7,3.2 L0,6.4 z" fill="#1d4ed8"/></marker>
    <marker id="ahr" markerWidth="9" markerHeight="9" refX="7" refY="3.2" orient="auto"><path d="M0,0 L7,3.2 L0,6.4 z" fill="#b91c1c"/></marker>
    <marker id="aho" markerWidth="9" markerHeight="9" refX="7" refY="3.2" orient="auto"><path d="M0,0 L7,3.2 L0,6.4 z" fill="#b45309"/></marker>
  </defs>

  <!-- BAND A -->
  <rect x="20" y="8" width="136" height="22" rx="11" fill="#0f172a"/>
  <text x="88" y="23.5" font-size="14" fill="#f8fafc" text-anchor="middle" font-weight="700">專案層・一個東西</text>

  <rect x="20"  y="44" width="175" height="82" rx="9" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
  <text x="107" y="72"  font-size="17" text-anchor="middle" font-weight="700" fill="#111827">想法</text>
  <text x="107" y="92"  font-size="12" text-anchor="middle" fill="#6b7280">經驗・借鏡經典</text>
  <text x="107" y="112" font-size="11.5" text-anchor="middle" fill="#94a3b8">NotebookLM</text>

  <rect x="218" y="44" width="240" height="82" rx="9" fill="#eff6ff" stroke="#93c5fd" stroke-width="1.5"/>
  <text x="338" y="72"  font-size="17" text-anchor="middle" font-weight="700" fill="#1d4ed8">規格書</text>
  <text x="338" y="92"  font-size="12" text-anchor="middle" fill="#6b7280">做什麼・不做什麼・怎麼算做好</text>
  <text x="338" y="112" font-size="11.5" text-anchor="middle" fill="#94a3b8">ChatGPT／Claude・Fable 5.1</text>

  <rect x="481" y="32" width="320" height="106" rx="11" fill="#f8fafc" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="5 4"/>
  <rect x="496" y="52" width="130" height="62" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
  <text x="561" y="80"  font-size="17" text-anchor="middle" font-weight="700" fill="#111827">執行</text>
  <text x="561" y="99"  font-size="11.5" text-anchor="middle" fill="#94a3b8">Sonnet</text>
  <rect x="656" y="52" width="130" height="62" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
  <text x="721" y="80"  font-size="17" text-anchor="middle" font-weight="700" fill="#111827">優化</text>
  <text x="721" y="99"  font-size="11.5" text-anchor="middle" fill="#94a3b8">Sonnet</text>
  <path d="M628,68 Q641,58 654,68" fill="none" stroke="#1d4ed8" stroke-width="1.8" marker-end="url(#ahb)"/>
  <path d="M654,98 Q641,108 628,98" fill="none" stroke="#1d4ed8" stroke-width="1.8" marker-end="url(#ahb)"/>
  <text x="641" y="131" font-size="12.5" text-anchor="middle" fill="#1d4ed8" font-weight="700">疊代・每版存 GitHub</text>

  <rect x="824" y="44" width="185" height="82" rx="9" fill="#fef2f2" stroke="#fca5a5" stroke-width="1.5"/>
  <text x="916" y="72"  font-size="17" text-anchor="middle" font-weight="700" fill="#b91c1c">交叉抓錯</text>
  <text x="916" y="92"  font-size="12" text-anchor="middle" fill="#6b7280">讓 AI 互相打臉</text>
  <text x="916" y="112" font-size="11.5" text-anchor="middle" fill="#94a3b8">ChatGPT・Gemini・Claude</text>

  <rect x="1032" y="44" width="185" height="82" rx="9" fill="#0f172a"/>
  <text x="1124" y="72" font-size="17" text-anchor="middle" font-weight="700" fill="#f8fafc">成品・上線</text>
  <text x="1124" y="92" font-size="12" text-anchor="middle" fill="#94a3b8">別人打得開</text>
  <text x="1124" y="112" font-size="11.5" text-anchor="middle" fill="#64748b">GitHub Pages</text>

  <g stroke="#64748b" stroke-width="1.8" marker-end="url(#ah)" fill="none">
    <path d="M197,85 L214,85"/><path d="M460,85 L477,85"/><path d="M803,85 L820,85"/><path d="M1011,85 L1028,85"/>
  </g>

  <!-- BRANCH -->
  <rect x="481" y="162" width="320" height="76" rx="9" fill="#fff7ed" stroke="#f59e0b" stroke-width="2"/>
  <text x="641" y="188" font-size="15.5" text-anchor="middle" font-weight="700" fill="#b45309">卡住了？先問「專業團隊怎麼做」</text>
  <text x="641" y="208" font-size="12" text-anchor="middle" fill="#92400e">人類九階段 ➜ 翻成 AI 分工：憲法／角色卡／任務單</text>
  <text x="641" y="227" font-size="11.5" text-anchor="middle" fill="#b45309">Claude Code subagent</text>
  <path d="M545,140 L545,158" stroke="#b45309" stroke-width="1.8" stroke-dasharray="5 3" marker-end="url(#aho)" fill="none"/>
  <text x="504" y="154" font-size="11.5" fill="#b45309" text-anchor="middle">轉不動</text>
  <path d="M740,158 L740,140" stroke="#b45309" stroke-width="1.8" stroke-dasharray="5 3" marker-end="url(#aho)" fill="none"/>
  <text x="794" y="154" font-size="11.5" fill="#b45309" text-anchor="middle">帶答案回來</text>

  <g stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="3 5">
    <path d="M338,128 L338,254"/><path d="M916,128 L916,254"/><path d="M641,240 L641,254"/>
  </g>

  <!-- BAND B -->
  <rect x="20" y="254" width="1198" height="172" rx="12" fill="#fbfdff" stroke="#93c5fd" stroke-width="1.6" stroke-dasharray="7 5"/>
  <rect x="34" y="244" width="356" height="22" rx="11" fill="#1d4ed8"/>
  <text x="212" y="259.5" font-size="14" fill="#ffffff" text-anchor="middle" font-weight="700">對話層・上面每一格內部都跑這個迴圈（SODA）</text>

  <rect x="60"  y="292" width="150" height="66" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.4"/>
  <text x="135" y="318" font-size="15" text-anchor="middle" font-weight="700" fill="#111827">給現況＋白話說</text>
  <text x="135" y="340" font-size="12" text-anchor="middle" fill="#6b7280">S・See</text>
  <rect x="240" y="292" width="150" height="66" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.4"/>
  <text x="315" y="318" font-size="15" text-anchor="middle" font-weight="700" fill="#111827">改寫成專業 prompt</text>
  <text x="315" y="340" font-size="12" text-anchor="middle" fill="#6b7280">AI 1</text>
  <rect x="420" y="292" width="150" height="66" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.4"/>
  <text x="495" y="318" font-size="15" text-anchor="middle" font-weight="700" fill="#111827">產出結果＋選項</text>
  <text x="495" y="340" font-size="12" text-anchor="middle" fill="#6b7280">O・Options</text>
  <rect x="600" y="292" width="170" height="66" rx="8" fill="#fef2f2" stroke="#fca5a5" stroke-width="1.4"/>
  <text x="685" y="318" font-size="15" text-anchor="middle" font-weight="700" fill="#b91c1c">兩個 AI 各自盲審</text>
  <text x="685" y="340" font-size="12" text-anchor="middle" fill="#6b7280">不給看彼此・要附證據</text>
  <rect x="800" y="286" width="170" height="78" rx="8" fill="#fff7ed" stroke="#f59e0b" stroke-width="2.2"/>
  <text x="885" y="314" font-size="16" text-anchor="middle" font-weight="700" fill="#b45309">你拍板・定共識</text>
  <text x="885" y="335" font-size="12" text-anchor="middle" fill="#92400e">D・Decide</text>
  <text x="885" y="353" font-size="11.5" text-anchor="middle" fill="#92400e">這一格不是 AI，是人</text>
  <rect x="1000" y="292" width="160" height="66" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.4"/>
  <text x="1080" y="318" font-size="15" text-anchor="middle" font-weight="700" fill="#111827">才動手執行</text>
  <text x="1080" y="340" font-size="12" text-anchor="middle" fill="#6b7280">A・Act</text>

  <g stroke="#64748b" stroke-width="1.7" marker-end="url(#ah)" fill="none">
    <path d="M212,325 L236,325"/><path d="M392,325 L416,325"/><path d="M572,325 L596,325"/>
    <path d="M772,325 L796,325"/><path d="M972,325 L996,325"/>
  </g>
  <path d="M885,366 Q885,404 690,404 Q495,404 495,362" fill="none" stroke="#b91c1c" stroke-width="1.8" stroke-dasharray="6 4" marker-end="url(#ahr)"/>
  <rect x="596" y="390" width="196" height="24" rx="12" fill="#fef2f2" stroke="#fca5a5" stroke-width="1.2"/>
  <text x="694" y="406.5" font-size="12.5" text-anchor="middle" fill="#b91c1c" font-weight="700">停損：最多兩輪，沒共識你裁</text>

  <!-- BAND C -->
  <rect x="20" y="442" width="152" height="22" rx="11" fill="#374151"/>
  <text x="96" y="457.5" font-size="14" fill="#f8fafc" text-anchor="middle" font-weight="700">貫穿層・從頭到尾</text>

  <rect x="20"  y="474" width="390" height="98" rx="10" fill="#fff7ed" stroke="#fdba74" stroke-width="1.6"/>
  <text x="215" y="500" font-size="16" text-anchor="middle" font-weight="700" fill="#b45309">人的三件事</text>
  <text x="215" y="524" font-size="13.5" text-anchor="middle" fill="#7c2d12">定範圍　·　裁分歧　·　決定動手</text>
  <text x="215" y="548" font-size="12.5" text-anchor="middle" fill="#9a3412">不寫程式，但這三件不能外包</text>

  <rect x="434" y="474" width="370" height="98" rx="10" fill="#eff6ff" stroke="#93c5fd" stroke-width="1.6"/>
  <text x="619" y="500" font-size="16" text-anchor="middle" font-weight="700" fill="#1d4ed8">工作台</text>
  <text x="619" y="524" font-size="13" text-anchor="middle" fill="#1e3a8a">ChatGPT・Gemini・Claude ＋ VS Code</text>
  <text x="619" y="548" font-size="12.5" text-anchor="middle" fill="#3730a3">Git／GitHub：看差異・存檔點・降落傘・發佈</text>

  <rect x="828" y="474" width="390" height="98" rx="10" fill="#f0fdf4" stroke="#86efac" stroke-width="1.6"/>
  <text x="1023" y="500" font-size="16" text-anchor="middle" font-weight="700" fill="#166534">四道品質閘門</text>
  <text x="1023" y="524" font-size="13.5" text-anchor="middle" fill="#14532d">回歸測試綠　·　變更說明　·　改前備份</text>
  <text x="1023" y="548" font-size="12.5" text-anchor="middle" fill="#166534">＋落地驗證：不信文件，查產物</text>

  <text x="20" y="592" font-size="12" fill="#9ca3af">工具名為 2026 年 9 月的現況。AI 日新月異，名字一定會換——但每一格需要的「角色」不會換。看角色，不要背工具。</text>
</svg>
</div>

---

<!-- 七-2 -->
# 對話層：一次來回怎麼跑

<div class="lead">「謀定而後動。」——先把要做什麼談清楚，再讓 AI 動手。</div>

| 步 | 你做的事 | 最容易省略的那一句 |
| :--- | :--- | :--- |
| **S・See** | 把現況丟給它：一張圖、一份規格、一段程式 | 不給現況就問，它只能憑空編 |
| **O・Options** | 要它給**幾個**方向，不要只給一個答案 | 「給我三個做法和各自的代價」 |
| **－盲審** | 另外兩個 AI 各自檢查，<b>不給看彼此的結果</b> | 「每個問題附第三者能照做的重現步驟」 |
| **D・Decide** | <span class="highlight">你拍板</span>。這一格不是 AI，是人 | 停損：最多兩輪，沒共識由你裁 |
| **A・Act** | 定案之後才動手，做完寫回規格書 | 沒定案就動手＝白做一輪 |

- 中間那條「盲審」是原本 SODA 沒有的，是踩過坑之後補上去的——<span class="highlight">同一個 AI 檢查不出自己的盲點</span>

---

<!-- 七-3 -->
# 專案層：一個東西怎麼走完

<div class="lead">五格走完就是一個成品。每一格的「離場條件」都很具體。</div>

| 格 | 這一格在問什麼 | 什麼時候算過關 |
| :--- | :--- | :--- |
| **想法** | 誰的什麼痛點？有沒有現成的可以借鏡？ | 講得出一句話賣點 |
| **規格書** | 做什麼、**不做**什麼、怎麼算做好 | 一頁講得完，而且**別人看得懂** |
| **執行 ⇄ 優化** | 這一輪只改一件事 | 跑得起來，測試綠，寫了變更說明 |
| **交叉抓錯** | 有沒有人**獨立**驗過？ | 兩個 AI 各自查過，分歧你裁完 |
| **成品・上線** | 別人打不打得開？ | 給一個沒看過的人，他自己會用 |

- 大專案會把「規格書」再拆成規格書（做什麼）與工程書（怎麼做、怎麼驗）；<span class="highlight">你的第一個作品，一份就夠</span>

---

<!-- 七-4 -->
# 兩層的關係：一以貫之

<div class="lead">上排每一格的內部，跑的都是同一個六步迴圈。這是整張圖唯一要記住的事。</div>

<div class="grid">
  <div class="box blue">
    <strong>寫規格書那一格</strong><br>
    給它你的筆記 ➔ 要三個版本<br>
    ➔ 另一個 AI 挑漏洞<br>
    ➔ <b>你選一版</b> ➔ 定稿
  </div>
  <div class="box">
    <strong>修一個 bug 那一格</strong><br>
    給它畫面截圖 ➔ 要三種可能原因<br>
    ➔ 另一個 AI 覆驗<br>
    ➔ <b>你決定改哪個</b> ➔ 改
  </div>
  <div class="box red">
    <strong>調一個數字那一格</strong><br>
    給它現在的數值 ➔ 要三組方案<br>
    ➔ 跑模擬驗<br>
    ➔ <b>你看手感決定</b> ➔ 套用
  </div>
</div>

- 所以你只要練熟**一個**迴圈，就能用在流程的**每一格**——這是它為什麼能搬到別的領域

---

<!-- 七-5 -->
<!-- _class: dense -->
# 卡住時的岔路：他山之石

<div class="lead">「他山之石，可以攻玉。」——《詩經・小雅》。這招是做到第 26 批（S26）才學會的。</div>

<div class="grid">
  <div class="box red">
    <strong>症狀（S26 之後）</strong><br>
    規矩每次都要重講一遍<br>
    「做好了」沒有驗收標準<br>
    <b>AI 自己說自己測過了</b><br>
    企劃、實作、測試擠在同一個對話<br>
    修 A 順手動了 B
  </div>
  <div class="arrow">➔</div>
  <div class="box blue">
    <strong>那一句救命的話</strong><br>
    不是問「這個怎麼修」<br>
    是問<br>
    <b>「這件事，專業的團隊<br>是怎麼分工處理的？」</b>
  </div>
  <div class="arrow">➔</div>
  <div class="box">
    <strong>拿回來的答案</strong><br>
    人類遊戲團隊的九個階段<br>
    與九類角色分工<br>
    ➔ 翻成 AI 版：<br>
    <b>憲法／角色卡／任務單</b>
  </div>
</div>

- 這招不限做遊戲：寫報告卡住就問「研究機構怎麼分工」，辦活動卡住就問「專業公關怎麼跑流程」
- 第五部把它列為<b>第六條心法</b>——前五條讓你把事情做完，這一條讓你在做不下去時還走得下去

---

<!-- 七-6 -->
# 分工要落地，靠的是兩條硬規則

<div class="lead">角色卡寫得再漂亮，少了這兩條都會走回原形。</div>

<div class="grid">
  <div class="box blue">
    <strong>① 把「不做」寫進權限，不是寫進叮嚀</strong><br><br>
    寫在 prompt 裡的「請不要改程式」是<b>請求</b>——它會忘、會順手。<br><br>
    寫在工具白名單裡（不給它編輯權），它就<span class="highlight">真的改不了</span>。
  </div>
  <div class="box red">
    <strong>② 產出者與驗證者，永遠不是同一個</strong><br><br>
    球員不能兼裁判。<b>同一個對話</b>裡的 AI 看不到自己的盲點，因為它記得自己為什麼那樣寫。<br><br>
    開一個<b>乾淨的新對話</b>去驗，就是第六部「盲審」在專案尺度的版本。
  </div>
</div>

- 這兩條的共同點：<span class="highlight">不靠自覺，靠設計</span>——把紀律變成「想違反也違反不了」的結構

---

<!-- 七-7 -->
<!-- _class: dense -->
# 工具對照：作者當時實際在用的

<div class="lead">先看「角色」欄，再看工具欄。角色不會過期，工具一定會。</div>

| 流程位置 | 這一格需要什麼能力 | 作者當時用的（2026-09） |
| :--- | :--- | :--- |
| 想法・借鏡經典 | 能一次吃下大量長文件並問答 | **NotebookLM** |
| 規格書 | 對話順、能一直改 | **ChatGPT** ／ **Claude** |
| 規格書（大專案） | 長脈絡、能扛整個專案不失憶 | **Claude Fable 5.1**（高階模型） |
| 執行・優化 | 寫得快、改得快、便宜 | **Claude Sonnet** |
| 內容批量生成 | 照著範例產一整批卡片 | 任一 LLM ＋ 自檢指令 |
| 交叉抓錯 | **來源不同**的兩三個模型 | **ChatGPT・Gemini・Claude** |
| 專業分工 | 能開多個獨立角色、能限制權限 | **Claude Code**（subagent） |
| 工作台 | 看差異、即時預覽、內建終端機 | **VS Code** ＋ **Git／GitHub** |
| 發布 | 免費、有網址、別人打得開 | **GitHub Pages** |

- 查證日期 2026-09-08。<span class="highlight">AI 日新月異，這張表半年後一定有東西要換</span>——換的時候，對照左邊兩欄找替代品就好

---

<!-- 七-8 -->
# 搬到你的領域：換題目，不換流程

<div class="lead">同一張圖，把「做遊戲」換成「寫一份產業研究報告」。一格都不用改。</div>

| 流程位置 | 做一款遊戲 | 寫一份產業／公司研究報告 |
| :--- | :--- | :--- |
| **想法** | 財商桌遊，解決什麼痛點 | 為什麼看這個產業，論點是什麼 |
| **規格書** | 15 輪、6 職業、怎麼算贏 | 涵蓋範圍、**不談什麼**、交付格式與截止日 |
| **執行 ⇄ 優化** | 一輪改一個機制 | 一輪寫一節，寫完就查證，不囤到最後 |
| **卡住的岔路** | 問「遊戲團隊怎麼分工」 | 問「**研究機構怎麼分工**」：資料、產業、財務、審稿 |
| **交叉抓錯** | 三個 AI 互相打臉 | 一個 AI 挑數字、一個挑邏輯、**你裁決** |
| **四道閘門** | 回歸測試、變更說明、備份、**落地驗證** | **來源逐項回查**、改版記錄、原稿留底、查無要標 UNKNOWN |
| **成品・上線** | 別人打得開就能玩 | 別人照著讀，**推得出同一個結論** |

- 唯一真正換掉的是「怎麼算做好」那一欄。<span class="highlight">流程是通的，驗收標準是你的專業</span>
