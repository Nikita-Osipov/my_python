import tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        self.value = tkinter.StringVar()

        self.side = tkinter.Label(self.top_frame, textvariable=self.value)
        self.side.pack()
        
        self.button1 = tkinter.Button(self.bottom_frame,text='Лево',command=self.show0)
        self.button2 = tkinter.Button(self.bottom_frame,text='Центр',command=self.show1)
        self.button3 = tkinter.Button(self.bottom_frame,text='Право',command=self.show2)
        

        self.button1.pack(side='left')
        self.button2.pack(side='left')
        self.button3.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()        
        tkinter.mainloop()
        
    def show0(self):
        self.value.set('Лево')
    def show1(self):
        self.value.set('Центр')
    def show2(self):
        self.value.set('Право')


my_gui = MyGUI()
