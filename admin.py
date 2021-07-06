from tkinter import *
from tkinter import messagebox
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
                               database='LifeChoices', auth_plugin='mysql_native_password')
mycursor = mydb.cursor()

logo = PhotoImage(file='Logo-Life-Choices.png')
logo = logo.subsample(3)
lc_logo = Label(root, image=logo, height=300, width=600, bg='black')
lc_logo.place(relx=0.13, rely=0)

header = Label(root, text='Welcome to the admin account', font=50, bg='black', fg='#9ce57e')
header.place(relx=0.1, rely=0.3)

frame = Frame(root, bg='black', height=500, width=700, borderwidth=2, relief='ridge')
frame.place(elx=0.1, rely=0.4)

inside_label = Label(frame, text='Amount of people inside the building:')
inside_label.place(relx=0.1, rely=0.1)
inside_entry = Entry(frame, width=10)
inside_entry.place(relx=0.5, rely=0.1)

user_info_label = Label(frame, text='')



root.mainloop()
