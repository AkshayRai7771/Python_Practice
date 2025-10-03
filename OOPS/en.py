class BankAccount:
    def __init__(self,acc_no,bal):
        self.acc_no = acc_no
        self.__bal = bal
    
    def depo(self,amount):
        self.__bal += amount
        print("Deposited ", amount)
    
    def show_bal(self):
        return self.__bal
    
    def show_acc_no(self):
        return self.acc_no

acc = BankAccount(1,5000)
acc.depo(10000)

print(acc.show_acc_no() ," account has ",acc.show_bal()," RS")
