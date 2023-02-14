#!/usr/bin/env python3

from PIL import Image, ImageDraw, ImageFont

OUTPUT_PATH = 'Stamped'

# image parameters
PAD_RATIO = 0.05

def main():

	with Image.open("test.jpg") as img:

		pad = PAD_RATIO * max(img.width, img.height)
		draw = ImageDraw.Draw(img)
		text_to_write = '21  JAN  2023'
		font = ImageFont.truetype("Tahoma.ttf", 48)
		draw.text((img.width - pad, img.height - pad), text_to_write, font=font, fill=(255, 119, 51), stroke_width=1, anchor='rb')
		img.show()

    #im.save("out", "jpg")

main()