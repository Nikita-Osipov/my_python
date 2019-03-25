def calc(x,y):
    s = input('Введите оператор: ')
    if s == '+':
        print(x+y)
    elif s == '-':
        print(x-y)
    elif s == '*':
        print(x*y)
    elif s == '/':
        try:
            print(x/y)
        except ZeroDivisionError:
            print('Ошибка деления на ноль')
    else:
        print('Неизвестный оператор')
