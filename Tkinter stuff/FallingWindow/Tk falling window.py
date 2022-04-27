from tkinter import *
from crafting import Craft


def change(x):
    txt = combobox.get()

    for k in range(len(names)):
        if names[k] == txt:
            label.configure(image=imgs[k])
            break



fnt_1 = ('Times New Roman', 11, 'bold')

path = "C:\\pictures\\OOPlangs\\"
names = ['C#', 'JavaScript', 'Java', 'Python']
files = ['c#.png', 'js.png', 'java.png', 'python.png']

window = Craft.crafting_window()

imgs = [PhotoImage(file = path + png_name) for png_name in files]

i  = 0

label = Craft.crafting_label(window, imgs, i)
combobox = Craft.crafting_combobox(names, window, fnt_1, i)

combobox.bind('<<ComboboxSelected>>', change)
combobox.place(x = 10, y = 220, width = 200, height = 30)

button = Craft.crafting_button(window)

window.mainloop()