from tkinter import *
from tkinter import messagebox
import mysql.connector
import rsaidnumber

root = Tk()
# Creating window title
root.title('Login')
# Setting window size
root.geometry('700x600')
# Ensuring window size isn't adjustable
root.resizable('False', 'False')

mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='LifeChoices',
                               auth_plugin='mysql_native_password')
mycursor = mydb.cursor()

header = Label(root, text='Welcome to LifeChoices Coding Academy. Please sign in.')
header.place(relx=0.1, rely=0.1)

name_label = Label(root, text='Please enter your name:')
name_label.place(relx=0.1, rely=0.2)
name_entry = Entry(root, width=25)
name_entry.place(relx=0.5, rely=0.2)

surname_label = Label(root, text='Please enter your surname:')
surname_label.place(relx=0.1, rely=0.3)
surname_entry = Entry(root, width=25)
surname_entry.place(relx=0.5, rely=0.3)


def login():
    name = name_entry.get()
    surname = surname_entry.get()
    login_query = 'SELECT * FROM Login'
    mycursor.execute(login_query)
    user_info = mycursor.fetchall()
    print(user_info)
    if name == '' or surname == '':
        raise ValueError
    elif (name, surname) in user_info:
        messagebox.showinfo(message='You have successfully logged in')
    else:
        user_found = False
        for info in user_info:
            if name and surname in info:
                user_found = True
            if user_found:
                messagebox.showerror(message='Invalid details. Make sure you are registered on the system before '
                                             'signing in.')


signIn_button = Button(root, text='Sign In', width=20, command=login)
signIn_button.place(relx=0.51, rely=0.4)

frame = Frame(root, width=600, height=200, borderwidth=2, relief='ridge')
frame.place(relx=0.1, rely=0.5)

newUser_label = Label(frame, text='If you are new to LifeChoices please register as new user before logging in.')
newUser_label.place(relx=0.1, rely=0.2)


def register():
    root.destroy()
    import register


register_button = Button(frame, text='Register', width=20, command=register)
register_button.place(relx=0.35, rely=0.5)

root.mainloop()