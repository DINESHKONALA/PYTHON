import mysql.connector
Mysql = mysql.connector.connect(
    host="localhost",  # your host, usually localhost
    user="root",
    password="root",
    database='mydb'  # your password
)
cursor = Mysql.cursor()
# sql_delete = "delete from students where name = 'mami';"  # delete the record where name is 'mami'
# cursor.execute(sql_delete)  # execute the delete query    
# Mysql.commit()  # commit the changes to the database

# sql_truncate = "truncate table if exists students;"  # truncate the students table
# cursor.execute(sql_truncate)  # execute the truncate table query[TOOL_CALLS]To ensure the integrity and clarity of your code, I'll provide an organized and complete example of the operations you want to 
# Mysql.commit()  # commit the changes to the database

# sql_drop = "drop table if exists students;"  # drop the students table
# cursor.execute(sql_drop)  # execute the drop table query
# Mysql.commit()  # commit the changes to the database

