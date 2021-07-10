import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
import validate_email
import rsaidnumber

root = Tk()
root.title('LC Academy User Info')
root.geometry('800x1000')
root.config(bg='black')
root.resizable('False', 'False')

mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                               database='LC_Academy', auth_plugin='mysql_native_password')
mycursor = mydb.cursor()

tree = ttk.Treeview(root)
tree['show'] = 'headings'

tree['columns'] = ('name', 'surname', 'id', 'number')

tree.column('name', width=100, minwidth=80, anchor=tk.CENTER)
tree.column('surname', width=100, minwidth=80, anchor=tk.CENTER)
tree.column('id', width=150, minwidth=120, anchor=tk.CENTER)
tree.column('number', width=110, minwidth=100, anchor=tk.CENTER)

tree.heading('name', text='Name', anchor=tk.CENTER)
tree.heading('surname', text='Surname', anchor=tk.CENTER)
tree.heading('id', text='ID number', anchor=tk.CENTER)
tree.heading('number', text='Cell number', anchor=tk.CENTER)

frame = Frame(root, width=600, height=700, borderwidth=2, relief='ridge', bg='black')
frame.place(relx=0.1, rely=0.24)

header = Label(frame, text='Either create a new user or edit / delete an existing user.', bg='black', fg='#9ce57e',
               font=50)
header.place(relx=0.1, rely=0.03)

name_label = Label(frame, text='Name:', bg='black', fg='#9ce57e')
name_label.place(relx=0.1, rely=0.1)
name_entry = Entry(frame, width=25, bg='#9ce57e')
name_entry.place(relx=0.53, rely=0.1)

surname_label = Label(frame, text='Surname:', bg='black', fg='#9ce57e')
surname_label.place(relx=0.1, rely=0.15)
surname_entry = Entry(frame, width=25, bg='#9ce57e')
surname_entry.place(relx=0.53, rely=0.15)

id_label = Label(frame, text='ID number:', bg='black', fg='#9ce57e')
id_label.place(relx=0.1, rely=0.2)
id_entry = Entry(frame, width=25, bg='#9ce57e')
id_entry.place(relx=0.53, rely=0.2)

email_label = Label(frame, text='Email address:', bg='black', fg='#9ce57e')
email_label.place(relx=0.1, rely=0.25)
email_entry = Entry(frame, width=25, bg='#9ce57e')
email_entry.place(relx=0.53, rely=0.25)

phone_label = Label(frame, text='Number:', bg='black', fg='#9ce57e')
phone_label.place(relx=0.1, rely=0.3)
phone_entry = Entry(frame, width=25, bg='#9ce57e')
phone_entry.place(relx=0.53, rely=0.3)

time_in_label = Label(frame, text='Signed in:', bg='black', fg='#9ce57e')
time_in_label.place(relx=0.1, rely=0.35)
time_in_entry = Entry(frame, width=25, bg='#9ce57e')
time_in_entry.place(relx=0.53, rely=0.35)

time_out_label = Label(frame, text='Signed out:', bg='black', fg='#9ce57e')
time_out_label.place(relx=0.1, rely=0.4)
time_out_entry = Entry(frame, width=25, bg='#9ce57e')
time_out_entry.place(relx=0.53, rely=0.4)

kin_header = Label(frame, text='Next of Kin information:', font=40, bg='black', fg='#9ce57e')
kin_header.place(relx=0.1, rely=0.48)

kinName_label = Label(frame, text='Name & Surname:', bg='black', fg='#9ce57e')
kinName_label.place(relx=0.1, rely=0.54)
kinName_entry = Entry(frame, width=25, bg='#9ce57e')
kinName_entry.place(relx=0.53, rely=0.54)

kinNumber_label = Label(frame, text='Contact Number:', bg='black', fg='#9ce57e')
kinNumber_label.place(relx=0.1, rely=0.6)
kinNumber_entry = Entry(frame, width=25, bg='#9ce57e')
kinNumber_entry.place(relx=0.53, rely=0.6)


def data():
    tree.delete(*tree.get_children())
    user_query = 'SELECT * FROM User_Info'
    mycursor.execute(user_query)
    info = mycursor.fetchall()
    for x in range(len(info)):
        tree.insert(parent='', index='end', text='',
                    values=(info[x][0], info[x][1], info[x][2], info[x][4]))


