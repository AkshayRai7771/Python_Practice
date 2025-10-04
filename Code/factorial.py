# print fact of 5

def fact (n):
    if n == 1:
        return 1
    return n*fact(n-1)

n = int(input("Enter the number :"))
result = fact(n)
print (result)