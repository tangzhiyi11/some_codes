#!/usr/bin/env python
# coding=utf-8

from PIL import Image, ImageDraw, ImageFont

if __name__ == '__main__':
    image = Image.open("test.jpg")
    draw = ImageDraw.Draw(image)
    my_font = ImageFont.truetype('test.ttf', size=40)
    fillcolor = '#ff0000'
    width, height = image.size
    draw.text((width-40, 0), '99', font=my_font, fill=fillcolor)
    image.save('result.jpg')

