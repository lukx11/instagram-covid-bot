from PIL import Image, ImageDraw, ImageFont
import datetime
import requests
from sys import platform
import random
import os
from instabot import Bot
bot = Bot()
bot.login(username="USERNAME", password="PASSWORD", ask_for_code=True, use_cookie=False)
response = requests.get("https://corona-api.com/countries/PL")
dzisiajzarazonych = response.json()['data']['today']['confirmed']
print(dzisiajzarazonych)
if platform == 'win32':
    fnt = ImageFont.truetype(r"/Windows/Fonts/Arial.ttf", 200)
else:
    fnt = ImageFont.truetype(r"/Library/Fonts/Arial.ttf", 200)
losuj = random.randint(1,4)
#dzisiajzarazonych = 9902 #w razie awarii api
im1 = Image.open('cov'+str(losuj)+'.jpg')
im1 = Image.open('cov4.jpg')

img = im1.resize((1080,1080))
d = ImageDraw.Draw(img)
img_name = "{:%d-%m-%Y}.jpeg"
img_name = img_name.format(datetime.datetime.now())
img.save(img_name)
imgg =Image.open(img_name)
imgg.paste(im1)
draw = ImageDraw.Draw(imgg)
w, h = d.textsize(str(dzisiajzarazonych), font=fnt)
draw.text(((1080 - w) / 2, (1080 - h) / 2), str(dzisiajzarazonych), font=fnt, fill=(255, 255, 255))
imgg.save(img_name)

bot.upload_photo(img_name, caption='Dzisiaj, '+img_name[:-5]+' mamy '+str(dzisiajzarazonych)+' nowych i potwierdzonych przypadków zakażenia koronawirusem #koronawirus #raport #covid #covid19 #raport #zakazeni #poland #polska #polska #poland #polish #polis #korona #koronavírus #koronaferie #koronavirüsü #koronawiruspolska #koronavirus_2020_news #koronawiruswpolsce #koronawirusfakty')
