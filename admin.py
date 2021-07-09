from tkinter import *
from tkinter import messagebox
import mysql.connector
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


root = Tk()
# Creating window title
root.title('Admin Account')
# Setting window size
root.geometry('800x700')
# Ensuring window size isn't adjustable
root.resizable('False', 'False')
# Setting background color
root.config(bg='black')

mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                               database='LC_Academy', auth_plugin='mysql_native_password')
mycursor = mydb.cursor()


logo = PhotoImage(file='Logo-Life-Choices.png')
logo = logo.subsample(3)
lc_logo = Label(root, image=logo, height=300, width=600, bg='black')
lc_logo.place(relx=0.13, rely=0)

header = Label(root, text='Welcome to the admin account', font=60, bg='black', fg='#9ce57e')
header.place(relx=0.15, rely=0.33)

frame = Frame(root, bg='black', height=300, width=700, borderwidth=2, relief='ridge')
frame.place(relx=0.06, rely=0.4)

inside_label = Label(frame, text='Amount of people signed in:', bg='black', fg='#9ce57e')
inside_label.place(relx=0.1, rely=0.1)
inside_entry = Entry(frame, width=10, bg='#9ce57e', state='readonly')
inside_entry.place(relx=0.45, rely=0.1)


def inside_building():
    query = 'SELECT * FROM SignIn WHERE time_out is NULL'
    mycursor.execute(query)
    time_in = mycursor.fetchall()
    numbers = len(time_in)
    inside_entry.config(state='normal')
    inside_entry.insert(0, numbers)
    inside_entry.config(state='readonly')
    print(numbers)


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


def send_email():
    query = 'SELECT * FROM SignIn WHERE time_out is NULL'
    mycursor.execute(query)
    time_in = mycursor.fetchall()
    numbers = len(time_in)
    admin_query = 'SELECT * FROM Admin_SignIn'
    mycursor.execute(admin_query)
    admin_info = mycursor.fetchall()
    with open('email.txt', 'r') as file:
        for line in file:
            if 'Email' in line:
                user_email = line[7:-1]
    if numbers >= 1:
        if user_email in admin_info:
            sender_email_id = 'lottogenerator1@gmail.com'
            receiver_email_id = [user_email]
            password = 'winnerWinner'
            subject = 'Not all users have signed out'
            msg = MIMEMultipart()
            msg['From'] = sender_email_id
            msg['To'] = ','.join(receiver_email_id)
            msg['Subject'] = subject
            body = 'Good afternoon / evening. \n Not all users have signed out for the day. Please do so on their ' \
                   'behalf in the admin account. \n Kind regards, \n LifeChoices Academy Team'
            msg.attach(MIMEText(body, 'plain'))
            text = msg.as_string()
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login(sender_email_id, password)
            s.sendmail(sender_email_id, receiver_email_id, text)
            s.quit()
            messagebox.showinfo(message='A message has been sent to admin regarding users still signed in.')


def user_info():
    import data


def sign_in():
    root.destroy()
    import signIn


def register():
    root.destroy()
    import register


def admin_login():
    root.destroy()
    import admin_login


def quit_():
    root.destroy()


update()

update_button = Button(frame, text='Update', width=10, command=lambda: [update()], bg='#9ce57e')
update_button.place(relx=0.7, rely=0.1)

user_info_label = Label(frame, text='To view all the user information click the button:', bg='black', fg='#9ce57e')
user_info_label.place(relx=0.1, rely=0.3)

user_info_button = Button(frame, text='User Info', width=10, command=user_info, bg='#9ce57e')
user_info_button.place(relx=0.7, rely=0.3)

return_label = Label(frame, text='Would you like to return to one of the previous windows?', bg='black', fg='#9ce57e')
return_label.place(relx=0.1, rely=0.52)

admin_button = Button(frame, text='Admin Login', bg='#9ce57e', width=10, command=admin_login)
admin_button.place(relx=0.1, rely=0.72)

signIn_button = Button(frame, text='Sign In / Out', bg='#9ce57e', width=10, command=sign_in)
signIn_button.place(relx=0.4, rely=0.72)

register_button = Button(frame, text='Register', bg='#9ce57e', width=10, command=register)
register_button.place(relx=0.7, rely=0.72)

mail_admin_button = Button(root, text='Email Admin', bg='#9ce57e', width=10, command=send_email)
mail_admin_button.place(relx=0.41, rely=0.88)

quit_button = Button(root, text='Quit', bg='#9ce57e', width=10, command=quit_)
quit_button.place(relx=0.67, rely=0.88)

root.mainloop()
