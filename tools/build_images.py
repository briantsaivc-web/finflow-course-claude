#!/usr/bin/env python3
"""批次:裁切 + 去除終端機邊緣光暈 + 紅框編號 → images/<name>.png"""
import os, subprocess, sys
from PIL import Image

RAW, OUT = "tools/raw", "images"
os.makedirs(OUT, exist_ok=True)

# name: (src, crop or None, [ "x0,y0,x1,y1|num|label", ... ])
SPEC = {
 "A01-home": ("A01-home.jpg", None, ["1232,18,1290,60|1|點右上角的「+」|L", "282,105,356,140|2|或點這個綠色 New 也一樣|B"]),
 "A02-plus-menu": ("A02-plus-menu.jpg", None, ["1068,112,1290,150|1|點 New repository"]),
 "A03-new-blank": ("A03-new-blank.jpg", None, ["352,293,560,335|1|Owner=你的帳號(不用改)|B", "592,293,1200,335|2|在這裡輸入專案名稱|A"]),
 "A04-new-named": ("A04-new-named.jpg", None, ["592,293,1200,362|1|綠色勾勾=這個名字可以用"]),
 "A05-new-config": ("A05-new-config.jpg", None, ["1050,185,1180,225|1|Public", "1090,285,1180,322|2|Add README 保持 Off", "1022,362,1180,402|3|No .gitignore", "1044,442,1180,482|4|No license", "1036,530,1200,570|5|按 Create repository"]),
 "A06-empty-repo": ("A06-empty-repo.jpg", None, ["433,543,1420,575|1|這是 Repository 網址(程式碼的家)"]),
 "A07-empty-repo-cmds": ("A07-empty-repo-cmds.jpg", None, ["73,420,1478,512|1|待會在指令列要用的三行,GitHub 先幫你準備好了"]),
 "B00-git-not-found": ("B00-git-not-found.png", (8,44,1096,140), ["0,20,560,46|!|看到這行=電腦還沒裝 Git"]),
 "B01-git-version": ("B01-git-version.png", (8,44,1096,140), ["0,20,320,46|1|有版本號=Git 裝好了"]),
 "B03-init": ("B03-init.png", (8,44,1096,180), ["0,42,1088,88|1|出現 Initialized=這個資料夾變成 Git 專案了"]),
 "B04-commit-identity-error": ("B04-commit-identity-error.png", (8,44,1096,340), ["0,108,600,176|!|第一次用 Git 幾乎一定會看到這個", "0,238,600,278|2|照它說的做兩行設定(下一步)"]),
 "B05-config-identity": ("B05-config-identity.png", (8,44,1096,140), ["0,0,1088,70|1|打完沒有任何回應=設定成功(正常)"]),
 "B06-commit": ("B06-commit.png", (8,44,1096,150), ["0,42,640,108|1|看到 1 file changed=存檔點建立成功"]),
 "B07-push": ("B07-push.png", (8,44,1096,310), ["0,208,720,258|1|看到這兩行=上傳成功"]),
 "C01-repo-with-file": ("C01-repo-with-file.jpg", None, ["40,297,940,332|1|index.html 已經在 GitHub 上了|B", "948,62,1035,92|2|接著點 Settings|L"]),
 "C03-settings-sidebar-pages": ("C03-settings-sidebar-pages.jpg", None, ["30,285,300,318|1|左邊選單往下捲,點 Pages"]),
 "C04-pages-disabled": ("C04-pages-disabled.jpg", None, ["332,288,512,318|1|Source 保持 Deploy from a branch|A", "332,408,408,440|2|點 None|B"]),
 "C05-pages-branch-dropdown": ("C05-pages-branch-dropdown.jpg", None, ["340,420,650,450|1|選 main"]),
 "C06-pages-main-root": ("C06-pages-main-root.jpg", None, ["332,152,428,182|1|main|B", "440,152,552,182|2||B", "563,152,626,182|3|按 Save(② / (root) 不用改)|A"]),
 "C07-pages-saved": ("C07-pages-saved.jpg", None, ["0,102,1290,158|1|出現 source saved=設定完成,接著等它建置"]),
 "C08-actions-inprogress": ("C08-actions-inprogress.jpg", None, ["376,362,1262,410|1|黃色圈圈=正在建置,等 1~2 分鐘"]),
 "C09-actions-done": ("C09-actions-done.jpg", None, ["376,362,1262,410|1|綠色勾勾=建置完成"]),
 "C10-pages-live": ("C10-pages-live.jpg", None, ["332,230,900,275|1|這一行就是你的網站網址|B", "915,236,1020,268|2|點 Visit site 打開|A"]),
 "C11-site": ("C11-site.jpg", None, []),
}

def deglow(im):
    """終端機截圖:把接近黑的漸層光暈壓成純黑"""
    px = im.load(); w, h = im.size
    for y in range(h):
        for x in range(w):
            r, g, b = px[x, y]
            if max(r, g, b) < 70 and (r + g + b) < 150:
                px[x, y] = (12, 12, 12)
    return im

for name, (src, crop, boxes) in SPEC.items():
    im = Image.open(os.path.join(RAW, src)).convert("RGB")
    if crop:
        im = deglow(im.crop(crop))
        # 終端機截圖加黑邊,讓編號圓點與標籤不被裁掉
        PAD = 40
        canvas = Image.new("RGB", (im.width + PAD * 2, im.height + PAD * 2), (12, 12, 12))
        canvas.paste(im, (PAD, PAD)); im = canvas
        def shift(spec):
            parts = spec.split("|"); c = [int(v) + PAD for v in parts[0].split(",")]
            return "|".join([",".join(map(str, c))] + parts[1:])
        boxes = [shift(b) for b in boxes]
    tmp = os.path.join(OUT, f"_{name}.png"); im.save(tmp)
    dst = os.path.join(OUT, f"{name}.png")
    subprocess.run([sys.executable, "tools/annotate.py", tmp, dst, *boxes], check=True)
    os.remove(tmp)
print("done", len(SPEC))
