// 從母版內容產生「GitHub 三步驟實戰」簡報樣張
const pptxgen = require("pptxgenjs");
const fs = require("fs");
const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE"; // 13.33 x 7.5
const INK = "1F2328", DIM = "57606A", GREEN = "1A7F37", RED = "CF222E", BG = "FFFFFF", DARK = "0D1117", PANEL = "F6F8FA", WARN = "FFF8C5";
const HFONT = "Microsoft JhengHei", BFONT = "Microsoft JhengHei", MONO = "Courier New";

function img(name) { return `images/${name}.png`; }
function imgSize(name) {
  // 讀 PNG 尺寸
  const b = fs.readFileSync(img(name));
  return { w: b.readUInt32BE(16), h: b.readUInt32BE(20) };
}
function fit(name, boxW, boxH) {
  const { w, h } = imgSize(name); const r = Math.min(boxW / w, boxH / h);
  return { w: w * r, h: h * r };
}
function badge(slide, text, x, y) {
  slide.addShape(pres.ShapeType.ellipse, { x, y, w: 0.55, h: 0.55, fill: { color: GREEN } });
  slide.addText(text, { x, y, w: 0.55, h: 0.55, fontFace: HFONT, fontSize: 14, bold: true, color: "FFFFFF", align: "center", valign: "middle", margin: 0, isTextBox: true });
}

// 封面
{
  const s = pres.addSlide(); s.background = { color: DARK };
  s.addText("把你的作品放上網", { x: 0.8, y: 2.0, w: 11.7, h: 1.2, fontFace: HFONT, fontSize: 44, bold: true, color: "FFFFFF", isTextBox: true });
  s.addText("GitHub 三步驟實戰:建立 Repository → 推上去 → 開 GitHub Pages", { x: 0.8, y: 3.2, w: 11.7, h: 0.7, fontFace: BFONT, fontSize: 22, color: "C9D1D9", isTextBox: true });
  s.addText("全程實機錄製・截圖日期 2026-09-02", { x: 0.8, y: 6.3, w: 11.7, h: 0.5, fontFace: BFONT, fontSize: 14, color: "8B949E", isTextBox: true });
  s.addNotes("本章目標:讓完全沒碰過 GitHub 的學員,在 20 分鐘內拿到一個可以分享的網址。");
}
// 三步驟總覽
{
  const s = pres.addSlide(); s.background = { color: BG };
  s.addText("今天只做三件事", { x: 0.6, y: 0.5, w: 12, h: 0.9, fontFace: HFONT, fontSize: 36, bold: true, color: INK, isTextBox: true });
  const steps = [["1", "在 GitHub 建一個空的 Repository", "程式碼的家,先蓋好"], ["2", "用命令提示字元把檔案推上去", "8 行指令,照抄就好"], ["3", "啟用 GitHub Pages", "拿到任何人都能打開的網址"]];
  steps.forEach((st, i) => {
    const x = 0.6 + i * 4.1;
    s.addShape(pres.ShapeType.roundRect, { x, y: 2.0, w: 3.8, h: 3.4, fill: { color: PANEL }, rectRadius: 0.15, line: { color: "D0D7DE", width: 1 } });
    s.addShape(pres.ShapeType.ellipse, { x: x + 0.3, y: 2.3, w: 0.8, h: 0.8, fill: { color: GREEN } });
    s.addText(st[0], { x: x + 0.3, y: 2.3, w: 0.8, h: 0.8, fontFace: HFONT, fontSize: 24, bold: true, color: "FFFFFF", align: "center", valign: "middle", margin: 0, isTextBox: true });
    s.addText(st[1], { x: x + 0.3, y: 3.3, w: 3.2, h: 1.0, fontFace: HFONT, fontSize: 18, bold: true, color: INK, isTextBox: true, margin: 0 });
    s.addText(st[2], { x: x + 0.3, y: 4.3, w: 3.2, h: 0.8, fontFace: BFONT, fontSize: 14, color: DIM, isTextBox: true, margin: 0 });
  });
  s.addText("需要準備:GitHub 帳號・裝好 Git for Windows・一個放了 index.html 的資料夾", { x: 0.6, y: 6.2, w: 12, h: 0.5, fontFace: BFONT, fontSize: 14, color: DIM, isTextBox: true });
}

