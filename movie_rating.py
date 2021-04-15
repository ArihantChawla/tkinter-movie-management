## need to write a page to display the info now

from tkinter import *
import tkinter as tk
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

from PIL import ImageTk, Image   # pip3 install pillow


def wl():
    connection =mysql.connect(host="localhost", user="ashna03",password="password", database ="movie_project")
    cursor = connection.cursor()
    moviename= e_moviename.get()
    print(moviename)
    query = "Select * from movie_ratings where primary_title='"+ str(moviename) + "'"
    cursor.execute(query)
    result = cursor.fetchone()
    print(result)
    tid = result[0]
    moviename = result[3]

    query = "INSERT INTO watchlist VALUES('" + str(tid) + "','" + str(moviename) + "',1111111111);"
    cursor.execute(query)
    connection.commit()
    connection.close()
    MessageBox.showinfo("Button Clicked")

def enter_rating():
    connection =mysql.connect(host="localhost", user="ashna03",password="password", database ="movie_project")
    cursor = connection.cursor()
    moviename= e_moviename.get()
    rating = e_rate.get()
    print(moviename)
    print(rating)
    query = "Select * from movie_ratings where primary_title='"+ str(moviename) + "'"
    cursor.execute(query)
    result = cursor.fetchone()
    print(result)
    tid = result[0]
    moviename = result[3]

    query = "INSERT INTO user_ratings VALUES('" + str(tid) + "','" + str(moviename) + "'," + rating  + ",1111111111);"
    cursor.execute(query)
    connection.commit()
    connection.close()
    MessageBox.showinfo("Button Clicked")


def rt():
    nnW = tk.Toplevel(root)
    #nnW.geometry("1800x1200")
    nnW.title("Rating")

    e_rate = Entry(nnW)
    e_rate.place(x=300, y=580)
    rate = Button(nnW, text = "Rate this Movie", font=('comic sans ms' , 14, 'italic'), bg = "white", command = enter_rating)
    rate.place(x=380, y=550)


def fetch():
    moviename= e_moviename.get()
    connection =mysql.connect(host="localhost", user="ashna03",password="password", database ="movie_project")
    cursor = connection.cursor()
    query = "Select * from movie_ratings where primary_title='"+ str(moviename) + "'"
    cursor.execute(query)
    result = cursor.fetchone()

    tid = result[0]
    print(tid)
    type = result[1]
    year = result[2]
    moviename = result[3]
    print(moviename)
    runtime = result[4]
    genres = result[5]
    rating = result[6]
    votes = result[7]
    connection.close()
    nW = tk.Toplevel(root)
    nW.geometry("1800x1200")
    nW.title(moviename)

    ####
    bg = ImageTk.PhotoImage(file="images/back.jpg")
    bgL = Label(nW, image=bg).place(x=0, y=0, relwidth=1, relheight=1)


    ###
    mname = Label(nW, text =  "Movie             " + str(moviename), font= ('Arial',25, 'bold'))
    mname.place(x=300, y=300)

    genre = Label(nW, text =  "Genre            " + genres.split(',')[0], font= ('Arial',25, 'bold'))
    genre.place(x=300, y=370)

    ratings = Label(nW, text ="Rating            " + str(rating), font= ('Arial',25, 'bold'))
    ratings.place(x=300, y=440)

    year1 = Label(nW, text =   "Year              "+ str(year),font= ('Arial',25, 'bold'))
    year1.place(x=300, y=510)

    addtoWatchlist = Button(nW, text = "Add to Watchlist", font=('comic sans ms' , 14, 'italic'), bg = "white", command = wl)
    addtoWatchlist.place(x=300, y=550)

    rate = Button(nW, text = "Rate this Movie", font=('comic sans ms' , 14, 'italic'), bg = "white", command = rt)
    rate.place(x=380, y=550)


    pic= Image.open("posters/" + str(tid) + ".jpg")
    resized =pic.resize((400,550), Image.ANTIALIAS)
    #resized.show()
    new_pic = ImageTk.PhotoImage(resized)
    pict=Label(nW, image=new_pic).place(x=800, y= 130).pack(pady=20)



root = Tk()
root.geometry("1800x1200")
root.title("Registration Form")

bg = ImageTk.PhotoImage(file="images/back.jpg")
bgL = Label(root, image=bg).place(x=0, y=0, relwidth=1, relheight=1)



moviename = Label(root, text ="Movie Name",font= ('comic sans ms',15, 'bold'))
moviename.place(x=500, y=130)

e_moviename = Entry()
e_moviename.place(x=650, y=130)
Fetch = Button(root, text = "Fetch", font=('comic sans ms' , 14, 'italic'), bg = "white", command = fetch)
Fetch.place(x=650, y=200)



root.mainloop()
