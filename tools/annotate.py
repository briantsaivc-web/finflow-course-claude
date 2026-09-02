#!/usr/bin/env python3
"""在截圖上畫紅框+編號圓點+說明標籤。
用法: python3 annotate.py in.png out.png "x0,y0,x1,y1|1|說明" "x0,y0,x1,y1|2|說明" ...
座標為圖檔像素。說明可省略。也可加 --crop x0,y0,x1,y1 先裁切。
"""
import sys
from PIL import Image, ImageDraw, ImageFont

RED = (230, 40, 40)
FONT_CJK = "/usr/share/fonts/opentype/noto/NotoSansCJK-Black.ttc"

def font(size):
    try:
        return ImageFont.truetype(FONT_CJK, size)
    except Exception:
        return ImageFont.load_default()

def main():
    args = sys.argv[1:]
    crop = None
    if "--crop" in args:
        i = args.index("--crop"); crop = tuple(int(v) for v in args[i+1].split(",")); del args[i:i+2]
    src, dst, *boxes = args
    im = Image.open(src).convert("RGB")
    if crop:
        im = im.crop(crop)
    d = ImageDraw.Draw(im)
    W, H = im.size
    lw = max(4, W // 300)
    r = max(16, W // 60)
    f_num = font(int(r * 1.3))
    f_lab = font(max(18, W // 55))
    for spec in boxes:
        parts = spec.split("|")
        x0, y0, x1, y1 = (int(v) for v in parts[0].split(","))
        num = parts[1] if len(parts) > 1 else ""
        label = parts[2] if len(parts) > 2 else ""
        pos = parts[3] if len(parts) > 3 else ""   # A=上 B=下 L=左 (省略=自動)
        d.rectangle((x0, y0, x1, y1), outline=RED, width=lw)
        if num:
            cx, cy = x0, y0
            d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=RED)
            d.text((cx, cy), num, fill="white", font=f_num, anchor="mm")
        if label:
            tw = d.textlength(label, font=f_lab); th = f_lab.size + 10
            bw = tw + 12
            if pos == "B":
                lx = x0; ly = y1 + 8
            elif pos == "A":
                lx = x0 + r + 6; ly = y0 - th - 6
            elif pos == "L" or (not pos and x0 - r - 10 - bw >= 0 and x0 > W * 0.35):
                # 左側有空間:標籤放在框的左邊,垂直置中
                lx = x0 - r - 10 - bw; ly = (y0 + y1) // 2 - th // 2
            else:
                lx = x0 + r + 6; ly = y0 - th - 6
                if ly < 0: ly = y1 + 6
                if lx + bw > W: lx = max(0, W - bw)
            d.rectangle((lx, ly, lx + bw, ly + th), fill=RED)
            d.text((lx + 6, ly + 5), label, fill="white", font=f_lab)
    im.save(dst)
    print("saved", dst, im.size)

if __name__ == "__main__":
    main()
