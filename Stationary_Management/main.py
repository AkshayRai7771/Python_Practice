from Products import add_products
from discount import check_discount_existing_customer,discounted_price
from Billing import start_billing
from Display import display_products,display_customers
def Menu(run):
 match run.upper():
    
        case "1":
            add_products()
        case "2":
            start_billing()
        case "3":
            check_discount_existing_customer()
        case "4":
            discounted_price()
        case "5":
            show = display_products()
            print("(ID, Name, Price, Quantity)")
            for i in range(0,len(show)):
                print(show[i])
        case "6":
            show = display_customers()
            print("(ID, Name, Email, Total Amount, No. of Purchase)")
            for i in range(0,len(show)):
                print(show[i])
        case _:
            print("Please select the valid options ")




if __name__ == "__main__":
    cmd= input("Choose an option:\n"
    "1. Add New Product\n"
    "2. Start Billing\n"
    "3. Check Discount for Existing Customers\n"
    "4. Calculate Discounted Price on Items\n"
    "5. Display Products\n"
    "6. Display Customers\n"
    "Q. Quit\n")
    while(cmd!='q') :
        Menu(cmd)
        cmd= input("Choose an option:\n"
    "1. Add New Product\n"
    "2. Start Billing\n"
    "3. Check Discount for Existing Customers\n"
    "4. Calculate Discounted Price on Items\n"
    "5. Display Products\n"
    "6. Display Customers\n"
    "Q. Quit\n")