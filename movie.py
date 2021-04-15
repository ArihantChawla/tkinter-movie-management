from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

from PIL import ImageTk, Image   # pip3 install pillow

def find(mname):
    cursor = connection.cursor()
    query= "select primary_title, genres, average_rating, year_release, tid from movie_ratings where primary_title like " + "'" + str(mname) + "';"
    cursor.execute(query)
    result = (cursor.fetchall())[0]
    print(result)
    #cursor =type(cursor))
    mname = Label(root, text =  "Movie             " + result[0], font= ('Arial',25, 'bold'))
    mname.place(x=300, y=300)

    genre = Label(root, text =  "Genre            " + result[1].split(',')[0], font= ('Arial',25, 'bold'))
    genre.place(x=300, y=370)

    ratings = Label(root, text ="Rating            " + str(result[2]), font= ('Arial',25, 'bold'))
    ratings.place(x=300, y=440)

    year = Label(root, text =   "Year              "+ str(result[3]),font= ('Arial',25, 'bold'))
    year.place(x=300, y=510)

    tid = result[4]
    return tid


root = Tk()
root.geometry("1800x1200")
root.title("Movie Ratings")
title=Label(root, bg='yellow', text ="Movie Browser", font= ('Comic sans ms',55, 'bold'))
title.pack(side = "left")
title.place(x=270, y=160)
connection =mysql.connect(host="localhost", user="ashna03", password="password", database ="movie_project")

tid = find('Bean')
#pic = Image.open("Untitled.jpg")
pic= Image.open("posters/" + str(tid) + ".jpg")
resized =pic.resize((400,550), Image.ANTIALIAS)
new_pic = ImageTk.PhotoImage(resized)
pict=Label(root, image=new_pic)
pict.pack(pady=20)
pict.place(x=800, y= 130)

connection.close()
root.mainloop()
