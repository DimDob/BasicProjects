from tkinter import Tk, Label, GROOVE, Button
from tkinter.ttk import Combobox


class Craft():

    @staticmethod
    def crafting_window():
        window = Tk()
        window.title("Езици за програмиране")
        window.geometry('220x300')
        window.resizable(False, False)
        return window

    @staticmethod
    def crafting_combobox(names, window, font, index):
        cb = Combobox(window, state='readonly')
        cb.configure(values=names)
        cb.current(index)
        cb.configure(font=font)
        return cb

    @staticmethod
    def crafting_label(window, imgs, index):
        label = Label(window, image=imgs[index])
        label.configure(relief=GROOVE)
        label.place(x=10, y=10, width=200, height=200)
        return label


    @staticmethod
    def crafting_button(window):
        button = Button(window, text='Ok')
        button.configure(command=window.destroy)
        button.place(x=60, y=260, width=100, height=30)
        return button