class a:
    def A(self):
        print("A")
class b(a):
    def A(self):
        print("B")
class c(b):
    def A(self):
        print("C")
B = b()
B1 = b()
C= c()
B.A()
C.A()
