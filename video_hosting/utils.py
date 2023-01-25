from datetime import datetime
from PIL import Image, ImageDraw, ImageFont


def do_timestamp(path):
    im = Image.open(path)
    width, height = im.size
    draw = ImageDraw.Draw(im)
    text = str(datetime.now().strftime('%Y-%m-%d'))
    font = ImageFont.truetype('arial.ttf', 36)
    textwidth, textheight = draw.textsize(text, font)
    margin = 20
    x = width - textwidth - margin
    y = height/2 - textheight + margin
    draw.text((x, y), text, font=font)
    im.save(path)