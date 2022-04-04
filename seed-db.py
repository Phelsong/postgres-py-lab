import psycopg2
from dotenv import dotenv_values
config = dotenv_values(".env")
myUser = config['USER_NAME']
myPassword = config['PASS_WORD']

#----------------------------------------------------------------
connect = psycopg2.connect(database = "py-lab", user = myUser, password = myPassword, host="localhost", port="5432")
cursor = connect.cursor()
#----------------------------------------------------------------

def dropTables():
    cursor.execute('''DROP TABLE IF EXISTS sales''')
    return;
    
def createTables():
    cursor.execute('''CREATE TABLE IF NOT EXISTS sales
               (ORDER_NUM INT PRIMARY KEY,
               ORDER_TYPE TEXT NOT NULL,
               CUST_NAME TEXT NOT NULL,
               PROD_NUM TEXT,
               PROD_NAME TEXT,              
               QUANTITY INT NOT NULL,
               PRICE REAL,
               DISCOUNT REAL,
               ORDER_TOTAL REAL);''')
    return;


def importData():
    cursor.execute('''COPY sales FROM 'Q:\\0.CodeProjects-Windows\\Py101\\postgres-py-lab\\red30-postgres.csv'
                  WITH DELIMITER ',' 
                  CSV HEADER;''')
    return;







dropTables()
createTables()
importData()




connect.commit()
connect.close()
