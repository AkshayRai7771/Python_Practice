from Add_Product import add_products
from discount import check_discount_existing_customer,discounted_price
from Old_customer import check_existing_customer

run = input("A/B/C/D: ")

match run.upper():
    
    case "A":
        add_products()
    case "B":
        check_existing_customer()
    case "C":
        check_discount_existing_customer()
    case "D":
        discounted_price()
    case _:
        print("Please select the valid options ")
