import mysql.connector
Mysql = mysql.connector.connect(
    host="localhost",  # your host, usually localhost       
    user="root",
    password="root",
    database = 'mydb')  # your password
cursor = Mysql.cursor()

# student_table = "create table students (id int auto_increment primary key, name varchar(255), age int)"
# # cursor.execute(student_table)

SqlFormula = "insert into students (name, age) values (%s, %s)"
student1 = ("mami",20)
student2 = [("levi", 20),("mikasa", 19), ("armin", 18), ("eren", 20), ("reiner", 21), ("bertholdt", 22), ("annie", 23)]
cursor.execute(SqlFormula, student1)
cursor.executemany(SqlFormula, student2)  # insert multiple records at once
# cursor.execute("select * from students")  # select all records from the students table
Mysql.commit()  # commit the changes to the database
