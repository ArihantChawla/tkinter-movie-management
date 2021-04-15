from tkinter import *
import tkinter.messagebox as MessageBox
from PIL import ImageTk,Image
import pymysql
import mysql.connector as mysql
from tkinter import ttk
import os
import sys





#bg = ImageTk.PhotoImage(file="Untitled.png")
#	bgL = Label(root, image=bg).place(x=0, y=0, relwidth=1, relheight=1)









def check():
    uname= login_e1.get()
    password= login_e2.get()
    #print(uname)
    #print(password)
    if(uname=="" or password==""):
        MessageBox.showinfo("Insert Status", "All fields are required")
    else:
        connection =mysql.connect(host="localhost", user="ashna03", password="password", database ="movie_project")
        cursor = connection.cursor()
        query= "select username, Password from users"

        ### SEE THIS: other sers not able to login

        cursor.execute(query)
        check = 0
        for (username,pas) in cursor:
            if uname == username and password == pas:
                check = 1

        if check:
            MessageBox.showinfo("Insert Status", "Login Successful")
            print("Login successful")
            os.execl(sys.executable, "python3", "user_rating.py", uname)
            # ADD COMMAND TO OPEN ACCOUNT WINDOW


        else:
            MessageBox.showinfo("Insert Status", "Please check the details again")
            print("Login unsuccessful")
        cursor.execute("commit")

        login_e1.delete(0, 'end')
        login_e2.delete(0, 'end')

        connection.close()

def sup():
    os.execl(sys.executable, "python3", "RegForm.py")


# find position where tkinter window is to be centered


main_win = Tk()
ws = main_win.winfo_screenwidth()  # width of the screen
hs = main_win.winfo_screenheight()  # height of the screen
xcenter = (ws / 2) - (700 / 2)  # 700 is the width and height of the tkinter window
ycenter = (hs / 2) - (700 / 2)
main_win.geometry("700x700+%d+%d"%(xcenter,(ycenter)))  # size and placement of the tkinter window WxH+X+Y
main_win.configure(bg='#ffffff') # background color of tkinter window

#Headings
l1 = Label(main_win, text = 'A.R. Movies', bg = 'white', fg = 'blue', anchor = 'w', font=('monotype corsiva', 26,'bold'))
l2 = Label(main_win, text = 'Keep track of all your favorite movies', bg = 'white', fg = 'blue', anchor = 'w', font=('monotype corsiva', 15,'bold'))
l1.place(relx = 0.4, rely = 0.05)
l2.place(relx = 0.35, rely = 0.15)

#frame for log in
Frame_login = Frame(main_win, bg="#FFBB00", bd=4)
Frame_login.place(relx = 0.05, rely = 0.3, relwidth=0.5,relheight=0.4)

login_l0 = Label(Frame_login, text = 'Log In:', bg = 'white', fg = 'blue', font=('monotype corsiva', 15))
login_l0.place(relx=0.5,rely=0, relwidth=0.2, relheight=0.2)

login_l1 = Label(Frame_login, text = 'Username:', bg = 'white', fg = 'blue', font=('monotype corsiva', 15))
login_l1.place(relx=0,rely=0.3, relwidth=0.3, relheight=0.15)
login_e1 = Entry(Frame_login, bg = 'white', fg = 'blue')
login_e1.place(relx = 0.5, rely = 0.33)

login_l2 = Label(Frame_login, text = 'Password:', bg = 'white', fg = 'blue', font=('monotype corsiva', 15))
login_l2.place(relx=0,rely=0.6, relwidth=0.3, relheight=0.15)
login_e2 = Entry(Frame_login, bg = 'white', fg = 'blue', show = '*')
login_e2.place(relx = 0.5, rely = 0.67)

login_btn = Button(Frame_login, text = 'Log In', width = 10, command = check) # command--open cw1
login_btn.place(relx = 0.7, rely = 0.85)


#outside frame
l3 = Label(main_win, text = 'New to A.R.?',bg = 'white', fg = 'blue', font=('monotype corsiva', 15))
l3.place(relx = 0.68, rely = 0.4)
signup_btn = Button(main_win, text = 'Sign Up', width = 10, command = sup)
signup_btn.place(relx = 0.7, rely = 0.5)



main_win.mainloop()
