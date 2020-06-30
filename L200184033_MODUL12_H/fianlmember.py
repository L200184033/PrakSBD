import mysql.connector
import os
 
con = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="perpustakaan"
)


def insert_data(con):
  id = input("Masukan id: ")
  nama = input("Masukan nama: ")
  alamat = input("Masukan alamat: ")
  cursor = con.cursor()
  sql = "INSERT INTO guruu (id, nama, alamat) VALUES (%s, %s, %s)"
  val = (id, nama, alamat)
  cursor.execute(sql, val)
  con.commit()

  print("{} data berhasil ditambahkan".format(cursor.rowcount))


def show_data(con):
  cur = con.cursor()
  sql = "SELECT * FROM guruu"
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
  id = input("id member> ")
  nama = input("nama member baru: ")
  alamat = input("alamat member baru: ")

  sql = "UPDATE guruu SET id=%s, nama=%s WHERE alamat=%s"
  val = (id, nama, alamat)
  cursor.execute(sql, val)
  con.commit()
  print("{} data berhasil diubah".format(cursor.rowcount))


def delete_data(con):
  cursor = con.cursor()
  show_data(con)
  id = input("pilih id member> ")
  sql = "DELETE FROM member WHERE id=%s"
  val = (id,)
  cursor.execute(sql, val)
  con.commit()
  print("Record member berhasil dihapus".format(cursor.rowcount))


def search_data(con):
  cur = con.cursor()
  keyword = input("Kata kunci(masukan id, nama, alamat): ")
  sql = "SELECT * FROM member WHERE id LIKE %s OR nama LIKE %s OR alamat LIKE %s"
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
