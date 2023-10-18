"""
before doing all of this you have to install MYSQL on your PC
and also interminal using command 'pip install mysql', and the 
install mysql connectors to django app using commands in the terminal
'pip intsall mysql-connector' and 'pip intsall mysql-connector-python'
 
"""
from django.db.utils import OperationalError
import pymysql

# creating an object to generate databse
database = pymysql.connect(
    host='localhost',
    user='root',
    passwd='Baaba+=123',
)

try:
    # cursor object to call databse creatingmethod
    curser = database.cursor()

    # writing the actual databse command
    curser.execute("CREATE DATABASE cagta")

    # displaying success messgae
    print("Done: You have Created Database")
except OperationalError as e:
    print("Something wrong happen")
