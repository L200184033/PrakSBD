import mysql.connector
 
con = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="perpustakaan"
)
 
cur = con.cursor()
sql = "INSERT INTO buku (kode_buku, nama_buku, jenis_buku) VALUES (%s, %s, %s)"
values = [
  ("55", "Matematika", "Pelajaran"),
  ("39", "10 Tips memasak", "Umum"),
  ("27", "Sejarah", "Pelajaran"),
  ("14", "Kumpulan lelucon masa kini", "Umum")
]
 
for val in values:
  cur.execute(sql, val)
  con.commit()
 
print("{} data berhasil ditambahkan".format(len(values)))
