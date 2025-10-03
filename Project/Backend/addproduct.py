from sqlcntn import get_connection
from removeproduct import delete_product
#inserting new product in database
def insert_new_product(connection,product):
    cursor = connection.cursor()
    query =  "INSERT INTO product_table (product_name,uom_id,price_per_unit) VALUES (%s,%s,%s);"
    data =  (product['product_name'],product['uom_id'],product['price_per_unit'])
    cursor.execute(query,data)
    connection.commit()

def get_all_products(connection):
    
    cursor = connection.cursor()
    query = "SELECT price_per_unit,product_id FROM product_table"
    cursor.execute(query)
    res= cursor.fetchall()
    for x in res:
        if x[0]<=45:
            delete_product(connection,x[1])
    result = [x[0] for x in cursor]
    # print(result)
    cursor.close()
    # return result

if __name__ == "__main__":
    connection = get_connection()
    # x = input("Enter name of your product: ")
    # y = input("Enter quantity type: ")
    # z = input("Enter Price you want to sell at: ")
    get_all_products(connection)
    # print("valeu of l : ",l)
    # # if x.strip() in l:
    #     print("already exist")
    # else:
    #     print(insert_new_product(connection,{'product_name':x,'uom_id':y,'price_per_unit':z}))

