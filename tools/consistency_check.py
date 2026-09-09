#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""FinFlow 課程・全課一致性台帳產生器
用法：python3 tools/consistency_check.py > notes/consistency-ledger.md
只讀不寫；所有結論都可由本腳本重跑複驗。
"""
import re, os, glob, collections, datetime, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

# ---- 檔案分類 ---------------------------------------------------------------
ALL_NOTES = sorted(glob.glob('notes/*.md'))
EXCLUDE   = ('project-history', 'soda-ai-interaction', 'github-tutorial-recording',
             'theme-sampler', 'consistency-ledger')
DECKS     = [f for f in ALL_NOTES if not any(e in f for e in EXCLUDE)]
# 專題／補充頁自成一套內部編號，不進主頁序
STANDALONE = ('part3-dara-case-study', 'part2-vscode-option', 'part2-ai-scope-control',
              'part7-methodology', 'panorama-slides')
MAIN = [f for f in DECKS if not any(s in f for s in STANDALONE)]

def read(p):
    return open(p, encoding='utf-8').read()

# ---- 1. 頁碼台帳 ------------------------------------------------------------
def page_index(files):
    pages, dups = {}, []
    for f in sorted(files):
        cur = None
        for line in read(f).split('\n'):
            m = re.match(r'<!--\s*第\s*(\d+[a-z]?)\s*頁\s*-->', line.strip())
            if m:
                cur = m.group(1)
            elif line.startswith('# ') and cur:
                if cur in pages:
                    dups.append((cur, pages[cur][0], os.path.basename(f)))
                pages[cur] = (os.path.basename(f), line[2:].strip())
                cur = None
    return pages, dups

pages, dups = page_index(MAIN)
nums = sorted(int(re.sub(r'\D', '', p)) for p in pages)
gaps = [n for n in range(min(nums), max(nums) + 1) if n not in nums]
unnum = sorted(int(re.sub(r'\D','',p)) if p.isdigit() else p for p in pages if not p.isdigit())

# ---- 2. 跨頁引用 ------------------------------------------------------------
refs, bad_refs = collections.Counter(), []
for f in sorted(DECKS + ['index.md']):
    for m in re.finditer(r'頁\s*(\d+)', read(f)):
        n = m.group(1)
        refs[n] += 1
        if n not in pages:
            bad_refs.append((os.path.basename(f), n))

# ---- 3. 術語口徑 ------------------------------------------------------------
TERM_PAIRS = [
    ('疊代', '迭代'), ('規格書', None), ('工程書', None),
    ('全景圖', '全景流程圖'), ('提示詞', None), ('造物者', None),
    ('鐵律', None), ('引擎', None),
]
# 並存用語：兩種說法都對，只列數量供人工判斷，不當成錯誤
COEXIST = [('交叉抓錯', '全景圖裡那一格的名字'),
           ('交叉審查', '這件事的一般說法（第六部標題用語）'),
           ('工程書', '大專案才拆出來的第二份文件')]
NUM_TOKENS = ['74 次', '49 次', '58 張', '15 輪', '6 張', '10 張',
              '五個心法', '第六條', '六個步驟', '四道閘門', '三條鐵律', '26 版', '七條', '五項']

SCAN = sorted(DECKS + ['index.md'] + glob.glob('chapters/*.md'))
def count_all(tok):
    hits = {}
    for f in SCAN:
        c = read(f).count(tok)
        if c:
            hits[os.path.basename(f)] = c
    return hits

# ---- 4. Step 系統 -----------------------------------------------------------
step_hits = collections.defaultdict(list)
for f in SCAN:
    for m in re.finditer(r'Step\s*([0-6])', read(f)):
        step_hits[m.group(1)].append(os.path.basename(f))

# ---- 5. 渲染產物同步 --------------------------------------------------------
stale = []
for f in DECKS:
    h = 'slides/' + os.path.basename(f).replace('.md', '.html')
    if not os.path.exists(h):
        stale.append((os.path.basename(f), 'HTML 不存在'))
    elif os.path.getmtime(h) < os.path.getmtime(f):
        stale.append((os.path.basename(f), 'HTML 比 md 舊'))

# ---- 6. 外部相依／emoji -----------------------------------------------------
ext, emo = [], []
# 純文字符號（➔ ➜ ☐ ⚠ ✓ ✕）不會被 marp 轉成外部圖片，白名單放行；
# 真正的把關是下面 HTML 的外部 <img> 計數必須為 0
SAFE = set('➔➜☐⚠✓✕・')
EMOJI = re.compile('[\U0001F300-\U0001FAFF☀-➿]')
for h in sorted(glob.glob('slides/*.html')):
    t = read(h)
    n_img = len(re.findall(r'<img[^>]*src="https?://', t))
    if n_img:
        ext.append((os.path.basename(h), n_img))
for f in DECKS:
    t = read(f)
    e = set(EMOJI.findall(t)) - SAFE
    if e:
        emo.append((os.path.basename(f), ''.join(sorted(e))))

# ---- 輸出 -------------------------------------------------------------------
o = print
o('# FinFlow 課程・全課一致性台帳')
o('')
o(f'產生時間：{datetime.date.today()}　產生方式：`python3 tools/consistency_check.py`')
o('')
o('本檔由腳本產生，**不要手改**。每批修訂後重跑並 diff，用來擋跨部回歸。')
o('')
o('## 1. 主頁序台帳')
o('')
o(f'- 有編號頁面：**{len(pages)}**，範圍 **{min(nums)}–{max(nums)}**')
o(f'- 缺號：{"**無**" if not gaps else gaps}')
o(f'- 不編號插頁：{", ".join(str(u) for u in unnum) if unnum else "無"}')
o(f'- 序（preface）與見證（testimonials）不進主頁序，第七部與各專題頁亦不編號')
o(f'- 主頁序自 **{min(nums)}** 起算；頁 1–2 在全書從未出現（封面與目次留白）')
o(f'- 重複頁碼：{"**無**" if not dups else dups}')
o('')
o('| 頁 | 標題 | 檔案 |')
o('| ---: | :--- | :--- |')
for p in sorted(pages, key=lambda x: (int(re.sub(r'\D', '', x)), x)):
    f, t = pages[p]
    o(f'| {p} | {t} | `{f}` |')
o('')
o('## 2. 跨頁引用')
o('')
o(f'- 引用總次數：**{sum(refs.values())}**，指向 **{len(refs)}** 個不同頁面')
o(f'- 指向不存在的頁碼：{"**無**" if not bad_refs else bad_refs}')
o('')
o('| 被引用的頁 | 次數 | 該頁標題 |')
o('| ---: | ---: | :--- |')
for n in sorted(refs, key=lambda x: int(x)):
    o(f'| {n} | {refs[n]} | {pages.get(n, ("", "**查無此頁**"))[1]} |')
o('')
o('## 3. 術語口徑')
o('')
o('| 用語 | 總次數 | 出現檔數 | 對照（不該出現的變體） |')
o('| :--- | ---: | ---: | :--- |')
for a, b in TERM_PAIRS:
    ha = count_all(a)
    hb = count_all(b) if b else {}
    warn = f'`{b}` × {sum(hb.values())}　⚠ {list(hb)}' if hb else (f'`{b}` × 0 ✓' if b else '—')
    o(f'| {a} | {sum(ha.values())} | {len(ha)} | {warn} |')
o('')
o('**並存用語**（兩種說法都對，只記數量，不是錯誤）：')
o('')
o('| 用語 | 次數 | 這個詞指的是 |')
o('| :--- | ---: | :--- |')
for t, why in COEXIST:
    h = count_all(t)
    o(f'| {t} | {sum(h.values())} | {why} |')
o('')
o('## 4. 數字口徑')
o('')
o('| 數字說法 | 總次數 | 出現在 |')
o('| :--- | ---: | :--- |')
for t in NUM_TOKENS:
    h = count_all(t)
    if h:
        o(f'| {t} | {sum(h.values())} | {", ".join(f"{k}×{v}" for k, v in sorted(h.items()))} |')
o('')
o('## 5. Step 編號系統')
o('')
o('第三部 Step0–Step6 是全課唯一的步驟編號；第四部一律用「提示詞 1～4」。')
o('')
o('| Step | 出現檔案 |')
o('| :--- | :--- |')
for k in sorted(step_hits):
    o(f'| Step{k} | {", ".join(sorted(set(step_hits[k])))} |')
o('')
o('## 6. 渲染產物同步')
o('')
o(f'- md 比 HTML 新或 HTML 缺漏：{"**無**" if not stale else stale}')
o(f'- HTML 外部圖片相依：{"**0**" if not ext else ext}')
o(f'- 原始檔殘留 emoji（純文字符號 {"".join(sorted(SAFE))} 白名單放行）：{"**無**" if not emo else emo}')
