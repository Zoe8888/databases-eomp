from tkinter import *
from tkinter import messagebox
import mysql.connector
import rsaidnumber
import datetime


# Initializing the window
root = Tk()
# Creating window title
root.title('Sign In')
# Setting window size
root.geometry('700x750')
# Ensuring window size isn't adjustable
root.resizable('False', 'False')
# Setting a background color
root.config(bg='black')

# Calling the database
mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                               database='LC_Academy', auth_plugin='mysql_native_password')
mycursor = mydb.cursor()

# Setting an image
logo = PhotoImage(file='Logo-Life-Choices.png')
logo = logo.subsample(3)
lc_logo = Label(root, image=logo, height=300, width=600, bg='black')
lc_logo.place(relx=0.1, rely=0)

# Creating a header for the sign in window
header = Label(root, text='Welcome to LifeChoices Coding Academy. Please sign in.', font=50, bg='black', fg='#9ce57e')
header.place(relx=0.1, rely=0.32)

# Name label & entry points
name_label = Label(root, text='Please enter your name:', bg='black', fg='#9ce57e')
name_label.place(relx=0.1, rely=0.4)
name_entry = Entry(root, width=25, bg='#9ce57e')
name_entry.place(relx=0.5, rely=0.4)

# Surname label & entry points
surname_label = Label(root, text='Please enter your surname:', bg='black', fg='#9ce57e')
surname_label.place(relx=0.1, rely=0.45)
surname_entry = Entry(root, width=25, bg='#9ce57e')
surname_entry.place(relx=0.5, rely=0.45)

# ID number label & entry points
id_label = Label(root, text='Please enter your ID number:', bg='black', fg='#9ce57e')
id_label.place(relx=0.1, rely=0.5)
id_entry = Entry (root, width=25, bg='#9ce57e')
id_entry.place(relx=0.5, rely=0.5)


# Sign in function. If the users details are in the database they will be signed in.
def sign_in():
    try:
        name = str(name_entry.get())
        surname = str(surname_entry.get())
        id_ = id_entry.get()
        rsaidnumber.parse(id_)
        login_query = 'SELECT name, surname, id FROM User_Info'
        mycursor.execute(login_query)
        user_info = mycursor.fetchall()
        print(user_info)
        print(name, surname, id_)
        if name == '' or surname == '' or id_ == '':
            messagebox.showerror(message='Please fill in all your details')
        elif len(id_) != 13:
            messagebox.showerror(message='Enter a valid ID number.')
        elif (name, surname, id_) not in user_info:
            messagebox.showerror(message='User not found. Please make sure you have registered before logging in.')
        else:
            messagebox.showinfo(message='You have successfully signed in. Have a lovely day!')
            # root.destroy()
            date = datetime.date.today()
            print(date)
            time = datetime.datetime.now()
            print(time)
            time_query = "INSERT INTO SignIn (name, surname, id, date, time_in) values ('{}', '{}', '{}', '{}', '{}')" \
                .format(name, surname, id_, date, time)
            mycursor.execute(time_query)
            mydb.commit()
    except ValueError:
        messagebox.showerror(message='Your ID number is invalid.')


# Sign out function. If the users details are in the database they will be signed out.
def sign_out():
    try:
        name = str(name_entry.get())
        surname = str(surname_entry.get())
        id_ = id_entry.get()
        time_out_query = 'SELECT * FROM User_Info'
        mycursor.execute(time_out_query)
        user_info = mycursor.fetchall()
        if name == '' or surname == '' or id_ == '':
            messagebox.showerror(message='Please fill in all your details')
        elif len(id_) != 13:
            raise ValueError
        elif (name, surname, id_) not in user_info:
            messagebox.showerror(message='User not found. Please make sure you have registered before singing in.')
        else:
            messagebox.showinfo(message='You have successfully signed out. Enjoy the rest of your day/evening!')
            root.destroy()
            time = datetime.datetime.now()
            print(time)
            time_query = "UPDATE SignIn SET time_out='{}' WHERE id='{}'".format(time, id_)
            mycursor.execute(time_query)
            mydb.commit()
    except ValueError:
        messagebox.showerror(message='Please enter a valid ID number.')


# Sign in button
signIn_button = Button(root, text='Sign In', width=20, command=sign_in, fg='black', bg='#9ce57e')
signIn_button.place(relx=0.51, rely=0.65)

# Sign out button
signOut_button = Button(root, text='Sign Out', width=20, command=sign_out, fg='black', bg='#9ce57e')
signOut_button.place(relx=0.1, rely=0.65)

# Frame for new users
frame = Frame(root, width=600, height=150, borderwidth=2, relief='ridge', bg='black')
frame.place(relx=0.07, rely=0.75)

# Label informing new users they need to register
newUser_label = Label(frame, text='If you are new to LifeChoices please register as new user before logging in.',
                      bg='black', fg='#9ce57e')
newUser_label.place(relx=0.1, rely=0.2)


# Function to take new users to the register window
def register():
    root.destroy()
    import register


# Register button for new users
register_button = Button(frame, text='Register', width=20, command=register, fg='black', bg='#9ce57e')
register_button.place(relx=0.35, rely=0.5)


# Function to take the user to the admin login window
def admin(event=None):
    root.destroy()
    import admin_login


# Bind key to open up the admin login window
root.bind('<Control-a>', admin)

root.mainloop()