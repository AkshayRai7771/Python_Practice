from Products import add_products
from discount import check_discount_existing_customer,discounted_price
from Billing import start_billing
from Display import display_products
def Menu(run):
 match run.upper():
    
        case "A":
            add_products()
        case "B":
            start_billing()
        case "C":
            check_discount_existing_customer()
        case "D":
            discounted_price()
        case "E":
            show = display_products()
            print("(ID, Name, Price, Quantity)")
            for i in range(0,len(show)):
                print(show[i])
        case _:
            print("Please select the valid options ")

if __name__ == "__main__":
    cmd= input("Choose options A/B/C/D/E/Q : ")
    while(cmd!='q') :
        Menu(cmd)
        cmd= input("Choose options A/B/C/D/E/Q : ")