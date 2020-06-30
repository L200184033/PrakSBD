from tkinter import *
import mysql.connector
import csv
from tkinter import ttk

root = Tk()
root.title('PERPUSTAKAAN')
root.geometry('450x380')

#Connect ke DB MySQL
mydb = mysql.connector.connect(
				user='root', 
				database='perpustakaan'
			)

# Check to see if connection to MySQL was created
# print(mydb)

# Create a cursor and initialize it
my_cursor = mydb.cursor()

# Clear Text Fields
def clear_fields():
	id_member_box.delete(0, END)
	nama_member_box.delete(0, END)
	alamat_member_box.delete(0, END)

# Submit Member To Database
def add_member():
	sql_command = "INSERT INTO member (id_member, nama_member, alamat_member) VALUES (%s, %s, %s)"
	values = (id_member_box.get(), nama_member_box.get(), alamat_member_box.get())
	my_cursor.execute(sql_command, values)

	# Commit the changes to the database
	mydb.commit()
	# Clear the fields
	clear_fields()

# Write To CSV Excel Function
def write_to_csv(result):
	with open('member.csv', 'a', newline='') as f:
		w = csv.writer(f, dialect='excel')
		for record in result:
			w.writerow(record)

# Edit Member
def edit_member():
	edit_member = Tk()
	edit_member.title("Edit Member")
	edit_member.geometry("1000x600")

	def update():
		
		sql_command = """UPDATE member SET nama_member = %s, alamat_member = %s WHERE id_member = %s""" 

		nama_member = nama_member_box1.get()
		alamat_member = alamat_member_box1.get()
		id_member = id_member_box1.get()

		input = (nama_member, alamat_member,id_member)
		my_cursor.execute(sql_command, input)

		# Commit the changes to the database
		mydb.commit()
		# Clear the fields
		edit_member.destroy()
		
	def edit_now(id, index):
		sql2 = "SELECT * FROM member WHERE id_member = %s"
		name2 = (id, )
		results = my_cursor.execute(sql2, name2)
		results = my_cursor.fetchall()
		print(results)

		#fart = Label(edit_member, text=id)
		#fart.grid(row=10, column=1)
		#Create Main Form To Enter Customer Data
		id_member_label = Label(edit_member, text="ID").grid(row=index+2, column=0, sticky=W, padx=10)
		nama_member_label = Label(edit_member, text="Nama").grid(row=index+3, column=0, sticky=W, padx=10)
		alamat_member_label = Label(edit_member, text="Alamat").grid(row=index+4, column=0, sticky=W, padx=10)

		global id_member_box1
		id_member_box1 = Entry(edit_member)
		id_member_box1.insert(0, results[0][0])
		id_member_box1.grid(row=index+2, column=1)

		global nama_member_box1
		nama_member_box1 = Entry(edit_member)
		nama_member_box1.grid(row=index+3, column=1, pady=5)
		nama_member_box1.insert(0, results[0][1])

		global alamat_member_box1
		alamat_member_box1 = Entry(edit_member)
		alamat_member_box1.grid(row=index+4, column=1, pady=5)
		alamat_member_box1.insert(0, results[0][2])

		edit_record = Button(edit_member, text="Save Record", command=update)
		edit_record.grid(row=index+6, column=0, padx=10)
		
	def search_now():
		selected = drop.get()
		sql = ""
		if selected == "Search by...":
			test = Label(edit_member, text="selection")
			test.grid(row=2, column=0)
		if selected == "Nama member":
			sql = "SELECT * FROM member WHERE nama_member = %s"
			
		if selected == "Alamat member":
			sql = "SELECT * FROM member WHERE alamat_member = %s"
			
		if selected == "ID member":
			sql = "SELECT * FROM member WHERE id_member = %s"
			
		searched = search_box.get()
		#sql = "SELECT * FROM member WHERE last_name = %s"
		name = (searched, )
		result = my_cursor.execute(sql, name)
		result = my_cursor.fetchall()

		if not result: 
			result = "Record Not Found..."
			searched_label = Label(edit_member, text=result)
			searched_label.grid(row=2, column=0)

		else:
			id_label2 = Label(edit_member, text="             ID member").grid(row=2, column=1, sticky=W, padx=10)
			nama_label2 = Label(edit_member, text="              Nama").grid(row=2, column=2, sticky=W, padx=10)
			alamat_label2 = Label(edit_member, text="Alamat").grid(row=2, column=3, sticky=W, padx=10)
			for index, x in enumerate(result):
				num = 0
				index += 2
				stuff = str(x[0])
				edit_button = Button(edit_member, text="Edit " + stuff, command=lambda: edit_now(stuff, index))
				edit_button.grid(row=index+1, column=num)
				for y in x:
					searched_label = Label(edit_member, text=y)
					searched_label.grid(row=index+1, column=num+1)
					num +=1
			 
			
	# Entry box to search for customer
	search_box = Entry(edit_member)
	search_box.grid(row=0, column=1, padx=10, pady=10)
	# Entry box Label search for customer
	search_box_label = Label(edit_member, text="Search member ")
	search_box_label.grid(row=0, column=0, padx=10, pady=10)
	# Entry box search  Button for customer
	search_button = Button(edit_member, text="Search member", command=search_now)
	search_button.grid(row=1, column=0, padx=10)
	# Drop Down Box
	drop = ttk.Combobox(edit_member, value=["Search by...", "Nama","Alamat", "ID member"])
	drop.current(0)
	drop.grid(row=0, column=2)


