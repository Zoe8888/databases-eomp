from tkinter import *
from tkinter import messagebox
import mysql.connector

# Initializing the window
root = Tk()
# Creating window title
root.title('Admin Account')
# Setting window size
root.geometry('800x700')
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

# Creating a header for the register window
header = Label(root, text='Welcome to the admin account', font=60, bg='black', fg='#9ce57e')
header.place(relx=0.15, rely=0.33)

# Creating a frame to display info
frame = Frame(root, bg='black', height=300, width=700, borderwidth=2, relief='ridge')
frame.place(relx=0.06, rely=0.4)

# Label & entry points of all users currently still signed in
inside_label = Label(frame, text='Amount of people signed in:', bg='black', fg='#9ce57e')
inside_label.place(relx=0.1, rely=0.1)
inside_entry = Entry(frame, width=10, bg='#9ce57e', state='readonly')
inside_entry.place(relx=0.45, rely=0.1)


# Function to check how many users are still signed in
def inside_building():
    query = 'SELECT * FROM SignIn WHERE time_out is NULL'
    mycursor.execute(query)
    time_in = mycursor.fetchall()
    numbers = len(time_in)
    inside_entry.config(state='normal')
    inside_entry.insert(0, numbers)
    inside_entry.config(state='readonly')
    print(numbers)


# Function to update how many users are still signed in
def update():
    query = 'SELECT * FROM SignIn WHERE time_out is NULL'
    mycursor.execute(query)
    time_in = mycursor.fetchall()
    numbers = len(time_in)
    inside_entry.config(state='normal')
    inside_entry.delete(0, END)
    inside_entry.insert(0, numbers)
    inside_entry.config(state='readonly')
    print(numbers)
    messagebox.showinfo(message='The amount of users signed in has been updated!')


# Opens treeview table with user data
def user_info():
    import data


# Opens the sign in / sign out window
def sign_in():
    root.destroy()
    import signIn


# Opens the register window
def register():
    root.destroy()
    import register


# Opens the admin login window
def admin_login():
    root.destroy()
    import admin_login


# Quits the programme
def quit_():
    root.destroy()


# Displays the update of people signed in
update()

# Update button
update_button = Button(frame, text='Update', width=10, command=update, bg='#9ce57e')
update_button.place(relx=0.7, rely=0.1)

# View user info label
user_info_label = Label(frame, text='To view all the user information click the button:', bg='black', fg='#9ce57e')
user_info_label.place(relx=0.1, rely=0.3)

# User info button
user_info_button = Button(frame, text='User Info', width=10, command=user_info, bg='#9ce57e')
user_info_button.place(relx=0.7, rely=0.3)

# Return to previous window label
return_label = Label(frame, text='Would you like to return to one of the previous windows?', bg='black', fg='#9ce57e')
return_label.place(relx=0.1, rely=0.52)

# Admin button
admin_button = Button(frame, text='Admin Login', bg='#9ce57e', width=10, command=admin_login)
admin_button.place(relx=0.1, rely=0.72)

# Sign in / out button
signIn_button = Button(frame, text='Sign In / Out', bg='#9ce57e', width=10, command=sign_in)
signIn_button.place(relx=0.4, rely=0.72)

# Register button
register_button = Button(frame, text='Register', bg='#9ce57e', width=10, command=register)
register_button.place(relx=0.7, rely=0.72)

# Quit button
quit_button = Button(root, text='Quit', bg='#9ce57e', width=10, command=quit_)
quit_button.place(relx=0.67, rely=0.88)

root.mainloop()
