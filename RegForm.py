from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import sys
import os
from PIL import ImageTk   # pip3 install pillow


def insert():
    fname= e_fname.get()
    lname= e_lname.get()
    uname= e_uname.get()
    contact= e_contact.get()
    email = e_email.get()
    age= e_age.get()
    gender=e_gender.get()
    password= e_password.get()
    cpassword = e_cpassword.get()
    if(fname=="" or lname=="" or uname=="" or contact=="" or email=="" or age=="" or password=="" or cpassword==""):
        MessageBox.showinfo("Insert Status", "All fields are required")
    elif (password != cpassword):
        MessageBox.showinfo("Insert Status", "Password and Confirm Password doesn't match")
    else:
        connection =mysql.connect(host="localhost", user="ashna03", password="password", database ="movie_project")
        cursor = connection.cursor()
        cursor.execute("insert into users values('"+ email +"','"+ gender +"','"+ contact +"','"+ fname +"','"+ lname +"','"+ age +"','"+ password +"','"+ uname +"');")
        cursor.execute("commit")

        e_fname.delete(0, 'end')
        e_lname.delete(0, 'end')
        e_uname.delete(0, 'end')
        e_contact.delete(0, 'end')
        e_email.delete(0, 'end')
        e_age.delete(0, 'end')
        e_gender.delete(0, 'end')
        e_password.delete(0, 'end')
        e_cpassword.delete(0, 'end')
        MessageBox.showinfo("Insert Status", "Inserted Successfully. Please Login with your new credentials")
        connection.close()
        os.execl(sys.executable, "python3", "MAIN.py")

root = Tk()
root.geometry("1800x1200")
root.title("Registration Form")

#bg = ImageTk.PhotoImage(file="Untitled.png")
#	bgL = Label(root, image=bg).place(x=0, y=0, relwidth=1, relheight=1)


fname = Label(root, text ="First Name", font= ('comic sans ms',15, 'bold'))
fname.place(x=500, y=240)

lname = Label(root, text ="Last Name", font= ('comic sans ms',15, 'bold'))
lname.place(x=500, y=270)

uname = Label(root, text ="User Name", font= ('comic sans ms',15, 'bold'))
uname.place(x=500, y=300)

contact = Label(root, text ="Contact No.",font= ('comic sans ms',15, 'bold'))
contact.place(x=500, y=330)

email = Label(root, text ="Email", font= ('comic sans ms',15, 'bold'))
email.place(x=500, y=360)

age= Label(root, text ="Age",font= ('comic sans ms',15, 'bold'))
age.place(x=500, y=390)

gender= Label(root, text ="Gender",font= ('comic sans ms',15, 'bold'))
gender.place(x=500, y=420)

password = Label(root, text ="Password",font= ('comic sans ms',15, 'bold'))
password.place(x=500, y=450)

cpassword = Label(root, text ="Confirm Password",font= ('comic sans ms',15, 'bold'))
cpassword.place(x=500, y=480)

e_fname = Entry()
e_fname.place(x=650, y=240)

e_lname = Entry()
e_lname.place(x=650, y=270)

e_uname = Entry()
e_uname.place(x=650, y=300)

e_contact = Entry()
e_contact.place(x=650, y=330)

e_email = Entry()
e_email.place(x=650, y=360)

e_age = Entry()
e_age.place(x=650, y=390)

e_gender = Entry()
e_gender.place(x=650, y=420)


e_password = Entry(show = '*')
e_password.place(x=650, y=450)

e_cpassword = Entry(show = '*')
e_cpassword.place(x=650, y=480)

Register = Button(root, text = "Register", font=('comic sans ms' , 14, 'italic'), bg = "white", command = insert)
Register.place(x=650, y=530)



root.mainloop()
