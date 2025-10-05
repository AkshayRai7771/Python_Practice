from SQL_connx import get_connection
from Update_Customer import update_customer,new_customer

def check_existing_customer ():
    connection  = get_connection()
    email = input("Enter Email of Customer : ")
    cursor = connection.cursor()
    query =  f"SELECT customer_id FROM sm_db.customer_info where email_address = '{email}';"
    cursor.execute(query)
    res = cursor.fetchone()
    print("res - ", res)
    if res is None:
        new_customer(email)
    else : 
        query =  f"SELECT total_amount FROM sm_db.customer_info where customer_id = '{res[0]}';"
        cursor.execute(query)
        t = cursor.fetchone()

        query =  f"SELECT no_of_purchase FROM sm_db.customer_info where customer_id = '{res[0]}';"
        cursor.execute(query)
        n = cursor.fetchone()
        update_customer(t[0],n[0],res[0])