function section(num, title, sub) {
  const s = pres.addSlide(); s.background = { color: DARK };
  s.addText(`第${num}步`, { x: 0.8, y: 2.3, w: 11.7, h: 0.8, fontFace: HFONT, fontSize: 24, color: "8B949E", isTextBox: true });
  s.addText(title, { x: 0.8, y: 3.0, w: 11.7, h: 1.1, fontFace: HFONT, fontSize: 40, bold: true, color: "FFFFFF", isTextBox: true });
  s.addText(sub, { x: 0.8, y: 4.2, w: 11.7, h: 0.8, fontFace: BFONT, fontSize: 18, color: "C9D1D9", isTextBox: true });
}

// 圖 + 說明頁
function stepSlide({ tag, title, image, lines, warn, notes }) {
  const s = pres.addSlide(); s.background = { color: BG };
  s.addText(tag, { x: 0.5, y: 0.35, w: 3, h: 0.4, fontFace: BFONT, fontSize: 12, color: DIM, isTextBox: true, margin: 0 });
  s.addText(title, { x: 0.5, y: 0.7, w: 12.3, h: 0.8, fontFace: HFONT, fontSize: 28, bold: true, color: INK, isTextBox: true, margin: 0 });
  const boxW = 8.6, boxH = 5.3; const sz = fit(image, boxW, boxH);
  s.addImage({ path: img(image), x: 0.5, y: 1.7, w: sz.w, h: sz.h });
  const tx = 9.4;
  s.addText(lines.map((t, i) => ({ text: t, options: { bullet: true, breakLine: i < lines.length - 1, paraSpaceAfter: 8 } })),
    { x: tx, y: 1.7, w: 3.5, h: warn ? 2.8 : 5.0, fontFace: BFONT, fontSize: 14, color: INK, valign: "top", isTextBox: true });
  if (warn) {
    s.addShape(pres.ShapeType.roundRect, { x: tx, y: 4.7, w: 3.5, h: 2.2, fill: { color: WARN }, rectRadius: 0.1, line: { color: "D4A72C", width: 1 } });
    s.addText([{ text: "⚠ 小心  ", options: { bold: true, color: "9A6700" } }, { text: warn }], { x: tx + 0.1, y: 4.75, w: 3.3, h: 2.1, fontFace: BFONT, fontSize: 12, color: INK, valign: "top", isTextBox: true });
  }
  if (notes) s.addNotes(notes);
}
// 指令頁
function cmdSlide({ tag, title, cmds, lines }) {
  const s = pres.addSlide(); s.background = { color: BG };
  s.addText(tag, { x: 0.5, y: 0.35, w: 3, h: 0.4, fontFace: BFONT, fontSize: 12, color: DIM, isTextBox: true, margin: 0 });
  s.addText(title, { x: 0.5, y: 0.7, w: 12.3, h: 0.8, fontFace: HFONT, fontSize: 28, bold: true, color: INK, isTextBox: true, margin: 0 });
  const h = Math.max(1.2, cmds.length * 0.42 + 0.5);
  s.addShape(pres.ShapeType.roundRect, { x: 0.5, y: 1.7, w: 12.3, h, fill: { color: DARK }, rectRadius: 0.1 });
  s.addText(cmds.map((c, i) => ({ text: c, options: { breakLine: i < cmds.length - 1 } })), { x: 0.7, y: 1.85, w: 11.9, h: h - 0.3, fontFace: MONO, fontSize: 16, color: "E6EDF3", valign: "top", isTextBox: true, margin: 0 });
  s.addText(lines.map((t, i) => ({ text: t, options: { bullet: true, breakLine: i < lines.length - 1, paraSpaceAfter: 8 } })), { x: 0.5, y: 1.9 + h, w: 12.3, h: 5.0 - h, fontFace: BFONT, fontSize: 15, color: INK, valign: "top", isTextBox: true });
}

