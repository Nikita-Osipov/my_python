s = "У лукоморья 123 дуб зеленый 456"
print("Индекс буквы 'я': ",s.find('я'))
print("Кол-во букв 'у': ",s.count('у'))
print(s.isalpha())
if s.isalpha() == False:
    print(s.upper())
k = int(len(s))
if k > 4:
    print(s.lower())
print(s.replace('У','О'))

