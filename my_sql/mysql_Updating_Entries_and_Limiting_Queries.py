import mysql.connector
Mysql = mysql.connector.connect(
    host="localhost",  # your host, usually localhost
    user="root",
    password="root",
    database='mydb'  # your password
)
cursor = Mysql.cursor()

# sql_update = "update students set age = 20 where name = 'mikasa';"
# cursor.execute(sql_update)  # update the age of mikasa to 20
# Mysql.commit()  # commit the changes to the database

# sql_update = "select * from students limit 3;"
# cursor.execute(sql_update)  # select the first 3 records from the students table
# for row in cursor.fetchall():
#     print(row)  # print each record that matches the condition

# sql_update = "select * from students limit 3 offset 2;"
# cursor.execute(sql_update)  # select the first 3 records from the students table, skipping the first 2
# for row in cursor.fetchall():
#     print(row)  # print each record that matches the condition

sql_update = "select * from students order by age desc limit 3;"
cursor.execute(sql_update)  # select the first 3 records from the students table, ordered by age in descending order
for row in cursor.fetchall():
    print(row)  # print each record that matches the condition

