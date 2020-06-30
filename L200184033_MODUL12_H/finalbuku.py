import mysql.connector
import os
 
con = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="perpustakaan"
)


def insert_data(con):
  kode_buku = input("Masukan kode: ")
  nama_buku = input("Masukan nama: ")
  jenis_buku = input("Masukan jenis: ")
  cursor = con.cursor()
  sql = "INSERT INTO buku (kode_buku, nama_buku, jenis_buku) VALUES (%s, %s, %s)"
  val = (kode_buku, nama_buku, jenis_buku)
  cursor.execute(sql, val)
  con.commit()

  print("{} data berhasil ditambahkan".format(cursor.rowcount))


def show_data(con):
  cur = con.cursor()
  sql = "SELECT * FROM buku"
  cur.execute(sql)
  result = cur.fetchall()
  
  if cur.rowcount < 0:
    print("Tidak ada data")
  else:
    for data in result:
      print(data)


def update_data(con):
  cursor = con.cursor()
  show_data(con)
  kode_buku = input("pilih kode buku> ")
  nama_buku = input("nama buku baru: ")
  jenis_buku = input("nama jenis baru: ")

  sql = "UPDATE buku SET kode=%s, nama=%s WHERE jenis=%s"
  val = (kode_buku, nama_buku, jenis_buku)
  cursor.execute(sql, val)
  con.commit()
  print("{} data berhasil diubah".format(cursor.rowcount))


def delete_data(con):
  cursor = con.cursor()
  show_data(con)
  kode = input("pilih kode buku> ")
  sql = "DELETE FROM buku WHERE kode=%s"
  val = (kode,)
  cursor.execute(sql, val)
  con.commit()
  print("Record pelajaran berhasil dihapus".format(cursor.rowcount))


def search_data(con):
  cur = con.cursor()
  keyword = input("Kata kunci(masukan kode, nama, jenis): ")
  sql = "SELECT * FROM buku WHERE kode LIKE %s OR nama LIKE %s OR jenis LIKE %s"
  val = ("%{}%".format(keyword), "%{}%".format(keyword), "%{}%".format(keyword))
  cur.execute(sql, val)
  result = cur.fetchall()
  
  if cur.rowcount < 0:
    print("Tidak ada data")
  else:
    for data in result:
      print(data)


def show_menu(con):
  print("=== APLIKASI PERPUSTAKAAN  ===")
  print("1. Tambahkan Data")
  print("2. Tampilkan Data")
  print("3. Update Data")
  print("4. Hapus Data")
  print("5. Cari Data")
  print("0. Keluar")
  print("------------------")
  menu = input("Pilih menu> ")

  #clear screen
  os.system("clear")

  if menu == "1":
    insert_data(con)
  elif menu == "2":
    show_data(con)
  elif menu == "3":
    update_data(con)
  elif menu == "4":
    delete_data(con)
  elif menu == "5":
    search_data(con)
  elif menu == "0":
    exit()
  else:
    print("Menu salah!")


if __name__ == "__main__":
  while(True):
    show_menu(con)