section("一", "在 GitHub 建立一個空的 Repository", "Repository = 一個專案的家。先蓋空的,等一下再把檔案搬進去。");
stepSlide({ tag: "第一步 1-1", title: "登入 GitHub,點右上角的「+」", image: "A01-home", lines: ["登入後看到的是你的首頁(Dashboard)", "右上角「+」或左邊綠色「New」都可以", "兩個按鈕功能一樣"] });
stepSlide({ tag: "第一步 1-2", title: "選「New repository」", image: "A02-plus-menu", lines: ["下拉選單第二項", "其他選項今天都用不到"] });
stepSlide({ tag: "第一步 1-3", title: "填專案名稱", image: "A04-new-named", lines: ["Owner 就是你的帳號,不用動", "名稱只能用英文、數字、-,不能有空格", "本章用 github-tutorial-demo", "看到綠色勾勾 = 名字可以用"] });
stepSlide({ tag: "第一步 1-4", title: "下半部全部保持預設,直接按 Create", image: "A05-new-config", lines: ["Public(Pages 免費版只給 Public 用)", "Add README 保持 Off", "No .gitignore / No license", "按綠色 Create repository"], warn: "README、.gitignore、license 三個都不要加。repo 越空,等一下從電腦推檔案越不會出錯。" });
stepSlide({ tag: "第一步 1-5", title: "建好了:記下你的 Repository 網址", image: "A06-empty-repo", lines: ["藍色區塊裡的網址 = 這個專案的家", "格式 github.com/你的帳號/專案名", "先複製起來,第二步要用"], warn: "這是「程式碼的家」,不是給別人玩的網址。給別人玩的網址第三步才會拿到,兩個很像,別搞混。" });
stepSlide({ tag: "第一步 1-5", title: "GitHub 已經幫你準備好指令", image: "A07-empty-repo-cmds", lines: ["往下捲會看到兩組指令", "我們用下面那組「push an existing repository」", "先看一眼就好,第二步會帶你打"] });

section("二", "用命令提示字元把檔案推上去", "8 行指令,照抄就好。會遇到的錯誤畫面我們也先給你看。");
cmdSlide({ tag: "第二步 2-0", title: "打開命令提示字元", cmds: ["按 Windows 鍵 → 直接打 cmd → Enter"], lines: ["跳出來的黑色視窗就是「命令提示字元」", "從開始功能表點「Git CMD」進來也一樣,畫面與指令完全相同"] });
stepSlide({ tag: "第二步 2-1", title: "先確認 Git 裝好了:git --version", image: "B01-git-version", lines: ["打 git --version 按 Enter", "看到版本號就對了", "版本數字跟截圖不同沒關係"] });
stepSlide({ tag: "第二步 2-1", title: "如果你看到的是這個……", image: "B00-git-not-found", lines: ["「'git' 不是內部或外部命令」", "= 還沒裝 Git,或裝完沒重開視窗"], warn: "到 git-scm.com/download/win 下載安裝,一路 Next 用預設值。裝完要重新開一個新的命令提示字元視窗。" });
cmdSlide({ tag: "第二步 2-2", title: "走進資料夾,初始化 Git", cmds: ['cd /d "%USERPROFILE%\\Downloads\\github-tutorial-demo"', "git init", "git branch -M main"], lines: ["cd = 走進資料夾(路徑換成你自己的)", "git init = 把這個資料夾變成 Git 專案", "git branch -M main = 主分支叫 main(GitHub 預設名稱,照打)"] });
stepSlide({ tag: "第二步 2-2", title: "成功長這樣", image: "B03-init", lines: ["出現 Initialized empty Git repository", "截圖裡的路徑是錄製用的,你的會不一樣,正常"] });
cmdSlide({ tag: "第二步 2-3", title: "把檔案加進來,建立第一個存檔點", cmds: ["git add .", 'git commit -m "第一次上傳:加入 index.html"'], lines: ["git add . = 把資料夾裡所有檔案排進這次要存的清單", "git commit -m \"說明\" = 正式存一個存檔點,寫一句說明", "第一次做 commit,幾乎一定會遇到下一頁的錯誤"] });
stepSlide({ tag: "第二步 2-3", title: "第一次用 Git 一定會看到:Please tell me who you are", image: "B04-commit-identity-error", lines: ["不是你打錯", "Git 要知道「這台電腦的存檔要署名誰」", "照它說的打兩行設定(下一頁)"], warn: "那行 warning: LF will be replaced by CRLF 是 Windows 換行符號提醒,可以無視。" });
cmdSlide({ tag: "第二步 2-3", title: "設定一次,以後都不用再打", cmds: ['git config --global user.name "你的名字"', 'git config --global user.email "你的email"'], lines: ["打完不會有任何回應 = 成功", "email 不一定要跟 GitHub 帳號一樣,但一樣最省事", "設定完,再打一次 git commit -m \"...\""] });
stepSlide({ tag: "第二步 2-3", title: "commit 成功長這樣", image: "B06-commit", lines: ["1 file changed = 一個檔案被存進存檔點", "後面那串英數字是這個存檔點的編號,不用記"] });
cmdSlide({ tag: "第二步 2-4", title: "告訴 Git 要推去哪裡,然後推上去", cmds: ["git remote add origin https://github.com/你的帳號/github-tutorial-demo.git", "git push -u origin main"], lines: ["網址換成 1-5 記下的那個,結尾要加 .git", "remote add origin = 幫遠端倉庫取綽號叫 origin", "push = 真的上傳"] });
stepSlide({ tag: "第二步 2-4", title: "push 成功長這樣", image: "B07-push", lines: ["最後兩行 [new branch] main -> main", "branch 'main' set up to track 'origin/main'", "= 上傳成功"], warn: "第一次 push 可能跳出「Connect to GitHub」登入視窗,這不是當機,選 Sign in with your browser 登入即可,以後不會再問。(錄製電腦已登入,故無此畫面截圖)" });

