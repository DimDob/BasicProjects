from tkinter import *
import sys


def click():
    global t
    t = txt.get()
    wnd.destroy()


def reject():
    global t
    t = ''
    wnd.destroy()

cancel = False


def goodbye():
    wnd = Tk()
    wnd.geometry('320x100')
    wnd.resizable(False, False)
    lbl = Label(master=wnd, text=f'Довиждане', relief=GROOVE)
    lbl.configure(font=fnt_1)
    lbl.place(x=10, y=10, height=40, width=300)

    btn = Button(master=wnd, text='Изход')
    btn.configure(font=fnt_3)
    btn.configure(command=wnd.destroy)
    btn.place(x=110, y=60, width=100, height=30)
    return wnd


def create():
    global txt

    wnd = Tk()
    wnd.geometry('300x150')
    wnd.title('Добре дошли')

    lbl = Label(master=wnd, text='Как е Вашето име?')  # в променлива lbl създавам обект на етиката
    lbl.configure(font=fnt_1)
    lbl.place(x=10, y=20)  # този метод поставя етикета в прозореца

    txt = Entry(master=wnd, width=30)
    txt.place(x=10, y=50)

    ok_button = Button(master=wnd, text='Ok')
    ok_button.configure(font=fnt_3)
    ok_button.place(x=10, y=80, width=100, height=30)
    ok_button.configure(command= click)

    reject_button = Button(master=wnd, text='Отмяна')
    reject_button.configure(font=fnt_3)
    reject_button.place(x=120, y=80, width=100, height=30)
    reject_button.configure(command=reject)
    return wnd




fnt_1 = ('Arial',13, 'bold')
fnt_2 = ('Arial',13, 'italic')
fnt_3 = ('Arial', 10, 'bold')



def result_window():
    msg = Tk()
    msg.title('Регистрацията е успешна.')
    msg.geometry('320x100')
    msg.resizable(False, False)

    lbl = Label(master = msg, text = f'Добре дошли, {t}!', relief = GROOVE)

    lbl.configure(font = fnt_1)
    lbl.place(x = 10, y = 10, height = 40, width = 300)

    btn = Button(master = msg, text = 'Ok')
    btn.configure(font = fnt_3)
    btn.configure(command = msg.destroy)
    btn.place(x = 110, y = 60, width = 100, height = 30)
    return msg.mainloop()



def error_window():
    exception_wnd = Tk()
    exception_wnd.title('Регистрацията не е успешна.')
    exception_wnd.geometry('320x100')
    exception_wnd.resizable(False, False)

    lbl = Label(master=exception_wnd, text=f'Моля въведете валидно име', relief=GROOVE)
    lbl.configure(font=fnt_1)
    lbl.place(x=10, y=10, height=40, width=300)

    btn = Button(master=exception_wnd, text='Връщане')
    btn.configure(font=fnt_3)
    btn.configure(command=exception_wnd.destroy)
    btn.place(x=110, y=60, width=100, height=30)
    exception_wnd.mainloop()



t = ''
def error_wndw_throw():
    error_window()
    wnd = create()
    wnd.mainloop()


try:
    wnd = create()
    wnd.mainloop()
    if len(t) == 0:
        goodbye().mainloop()
        sys.exit()

    if len(t.split()) >= 2:

        first_name, second_name = t.split()
        first_condition = (first_name is not None and second_name is not None)
        second_condition = len(first_name) >= 1 and len(second_name) >= 1
        third_condition = ''.join(t)
        fourth_condition = third_condition.replace(" ", "").isalpha()
        if first_condition and second_condition and third_condition and fourth_condition:
            result_window()
        else:
            error_window()
            wnd = create()
            wnd.mainloop()
    elif len(t) == 1 or not t.isalpha() or t.isdigit() or t.isspace() or len([t]) == 1 or not t.lower().isalpha():
        error_window()
        wnd = create()
        wnd.mainloop()

except ValueError:
    error_window()
    wnd = create()
    wnd.mainloop()







