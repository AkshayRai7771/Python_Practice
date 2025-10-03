from sqlcntn import get_connection
#printing all products in database 
def get_all_products(connection):
    
    cursor = connection.cursor()
    query = "SELECT product_table.product_id,product_table.product_name,product_table.uom_id,product_table.price_per_unit,uom_table.uom_name FROM product_table inner join uom_table on product_table.uom_id = uom_table.uom_id"
    cursor.execute(query)
    response =  []
    for (product_id,product_name,uom_id,price_per_unit,uom_name)in cursor :
        response.append (
            {
                "product_id":product_id,
                "product_name":product_name,
                "uom_id":uom_id,
                "price_per_unit":price_per_unit,
                "uom_name":uom_name
            }
        )
    return response


if __name__ == "__main__":
    connection = get_connection()
    print(get_all_products(connection))

