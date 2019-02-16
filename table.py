atmn = input('Введите номер элемента n: ')
if atmn:
    n = float(atmn)
    if n == 3.0:
        print('Литий')
    elif n == 25:
        print('Марганец')
    elif n == 80:
        print('Ртуть')
    elif n == 17:
        print('Хлор')
    else:
        print('Что это?')
else:
    print('Введите значение n')
        
