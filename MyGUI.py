import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        self.label1 = tkinter.Label(self.top_frame,text='Стивен Маркус\n274 Бэйли\nУэйнзвилль,Северная Каролина 27999')
        self.label1.pack(side='left')

        self.button1 = tkinter.Button(self.bottom_frame,text='Показать инфо',command=self.show)
        self.button2 = tkinter.Button(self.bottom_frame,text='Выйти',command=exit)

        self.button1.pack(side='left')
        self.button2.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()
        
        tkinter.mainloop()
    def show(self):
        tkinter.messagebox.showinfo('ИНФОРМАЦИЯ', 'ИНФОРМАЦИЯ')

my_gui = MyGUI()
