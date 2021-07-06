from tkinter import *
from tkinter import messagebox
import mysql.connector

root = Tk()
# Creating window title
root.title('Admin Login')
# Setting window size
root.geometry('500x400')
# Ensuring window size isn't adjustable
root.resizable('False', 'False')

header = Label(root, text='Log into admin account')
header.place(relx=0.1, rely=0.1)

adminId_label = Label(root, text='Please enter your admin ID:')
adminId_label.place(relx=0.1, rely=0.2)
adminId_entry = Entry(root, width=25)
adminId_entry.place(relx=0.5, rely=0.2)

password_label = Label(root, text='Please enter your password')
password_label.place(relx=0.1, rely=0.3)
password_entry = Entry(root, width=25)
password_entry.place(relx=0.5, rely=0.3)

login_button = Button(root, text='Login', width=25)
login_button.place(relx=0.5, rely=0.5)

root.mainloop()