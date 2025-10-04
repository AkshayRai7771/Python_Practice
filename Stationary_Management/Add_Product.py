from SQL_connx import get_connection

class Products:
    def __init__(self,products_name,product_date,product_price,product_quantity):
        self.name = products_name
        self.date = product_date
        self.price = product_price
        self.quant = product_quantity
    def update_product_table(self, connection):
        cursor = connection.cursor()
        query =  "INSERT INTO products_table (products_name,product_date,product_price,product_quantity) VALUES (%s,%s,%s,%s);"
        data =  (self.name,self.date,self.price,self.quant)
        cursor.execute(query,data)
        connection.commit()
            
def add_products():
    connection = get_connection()
    w = input("Enter name of your product: ")
    x = input("Enter puchase date in(YY:MM:DD): ")
    y = input("Enter Price of product: ")
    z = input("Enter Quantity : ")
    item = Products(w,x,y,z)
    item.update_product_table(connection)

    
# def add_new_product(connection,product):
#     cursor = connection.cursor()
#     query =  "INSERT INTO products_table (products_name,product_date,product_price,product_quantity) VALUES (%s,%s,%s,%s);"
#     data =  (product['products_name'],product['product_date'],product['product_price'],product['product_quantity'])
#     cursor.execute(query,data)
#     connection.commit()

# if __name__ == "__main__":
#     connection = get_connection()
#     w = input("Enter name of your product: ")
#     x = input("Enter puchase date in(YY:MM:DD): ")
#     y = input("Enter Price of product: ")
#     z = input("Enter Quantity : ")
#     add_new_product(connection,{'products_name':w,'product_date':x,'product_price':y,'product_quantity':z})