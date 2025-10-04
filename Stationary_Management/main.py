from Add_Product import add_products
from Update_Customer import new_customer
from billing import check

run = input("A/B/C/D")
print("run - ", run)

if run in ['A' , 'a']:
    print("here 1 -=")
    add_products()
elif run in ['B' , 'b']:
    print("inside elif")
    check()