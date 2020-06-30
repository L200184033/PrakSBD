import mysql.connector
import os
 
con = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="perpustakaan"
)


def insert_data(con):
  nama_buku = input("Masukan nama: ")
  tanggal_pinjam = input("Masukan tanggal: ")
  tanggal_kembali = input("Masukan tanggal: ")
  cursor = con.cursor()
  sql = "INSERT INTO siswa (nama buku, tanggal pinjam, tanggal kembali) VALUES (%s, %s, %s)"
  val = (nama_buku, tanggal_pinjam, tanggal_kembali)
  cursor.execute(sql, val)
  con.commit()

  print("{} data berhasil disimpan".format(cursor.rowcount))


def show_data(con):
  cur = con.cursor()
  sql = "SELECT * FROM peminjaman_pengembalian"
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
  nama_buku = input("nama buku> ")
  tanggal_pinjam = input("tanggal pinjam: ")
  tanggal_kembali = input("tangal kembali: ")

  sql = "UPDATE peminjaman_pengembalian SET nama=%s, tanggal pinjam=%s WHERE tanggal kembali=%s"
  val = (nama, alamat, nis)
  cursor.execute(sql, val)
  con.commit()
  print("{} data berhasil diubah".format(cursor.rowcount))


def delete_data(con):
  cursor = con.cursor()
  show_data(con)
  nama = input("pilih nama peminjaman pengembalian> ")
  sql = "DELETE FROM peminjaman pengembalian WHERE nama=%s"
  val = (nama,)
  cursor.execute(sql, val)
  con.commit()
  print("Record peminjaman pengembalian berhasil dihapus".format(cursor.rowcount))


def search_data(con):
  cur = con.cursor()
  keyword = input("Kata kunci(masukan nama buku, tanggal pinjam, tanggal kembali): ")
  sql = "SELECT * FROM peminjaman pengembalian WHERE nama buu LIKE %s OR tanggal pinjam LIKE %s OR tanggal kembali LIKE %s"
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
