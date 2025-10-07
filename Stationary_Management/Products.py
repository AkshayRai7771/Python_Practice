from SQL_connx import get_connection
from datetime import date

class Products:
    def __init__(self,product_id =None,products_name=None,listing_date = None,product_price = None,available_quantity = None,sold_quantity=0,updated_date=date.today()):
        self.name = products_name
        self.date = listing_date
        self.price = product_price
        self.quant = available_quantity
        self.id = product_id
        self.disdate = updated_date
        self.sold = sold_quantity
    def update_product_table(self, connection):
        cursor = connection.cursor()
        query =  f"SELECT product_id FROM sm_db.products_table WHERE products_name = '{self.name}' ;"
        cursor.execute(query)
        exists = cursor.fetchone()
        if exists is None:
            query =  "INSERT INTO products_table (products_name,listing_date,product_price,available_quantity,sold_quantity) VALUES (%s,%s,%s,%s,%s);"
            data =  (self.name,self.date,self.price,self.quant,self.sold)
            cursor.execute(query,data)
            connection.commit()
        else:
            ans = input("Product already exists do you want to update product details? Y/N ").upper()
            if ans == "Y":
                self.id = exists[0]
                self.edit_quantity(connection)
            elif ans == "N":
                pass
            else :
                print("Enter valid selection !")

    
    def edit_quantity(self,connection):
        cursor = connection.cursor()
        query = f"SELECT product_price,available_quantity FROM sm_db.products_table WHERE product_id = '{self.id}' ;"
        cursor.execute(query)
        x = cursor.fetchone()
        l = list (x)
        n = int(self.quant)
        n += l[1]
        self.quant = str(n)
        if len(l) == 0:
            print("Please Enter valid Product ID ")
        else :
            query =  f"UPDATE sm_db.products_table SET product_price = {self.price} , available_quantity ={self.quant},updated_date = '{date.today()}'  WHERE product_id = '{self.id}';"
            cursor.execute(query)
            connection.commit()
    
    
    def sold_items(self,connection):
        cursor = connection.cursor()
        query =  f"SELECT product_id FROM sm_db.products_table where products_name  = '{self.name}';"
        cursor.execute(query)
        res = cursor.fetchone()
        if res is None :
            print("Please enter valid details!")
            bool = False
        else :
            query =  f"SELECT available_quantity,sold_quantity FROM sm_db.products_table where product_id  = '{res[0]}';"
            cursor.execute(query)
            val = cursor.fetchall()
            x = int(self.sold)
            y = val[0][0]
            if  y == 0 :
                print("Item Out of Stock !")
                bool = False
                
            elif y < x :
                print(f"Not Enough Items! Available Quantity : {y} ")
                act = input("Do you wish to buy remaining amount ? Y/N  ")
                if act.upper() == 'Y':
                    update_sold(self.name,y)
                    bool = True
            else:
                y -= x
                x += val[0][1]
                query =  f"UPDATE sm_db.products_table SET  sold_quantity = {x} , available_quantity ={y}  WHERE product_id = '{res[0]}';"
                cursor.execute(query)
                connection.commit()
                bool = True
                print("after ",bool)
        return bool

        



      
def add_products():
    connection = get_connection()
    w = input("Enter name of your product: ").capitalize()
    x = input("Enter puchase date in(YY:MM:DD): ")
    y = input("Enter Price of product: ")
    z = input("Enter Quantity : ")
    a = 0
    item = Products(products_name=w,listing_date=x,product_price=y,available_quantity=z,sold_quantity=a)
    item.update_product_table(connection)

def update_quantity():
    connection  = get_connection()
    a = input("Enter Product ID : ")
    y = input("Enter Price of product: ")
    z = input("Enter Quantity : ")
    item = Products(product_id=a,product_price=y,available_quantity=z)
    item.edit_quantity(connection)

def update_sold(w,z):
    connection = get_connection()
    items_sold = z
    items_name = w
    item = Products(products_name=items_name,sold_quantity=items_sold)
    bool = item.sold_items(connection)
    return bool




    
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