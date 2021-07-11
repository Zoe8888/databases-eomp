from tkinter import *
from tkinter import messagebox
import mysql.connector


# Initializing the window
root = Tk()
# Creating window title
root.title('Admin Login')
# Setting window size
root.geometry('700x550')
# Ensuring window size isn't adjustable
root.resizable('False', 'False')
# Setting background color
root.config(bg='black')

# Calling the database
mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                               database='LC_Academy', auth_plugin='mysql_native_password')
mycursor = mydb.cursor()

# Setting an image
logo = PhotoImage(file='Logo-Life-Choices.png')
logo = logo.subsample(3)
lc_logo = Label(root, image=logo, height=300, width=600, bg='black')
lc_logo.place(relx=0.13, rely=0)

# Admin login header
header = Label(root, text='Log into admin account', bg='black', fg='#9ce57e', font=50)
header.place(relx=0.1, rely=0.43)

# Admin ID label 7 entry point
adminId_label = Label(root, text='Please enter your ID number:', bg='black', fg='#9ce57e')
adminId_label.place(relx=0.1, rely=0.53)
adminId_entry = Entry(root, width=25, bg='#9ce57e')
adminId_entry.place(relx=0.5, rely=0.53)

# Admin password label 7 entry point
password_label = Label(root, text='Please enter your password:', bg='black', fg='#9ce57e')
password_label.place(relx=0.1, rely=0.6)
password_entry = Entry(root, width=25, bg='#9ce57e')
password_entry.place(relx=0.5, rely=0.6)


# Function to log into admin account
def login():
    id_ = adminId_entry.get()
    password = password_entry.get()
    query = 'SELECT * from Admin_SignIn'
    mycursor.execute(query)
    admin_details = mycursor.fetchall()
    print(admin_details)
    if id_ == '' or password == '':
        messagebox.showerror(message='Please enter all fields.')
    elif (id_, password) in admin_details:
        messagebox.showinfo(message='You have successfully logged into the admin account.')
        root.destroy()
        import admin
    else:
        admin = False
        for details in admin_details:
            if id_ in details:
                admin = True
            if admin:
                messagebox.showerror(message='Incorrect password entered.')
        else:
            messagebox.showerror(message='Error! Incorrect details entered.')


# Login button
login_button = Button(root, text='Login', width=22, bg='#9ce57e', command=login)
login_button.place(relx=0.5, rely=0.7)


root.mainloop()