import random
k = random.randint(1,4)
n = int(input('Введите число от 1 до 4 '))
if n == k:
    print('Победа')
elif n > k:
    print('Меньше введенного числа')
else:
    print('Больше введенного числа')

