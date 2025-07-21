import mysql.connector
Mysql = mysql.connector.connect(
    host="localhost",  # your host, usually localhost
    user="root",
    password="root",
    database='mydb'  # your password
)

cursor = Mysql.cursor()

# cursor.execute("select * from students")  # select all records from the students table
# for row in cursor.fetchall():  # fetch all records
#     print(row)  # print each record

# cursor.execute("select * from students")
# for row in cursor.fetchone():
#     print(row)  # fetch one record at a time and print it



# sql_query = "select * from students where age < 20"

# sql_query = "select * from students where name like '%m%'; "  # SQL query to select records with age less than 20

sql_query = "select * from students where name like 'm%'; "  # SQL query to select records where name starts with 'm'
cursor.execute(sql_query)  
for row in cursor.fetchall():
    print(row)  # print each record that matches the condition
