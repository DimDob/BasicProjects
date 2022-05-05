from tkinter import *
from tkinter.messagebox import *

class MyApp:
    def __init__(self):
        self.setValues()
        self.makeMainWindow()
        self.setVars()
        self.makeMainMenu()
        self.makeToolBar()
        self.makeFrame()
        self.makePopupMenu()
        self.showMainWindow()


    def setValues(self):
        self.Width = 900
        self.Height = 500

        self.h = 50
        self.position = f'{self.Width}x{self.Height}'


        self.models = ['Ibiza', 'Leon', 'Ateca', 'Taracco']
        self.prices = ['12 000', '15 000', '250 000', '500 000']
        self.colors = ['red', 'black', 'orange', 'white', 'grey']

        self.imgFiles = ['ateca.png', 'ibiza.png', 'leon.png', 'taracco.png']
        self.path = 'C:\\Users\\amd\\Desktop\\models\\'

        self.font = ('Times New Roman', 12, 'bold', 'italic')


    def makeMainWindow(self):
        self.wnd = Tk()
        self.wnd.title('Избираме модел Seat')
        self.wnd.geometry(self.position)
        self.wnd.resizable(False,False)
    def showMainWindow(self):
        self.wnd.mainloop()


    def makeMainMenu(self):
        self.menubar = Menu(self.wnd)

        self.mModels = Menu(self.wnd, font = self.font, tearoff = 0) #TODO tearoff =  1
        self.mPrices = Menu(self.wnd, font = self.font, tearoff = 0)
        self.mColor = Menu(self.wnd, font = self.font, tearoff = 0)
        self.mAbout = Menu(self.wnd, font = self.font, tearoff = 0)
        self.Exit = Menu(self.wnd, font = self.font, tearoff = 0)


        self.mAbout.add_command(label = 'Характеристики на моделите', command = self.showDialog)
        self.mPrices.add_command(label = 'Цени на моделите', command = self.showPrices)
        self.mColor.add_command(label = 'Възможни цветове', command = self.showColors)
        self.mModels.add_command(label = 'Налични модели', command = self.showModels)
        self.Exit.add_command(label = 'Изход', command = self.clExit)

        self.menubar.add_cascade(label = 'Модели', menu = self.mModels)
        self.menubar.add_cascade(label = 'Цени', menu = self.mPrices)
        self.menubar.add_cascade(label = 'Възможни цветове на колите', menu = self.mColor)
        self.menubar.add_cascade(label = 'Характеристики', menu = self.mAbout)
        self.menubar.add_cascade(label = 'Изход', menu = self.Exit)

        self.wnd.config(menu = self.menubar)

    def makeToolBar(self):
        self.images = []
        self.buttons = []

        mt = [self.clBold, self.clBold, self.clItalic]
        self.toolbar = Frame(self.wnd, bd = 3, relief = RAISED)


        for img in self.imgFiles:
            self.images.append(PhotoImage(file = self.path + img))
            self.buttons.append(Button(self.toolbar, image = self.images[-1]))
            self.buttons[-1].pack(side = 'left', padx = 0, pady =0 )

        for current in range(len(mt)):
            self.buttons[current].configure(command = mt[current])


        self.toolbar.place(x = 2, y = 2, width = 895, height = 170)



    def makeFrame(self):
        txt = f'SEAT е испански производител на автомобили.' + '\n'\
              + 'Създаден през 1950 г. с подкрепата на FIAT, сега е изцяло собственост на Volkswagen Group.'+ '\n' \
              + 'Централата на компанията се намира в Марторей, Барселона.'
        self.frame = Frame(self.wnd, bd = 1, relief = RAISED)
        label = Label(self.frame, text = 'Автомобили Seat', font = ('Times New Roman', 16, 'bold', 'italic')).pack(side = 'top')
        self.lblText = Label(self.frame, textvariable = self.text, relief = RAISED)
        self.lblText.pack(side = 'top', fill = 'both', padx = 1, pady = 1)
        self.frame.place(x = 5, y = 180, width =890, height = 315)

        label2 = Label(label, text = txt, font = ('Arial Italic', 14) )
        label2.place(x =10, y = 300)



    def makePopupMenu(self):
        self.popup = Menu(self.wnd, tearoff = 0, font = self.font)

        self.popup.add_command(label = 'Изход от програмата', command = self.clExit)
        self.wnd.bind('<Button-3>', lambda x: self.popup.tk_popup(x.x_root, x.y_root))



    def setVars(self):
        self.text = StringVar()
        self.name = StringVar()
        self.bi = [BooleanVar(), BooleanVar()]
        self.size = IntVar()
        self.color = StringVar()


    def clExit(self):
        self.wnd.destroy()

    def clBold(self):
        self.bi[0].set(not self.bi[0].get())

    def clItalic(self):
        self.bi[1].set(not self.bi[1].get())

    def clNormal(self):
        self.bi[0].set(False)
        self.bi[1].set(False)

    def showDialog(self):
        characteristics = "Seat Ibiza - година: 2010, тип: Купе, конски сили: 85, двигател: 1.4" +\
                          '\n'+ 'Seat Ateca - година: 2011, тип: Хечбег, конски сили: 135, двигател: 1.5' +\
                          '\n' + 'Seat Leon - година: 2015, тип: Седан, конски сили: 185, двигател: 1.7' +'\n'\
                          + 'Seat Taracco - година: 2022, тип: Dvip, конски сили: 285, двигател: 1.9'



        showinfo('Характеристики на моделите', characteristics)
    def showColors(self):
        colors = 'Seat Ateca - оранжев' + '\n' +  'Seat Leon - червен ' + '\n' + 'Seat Ibiza - бял' + '\n' + 'Seat Taracco - сив'
        showinfo('Възможни цветове на колите', colors)


    def showPrices(self):
        prices = 'Seat Ateca - 50 000$' + '\n' + 'Seat Leon - 25 000$' + '\n' + 'Seat Ibiza - 15 000$' + '\n' + 'Seat Taracco - 250 000$'
        showinfo('Цени на моделите', prices)

    def showModels(self):
        models = 'Seat Ibiza SC' + '\n' + 'Seat Leon' + '\n' + 'Seat Ateca' + '\n' + 'Seat Taracco'
        showinfo('Налични модели', models)

MyApp()


