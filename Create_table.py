import mysql.connector

con = mysql.connector.connect(host="localhost", user="amith", password="amith@123", database="mydb")
cur = con.cursor()

# sql = "create table student(id int(10), name varchar(25), sub varchar(10), marks int(10))"
# cur.execute(sql)
# print("created table")

sql = "insert into student(id,name,sub,marks) values(1,'abc','kan','125')"
cur.execute(sql)
con.commit()
print("Inserted values")
