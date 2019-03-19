lst = []
while True:
    print('Простой todo:\n1. Добавить задачу.\n2. Вывести список задач.\n3. Выход. ')
    s = int(input('Укажите число: '))
    if s == 1:
        t = input('Сформулируйте задачу: ')
        k = input('Добавьте категорию к задаче: ')
        u = input('Добавьте время к задаче: ')
        l = 'Задача: '+t+' Категория: '+k+' Дата: '+u
        lst.append(l)
    elif s == 2:
        for i in lst:
            print(i)
    elif s == 3:
        print('Выход из программы!')
        break
    
        
