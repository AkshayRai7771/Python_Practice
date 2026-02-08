from SQL_connx import get_connection
from datetime import date
def update_history_of_soldproducts(customer_id,product_id,item_quant):
    connection  = get_connection()
    cursor = connection.cursor()
    query =  "INSERT INTO sm_db.history_of_sold_products (customer_id,product_id,quantity_sold,date) VALUES (%s,%s,%s,%s);"
    today = date.today() 
    data =  (customer_id,product_id,item_quant,today)
    cursor.execute(query,data)
    connection.commit()
    print("Details saved in Database :) ")
    