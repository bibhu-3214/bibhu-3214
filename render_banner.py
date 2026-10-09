from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import math

ROOT = Path(__file__).parent
W, H = 1400, 490
BG = '#0C111B'
GOLD = '#C9AE7B'
IVORY = '#F4F0E8'
MUTED = '#A7B1C0'
def font(size, bold=False, mono=False):
    family = 'DejaVuSansMono' if mono else 'DejaVuSans'
    return ImageFont.truetype('/usr/share/fonts/truetype/dejavu/'+family+('-Bold' if bold else '')+'.ttf', size)
base = Image.new('RGB',(W,H),BG)
d = ImageDraw.Draw(base)
d.rounded_rectangle((1,1,W-2,H-2),radius=24,outline='#2B3443',width=2)
d.rectangle((58,57,94,60),fill=GOLD)
d.text((110,47),'BPS  /  FRONTEND ENGINEERING',font=font(17,mono=True),fill=GOLD)
d.text((56,116),'Bibhu Prasad',font=font(64,True),fill=IVORY)
d.text((56,193),'Sahu.',font=font(64,True),fill=IVORY)
d.text((60,288),'Complex workflows.',font=font(28),fill=MUTED)
d.text((60,331),'Clear interfaces.',font=font(28),fill=IVORY)
d.line((60,401,1338,401),fill='#2B3443',width=1)
d.text((60,430),'REACT   /   REDUX   /   JAVASCRIPT',font=font(17,mono=True),fill=MUTED)
d.text((1100,430),'BIBHU-3214',font=font(17,mono=True),fill=GOLD)
# An abstract interface composition, not a product screenshot.
for x in range(862,1340,36):
    for y in range(70,370,36):
        d.ellipse((x,y,x+1,y+1),fill='#293345')
d.rounded_rectangle((932,74,1297,333),radius=15,fill='#121B29',outline='#384459',width=2)
d.line((932,113,1297,113),fill='#384459',width=1)
for x,c in [(953,'#C9AE7B'),(971,'#66748B'),(989,'#66748B')]:
    d.ellipse((x,90,x+6,96),fill=c)
d.text((954,137),'interface / architecture',font=font(14,mono=True),fill=MUTED)
d.rounded_rectangle((954,177,1273,210),radius=6,fill='#1D2A3E')
d.rectangle((968,189,1166,193),fill='#70849C')
d.rounded_rectangle((954,225,1105,294),radius=6,fill='#1A2535')
d.rounded_rectangle((1121,225,1273,294),radius=6,fill='#1A2535')
d.rectangle((968,243,1067,247),fill='#66748B')
d.rectangle((1135,243,1241,247),fill='#66748B')
d.rectangle((968,265,1029,268),fill='#384A62')
d.rectangle((1135,265,1197,268),fill='#384A62')
d.rounded_rectangle((853,303,1131,371),radius=12,fill='#172132',outline='#4D5563',width=1)
d.text((876,326),'< thoughtful systems />',font=font(16,mono=True),fill=GOLD)
base.save(ROOT/'assets/profile-banner.png')
frames=[]
for i in range(48):
    frame=base.copy(); draw=ImageDraw.Draw(frame)
    # Slow, understated progress along the top window edge; typography never moves.
    x=949 + int(330*i/47)
    draw.line((949,115,x,115),fill=GOLD,width=2)
    draw.ellipse((x-3,112,x+3,118),fill=IVORY)
    frames.append(frame)
frames[0].save(ROOT/'assets/profile-banner.gif',save_all=True,append_images=frames[1:],duration=[90]*47+[1100],loop=0,optimize=True,disposal=1)
print('Banner rendered:', (ROOT/'assets/profile-banner.gif').stat().st_size, 'bytes; 48 frames')
for number,title,subtitle,name in [
    ('01','Bill Management','CUSTOMERS  /  PRODUCTS  /  BILLING','project-billing.png'),
    ('02','Identity & Notes','AUTHENTICATION  /  PERSONAL WORKSPACE','project-notes.png')]:
    card=Image.new('RGB',(700,215),BG); cd=ImageDraw.Draw(card)
    cd.rounded_rectangle((1,1,698,213),radius=16,outline='#2B3443',width=2)
    cd.text((32,26),'SELECTED WORK  /  '+number,font=font(15,mono=True),fill=GOLD)
    cd.text((29,76),title,font=font(37,True),fill=IVORY)
    cd.text((32,157),subtitle,font=font(13,mono=True),fill=MUTED)
    cd.line((32,194,668,194),fill='#2B3443',width=1)
    cd.line((32,194,104,194),fill=GOLD,width=2)
    card.save(ROOT/'assets'/name)
