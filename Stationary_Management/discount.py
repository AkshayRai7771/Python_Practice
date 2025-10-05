from SQL_connx import get_connection
from datetime import datetime, timedelta

def check_discount_existing_customer():
    connection  = get_connection()
    email = input("Enter Email of Customer : ")
    cursor = connection.cursor()
    query =  f"SELECT customer_id FROM sm_db.customer_info where email_address = '{email}';"
    cursor.execute(query)
    res = cursor.fetchone()
    if res is None:
        print("Customer not found")
    else : 
        query =  f"SELECT total_amount FROM sm_db.customer_info where customer_id = '{res[0]}';"
        cursor.execute(query)
        t = cursor.fetchone()

        query =  f"SELECT no_of_purchase FROM sm_db.customer_info where customer_id = '{res[0]}';"
        cursor.execute(query)
        n = cursor.fetchone()
        if t[0]>500 or n[0]>5:
            print("Customer is eligible for special discount")
        else : print("Customer is not eligible for special discount")

def discounted_price():
    # curr = datetime.now() - datetime.now()
    connection  = get_connection()
    cursor = connection.cursor()
    query =  f"SELECT product_id FROM sm_db.products_table WHERE product_date <= 250701;"
    cursor.execute(query)
    res = cursor.fetchall()
    l = []
    for i in range(0,len(res)):
        l.append(res[i][0])
    if len(l)==0:
        print("No old products found")
    else :
        query =  f"UPDATE sm_db.products_table SET product_price = product_price*0.8 WHERE product_id in {tuple(l)};"
        cursor.execute(query)
        query =  f"UPDATE sm_db.products_table SET product_date = 250901 WHERE product_date <= 250701;"
        cursor.execute(query)
        connection.commit()
