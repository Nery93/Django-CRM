#Install Mysql
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password123'
)

#prepare a cursor object

cursorObject = dataBase.cursor()

# Create a Database

cursorObject.execute("CREATE DATABASE company")

print("All Done!")