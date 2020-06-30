import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd=""
)

cursor = mydb.cursor()
cursor.execute("CREATE DATABASE perpustakaan")

print("Database perpustakaan sukses dibuat")
