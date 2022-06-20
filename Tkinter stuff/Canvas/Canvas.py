from tkinter import *
from math import *

def msEnter(env):
    cnv.itemconfig(Pct, image = img_2)

def msLeave(evt):
    cnv.itemconfig(Pct, image = img_1)
    cnv.delete('ln')

def msMotion(evt):
    x = evt.x
    y = evt.y

    cnv.delete('ln')
    cnv.create_line(x,5,x,H-5,fill = clr_C1, width=2,tag = 'ln')
    cnv.create_line(5,y,W-5,y,fill = clr_C1, width =2 , tag='ln')
    Rxy = cnv.coords(Rtn)
    Cxy = cnv.coords(Crl)

    x0=(Cxy[2] + Cxy[0])/2
    y0 = (Cxy[3] + Cxy[1])/2

    r = sqrt((x-x0)**2 + (y-y0)**2)


    if r < R:
        cnv.itemconfig(Crl,fill = clr_C2)
        cnv.itemconfig(Rtn, fill = clr_C1)
        return
    else:
        cnv.itemconfig(Crl,fill=clr_C1)

    if x > Rxy[0] and x < Rxy[2] and y > Rxy[1] and y < Rxy[3]:
        cnv.itemconfig(Rtn, fill = clr_R2)
    else:
        cnv.itemconfig(Rtn, fill = clr_R1)

def msUp(evt):
    cnv.move('Lns',0,-1)
    cnv.move(Crl,0,3)

def msDown(evt):
    cnv.move('Lns',0,1)
    cnv.move(Crl,0,-3)

def msLeft(evt):
    cnv.move(Txt,-1,0)

def msRight(evt):
    cnv.move(Txt,1,0)

W = 600
H = 400

w = 200
h=100

N= 10
d = 20
R=30
fnt = ('Arial',20,'bold')

txt = 'Син текст'
clr = 'lightgreen'
clr_1 = 'lightyellow'
clr_2 = 'yellow'

clr_C1 = 'red'
clr_C2 = 'white'

clr_R1 = 'white'
clr_R2 = 'green'


wnd= Tk()
wnd.geometry(str(W+1) + 'x' + str(H+10) + '+400+300')
wnd.title('Графика')
wnd.resizable(False,False)
cnv = Canvas(wnd, bg= clr_1, bd= 3 , relief = GROOVE)
cnv.place(x=5,y=5,width = W, height = H)
cnv.focus_set()
Txt = cnv.create_text(W/2,50,text = txt, font = fnt, fill = 'blue')
for k in range(N):
    x1 = 70+k*d
    y1= H/4 + 10*k
    x2=W-70-d*k
    y2=H/4+10*k
    cnv.create_line(x1,y1,x2,y2,fill = clr, width = 5, tag = 'Lns')


x1 = W/2-R
y1=H/2-R+30
x2=W/2+R
y2=H/2+R+30
Crl = cnv.create_oval(x1,y1,x2,y2,fill = clr_C1)

x1=20
y1=H-h-20
x2=x1+w
y2=y1+h

Rtn=cnv.create_rectangle(x1,y1,x2,y2,fill = clr_C2)


img_1 = PhotoImage(file = "C:\\Users\\amd\\Desktop\\faces\\sad.png")
img_2 = PhotoImage(file = "C:\\Users\\amd\\Desktop\\faces\\smiley.png")


Pct = cnv.create_image(W-20,H-20,anchor = SE, image = img_1)
cnv.bind('<Left>', msLeft)
cnv.bind('<Right>', msRight)
cnv.bind("<Up>", msUp)
cnv.bind('<Down>', msDown)
cnv.bind('<Enter>', msEnter)
cnv.bind('<Leave>', msLeave)
cnv.bind("<Motion>", msMotion)
cnv.bind('<Button-1>', lambda evt: cnv.config(bg = clr_2))
cnv.bind('<Button-3>', lambda evt: cnv.config(bg = clr_1))

wnd.mainloop()