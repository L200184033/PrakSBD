import mysql.connector
 
con = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="perpustakaan"
)
 
cur = con.cursor()
sql = "INSERT INTO member (id, nama, alamat) VALUES (%s, %s, %s)"
values = [
  ("100201", "Lisa Kamado", "Jl. nanas RT.005/02"),
  ("100202", "Sartono", "Jl. semangka RT.004/01"),
  ("100203", "Nur Hidayat", "Jl. durian RT.012/015"),
  ("100204", "Isbani", "Jl. belimbing RT.001/09")
]
 
for val in values:
  cur.execute(sql, val)
  con.commit()
 
print("{} data berhasil ditambahkan".format(len(values)))
