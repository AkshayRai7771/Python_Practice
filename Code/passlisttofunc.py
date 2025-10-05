def count(lst):
    even = 0
    odd = 0
    for i in range(0,len(lst)):
        if lst[i] %2 == 0 :
            even+=1
        else : odd +=1
    return even,odd

l = []
n = int(input("Enter any Number : "))
for i in range(1,n+1):
    l.append(i)
print("List of Integers : ",l)
even_count , odd_count = count(l)
print(f"Number of Even Integers : {even_count} and Number of Odd Integers : {odd_count} ")
