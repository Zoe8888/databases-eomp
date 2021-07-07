import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector


root = Tk()
# Creating window title
root.title('Admin Account')
# Setting window size
root.geometry('800x800')
# Ensuring window size isn't adjustable
root.resizable('False', 'False')
# Setting background color
root.config(bg='black')

mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                               database='LC_Academy', auth_plugin='mysql_native_password')
mycursor = mydb.cursor()


mycursor.execute('SELECT * FROM Register')
tree = ttk.Treeview(root)
tree['show'] = 'headings'
# mycursor.execute('SELECT * FROM NextOfKin')
# tree = ttk.Treeview(root)

tree['columns'] = ['name', 'surname', 'id', 'number', 'kinName', 'kinNumber']

tree.column('00', width=60, minwidth=60, anchor=tk.CENTER)
tree.column('name', width=60, minwidth=60, anchor=tk.CENTER)
tree.column('surname', width=60, minwidth=60, anchor=tk.CENTER)
tree.column('id', width=60, minwidth=60, anchor=tk.CENTER)
tree.column('number', width=60, minwidth=60, anchor=tk.CENTER)
tree.column('kinName', width=60, minwidth=60, anchor=tk.CENTER)
tree.column('kinNumber', width=60, minwidth=60, anchor=tk.CENTER)

tree.heading('0', text='0', anchor=tk.CENTER)
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


logo = PhotoImage(file='Logo-Life-Choices.png')
logo = logo.subsample(3)
lc_logo = Label(root, image=logo, height=300, width=600, bg='black')
lc_logo.place(relx=0.13, rely=0)

header = Label(root, text='Welcome to the admin account', font=50, bg='black', fg='#9ce57e')
header.place(relx=0.1, rely=0.3)

frame = Frame(root, bg='black', height=400, width=700, borderwidth=2, relief='ridge')
frame.place(relx=0.1, rely=0.4)

inside_label = Label(frame, text='Amount of people inside the building:')
inside_label.place(relx=0.1, rely=0.1)
inside_entry = Entry(frame, width=10)
inside_entry.place(relx=0.5, rely=0.1)

user_info_label = Label(frame, text='')

# select * from table where time_out = NULL


tree.pack()
root.mainloop()
