a = [1, 2, 3, 2, 1]
b = [3, 2, 2, 3, 3, 2]
s = set()
for i in range(0,len(a)):
    s.add(a[i])
for i in range(0,len(b)):
    s.add(b[i])
print(s)