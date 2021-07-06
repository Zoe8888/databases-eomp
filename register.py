from tkinter import *
from tkinter import messagebox
import mysql.connector
import rsaidnumber

root = Tk()
# Creating window title
root.title('Register')
# Setting window size
root.geometry('800x800')
# Ensuring window size isn't adjustable
root.resizable('False', 'False')
root.config(bg='black')

mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                               database='LifeChoices', auth_plugin='mysql_native_password')
mycursor = mydb.cursor()

logo = PhotoImage(file='Logo-Life-Choices.png')
logo = logo.subsample(3)
lc_logo = Label(root, image=logo, height=300, width=600, bg='black')
lc_logo.place(relx=0.1, rely=0)

header = Label(root, text='Please enter in your details to be registered.', bg='black', fg='#9ce57e', font=50)
header.place(relx=0.1, rely=0.27)

name_label = Label(root, text='Please enter your name:', bg='black', fg='#9ce57e')
name_label.place(relx=0.1, rely=0.35)
name_entry = Entry(root, width=25, bg='#9ce57e')
name_entry.place(relx=0.53, rely=0.35)

surname_label = Label(root, text='Please enter your surname:', bg='black', fg='#9ce57e')
surname_label.place(relx=0.1, rely=0.4)
surname_entry = Entry(root, width=25, bg='#9ce57e')
surname_entry.place(relx=0.53, rely=0.4)

id_label = Label(root, text='Please enter your ID number:', bg='black', fg='#9ce57e')
id_label.place(relx=0.1, rely=0.45)
id_entry = Entry(root, width=25, bg='#9ce57e')
id_entry.place(relx=0.53, rely=0.45)

phone_label = Label(root, text='Please enter your phone number:', bg='black', fg='#9ce57e')
phone_label.place(relx=0.1, rely=0.5)
phone_entry = Entry(root, width=25, bg='#9ce57e')
phone_entry.place(relx=0.53, rely=0.5)

frame = Frame(root, width=600, height=150, borderwidth=2, relief='ridge', bg='black')
frame.place(relx=0.1, rely=0.6)

kin_label = Label(frame, text='Next of Kin information:', bg='black', fg='#9ce57e')
kin_label.place(relx=0.1, rely=0.1)

kinName_label = Label(frame, text='Name & Surname:', bg='black', fg='#9ce57e')
kinName_label.place(relx=0.1, rely=0.4)
kinName_entry = Entry(frame, width=30, bg='#9ce57e')
kinName_entry.place(relx=0.5, rely=0.4)

kinNumber_label = Label(frame, text='Contact Number:', bg='black', fg='#9ce57e')
kinNumber_label.place(relx=0.1, rely=0.6)
kinNumber_entry = Entry(frame, width=30, bg='#9ce57e')
kinNumber_entry.place(relx=0.5, rely=0.6)


def register():
    name = name_entry.get()
    surname = surname_entry.get()
    float(int(id_entry.get()))
    id = id_entry.get()
    float(int(phone_entry.get()))
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
    kin_name_query = 'SELECT fullName from NextOfKin'
    mycursor.execute(kin_name_query)
    kin_names = mycursor.fetchall()
    kin_num_query = 'SELECT number from NextOfKin'
    mycursor.execute(kin_num_query)
    kin_numbers = mycursor.fetchall()
    # try:
    if name == '' or surname == '' or id == '' or number == '' or kin_name == '' or kin_num == '':
        messagebox.showerror(message='Please make sure you filled all of the categories.')
    elif name in names and surname in surnames:
        messagebox.showerror(message='An account with these details has already been registered.')
    elif len(id) != 13:
        messagebox.showerror(message='Your ID number has to be 13 digits.')
    elif id in ids:
        messagebox.showerror(message='This ID number has already been registered with another user.')
    elif len(number) != 10:
        messagebox.showerror(message='Your cell number has to be 10 digits.')
    elif number in numbers:
        messagebox.showerror(message='This number has already been registered as another users contact number.')
    elif len(kin_num) != 10:
        messagebox.showerror(message='Your cell number has to equal 10 digits.')
    else:
        register_query = "INSERT INTO User_Info (name, surname, id, number) VALUES ('{}', '{}', '{}', '{}')". \
            format(name, surname, id, number)
        register_kin_query = "INSERT INTO NextOfKin (fullName, number) VALUES ('{}', '{}')".format(kin_name, kin_num)
        mycursor.execute(register_query, register_kin_query)
        messagebox.showinfo(message='You have been successfully registered. Please sign in in the next window.')
        root.destroy()
        import signIn
    # except ValueError:



register_button = Button(root, text='Register', width=20, command=register, bg='#9ce57e')
register_button.place(relx=0.55, rely=0.85)


root.mainloop()