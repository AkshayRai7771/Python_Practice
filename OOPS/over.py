#overloading
class A:

    sum = 0
    def add(self,a=None,b=None,c=None):
        if a != None and b != None and c != None:
            sum = int(a) + int(b) + int(c)
        elif a!=None and b!=None:
            sum = int(a) + int(b)
        else: sum = int(a)
        
        return int(sum)
    
add1 = A()

print(add1.add(1.1,2.1,"3"))
print(add1.add(2,'8'))

#overriding
class a:
    def show(self):
        print("We are in A")
class b(a):
    def show(self):
        print("We are in B") #pass
class c(b):
    def show(self):
        print("We are in C")
B = b()
#B1 = b()
# B1.show() output will be We are in A 
C= c()
B.show()
C.show()
