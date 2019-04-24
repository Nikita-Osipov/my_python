from tkinter import *

def click():
    global y
    try:
        s = int(entry.get())
        y = 4/3*(3.14*s*s*s)
        label.config(text = y)
    except Exception as err:
        print(err)

def save():
    f = open('text.txt','w')
    f.write(str(y))

def html():
    Html_file = open('filename','w')
    Html_file.write(str(y))

    
window = Tk()
convas = Canvas(window)
convas.pack()
window.title('Sphere V')

frame = Frame(window)
frame.pack()

entry = Entry(frame)
entry.pack()

label = Label(frame)
label.pack()

var = StringVar(window)
var.set("Выберите способ сохранения") # initial value

option = OptionMenu(window, var, "text","HTML")
option_window = convas.create_window(147, 90, anchor=NW, window=option)
option.update()


def ok():
    if var.get() == "text":
        save()
    elif var.get() == "HTML":
        html()
    window.quit()

button1 = Button(text = 'Вычислить', command = click)
button1.configure(width = 0, activebackground = "#D2D2D2")
button1_window = convas.create_window(150, 10, anchor=NW, window=button1)
button1.update()

      
button2 = Button(text='Сохранить', command = ok)
button2.configure(width = 0, activebackground = "#D2D2D2")
button2_window = convas.create_window(150, 50, anchor=NW, window=button2)
button2.update()

window.mainloop()