section("三", "啟用 GitHub Pages,拿到你的網址", "在 Settings 裡按三下,等 1~2 分鐘,網址就出來了。");
stepSlide({ tag: "第三步 3-1", title: "回到 GitHub,確認檔案上去了", image: "C01-repo-with-file", lines: ["重新整理 Repository 頁面", "index.html 出現在檔案列表", "接著點右上方 Settings(齒輪)"] });
stepSlide({ tag: "第三步 3-2", title: "左邊選單往下捲,找到 Pages", image: "C03-settings-sidebar-pages", lines: ["在「Code, planning, and automation」那一區", "很多人卡在這裡:選單很長,要往下捲"] });
stepSlide({ tag: "第三步 3-3", title: "Branch 選 main", image: "C05-pages-branch-dropdown", lines: ["Source 保持 Deploy from a branch", "Branch 原本是 None,點它,選 main"], warn: "有些教學叫你選 gh-pages,那是專案有自動建置設定時才會出現的分支。資料夾裡直接放 index.html 的專案,選 main 就對了。" });
stepSlide({ tag: "第三步 3-3", title: "資料夾保持 / (root),按 Save", image: "C06-pages-main-root", lines: ["① main  ② / (root) 不用改  ③ Save", "上方出現 GitHub Pages source saved 就完成"] });
stepSlide({ tag: "第三步 3-4", title: "等 GitHub 幫你建置(1~2 分鐘)", image: "C08-actions-inprogress", lines: ["點上方 Actions 分頁可以看進度", "黃色圈圈 = 正在建置", "綠色勾勾 = 完成(本次錄製 1 分 12 秒)"] });
stepSlide({ tag: "第三步 3-5", title: "拿到網址:Your site is live at ...", image: "C10-pages-live", lines: ["回到 Settings → Pages", "上方多出一個框,那一行就是你的網址", "格式 你的帳號.github.io/專案名", "點 Visit site 打開"] });
stepSlide({ tag: "第三步 3-5", title: "看到這一頁,你的作品已經在網路上了", image: "C11-site", lines: ["把網址傳給朋友,他們就能打開", "404 的話再等一分鐘重新整理", "五分鐘還 404:回 Actions 看有沒有紅色叉叉,通常是檔名不是 index.html"] });

cmdSlide({ tag: "之後", title: "以後更新只要三行", cmds: ["git add .", 'git commit -m "寫一句這次改了什麼"', "git push"], lines: ["改完 index.html,回到同一個資料夾打這三行", "GitHub 會自動重新建置,一樣等 1~2 分鐘", "每一次 commit 都是一個可以回去的存檔點 —— 這就是 GitHub 當「時光機」的用法"] });
{
  const s = pres.addSlide(); s.background = { color: DARK };
  s.addText("你已經完成了", { x: 0.8, y: 1.6, w: 11.7, h: 1.0, fontFace: HFONT, fontSize: 40, bold: true, color: "FFFFFF", isTextBox: true });
  const items = ["在 GitHub 蓋了一個專案的家", "用指令把檔案推了上去", "拿到一個任何人都能打開的網址"];
  items.forEach((t, i) => { badge(s, String(i + 1), 0.9, 3.0 + i * 0.85); s.addText(t, { x: 1.7, y: 3.0 + i * 0.85, w: 10, h: 0.55, fontFace: BFONT, fontSize: 20, color: "E6EDF3", valign: "middle", isTextBox: true, margin: 0 }); });
  s.addText("下一步:把 index.html 換成你自己做的遊戲,再推一次。", { x: 0.8, y: 5.9, w: 11.7, h: 0.6, fontFace: BFONT, fontSize: 18, color: "8B949E", isTextBox: true });
}

pres.writeFile({ fileName: "samples/github-tutorial_slides_sample.pptx" }).then(f => console.log("wrote", f));
