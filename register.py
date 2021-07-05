from tkinter import *
from tkinter import messagebox
import mysql.connector
import rsaidnumber

root = Tk()
# Creating window title
root.title('Login')
# Setting window size
root.geometry('800x800')
# Ensuring window size isn't adjustable
root.resizable('False', 'False')

mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='LifeChoices',
                               auth_plugin='mysql_native_password')
mycursor = mydb.cursor()

header = Label(root, text='Welcome to LifeChoices Coding Academy. Please sign in.', width=80)
header.place(relx=0.1, rely=0.1)

name_label = Label(root, text='Please enter your name:')
name_label.place(relx=0.1, rely=0.2)
name_entry = Entry(root, width=25)
name_entry.place(relx=0.53, rely=0.2)

surname_label = Label(root, text='Please enter your surname:')
surname_label.place(relx=0.1, rely=0.3)
surname_entry = Entry(root, width=25)
surname_entry.place(relx=0.53, rely=0.3)

id_label = Label(root, text='Please enter your ID number:')
id_label.place(relx=0.1, rely=0.4)
id_entry = Entry(root, width=25)
id_entry.place(relx=0.53, rely=0.4)

phone_label = Label(root, text='Please enter your phone number:')
phone_label.place(relx=0.1, rely=0.5)
phone_entry = Entry(root, width=25)
phone_entry.place(relx=0.53, rely=0.5)

frame = Frame(root, width=500, height=200, borderwidth=2, relief='ridge')
frame.place(relx=0.1, rely=0.6)

kin_label = Label(frame, text='Next of Kin information:')
kin_label.place(relx=0.1, rely=0.1)

kinName_label = Label(frame, text='Name & Surname:')
kinName_label.place(relx=0.1, rely=0.25)
kinName_entry = Entry(frame, width=20)
kinName_entry.place(relx=0.5, rely=0.25)

kinNumber_label = Label(frame, text='Contact Number:')
kinNumber_label.place(relx=0.1, rely=0.4)
kinNumber_entry = Entry(frame, width=20)
kinNumber_entry.place(relx=0.5, rely=0.4)

login_button = Button(root, text='Login', width=20)
login_button.place(relx=0.1, rely=0.9)

register_button = Button(root, text='Register', width=20)
register_button.place(relx=0.55, rely=0.9)



def register():
    name = name_entry.get()
    surname = surname_entry.get()
    int(id_entry.get())
    id = id_entry.get()
    int(phone_entry.get())
    number = phone_entry.get()
    kin_name = kinName_entry.get()
    int(kinNumber_entry.get())
    kin_num = kinNumber_entry.get()
    name_query = 'SELECT name from Login'
    mycursor.execute(name_query)
    names = mycursor.fetchall()
    surname_query = 'SELECT surname from Login'
    mycursor.execute(surname_query)
    surnames = mycursor.fetchall()
    id_query = 'SELECT id from Login'
    mycursor.execute(id_query)
    ids = mycursor.fetchall()
    number_query = 'SELECT number from Login'
    mycursor.execute(number_query)
    numbers = mycursor.fetchall()
    kin_name_query = 'SELECT kinName from NextOfKin'
    mycursor.execute(kin_name_query)
    kin_names = mycursor.fetchall()
    kin_num_query = 'SELECT kinNumber from NextOfKin'
    mycursor.execute(kin_num_query)
    kin_numbers = mycursor.fetchall()
    try:
        if name == '' or surname == '' or id == '' or number == '' or kin_name == '' or kin_num == '':
            raise ValueError
        elif name in names and surname in surnames:
            messagebox.showerror(message='An account with these details has already been registered.')
        elif len(id) != 13:
            messagebox.showerror(message='Your ID number has to be 13 digits.')
        elif id in ids:
            messagebox.showerror(message='This ID number has already been registered with another user.')
        elif len(number) != 10:
            messagebox.showerror(message='Your cell number has to equal 10 digits.')
        elif number in numbers:
            messagebox.showerror(message='This number has already been registered as another users contact number.')
        elif len(kin_num) != 10:
            messagebox.showerror(message='Your cell number has to equal 10 digits.')
        else:
            register_query = "INSERT INTO Login (name, surname, id, number) VALUES ('{}', '{}', '{}', '{}')".\
                            format(name, surname, id, number)
            register_kin_query = "INSERT INTO NextOfKin (name, number) VALUES ('{}', '{}')".format(kin_name, kin_num)
            mycursor.execute(register_query, register_kin_query)
            messagebox.showinfo(message='You have been successfully registered. Have a lovely day!')
    except ValueError:
        messagebox.showerror(message='Please make sure you filled all of the categories.')


root.mainloop()