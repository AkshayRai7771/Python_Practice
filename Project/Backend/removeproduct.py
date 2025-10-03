from sqlcntn import get_connection
#delete product 
def delete_product(connection, product_id):
    cursor = connection.cursor()
    query =  "DELETE FROM product_table WHERE product_id=" + str(product_id)
    cursor.execute(query)
    connection.commit()
    cursor.close()

# if __name__ == "__main__":
#     connection = get_connection()
#     n =  int(input("Enter Product ID you want to remove :"))
#     print(delete_product(connection,n))