# Search member
def search_member():
	search_member = Tk()
	search_member.title("Search member")
	search_member.geometry("1000x600")

	def search_now():
		selected = drop.get()
		sql = ""
		if selected == "Search by...":
			test = Label(search_member, text="selection")
			test.grid(row=2, column=0)
		if selected == "Nama":
			sql = "SELECT * FROM member WHERE nama_member = %s"
			
		if selected == "Alamat":
			sql = "SELECT * FROM member WHERE alamat = %s"

		if selected == "ID member":
			sql = "SELECT * FROM member WHERE id_Tamu = %s"
			
		
		searched = search_box.get()
		#sql = "SELECT * FROM member WHERE last_name = %s"
		name = (searched, )
		result = my_cursor.execute(sql, name)
		result = my_cursor.fetchall()

		if not result: 
			result = "Record Not Found..."
			searched_label = Label(search_member, text=result)
			searched_label.grid(row=2, column=0)

		else:
			id_label2 = Label(search_member, text="    ID member").grid(row=2, column=0, sticky=W, padx=10)
			nama_label2 = Label(search_member, text="              Nama").grid(row=2, column=1, sticky=W, padx=10)
			alamat_label2 = Label(search_member, text="       Alamat").grid(row=2, column=2, sticky=W, padx=10)
		
			for index, x in enumerate(result):
				num = 0
				index += 2
				for y in x:
					searched_label = Label(search_member, text=y)
					searched_label.grid(row=index+1, column=num)
					num +=1
			 
			csv_button = Button(search_member, text="Save to Excel", command=lambda: write_to_csv(result))
			csv_button.grid(row=index+2, column=0)

		#searched_label = Label(search member, text=result)
		#searched_label.grid(row=3, column=0, padx=10, columnspan=2)
		

	# Entry box to search for customer
	search_box = Entry(search_member)
	search_box.grid(row=0, column=1, padx=10, pady=10)
	# Entry box Label search for customer
	search_box_label = Label(search_member, text="Search member ")
	search_box_label.grid(row=0, column=0, padx=10, pady=10)
	# Entry box search  Button for customer
	search_button = Button(search_member, text="Search member", command=search_now)
	search_button.grid(row=1, column=0, padx=10)

#	searched_label = Label(search_member, text=y)
#	searched_label.grid(row=index, column=num)

	# Drop Down Box
	drop = ttk.Combobox(search_member, value=["Search by...", "Nama","Alamat", "ID Tamu"])
	drop.current(0)
	drop.grid(row=0, column=2)
	
def hapus_member():
	hapus_member = Tk()
	hapus_member.title("Hapus member")
	hapus_member.geometry("400x300")

	id_label2 = Label(hapus_member,text="ID member : ")
	id_label2.grid(row=1,column=0,pady=10)

	id_box2 = Entry(hapus_member)
	id_box2.grid(row=1, column=1,pady=10)

	def hapus_now():
		delete = id_box2.get()
		sql = """DELETE FROM member WHERE id_member =%s"""
		name = (delete, )
		my_cursor.execute(sql, name)
		mydb.commit()
		hapus_Tamu.destroy()

	id_button = Button(hapus_member,text="Hapus",command=hapus_now)
	id_button.grid(row=2, column=0,columnspan=2)

# List Cusomters 
def list_Tamu():
	list_member_query = Tk()
	list_member_query.title("List Semua member")
	list_member_query.geometry("800x600")
	id_label2 = Label(list_member_query, text="    ID Tamu").grid(row=0, column=0, sticky=W, padx=10)
	nama_label2 = Label(list_member_query, text="Nama").grid(row=0, column=1, sticky=W, padx=10)
	alamat_label2 = Label(list_member_query, text="Alamat").grid(row=0, column=2, sticky=W, padx=10)
	
	# Query The Database
	my_cursor.execute("SELECT * FROM member")
	result = my_cursor.fetchall()
	
	for index, x in enumerate(result):
		num = 0
		for y in x:
			lookup_label = Label(list_member_query, text=y)
			lookup_label.grid(row=index+1, column=num)
			num +=1
	csv_button = Button(list_member_query, text="Save to Excel", command=lambda: write_to_csv(result))
	csv_button.grid(row=index+2, column=0)
# Create a Label
title_label = Label(root, text="Database member", font=("Helvetica", 16))
title_label.grid(row=0, column=0, columnspan=2, pady=10)

#Create Main Form To Enter Train Data
id_member_label = Label(root, text="ID").grid(row=1, column=0, sticky=W, padx=10)
nama_member_label = Label(root, text="Nama").grid(row=2, column=0, sticky=W, padx=10)
alamat_member_label = Label(root, text="Alamat").grid(row=3, column=0, sticky=W, padx=10)

# Create Entry Boxes
id_member_box = Entry(root)
id_member_box.grid(row=1, column=1)

nama_member_box = Entry(root)
nama_member_box.grid(row=2, column=1, pady=5)

alamat_member_box = Entry(root)
alamat_member_box.grid(row=3, column=1, pady=5)

# Create Buttons
add_member_button = Button(root, text="Tambah member", command=add_member)
add_member_button.grid(row=6, column=0, padx=10, pady=10)

clear_fields_button = Button(root, text="Clear Fields", command=clear_fields)
clear_fields_button.grid(row=6, column=1)
# List Tamu button
list_member_button = Button(root, text="List member", command=list_member)
list_member_button.grid(row=7, column=0, sticky=W, padx=10)	
# Search Tamu
search_member_button = Button(root, text="Cari member", command=search_Tamu)
search_member_button.grid(row=7, column=1, sticky=W, padx=10)
# Edit Tamu
edit_member_button = Button(root, text="Edit member", command=edit_member)
edit_member_button.grid(row=8, column=0, sticky=W, padx=10, pady=10)

hapus_member_button = Button(root, text="Hapus member", command=hapus_member)
hapus_member_button.grid(row=8, column=1, sticky=W, padx=10, pady=10)

root.mainloop()
