import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="perpustakaan"
)

cursor = mydb.cursor()

query = """
CREATE TABLE member
(
    id INT(10),
    nama VARCHAR(100),
    alamat VARCHAR(100)
)
"""

cursor.execute(query)

print("Table member sukses dibuat")