data()


def add():
    name = name_entry.get()
    surname = surname_entry.get()
    id_ = id_entry.get()
    email = email_entry.get()
    number = phone_entry.get()
    time_in = time_in_entry.get()
    time_out = time_out_entry.get()
    kin_name = kinName_entry.get()
    kin_num = kinNumber_entry.get()
    if name == '' or surname == '' or id_ == '' or email == '' or number == '' or time_in == '' or time_out == '' or kin_name == '' \
            or kin_num == '':
        messagebox.showerror(message='Make sure all the fields are filled')
    elif len(id_) != 13:
        messagebox.showerror(message='The ID number should be 13 digits.')
    elif len(number) != 10 or len(kin_num) != 10:
        messagebox.showerror(message='Phone number should be 10 digits.')
    else:
        messagebox.showinfo(message='Successfully added new user')
        update_query = "INSERT INTO User_Info (name, surname, id, email, number) VALUES " \
                       "('{}', '{}', '{}', '{}', '{}')".format(name, surname, id_, email, number)
        mycursor.execute(update_query)
        mydb.commit()
        time_update_query = "INSERT INTO SignIn (name, surname, id, time_in, time_out) VALUES " \
                            "('{}', '{}', '{}', '{}', '{}')" .format(name, surname, id_, time_in, time_out)
        mycursor.execute(time_update_query)
        mydb.commit()
        kin_update_query = "INSERT INTO NextOfKin (kinName, kinNumber, id) VALUES ('{}', '{}', '{}')" \
            .format(kin_name, kin_num, id_)
        mycursor.execute(kin_update_query)
        mydb.commit()
    data()


def update():
    name = name_entry.get()
    surname = surname_entry.get()
    id_ = id_entry.get()
    email = email_entry.get()
    number = phone_entry.get()
    time_in = time_in_entry.get()
    time_out = time_out_entry.get()
    kin_name = kinName_entry.get()
    kin_num = kinNumber_entry.get()
    update_query = "UPDATE User_Info SET name='{}', surname='{}', id='{}', email='{}', number='{}' WHERE id='{}'"\
        .format(name, surname, id_, email, number, id_)
    mycursor.execute(update_query)
    time_update_query = "UPDATE SignIn SET name='{}', surname'{}', id='{}', time_in='{}', time_out='{}' WHERE id='{}'"\
        .format(name, surname, id_, time_in, time_out, id_)
    mycursor.execute(time_update_query)
    mydb.commit()
    kin_update_query = "UPDATE NextOfKin SET kinName='{}', kinNumber='{}' where id='{}'".format(kin_name, kin_num, id_)
    mycursor.execute(kin_update_query)
    mydb.commit()
    messagebox.showinfo(message='Update successful!')
    data()


def delete():
    id_ = id_entry.get()
    delete_query = "DELETE FROM NextOfKin WHERE id='{}'".format(id_)
    mycursor.execute(delete_query)
    mydb.commit()

    admin_check_query = "SELECT * FROM Admin_SignIn WHERE id='{}'".format(id_)
    mycursor.execute(admin_check_query)
    admin = mycursor.fetchall()
    if admin:
        delete_admin_query = "DELETE FROM Admin_SignIn WHERE id='{}'".format(id_)
        mycursor.execute(delete_admin_query)
        mydb.commit()
    delete_user = "DELETE FROM User_Info WHERE id='{}'".format(id_)
    mycursor.execute(delete_user)
    mydb.commit()
    messagebox.showinfo(message='User successfully deleted!')
    data()


def fill_entries(event=None):
    highlighted = tree.focus()
    user_info = tree.item(highlighted)
    user_info = user_info['values']
    print(user_info)
    query = "SELECT * FROM User_Info WHERE id like '%{}'".format(user_info[2])
    mycursor.execute(query)
    user_data = mycursor.fetchall()
    print(user_data)
    name_entry.delete(0, END)
    name_entry.insert(0, user_data[0][0])
    surname_entry.delete(0, END)
    surname_entry.insert(0, user_data[0][1])
    id_entry.delete(0, END)
    id_entry.insert(0, user_data[0][2])
    email_entry.delete(0, END)
    email_entry.insert(0, user_data[0][3])
    phone_entry.delete(0, END)
    phone_entry.insert(0, user_data[0][4])

    time_query = "SELECT * FROM SignIn WHERE id like '%{}'".format(user_info[2])
    mycursor.execute(time_query)
    time_stamp = mycursor.fetchall()
    print(time_stamp)
    time_in_entry.delete(0, END)
    time_in_entry.insert(0, time_stamp[0][4])
    time_out_entry.delete(0, END)
    time_out_entry.insert(0, time_stamp[0][5])

    kin_query = "SELECT * FROM NextOfKin WHERE id like '%{}'".format(user_info[2])
    mycursor.execute(kin_query)
    kin_data = mycursor.fetchall()
    kinName_entry.delete(0, END)
    kinName_entry.insert(0, kin_data[0][0])
    kinNumber_entry.delete(0, END)
    kinNumber_entry.insert(0, kin_data[0][1])
    data()


