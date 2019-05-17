from tkinter import*
import json

root = Tk()
root.geometry('720x185')
root.title('Менеджер задач')
text = Text(width=55, height=11,background="oldlace")
text.grid(row=0,rowspan=6,column=3)
text.configure(state=DISABLED)
root.configure(background="white")

try:
    o = open("tasks.json", 'r')
    js_data = json.load(o)
    o.close()
except Exception:
    d = open("tasks.json", 'w')
    d.close()
    js_data = []
    
def newtask():
    myfile = open("tasks.json", 'w')
    y = [{
        'task: ': z.get(),
        'category: ': k.get(),
        'time: ': t.get()
        }]
    global js_data
    m = js_data+y
    js_data = m
    json.dump(m,myfile)
    myfile.close()

def outoftask():
    try:
        text = Text(width=55, height=11,background="oldlace")
        text.grid(row=0,rowspan=6,column=3)
        f = open("tasks.json", 'r', encoding='utf-8')
        js2_data = json.load(f)
        text.configure(state=NORMAL)
        for line in reversed(js2_data):
            text.insert(1.0, 'Задача: '+line['task: ']+' Категория: '+line['category: ']+' Время: '+line['time: ']+'\n')
        text.configure(state=DISABLED)
        f.close()
    except Exception:
        text = Text(width=55, height=11,background="oldlace")
        text.grid(row=0,rowspan=6,column=3)
        text.configure(state=NORMAL)
        text.insert(1.0,'Список пуст')
        text.configure(state=DISABLED)
 
Label(text="Задача: ",background="white",font="AmericanTypewritr 12").grid(row=0, column=0)
z = table_name = Entry(width=30,background="oldlace")
table_name.grid(row=0, column=1)

Label(text="Категория: ",background="white",font="AmericanTypewritr 12").grid(row=1, column=0)
k = table_name = Entry(width=30,background="oldlace")
table_name.grid(row=1, column=1)

Label(text="Время: ",background="white",font="AmericanTypewritr 12").grid(row=2, column=0)
t = table_name = Entry(width=30,background="oldlace")
table_name.grid(row=2, column=1)

button1 = Button(text="Добавить",font="AmericanTypewritr 12",background="ivory", command=newtask).grid(row=3, column=0, columnspan=2)
button2 = Button(text="Список задач",font="AmericanTypewritr 12",background="ivory", command=outoftask).grid(row=4, column=0, columnspan=2)
button3 = Button(text="Выход",font="AmericanTypewritr 12",background="ivory", command=root.destroy).grid(row=5, column=0, columnspan=2)

root.mainloop()

