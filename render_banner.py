"""Original geometric motion system. Run with Python 3 + Pillow >= 10.
No external images/fonts downloaded. GIFs play once (6s); PNG fallbacks included.
"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import math, os
ROOT = Path(__file__).parent
W,H=1200,560
BG='#080e20'; PANEL='#101c36'; LINE='#253959'; BLUE='#497cff'; CYAN='#8edbff'; WHITE='#f2f6ff'; MUTED='#a7b9d7'
def font(n,bold=False):
    candidates=[os.environ.get('PROFILE_FONT_BOLD' if bold else 'PROFILE_FONT',''), '/System/Library/Fonts/Supplemental/Arial'+(' Bold' if bold else '')+'.ttf','/usr/share/fonts/truetype/dejavu/DejaVuSans'+('-Bold' if bold else '')+'.ttf']
    for p in candidates:
        if p and Path(p).exists(): return ImageFont.truetype(p,n)
    raise RuntimeError('Set PROFILE_FONT and PROFILE_FONT_BOLD to local TTF fonts')
def txt(d,xy,s,n=24,c=WHITE,b=False): d.text(xy,s,font=font(n,b),fill=c)
def box(d,xy,fill=PANEL,outline=LINE,r=16): d.rounded_rectangle(xy,r,fill=fill,outline=outline,width=2)
def base(h=H):
    im=Image.new('RGB',(W,h),BG); d=ImageDraw.Draw(im)
    for x in range(0,W,40): d.line((x,0,x,h),fill='#0e1830')
    for y in range(0,h,40): d.line((0,y,W,y),fill='#0e1830')
    d.rectangle((0,0,7,h),fill=BLUE)
    return im,d
def hero(t):
    im,d=base(); txt(d,(48,38),'BPS / FRONTEND ENGINEERING',22,CYAN,True)
    txt(d,(45,94),'Bibhu Prasad Sahu',62,WHITE,True)
    txt(d,(48,174),'Complex workflows. Clear interfaces.',31,MUTED)
    # A code-to-state-to-interface scene; labels stay fixed and readable.
    for x,label in [(48,'01 / COMPONENT'),(443,'02 / STATE'),(838,'03 / INTERFACE')]:
        box(d,(x,256,x+310,460)); txt(d,(x+22,276),label,20,CYAN,True)
    for k,(s,c) in enumerate([('<Workspace>',CYAN),('  state → view',WHITE),('  onAction()',MUTED),('</Workspace>',CYAN)]): txt(d,(70,320+k*28),s,23,c)
    for k,s in enumerate(['input','update','render']):
        y=326+k*39; d.ellipse((468,y,479,y+11),fill=BLUE if t>=k*.24 else LINE); txt(d,(494,y-6),s,24)
        d.line((620,y+6,720,y+6),fill=LINE,width=5)
        d.line((620,y+6,620+int(100*min(1,max(0,(t-k*.2)*2))),y+6),fill=BLUE,width=5)
    box(d,(861,324,1125,354),fill='#203863',r=6)
    for k in range(3):
        x=861+k*91; box(d,(x,373,x+80,432),r=7)
        hh=int(12+28*(.5+.5*math.sin(t*math.pi*2+k)))
        d.rectangle((x+14,418-hh,x+66,418),fill=BLUE if k!=1 else CYAN)
    for start in [361,756]:
        d.line((start,358,start+77,358),fill=LINE,width=2)
        x=start+int(77*t); d.ellipse((x-5,353,x+5,363),fill=CYAN)
    txt(d,(48,500),'REACT / REDUX / JAVASCRIPT',23,MUTED)
    txt(d,(907,500),'BUILD WITH INTENT',19,CYAN)
    return im

def project(t,forma=False):
    im,d=base(400); title='Forma' if forma else 'BillFlow'
    txt(d,(46,30),'02 / SELECTED WORK' if forma else '01 / SELECTED WORK',21,CYAN,True)
    txt(d,(43,76),title,62,WHITE,True)
    txt(d,(46,157),'Recruitment workspace' if forma else 'Billing workspace',28,MUTED)
    txt(d,(46,216),'React + TypeScript' if forma else 'React + Redux',24,WHITE)
    txt(d,(46,324),'FRONTEND DEMO / LOCAL DATA',20,CYAN)
    box(d,(550,35,1150,362))
    txt(d,(578,58),'CANDIDATE JOURNEY' if forma else 'CUSTOMER → INVOICE',22,CYAN,True)
    labels=['Intake','Review','Shortlist'] if forma else ['Customer','Items','Invoice']
    for k,label in enumerate(labels):
        x=580+k*184
        box(d,(x,113,x+158,270),fill='#172744',r=12)
        txt(d,(x+15,132),label,22,WHITE,True)
        if forma:
            d.ellipse((x+53,179,x+89,215),fill=BLUE)
            d.rounded_rectangle((x+36,223,x+107,239),8,fill='#355480')
        else:
            for j in range(3): d.rounded_rectangle((x+18,183+j*22,x+130-j*16,190+j*22),3,fill=BLUE if j==0 else '#355480')
    d.line((598,308,1102,308),fill=LINE,width=3)
    x=598+int(504*t); d.line((598,308,x,308),fill=BLUE,width=3); d.ellipse((x-7,301,x+7,315),fill=CYAN)
    txt(d,(578,331),'ILLUSTRATIVE WORKFLOW',16,MUTED)
    return im

def save(name,fn):
    frames=[fn(i/59) for i in range(60)]
    frames[0].save(ROOT/'assets'/f'{name}.png')
    # Fixed palette eliminates frame-to-frame color shimmer; delta frames reduce size.
    palette=frames[0].quantize(colors=96)
    frames=[f.quantize(palette=palette,dither=Image.Dither.NONE) for f in frames]
    frames[0].save(ROOT/'assets'/f'{name}.gif',save_all=True,append_images=frames[1:],duration=100,optimize=True,disposal=1)
    print(name,(ROOT/'assets'/f'{name}.gif').stat().st_size)
if __name__=='__main__':
    save('profile-cobalt',hero)
    save('billflow-cobalt',project)
    save('forma-cobalt',lambda t:project(t,True))
