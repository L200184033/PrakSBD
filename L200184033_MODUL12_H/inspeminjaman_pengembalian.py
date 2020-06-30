import mysql.connector
 
con = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="perpustakaan"
)
 
cur = con.cursor()
sql = "INSERT INTO peminjaman_pengembalian (nama_buku, tanggal_pinjam, tanggal_kembali) VALUES (%s, %s, %s)"
values = [
  ("Matematika", "15 November 2020", "22 November 2020"),
  ("10 Tips memasak", "15 November 2020", "29 November 2020"),
  ("Sejarah", "15 November 2020", "22 November 2020"),
  ("Kumpulan lelucon masa kini", "15 November 2020", "29 November 2020")
]
 
for val in values:
  cur.execute(sql, val)
  con.commit()
 
print("{} data berhasil ditambahkan".format(len(values)))
