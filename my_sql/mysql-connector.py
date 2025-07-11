import mysql.connector 
Mysql=mysql.connector.connect(
    host="localhost",   # your host, usually localhost      
    user="root",
    password="root",  # your password
    # database="sys"  # name of the database to use

)
# print(Mysql.cursor().execute("create database mydb"))
cursor = Mysql.cursor()
execute = cursor.execute("show databases;")
# print(execute)
# execute = cursor.execute("use mydb;")
# execute = cursor.execute("drop database mydb;")

# print(execute)
# for db in cursor:
#     print(db)
# for db in execute:
#     print(db)

