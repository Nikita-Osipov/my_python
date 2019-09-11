import tkinter

class KiloConverterGUI:
    def __init__(self):

        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.mid2_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        self.prompt_label1 = tkinter.Label(self.top_frame,text='Введите количество галлонов:')
        self.galon = tkinter.Entry(self.top_frame,width=10)

        self.prompt_label1.pack(side='left')
        self.galon.pack(side='left')

        self.prompt_label2 = tkinter.Label(self.mid_frame,text='Введите количество миль:')
        self.milll = tkinter.Entry(self.mid_frame,width=10)

        self.prompt_label2.pack(side='left')
        self.milll.pack(side='left')

        self.result = tkinter.Label(self.mid2_frame,text='Милли на галлон (MPG):')

        self.value = tkinter.StringVar()

        self.MpG = tkinter.Label(self.mid2_frame,textvariable=self.value)

        self.result.pack(side='left')
        self.MpG.pack(side='left')

        self.calc_button = tkinter.Button(self.bottom_frame,text='Преобразовать',command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame,text='Выйти',command=self.main_window.destroy)

        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.mid_frame.pack()
        self.mid2_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()


    def convert(self):
        gall = float(self.galon.get())
        ml = float(self.milll.get())
        MpG = ml / gall
        self.value.set(MpG)

kilo_conv = KiloConverterGUI()
