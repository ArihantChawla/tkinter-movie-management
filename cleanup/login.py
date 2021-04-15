from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

def check():
    uname= e_uname.get()
    password= e_password.get()
    if(uname=="" or password==""):
        MessageBox.showinfo("Insert Status", "All fields are required")
    else:
        connection =mysql.connect(host="localhost", user="ashna03", password="password", database ="movie_project")
        cursor = connection.cursor()
        query= "select FName, Password from users"
        cursor.execute(query)
        for (uname,pas) in cursor:
            check = 0
            if uname == uname and password == pas:
                check = 1            
        if check:
            MessageBox.showinfo("Insert Status", "Login Successful")
            print("Login successful")
        else:
            MessageBox.showinfo("Insert Status", "Please check the details again")
            print("Login unsuccessful")
        cursor.execute("commit")

        e_uname.delete(0, 'end')
        e_password.delete(0, 'end')

        connection.close()


root = Tk()
root.geometry("1800x1200")
root.title("Login Form")

uname = Label(root, text ="User Name", font= ('comic sans ms',15,'bold'))
uname.place(x=500, y=240)

password = Label(root, text ="Password",font= ('comic sans ms',15,'bold'))
password.place(x=500, y=270)

e_uname = Entry()
e_uname.place(x=650, y=240)

e_password = Entry()
e_password.place(x=650, y=270)

Register = Button(root, text = "Login", font=('comic sans ms' , 14, 'italic'), bg = "white", command = check)
Register.place(x=650, y=330)

root.mainloop()
