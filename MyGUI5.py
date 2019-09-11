import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
 
        self.radio_var = tkinter.IntVar()
 
        self.radio_var.set(1)

        self.rb1 = tkinter.Radiobutton(self.top_frame,text='Дневное время (6:00 - 17:59)',variable=self.radio_var,value=1)
        self.rb2 = tkinter.Radiobutton(self.top_frame,text='Вечернее время (18:00 - 23:59)',variable=self.radio_var,value=2)
        self.rb3 = tkinter.Radiobutton(self.top_frame,text='Непиковый период (00:00 - 5:59)',variable=self.radio_var,value=3)

        self.inMin = tkinter.Label(self.top_frame,text='Введите количество минут:')
        self.minGet = tkinter.Entry(self.top_frame,width=10)

        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        self.inMin.pack(side='left')
        self.minGet.pack(side='left')

        self.showRes_button = tkinter.Button(self.bottom_frame,text='Показать стоимость',command=self.show_choice)
        self.quit_button = tkinter.Button(self.bottom_frame,text='Выйти',command=self.main_window.destroy)

        self.showRes_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def show_choice(self):
        if self.radio_var.get() == 1:
            res = int(self.minGet.get())*10/100
        elif self.radio_var.get() == 2:
            res = int(self.minGet.get())*12/100
        else:
            res = int(self.minGet.get())*5/100
            
        tkinter.messagebox.showinfo('Общая стоимость', 'Ваши затраты ' + '$' + str(res))

my_gui = MyGUI()
