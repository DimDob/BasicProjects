from tkinter import *
from datetime import *
import random

def getCity():

    n = random.randint(0,5)
    cities = ['Sofiq',
              'Varna',
              'Plovdiv',
              'Silistra',
              'Smolyan',
              'Shumen']
    return cities[n]

def getName():
    global num

    name =  scale.get()
    return name

def getFont():
    name = getName()
    result = name, fnt_1
    return result


def setAll(*args):
    name, font = getFont()
    label.configure(font = font)


    txt = f'\nТекуща '
    txt += f" честота: {name}"

    text.set(txt)


fnt_1 = ['Times New Roman', 13, 'bold', 'italic']
fnt_2 = ['Arial', 12 , 'italic']
fnt_3 = ['Times New Roman', 12, 'bold', 'italic']
min_frequency = 70.0
max_frequency = 100.0

W = 800
H = 420

Hf = 100
Wl = W/3
Hl = 315

Hb = 60
Ws = W - Wl - 15
Hs = Hl - Hb - 5


wnd = Tk()
wnd.title('Радио')
wnd.geometry(str(W) + 'x' + str(H))
wnd.resizable(False, False)



frame_scale = Frame(wnd, bd=3, relief = GROOVE)
frame_text = Frame(wnd, bd = 3, relief = GROOVE)
frame_button = Frame(wnd, bd = 3, relief = GROOVE)
frame_list = Frame(wnd, bd = 3, relief = GROOVE)
frame_check = Frame(frame_list, bd = 3, relief = GROOVE)

text = StringVar()
bass= StringVar()
audio = StringVar()
media = StringVar()
frequency = StringVar()
city = getCity()



label = Label(frame_text, textvariable = text)


label_text = Label(frame_text, text = f'Радио {city}', font = fnt_2)
label_size = Label(frame_scale, text = 'Наствойване на честота:  ', font = fnt_2)

label.configure(bg = 'white', relief = RAISED)

radiobutton_1 = Radiobutton(frame_scale, text = 'Бас', variable = bass)
radiobutton_1.configure(font = fnt_2)

radiobutton_2 = Radiobutton(frame_scale, text = 'Аудио', variable = audio)
radiobutton_2.configure(font = fnt_2)

radiobutton_3 = Radiobutton(frame_scale, text = 'Медия', variable = media)
radiobutton_3.configure(font = fnt_2)

scale = Scale(frame_scale, orient = HORIZONTAL)
scale.configure(from_=min_frequency, to = max_frequency)

scale.configure(tickinterval = 2, resolution = 1)
scale.config(command = setAll)


setAll()

checkbutton_1 = Checkbutton(frame_check, text = 'Аудио', variable = audio)
checkbutton_1.configure(onvalue = '', offvalue = 'italic', font = fnt_1)

checkbutton_2 = Checkbutton(frame_check, text = 'Медия', variable = media)
checkbutton_2.configure(onvalue = '', offvalue = 'italic', font = fnt_1)

checkbutton_3 = Checkbutton(frame_check, text = 'Бас', variable = bass)
checkbutton_3.configure(onvalue = '', offvalue = 'italic', font = fnt_1)

listbox = Listbox(frame_list, selectmode = SINGLE, font = fnt_3)
listbox.configure(bg = 'gray96', selectbackground = 'gray')
listbox.configure(activestyle = 'none', height =5)

date = datetime.date(datetime.now())
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

listbox.insert(END,f"Днешна дата:{date}")
listbox.insert(END, f'Часът в момента: {current_time}')

listbox.select_set(0)

listbox.bind("<<ListboxSelect>>", setAll)

button = Button(frame_button, text = 'Exit', font = fnt_1)
button.configure(command = wnd.destroy)

label_text.pack(side = 'top',fill = 'x', padx = 5, pady = 5)
label.pack(side = 'top', fill = 'both', padx = 45, pady = 3)
scale.pack(side = 'bottom', fill = 'x', padx = 5, pady = 5)
label_size.pack(side = 'bottom', fill = 'x', padx = 5, pady = [25,5])

radiobutton_1.pack(side = 'left', fill = 'x', padx = 5, pady = 5)
radiobutton_2.pack(side = 'left', fill = 'x', padx = 5, pady = 5)
radiobutton_3.pack(side = 'left', fill = 'x', padx = 5, pady = 5)

checkbutton_1.pack(side = 'left', fill = 'x', padx = 5, pady = 5)
checkbutton_2.pack(side = 'left', fill = 'x', padx = 5, pady = 5)
checkbutton_3.pack(side = 'left', fill = 'x', padx = 5, pady = 5)

listbox.pack(side = 'top', fill = 'x', padx = 5, pady = 5)
button.pack(side= 'bottom', fill = 'x', padx = 50, pady = 10)


frame_text.place(x = 5, y = 5, width = W-10, height = Hf)
frame_check.pack(side = 'bottom', fill = 'both', padx = 5, pady =5)
frame_list.place(x = 5, y = Hf + 10, height = Hl, width = Wl)
frame_scale.place(x = Wl + 10, y = Hf + 10, width = Ws, height = Hs)
frame_button.place(x = Wl + 10, y = Hf + Hs + 15, width = Ws, height = Hb)

label.place(x = 5, y = 5, width = 800, height = 100)

wnd.mainloop()