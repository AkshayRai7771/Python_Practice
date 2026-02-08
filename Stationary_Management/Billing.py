from SQL_connx import get_connection
from Update_Customer import update_existing_customer,new_customer
from Products import update_sold
from validation import is_valid_email
from history_of_sales import update_history_of_soldproducts

def start_billing ():
    connection  = get_connection()
    email = input("Enter Email of Customer : ")
    valid = is_valid_email(email)
    if valid == True:
        number_of_items = int(input("Enter number of different items bought : "))
        for i in range(number_of_items):

            item_name = input("Enter name of item :").capitalize()
            item_quant = int(input("No of item sold : "))
            lets_update = update_sold(item_name,item_quant)
            if lets_update == True:
                cursor = connection.cursor()
                query =  f"SELECT customer_id FROM sm_db.customer_info where email_address = '{email}';"
                cursor.execute(query)
                res = cursor.fetchone()
                if res is None:
                    new_customer(email)
                else : 
                    query =  f"SELECT total_amount FROM sm_db.customer_info where customer_id = '{res[0]}';"
                    cursor.execute(query)
                    t = cursor.fetchone()

                    query =  f"SELECT no_of_purchase FROM sm_db.customer_info where customer_id = '{res[0]}';"
                    cursor.execute(query)
                    n = cursor.fetchone()
                    update_existing_customer(t[0],n[0],res[0])
            else : 
                print("There is some Error!")
            #updating history table
            cursor = connection.cursor()
            query =  f"SELECT product_id FROM sm_db.products_table where products_name  = '{item_name}';"
            cursor.execute(query)
            product_id = cursor.fetchone()[0]
            update_history_of_soldproducts(res[0],product_id,item_quant)
            

    
