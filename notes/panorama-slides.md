---
marp: true
theme: finflow-clean
paginate: false
header: "FinFlow 實戰心法 | 先看地圖"
---

<!-- _class: dense -->
# 先看地圖：這門課的全景

<div class="lead">不會寫程式的人怎麼做出一個東西？答案不是某個工具，是這張流程。第七部會把每一格拆開講。</div>

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
