def fab(length):
    l = []
    x = 0
    y = 1 
    for i in range (0,length):
        if i == 0 :
            l.append(x)
        else : 
            z = x + y
            x = y
            y = z 
            l.append(x)
            
    return l

n = int(input("Enter any Number : "))
lst = []
lst = fab(n)
print(lst)