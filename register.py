from tkinter import *
from tkinter import messagebox
import mysql.connector
import rsaidnumber
import validate_email

root = Tk()
# Creating window title
root.title('Register')
# Setting window size
root.geometry('750x800')
# Ensuring window size isn't adjustable
root.resizable('False', 'False')
root.config(bg='black')

mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                               database='LC_Academy', auth_plugin='mysql_native_password')
mycursor = mydb.cursor()

logo = PhotoImage(file='Logo-Life-Choices.png')
logo = logo.subsample(3)
lc_logo = Label(root, image=logo, height=300, width=600, bg='black')
lc_logo.place(relx=0.1, rely=0)

header = Label(root, text='Please enter in your details to be registered.', bg='black', fg='#9ce57e', font=50)
header.place(relx=0.1, rely=0.3)

name_label = Label(root, text='Please enter your name:', bg='black', fg='#9ce57e')
name_label.place(relx=0.1, rely=0.37)
name_entry = Entry(root, width=25, bg='#9ce57e')
name_entry.place(relx=0.53, rely=0.37)

surname_label = Label(root, text='Please enter your surname:', bg='black', fg='#9ce57e')
surname_label.place(relx=0.1, rely=0.42)
surname_entry = Entry(root, width=25, bg='#9ce57e')
surname_entry.place(relx=0.53, rely=0.42)

id_label = Label(root, text='Please enter your ID number:', bg='black', fg='#9ce57e')
id_label.place(relx=0.1, rely=0.47)
id_entry = Entry(root, width=25, bg='#9ce57e')
id_entry.place(relx=0.53, rely=0.47)

email_label = Label(root, text='Please enter your email address:', bg='black', fg='#9ce57e')
email_label.place(relx=0.1, rely=0.52)
email_entry = Entry(root, width=25, bg='#9ce57e')
email_entry.place(relx=0.53, rely=0.52)

phone_label = Label(root, text='Please enter your phone number:', bg='black', fg='#9ce57e')
phone_label.place(relx=0.1, rely=0.57)
phone_entry = Entry(root, width=25, bg='#9ce57e')
phone_entry.place(relx=0.53, rely=0.57)

frame = Frame(root, width=600, height=150, borderwidth=2, relief='ridge', bg='black')
frame.place(relx=0.1, rely=0.65)

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
    id_ = id_entry.get()
    rsaidnumber.parse(id_)
    number = phone_entry.get()
    email = email_entry.get()
    kin_name = kinName_entry.get()
    kin_num = kinNumber_entry.get()
    id_query = 'SELECT id from User_Info'
    mycursor.execute(id_query)
    ids = mycursor.fetchall()
    user_query = 'SELECT * FROM User_Info'
    mycursor.execute(user_query)
    user_info = mycursor.fetchall()
    if name == '' or surname == '' or id_ == '' or number == '' or email == '' or kin_name == '' or kin_num == '':
        messagebox.showerror(message='Please make sure you filled all of the categories.')
    elif len(id_) != 13:
        messagebox.showerror(message='Please enter a valid ID number.')
    elif id_ in ids:
        messagebox.showerror(message='This ID number has already been registered with another user.')
    elif not validate_email.validate_email(email, verify=False):
        messagebox.showerror(message='Please enter a valid email address.')
    elif len(number) != 10:
        messagebox.showerror(message='Your cell number has to be 10 digits.')
    elif len(kin_num) != 10:
        messagebox.showerror(message='The cell number has to be 10 digits.')
    elif not user_info:
        messagebox.showerror(message='This user is already registered. Please go to the sign in page.')
    else:
        register_query = "INSERT INTO User_Info (name, surname, id, email, number) VALUES " \
                         "('{}', '{}', '{}', '{}', '{}')".format(name, surname, id_, email, number)
        mycursor.execute(register_query)
        register_kin_query = "INSERT INTO NextOfKin (kinName, kinNumber, id) VALUES ('{}', '{}', '{}')"\
            .format(kin_name, kin_num, id_)

        user_email = {'email': email}
        text_to_file(user_email)

        mycursor.execute(register_kin_query)
        mydb.commit()
        messagebox.showinfo(message='You have been successfully registered. Please sign in in the next window.')
        root.destroy()
        import signIn


def text_to_file(register):
    with open('email.txt', 'a') as email:
        email.write('Email: {}'.format(register['user_email']))


def sign_in():
    root.destroy()
    import signIn


register_button = Button(root, text='Register', width=20, command=register, bg='#9ce57e')
register_button.place(relx=0.54, rely=0.88)

signIn_button = Button(root, text='Sign In', width=20, command=sign_in, bg='#9ce57e')
signIn_button.place(relx=0.14, rely=0.88)

update = 'alter table NextOfKin modify column kinNumber varchar(10)'
mycursor.execute(update)
mydb.commit()

root.mainloop()