def rev(l):
    i = 0
    j = len(l)-1
    while i<j:
        temp = l[j]
        l[j]=l[i]
        l[i]=temp
        i+=1
        j-=1
    return l

l = []
n = int(input("Enter the length of the array : "))
for i in range(0,n):
    x=int(input("Enter Int Value: "))
    l.append(x)
print(l)
print(rev(l))