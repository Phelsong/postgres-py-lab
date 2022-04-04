import psycopg2
from dotenv import dotenv_values
config = dotenv_values(".env")
myUser = config['USER_NAME']
myPassword = config['PASS_WORD']

#----------------------------------------------------------------
connect = psycopg2.connect(database = "py-lab", user = myUser, password = myPassword, host="localhost", port="5432")
cursor = connect.cursor()
#----------------------------------------------------------------

cursor.execute("SELECT * FROM sales LIMIT 10")
print(cursor.fetchall())








connect.commit()
connect.close()