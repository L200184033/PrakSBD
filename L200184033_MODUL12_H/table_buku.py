import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="perpustakaan"
)

cursor = mydb.cursor()

query = """
CREATE TABLE buku
(
    kode_buku INT(10),
    nama_buku VARCHAR(100),
    jenis_buku VARCHAR(100)
)
"""

cursor.execute(query)

print("Table buku sukses dibuat")
