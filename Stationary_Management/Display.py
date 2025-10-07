from SQL_connx import get_connection
from Products import update_quantity
# from Back_Menu import back


def display_products():
    connection  = get_connection()
    cursor = connection.cursor()
    query = "SELECT product_id,products_name,product_price,available_quantity FROM sm_db.products_table;"
    cursor.execute(query)
    x = cursor.fetchall()
    return x

def display_customers():
    pass




# if __name__ =="__main__":
#     ask()

