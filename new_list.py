#for
f = [2,4,9,16,25]
for i in range(len(f)):
    f[i] = f[i]**2
print(f)
#map
m = [2,4,9,16,25]
print(list(map((lambda x: x**2),m)))
#gen
g = [2,4,9,16,25]
print([i**2 for i in g])
