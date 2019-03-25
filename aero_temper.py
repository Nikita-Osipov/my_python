nm = open('temper_stat.txt', 'r') 
k = float(nm.readline())
l = k
s = k
t = k
j = 1
for line in nm:
    j = j + 1
    t = t + float(line)
    if l <= float(line): 
        l = float(line) 
    if s >= float(line): 
        s = float(line)   
nm.close() 
print("наименьшее = ", s)
print("наибольшее = ", l)
print("средняя = ", t/j)
