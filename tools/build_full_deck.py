#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把全課 deck 併成一份完整投影片（依閱讀順序），輸出 notes/_full.md。

用法（repo 根目錄）：
    python3 tools/build_full_deck.py
    export CHROME_PATH=<chromium 路徑>
    npx @marp-team/marp-cli --theme-set themes --allow-local-files --html \
        --pdf  notes/_full.md -o dist/FinFlow實戰心法_全課合訂本.pdf
    npx @marp-team/marp-cli --theme-set themes --allow-local-files --html \
        --pptx notes/_full.md -o dist/FinFlow實戰心法_全課合訂本.pptx

notes/_full.md 是產生物，不進版控（見 .gitignore）。
新增或調整章節時，只要改下面的 ORDER，並回頭更新目次那張的投影片編號。
"""
import io, os, re, datetime
os.chdir('/home/claude/finflow-course-claude')

ORDER = [
 ("preface-slides.md",                    "序・起心動念"),
 ("testimonials-slides.md",               "見證・玩過的人怎麼說"),
 ("part0-shock-slides.md",                "第零部・震撼彈"),
 ("part1-mindset-slides.md",              "第一部・想法怎麼來"),
 ("part1-card-growth-slides.md",          "第一部・想法怎麼來"),
 ("part2-ai-partners-slides.md",          "第二部・地基與工具"),
 ("part2-habits-and-prompts-slides.md",   "第二部・地基與工具"),
 ("part2-git-and-techstack-slides.md",    "第二部・地基與工具"),
 ("part2-advanced-tactics-slides.md",     "第二部・地基與工具"),
 ("part3-five-days-sprint-slides.md",     "第三部・手把手做出第一版"),
 ("part3-debugging-and-balance-slides.md","第三部・手把手做出第一版"),
 ("part3-iteration-and-ui-slides.md",     "第三部・手把手做出第一版"),
 ("part3-testing-and-multiplayer-slides.md","第三部・手把手做出第一版"),
 ("part3-pitfalls-and-qa-slides.md",      "第三部・手把手做出第一版"),
 ("part3-shipping-and-wrap-slides.md",    "第三部・手把手做出第一版"),
 ("part4-spec-and-prompts-slides.md",     "第四部・換你做一個"),
 ("part4-build-and-ship-slides.md",       "第四部・換你做一個"),
 ("part5-closing-slides.md",              "第五部・結語與資源包"),
 ("part6-ai-cross-review-slides.md",      "第六部・讓 AI 互相抓錯"),
 ("part7-methodology-slides.md",          "第七部・方法論"),
 ("part8-self-review-slides.md",          "第八部・實證"),
 ("part2-vscode-option-slides.md",        "附錄・三種做法：命令列、VS Code、瀏覽器"),
 ("part2-ai-scope-control.md",            "附錄・AI 協作邊界管理"),
 ("part3-dara-case-study.md",             "附錄・DARA 數據治理實例"),
 ("panorama-slides.md",                   "附錄・全景圖單頁版"),
]

def body(path):
    t = io.open('notes/'+path, encoding='utf-8').read()
    # 去掉 YAML frontmatter
    t = re.sub(r'^---\n.*?\n---\n', '', t, count=1, flags=re.S)
    # 去掉交付標記
    t = t.replace('<!-- EOF: VERIFIED FULL FILE DELIVERY -->', '')
    return t.strip()

today = datetime.date.today()
out = []
out.append("""---
marp: true
theme: finflow-clean
paginate: true
header: "FinFlow 實戰心法"
---

<!-- _class: hero -->
<!-- _paginate: false -->
<!-- _header: "" -->
# FinFlow 實戰心法

<div class="lead">我不會寫程式，但我用 AI 做出了一套多人連線遊戲</div>

<div class="grid">
  <div class="box blue"><strong>八個部</strong><br>從想法到上線的完整流程</div>
  <div class="box"><strong>＋附錄</strong><br>三個專題與全景圖</div>
  <div class="box red"><strong>合訂本</strong><br>""" + str(today) + """</div>
</div>

---

<!-- _class: dense -->
<!-- _paginate: false -->
<!-- _header: "" -->
# 目次

| 投影片 | 內容 | 書上頁碼 |
| ---: | :--- | :--- |
| 3 | **序**　起心動念 | 不編號 |
| 8 | **見證**　玩過的人怎麼說 | 不編號 |
| 12 | **第零部**　震撼彈：這不是玩具 | 3–10 |
| 20 | **第一部**　想法怎麼來，以及三條鐵律 | 11–31 |
| 41 | **第二部**　地基與跟 AI 合作的方法 | 32–58 |
| 68 | **第三部**　手把手做出第一版，含真實踩坑 | 59–108 |
| 119 | **第四部**　換你做一個：四份可複製的提示詞 | 109–124 |
| 135 | **第五部**　結語與資源包 | 125–134 |
| 146 | **第六部**　讓 AI 互相抓錯（審程式） | 135–144 |
| 156 | **第七部**　方法論：全景圖與領域遷移 | 不編號 |
| 164 | **第八部**　實證：用這套方法審它自己 | 不編號 |
| 174 | **附錄**　三個專題與全景圖單頁版 | 不編號 |

- 內文裡的「頁 N」指的是**書上的頁碼**，跟左欄的投影片編號是兩套。換算：<span class="highlight">頁 3–85 → 投影片 N＋9；頁 86–125 → N＋10；頁 126–144 → N＋11</span>
- 差額來自 85b 與 125b 兩張刻意不編號的插頁，以及序與見證不進書上頁序
""")

prev_header = None
for path, hdr in ORDER:
    b = body(path)
    if hdr != prev_header:
        b = ('<!-- header: "FinFlow 實戰心法 | %s" -->\n' % hdr) + b
        prev_header = hdr
    out.append(b)

io.open('notes/_full.md','w',encoding='utf-8').write('\n\n---\n\n'.join(out) + '\n')
print("組好了")
