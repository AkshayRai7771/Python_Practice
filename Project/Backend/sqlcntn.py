import mysql.connector 
__cnx = None
def get_connection():
    global __cnx
    if __cnx is None:

        __cnx = mysql.connector.connect(user='root', password = '1234' , database='grocerystore',host='127.0.0.1')
    return __cnx