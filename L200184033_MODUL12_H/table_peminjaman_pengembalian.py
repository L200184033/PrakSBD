import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="perpustakaan"
)

cursor = mydb.cursor()

query = """
CREATE TABLE peminjaman_pengembalian
(
    nama_buku VARCHAR(100),
    tanggal_pinjam VARCHAR(100),
    tanggal_kembali VARCHAR(100)
)
"""

cursor.execute(query)

print("Table peminjaman_pengembalian sukses dibuat")
