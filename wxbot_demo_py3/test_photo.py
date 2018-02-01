#!/usr/bin/env python3
# coding:utf-8

import os
import sys
import datetime
import uuid

import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def set_watermark(image_file, text):
    img = Image.open(image_file)
    (img_x, img_y) = img.size

    print(os.path.basename(image_file))
    # 文字字体像素高度为图片高度的 1/20
    fontSzie = 1
    ttfont = ImageFont.truetype("yahei.ttf", fontSzie, encoding='unic')
    while ttfont.getsize(text)[0] < 0.3*img_x:
        fontSzie = fontSzie+1
        ttfont = ImageFont.truetype("yahei.ttf", fontSzie, encoding='unic')

    draw = ImageDraw.Draw(img)
    draw.text((int(img_x/4), 0), text, (100, 100, 0), font=ttfont)

    newdir = os.path.join("saved", "msgimgs", "revoke")
    if not os.path.exists(newdir):
        os.mkdir(newdir)

    img.save(newdir + '/' + '1.jpg', 'jpeg')


if __name__ == '__main__':
    set_watermark("C:\\Users\\lijiyang\\Pictures\\2.jpg", u"李继阳撤回的"+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
