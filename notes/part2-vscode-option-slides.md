---
marp: true
theme: default
paginate: true
header: "FinFlow 實戰心法 | 第二部補充・同一件事的三種做法"
style: |
  section {
    background: #ffffff;
    color: #111827;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang TC", sans-serif;
    padding: 50px 70px;
    font-size: 26px;
  }
  h1 {
    font-size: 2rem;
    color: #111827;
    border-bottom: 2px solid #e5e7eb;
    padding-bottom: 8px;
    margin-bottom: 16px;
  }
  .lead {
    font-size: 1.3rem;
    color: #1d4ed8;
    font-weight: 700;
    margin-bottom: 24px;
  }
  .highlight { color: #b91c1c; font-weight: bold; }
  .grid {
    display: flex;
    gap: 16px;
    margin: 24px 0;
    align-items: center;
  }
  .box {
    flex: 1;
    border: 2px solid #111827;
    padding: 16px;
    text-align: center;
    border-radius: 6px;
    background: #ffffff;
  }
  .box.blue { border-color: #1d4ed8; background: #eff6ff; }
  .box.red { border-color: #b91c1c; background: #fef2f2; }
  .arrow { font-size: 24px; font-weight: bold; color: #1d4ed8; }
  table { width: 100%; border-collapse: collapse; margin-top: 16px; font-size: 22px; }
  th { border-bottom: 2px solid #111827; text-align: left; padding: 10px; }
  td { border-bottom: 1px solid #e5e7eb; padding: 10px; }
---

<!-- S2-1 -->
# 你已經會的三步：命令提示字元版

<div class="lead">GitHub 章教的那三行，其實就是「挑檔案 → 存檔點 → 上傳」。</div>

<div class="grid">
  <div class="box">
    <strong>git add .</strong><br>
    把改過的檔案「挑」進這次存檔<br>
    <i>閉著眼睛全收</i>
  </div>
  <div class="arrow">➔</div>
  <div class="box">
    <strong>git commit -m "…"</strong><br>
    蓋一個存檔點，寫一句改了什麼<br>
    <i>只存在你的電腦</i>
  </div>
  <div class="arrow">➔</div>
  <div class="box blue">
    <strong>git push</strong><br>
    把存檔點上傳到 GitHub<br>
    <i>別人才看得到</i>
  </div>
</div>

- 這三步不會消失。接下來教的只是「同一件事，換一個介面」

---

<!-- S2-2 -->
# 同一件事，換一個介面：VS Code 的 Source Control

<div class="lead">三行指令 ＝ 三個按鈕。底下還是同一套 git，觀念不用重學。</div>

| 命令提示字元 | VS Code 左側 Source Control 面板 | 多了什麼 |
| :--- | :--- | :--- |
| `git add .` | 每個改過的檔旁邊按 **＋**（或 Changes 旁的 ＋ 全收） | **先看到改了哪些檔**，點一下看逐行紅綠對照 |
| `git commit -m "…"` | 上方框打一句話，按 **Commit** | 訊息框有提示，不會忘了寫 |
| `git push` | 按 **Sync Changes** | 順便先把 GitHub 上別人的改動拉下來 |

- <span class="highlight">改前先看差異</span>——這就是第六部「動手門檻」在日常裡的樣子

---

<!-- S2-3 -->
# 三種做法對照

<div class="lead">同一個 repo，三種介面，選你順手的。</div>

| | 命令提示字元 | 本機 VS Code | 瀏覽器 VS Code（github.dev） |
| :--- | :--- | :--- | :--- |
| 要安裝嗎 | Git | Git ＋ VS Code | **不用**，有瀏覽器就好 |
| 看得到逐行差異 | 要打 `git diff` | ✅ 點一下 | ✅ 點一下 |
| 能執行程式（build／測試） | ✅ | ✅（內建終端機） | ❌ 沒有終端機 |
| 預覽投影片（Marp） | ❌ | ✅ 裝擴充功能 | ✅ 網頁版擴充功能 |
| 匯出 pptx／pdf | 要跑 CLI | ✅ | ❌ 瀏覽器跑不了 |
| 適合 | 已經習慣指令的人 | 常改、想看差異、要匯出 | 只改文字、偶爾改、在平板上 |

- 查證日期 2026-09-08（GitHub Docs、Marp 官方討論區）；工具介面會變，以按鈕文字為準

---

<!-- S2-4 -->
# 瀏覽器版怎麼開：把 .com 改成 .dev

<div class="lead">不用安裝任何東西，手機平板也能改。</div>

<div class="grid">
  <div class="box">
    <strong>方法一：改網址</strong><br>
    github<b>.com</b>/你的帳號/repo<br>
    ↓<br>
    github<b>.dev</b>/你的帳號/repo
  </div>
  <div class="box blue">
    <strong>方法二：按一個鍵</strong><br>
    在 repo 頁面按鍵盤 <b>.</b><br>
    <i>（句點鍵）同一分頁開啟</i>
  </div>
  <div class="box red">
    <strong>三個限制</strong><br>
    沒有終端機、不能執行程式<br>
    只能用網頁版擴充功能<br>
    <b>沒 commit 前的修改只在瀏覽器裡</b>
  </div>
</div>

- 改完一定要 Commit ＋ Push；關掉分頁沒存，就沒了

---

<!-- S2-5 -->
# 本機版怎麼開：Open Folder，然後按 Trust

<div class="lead">第一次打開會看到藍色 Restricted Mode——這時 git 功能是關的。</div>

![w:520](../images/VSC-01-restricted-mode.png)

- File → Open Folder → 選 repo 資料夾 → 上方藍條 **Manage → Trust** → 左側第三個圖示就是 Source Control
- 截圖：Brian 電腦 2026-09-08

---

<!-- S2-6 -->
# 為什麼對這個課程特別有用

<div class="lead">三個實質好處，都跟「跟 AI 協作」直接相關。</div>

<div class="grid">
  <div class="box blue">
    <strong>改前先看差異</strong><br>
    AI 改了什麼，一行一行紅綠對照<br>
    <i>不接受沒看過的改動</i>
  </div>
  <div class="box">
    <strong>投影片即時預覽</strong><br>
    裝 Marp for VS Code<br>
    改一行馬上看到頁面<br>
    <i>本機版可直接匯出 pptx</i>
  </div>
  <div class="box red">
    <strong>AI 寫進來、你決定送不送</strong><br>
    AI 把檔案寫進資料夾<br>
    你在面板看到變更 → 打勾 → Sync<br>
    <i>不再需要 zip 來 zip 去</i>
  </div>
</div>

- 本課程 repo 的投影片全部是 Marp 格式，這個擴充功能等於「所見即所得」

---

<!-- S2-7 -->
# 踩坑提醒

<div class="lead">四個新手一定會遇到的狀況，先講。</div>

| 狀況 | 為什麼 | 怎麼辦 |
| :--- | :--- | :--- |
| Source Control 面板是空的、按鈕灰的 | Restricted Mode 下 git 關閉 | 上方藍條 Manage → Trust |
| github.dev 改完關分頁，東西不見 | 未 commit 的修改只存在瀏覽器 | 改完立刻 Commit ＋ Push |
| 按 Sync 跳出「合併」或衝突 | Sync ＝ 先 pull 再 push，遠端有人改過 | 一個人用的 repo 不會遇到；遇到就問 AI 怎麼解 |
| 第一次 Push 跳出登入視窗 | 跟 GitHub 章第一次 push 一樣 | 登入 GitHub 帳號即可，之後不會再問 |

---

<!-- S2-8 -->
# 要不要裝？三句話決定

<div class="lead">工具是選項，不是作業。</div>

<div class="grid">
  <div class="box">
    <strong>只改文字、偶爾改</strong><br>
    瀏覽器版就夠<br>
    <i>.com 改 .dev，零安裝</i>
  </div>
  <div class="box blue">
    <strong>常改、想看差異、要匯出簡報</strong><br>
    裝本機 VS Code<br>
    <i>＋ Marp 擴充功能</i>
  </div>
  <div class="box red">
    <strong>要跑程式（build、測試）</strong><br>
    本機 VS Code 內建終端機（Ctrl+`）<br>
    <i>或維持命令提示字元</i>
  </div>
</div>

- 不管選哪個，你做的都是同一件事：**挑檔案 → 存檔點 → 上傳**

