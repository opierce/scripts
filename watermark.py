#!/usr/bin/env python3
# coding: utf-8

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import time
import sys
from pathlib import Path
from stegano import lsb

def watermark_text(input_image_path, output_image_path, text):
    photo = Image.open(input_image_path)
    origin_x, origin_y, width, height = photo.getbbox()
    xPos = width - 400
    yPos = height - 50

    # make the image editable
    drawing = ImageDraw.Draw(photo)
    shadow_color = (0, 0, 0)
    text_color = (255, 255, 255)
    font = ImageFont.truetype("/Library/Fonts/Futura.ttc", 40)

    # draw thin border
    drawing.text((xPos-2, yPos), text, font=font, fill=shadow_color)
    drawing.text((xPos+2, yPos), text, font=font, fill=shadow_color)
    drawing.text((xPos, yPos-2), text, font=font, fill=shadow_color)
    drawing.text((xPos, yPos+2), text, font=font, fill=shadow_color)

    # draw true text
    drawing.text((xPos, yPos), text, fill=text_color, font=font)

    # preview and save image
    photo.show()
    photo.save(output_image_path)
    secret = lsb.hide(output_image_path, '© ' + time.strftime("%Y") + ' Owen Pierce')
    secret.save(output_image_path)
    # print(lsb.reveal(output_image_path))

if __name__ == '__main__':
    img_path = sys.argv[1]
    output_path = Path(img_path).stem + '_watermarked' + Path(img_path).suffix
    watermark_text(img_path, output_path,
                   text='© ' + time.strftime("%Y") + ' Owen Pierce')