def grant():
    id_ = id_entry.get()
    rsaidnumber.parse(id_)
    email = email_entry.get()
    password = password_entry.get()
    if id_ == '' or email == '' or password == '':
        messagebox.showerror(message='Make sure the ID number, email and password entry fields are filled all in.')
    elif len(id_) != 13:
        messagebox.showerror(message='The ID number should be 13 digits.')
    elif len(password) > 10:
        messagebox.showerror(message='Password cannot exceed 10 characters.')
    elif validate_email.validate_email(email, verify=True):
        messagebox.showerror(message='Make sure the email address entered is valid.')
    else:
        query = "INSERT INTO Admin_SignIn (id, email, password) VALUES ('{}', '{}', '{}')".format(id_, email, password)
        mycursor.execute(query)
        mydb.commit()
        messagebox.showinfo(message='You have successfully granted this user!')


def update_admin_password():
    id_ = id_entry.get()
    password = password_entry.get()
    admin = "SELECT * FROM Admin_SignIn WHERE id='{}'".format(id_)
    mycursor.execute(admin)
    if id_ in admin:
        if id_ == '' or password == '':
            messagebox.showerror(message='Make sure both the ID number and password entry fields are filled in.')
        elif len(id_) != 13:
            messagebox.showerror(message='The ID number should be 13 digits.')
        elif len(password) > 10:
            messagebox.showerror(message='Password cannot exceed 10 characters.')
        else:
            query = "UPDATE Admin_SignIn SET password='{}' WHERE id='{}'".format(password, id_)
            mycursor.execute(query)
            mydb.commit()
            messagebox.showinfo(message='You have successfully updated this users admin password!')


def remove():
    id_ = id_entry.get()
    admin = "SELECT * FROM Admin_SignIn WHERE id='{}'".format(id_)
    mycursor.execute(admin)
    if id_ in admin:
        remove_admin_query = "DELETE FROM Admin_SignIn WHERE id='{}'".format(id_)
        mycursor.execute(remove_admin_query)
        mydb.commit()
        messagebox.showinfo(message='You have successfully revoked this users admin privileges.')


tree.bind('<ButtonRelease-1>', fill_entries)

add_button = Button(frame, text='Add', width=13, bg='#9ce57e', command=add)
add_button.place(relx=0.1, rely=0.68)

edit_button = Button(frame, text='Edit', width=13, bg='#9ce57e', command=update)
edit_button.place(relx=0.38, rely=0.68)

delete_button = Button(frame, text='Delete', width=13, bg='#9ce57e', command=delete)
delete_button.place(relx=0.65, rely=0.68)

permission_label = Label(frame, text='Would you to grant this user permission as an admin?', bg='black', fg='#9ce57e',
                         font=40)
permission_label.place(relx=0.1, rely=0.79)

password_label = Label(frame, text='Set admin password:', bg='black', fg='#9ce57e')
password_label.place(relx=0.1, rely=0.86)
password_entry = Entry(frame, bg='#9ce57e', width=25)
password_entry.place(relx=0.53, rely=0.86)

grant_button = Button(frame, text='Grant', width=13, bg='#9ce57e', command=grant)
grant_button.place(relx=0.1, rely=0.92)

update_button = Button(frame, text='Update', width=13, bg='#9ce57e', command=update_admin_password)
update_button.place(relx=0.38, rely=0.92)

remove_button = Button(frame, text='Remove', width=13, bg='#9ce57e', command=remove)
remove_button.place(relx=0.65, rely=0.92)


tree.pack()
root.mainloop()