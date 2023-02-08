import os.path
from datetime import datetime
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
import platform

OS = platform.system()
BASE_DIR = Path(__file__).resolve().parent.parent

def do_timestamp(path):
    im = Image.open(path)
    width, height = im.size
    draw = ImageDraw.Draw(im)
    text = str(datetime.now().strftime('%Y-%m-%d'))
    if OS == 'Windows':
        font = ImageFont.truetype('arial.ttf', 36)
    else:
        font = ImageFont.truetype(os.path.join(BASE_DIR, 'static/fonts/COMICZ.TTF'), 36)
    textwidth, textheight = draw.textsize(text, font)
    margin = 20
    x = width - textwidth - margin
    y = height/2 - textheight + margin
    draw.text((x, y), text, font=font)
    im.save(path)