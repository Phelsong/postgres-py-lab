import psycopg2
from dotenv import dotenv_values
config = dotenv_values(".env")
myUser = config['USER_NAME']
myPassword = config['PASS_WORD']


psycopg2.connect(dataname = "py-lab", user = myUser, password = myPassword)