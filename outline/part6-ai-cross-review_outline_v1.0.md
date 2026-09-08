# 第六部（獨立章節）・讓 AI 互相抓錯：交叉審查與實證裁決（12 頁）

> 狀態：獨立最後章節 v1.0（2026-09-08），先不併入 134 頁主骨架，待 Brian 整理時再 merge。
> 定位：接在第五部結語之前或之後皆可；內容自足，不依賴前面章節。
> TA：程式小白。全章不出現程式碼；所有數字與案例都有 FinFlow 專案文件出處（S42／S43 變更說明、Gemini 對齊書、ChatGPT 對齊書）。

## 一句話
你不需要看得懂程式，也能讓三個 AI 互相抓錯——但真正讓錯誤現形的不是「投票」，是「拿出可重現的證據」。

## 頁面骨架

135. **開場：一個真實的下午**——三個 AI、五個 bug、四段錯的修改碼（案例：Gemini 除錯報告 → Claude 覆驗，2026-09-05）
136. **AI 會錯在哪**——不是不會寫，是「看起來對」：五個 bug 三真一半真一個機制寫錯；五段修法四段不能照抄（含一段會把房貸邏輯整個改壞）
137. **這件事有名字**——獨立驗證與確認（IV&V）、四眼原則、Fagan 審查、N 版本程式設計、多智能體辯論：你做的是它們的組合
138. **為什麼多一雙眼睛有用**——孔多塞陪審團定理（1785）：評審獨立且各自正確率過半，多數決越多人越準
139. **但有一個坑**——Knight & Leveson（1986）：獨立團隊寫的程式，錯在同一個地方的機率遠高於預期；三個 AI 訓練資料重疊更嚴重。「三個 AI 都同意」不是證據
140. **第二個坑：AI 會順著你**——趨同偏誤（sycophancy，Sharma 等 2023）：問「你同不同意」，AI 傾向同意；問「請找出他的錯」才有用（案例：Gemini 對齊書開頭整段稱讚）
141. **真正有效的那一步：實跑**——發現率 vs 準確率：多方審查提升發現率，實證裁決提升準確率；缺一個就變成假警報或集體錯誤（案例：Claude 用 Brian 電腦實跑 24,000 局才判定 Gemini 哪段錯）
142. **AI 也會糾正 AI**——ChatGPT 四個 bug 全真，而且糾正 Claude 兩次（範圍 7 個→15 個；單機存檔其實是重放）；Claude 實跑後承認（案例：S43，2026-09-07）
143. **七步流程（可以直接抄）**——作者產出 → 盲審（不給彼此結果、每項附重現步驟）→ 實證裁決（逐條實跑，分真／半真／假）→ 反向質詢（問「找錯」不問「同意」）→ 停損（最多兩輪）→ 人的三件事（定範圍、裁分歧、決定動手）→ 動手門檻（共識＋可重現測試＋備份＋全套回歸綠）
144. **三種提示詞模板**——盲審用、裁決用、反向質詢用（全文，可複製）
145. **什麼時候值得用**——成本誠實講：S43 三個模型兩天，一個人半天；適合引擎、多人同步、金錢計算這種難回頭的改動，不適合每一行
146. **你的角色**——你不寫程式，但你做三件事；本章結語：品管不是看懂程式，是要求證據

## 圖表／視覺
- 135：三欄時間軸（Gemini 報告 → Claude 覆驗 → 對齊書），標日期
- 136：五個 bug 的判定表（真／半真／機制錯）＋「修法四段不能照抄」紅字
- 138–139：兩張對照圖——「獨立評審」的正確率曲線 vs「錯在同一處」的示意
- 141：發現率／準確率四象限
- 143：七步流程圖（箭頭），停損標紅
- 144：三張提示詞卡（可截圖）
- 145：成本對照表（人力／時間／適用改動類型）

## 案例出處（全部可在 FinFlow 專案文件查證）
- `FinFlow_S42前置_Gemini除錯報告驗證_2026-09-05.md`（Gemini 五項判定、四段修法問題、scratch 腳本不存在）
- `FinFlow_S42變更說明_非回合破產遞延與五項防禦_v2.50.0.md`（S42 修復、28 支測試）
- `FinFlow_S43變更說明_動作信封驗證_設定範圍_NPC決定論_v2.51.0.md`（ChatGPT 四項、兩點糾正、29 支測試、simtest 前後指紋）
- Gemini 對齊書《FinFlow_Gemini對齊Claude覆驗結論與S42修復工程建議_2026-09-06.md》、ChatGPT 對齊意見（2026-09-07 對話）

## 文獻（已查到出處，僅供確認，非文獻探討）
- Condorcet, *Essai sur l'application de l'analyse à la probabilité des décisions rendues à la pluralité des voix*, 1785
- Knight, J. C. & Leveson, N. G., "An experimental evaluation of the assumption of independence in multiversion programming," *IEEE Trans. Software Engineering* 12(1), 1986
- Fagan, M. E., "Design and code inspections to reduce errors in program development," *IBM Systems Journal* 15(3), 1976
- NASA Software Engineering Handbook, SWE-141 Software Independent Verification and Validation
- Irving, G., Christiano, P., Amodei, D., "AI safety via debate," arXiv:1805.00899, 2018
- Du, Y. et al., "Improving Factuality and Reasoning in Language Models through Multiagent Debate," arXiv:2305.14325, 2023（ICML 2024）
- Sharma, M. et al., "Towards Understanding Sycophancy in Language Models," arXiv:2310.13548, 2023

## 待確認（Brian）
- 章節編號：暫用 135–146，merge 時依主骨架重編
- 第 145 頁成本數字用「兩天／半天」是這次的實際經驗，若要更保守可改為「數倍」
