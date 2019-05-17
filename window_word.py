from tkinter import*
import random
root = Tk()
pets = dict()
pets = {'dog':'собака','cat':'кот','rabbit':'кролик'}
p = random.choice(['dog','cat','rabbit'])
def answ():
    if pets[p]==f.get():
        y = 'Угадали!'
    else:
        y = 'Неверно'
    Label(text=y).grid(row=5, column=0)

 
Label(text='Случайное слово:').grid(row=0, column=0)
Label(text=p).grid(row=1, column=0)
Label(text='Укажите перевод слова:').grid(row=2, column=0)
Button(text='Готово!',command=answ).grid(row=6,column=0)
f = table_name = Entry(width=30)
table_name.grid(row=4, column=0)
Button(text='Выход',command=root.destroy).grid(row=7,column=0)

root.mainloop()
