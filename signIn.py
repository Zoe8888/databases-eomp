from tkinter import *
from tkinter import messagebox
import mysql.connector
import rsaidnumber
import datetime

root = Tk()
# Creating window title
root.title('Sign In')
# Setting window size
root.geometry('700x750')
# Ensuring window size isn't adjustable
root.resizable('False', 'False')
# Setting a background color
root.config(bg='black')

mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                               database='LifeChoices', auth_plugin='mysql_native_password')
mycursor = mydb.cursor()

logo = PhotoImage(file='Logo-Life-Choices.png')
logo = logo.subsample(3)
lc_logo = Label(root, image=logo, height=300, width=600, bg='black')
lc_logo.place(relx=0.1, rely=0)

header = Label(root, text='Welcome to LifeChoices Coding Academy. Please sign in.', font=50, bg='black', fg='#9ce57e')
header.place(relx=0.1, rely=0.32)

name_label = Label(root, text='Please enter your name:', bg='black', fg='#9ce57e')
name_label.place(relx=0.1, rely=0.4)
name_entry = Entry(root, width=25, bg='#9ce57e')
name_entry.place(relx=0.5, rely=0.4)

surname_label = Label(root, text='Please enter your surname:', bg='black', fg='#9ce57e')
surname_label.place(relx=0.1, rely=0.45)
surname_entry = Entry(root, width=25, bg='#9ce57e')
surname_entry.place(relx=0.5, rely=0.45)


def login():
    name = str(name_entry.get())
    surname = str(surname_entry.get())
    login_query = 'SELECT * FROM Login'
    mycursor.execute(login_query)
    user_info = mycursor.fetchall()
    print(user_info)
    print(name, surname)
    if not user_info:
        messagebox.showerror(message='User not found. Please make sure you have registered before logging in.')
    elif name == '' or surname == '':
        messagebox.showerror(message='Please fill in your details')
    else:
        messagebox.showinfo(message='You have successfully logged in')

    #
    # elif (name, surname) in user_info:
    #     messagebox.showinfo(message='You have successfully signed in. Have a lovely day!')
    # else:
    #     # user_found = False
    #     # for info in user_info:
    #     #     if name in info:
    #     #         user_found = True
    #     # if user_found:
    #     #     messagebox.showerror(message='Incorrect surname.')
    #     if name in user_info:
    #         messagebox.showerror(message='Incorrect surname.')
    #     else:
    #         messagebox.showerror(message='Invalid details. Make sure you are registered on the system before signing '
    #                                      'in.')


signIn_button = Button(root, text='Sign In', width=20, command=login, fg='black', bg='#9ce57e')
signIn_button.place(relx=0.51, rely=0.55)

frame = Frame(root, width=600, height=200, borderwidth=2, relief='ridge', bg='black')
frame.place(relx=0.07, rely=0.65)

newUser_label = Label(frame, text='If you are new to LifeChoices please register as new user before logging in.',
                      bg='black', fg='#9ce57e')
newUser_label.place(relx=0.1, rely=0.2)


def register():
    root.destroy()
    import register


register_button = Button(frame, text='Register', width=20, command=register, fg='black', bg='#9ce57e')
register_button.place(relx=0.35, rely=0.5)

sql = 'INSERT INTO Login (name, surname, id, number) VALUES (%s, %s, %s, %s)'
val = ('Zoe', 'Erispe', '9903200072086', '0849219477')
mycursor.execute(sql, val)

# update = 'UPDATE Login MODIFY id BIGINT'
# mycursor.execute(update)
# mydb.commit()

root.mainloop()