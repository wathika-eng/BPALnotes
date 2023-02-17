from mysql import mysql.connector

my = mysql.connector.connect(
    host="localhost",
    user="wathika",
    passwd="#Wathika01",
    auth_plugin="mysql_native_password",
)


my_cursor = mydb.my_cursor()

my_cursor.execute("CREATE DATABASE notes")

my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)
