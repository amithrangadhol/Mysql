import mysql.connector

con = mysql.connector.connect(host="localhost",user="amith",password="amith@123")
#print(con)

cur = con.cursor()
sql = "Create database mydb"
cur.execute(sql)
