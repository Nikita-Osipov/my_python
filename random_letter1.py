import random
dw = ['самовар','весна','лето']
n = random.choice(dw)
i = n.index(random.choice(n))
n1 = list(n)
n1[i] = '?'
n1 = ''.join(n1)
print(n1)
l = input('Введите букву: ')
if l == n[i]:
    print('Победа!\nСлово:',n)
else:
    print('Увы! Попробуй в другой раз.\nСлово:',n)
