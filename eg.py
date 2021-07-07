import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector

root = Tk()

mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                               database='LC_Academy', auth_plugin='mysql_native_password')
mycursor = mydb.cursor()

query = 'SELECT * FROM Register'
mycursor.execute(query)
print(query)
tree = ttk.Treeview(root)
tree['show'] = 'headings'
# mycursor.execute('SELECT * FROM NextOfKin')
# tree = ttk.Treeview(root)

tree['columns'] = ('name', 'surname', 'id', 'number', 'kinName', 'kinNumber')

tree.column('name', width=100, minwidth=60, anchor=tk.CENTER)
tree.column('surname', width=100, minwidth=60, anchor=tk.CENTER)
tree.column('id', width=100, minwidth=60, anchor=tk.CENTER)
tree.column('number', width=100, minwidth=60, anchor=tk.CENTER)
tree.column('kinName', width=150, minwidth=60, anchor=tk.CENTER)
tree.column('kinNumber', width=150, minwidth=60, anchor=tk.CENTER)

tree.heading('name', text='Name', anchor=tk.CENTER)
tree.heading('surname', text='Surname', anchor=tk.CENTER)
tree.heading('id', text='ID number', anchor=tk.CENTER)
tree.heading('number', text='Cell number', anchor=tk.CENTER)
tree.heading('kinName', text='Next of kin name', anchor=tk.CENTER)
tree.heading('kinNumber', text='Next of kin number', anchor=tk.CENTER)

i = 0
for row in mycursor:
    tree.insert('', i, text='', values=(row[0], row[1], row[2], row[3], row[4], row[5]))
    i = i + 1

tree.pack()
root.mainloop()