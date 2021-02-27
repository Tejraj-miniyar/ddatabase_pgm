import mysql.connector
#step 1: create connection with MYSQL
con=mysql.connector.connect(host="127.0.0.1",user="root",password="")

#step 2: create cursor object that can execute sql query
cursor=con.cursor();
#step 3: execute sql query with the help of cursor object
cursor.execute("show databases")

#iterate elements in cursor
print(cursor)
for records in cursor:
    print(records)
print("my name is tejraj")
