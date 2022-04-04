import psycopg2
from dotenv import dotenv_values
config = dotenv_values(".env")
myUser = config['USER_NAME']
myPassword = config['PASS_WORD']

#----------------------------------------------------------------
connect = psycopg2.connect(database = "py-lab", user = myUser, password = myPassword, host="localhost", port="5432")
cursor = connect.cursor()


def insert_Sale(connect, order_num, order_type, cust_name, prod_num, prod_name, quantity, price, discount): 
    order_total = quantity * price 
    if discount != 0:
        order_total = order_total * discount
    sale_data = (order_num, order_type, cust_name, prod_num, prod_name, quantity, price, discount, order_total)
    cursor = connect.cursor()
    cursor.execute(''' INSERT INTO sales (ORDER_NUM, ORDER_TYPE, CUST_NAME, PROD_NUM, PROD_NAME, QUANTITY, PRICE, DISCOUNT, ORDER_TOTAL)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)''', sale_data)
    connect.commit()
    cursor.execute('''SELECT CUST_NAME, ORDER_TOTAL from sales WHERE ORDER_NUM=%s;''', (order_num,))
    rows = cursor.fetchall()
    for row in rows:
        print("CUST_NAME=", row[0])
        print("ORDER_TOTAL=", row[1],"\n")

    
# cursor.execute('''  (1105910, 'Retail', 'SIMON COWELL', 'EB521', 'understanding AI', 3, 19.5, 0, 59.5)''')




order_num = int(input("What is the order number?\n"))
order_type = input("What is the order type?\n")
cust_name = input("What is the name of the customer?\n")
prod_num = input("What is the number of the product?\n")
prod_name = input("What is the name of the product?\n")
quantity = float(input("what is the quantity?\n"))
price = float(input("what is the price?\n"))
discount = float(input("what is the discount?\n"))                 


# 1105911, 'Retail', 'SIMON COWELL STRIKES AGAIN', 'EB521', 'understanding AI', 11, 19.5, .12
insert_Sale(connect, order_num, order_type, cust_name, prod_num, prod_name, quantity, price, discount)

connect.close()