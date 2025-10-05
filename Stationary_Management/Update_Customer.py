from SQL_connx import get_connection

class Customer:
    def __init__(self,total_amount,no_of_products,customer_id=None,customer_name = None,email_address=None):
        self.name = customer_name
        self.email = email_address
        self.amount = total_amount
        self.quanty = no_of_products
        self.id = customer_id
    def add_new_customer(self, connection):
        cursor = connection.cursor()
        query =  "INSERT INTO customer_info (customer_name,email_address,total_amount,no_of_purchase) VALUES (%s,%s,%s,%s);"
        data =  (self.name,self.email,self.amount,self.quanty)
        cursor.execute(query,data)
        connection.commit()
    def edit_customer(self,connection):
        cursor = connection.cursor()
        query =  "UPDATE sm_db.customer_info SET total_amount = %s , no_of_purchase = %s  WHERE (customer_id = %s);"
        data =  (self.amount,self.quanty,self.id)
        cursor.execute(query,data)
        connection.commit()



            
def new_customer(x):
    connection = get_connection()
    w = input("Enter name of the Customer: ")
    y = input("Enter total amount purchased : ")
    z = 1
    buyer = Customer(y,z,customer_name=w,email_address=x)
    buyer.add_new_customer(connection)

def update_customer(total,num,id):
    connection = get_connection()
    a = int(input("Enter amount :"))
    y = a + total
    z = num+1
    b = id
    update = Customer(y,z,b)
    update.edit_customer(connection)






# def update_customer(connection,customer):
#     cursor = connection.cursor()
#     query =  "INSERT INTO customer_info (customer_name,email_address,total_amount,no_of_purchase) VALUES (%s,%s,%s,%s);"
#     data =  (customer['customer_name'],customer['email_address'],customer['total_amount'],customer['no_of_purchase'])
#     cursor.execute(query,data)
#     connection.commit()

# # emailadd = input("Enter Email Address of Customer : ")

# if __name__ == "__main__":
#     connection = get_connection()
#     w = input("Enter name of the Customer: ")
#     x = input("Enter Email address of Customer: ")
#     y = input("Enter total amount purchased : ")
#     z = 1
#     update_customer(connection,{'customer_name':w,'email_address':x,'total_amount':y,'no_of_purchase':z})