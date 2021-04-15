from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import sys
from PIL import ImageTk, Image   # pip3 install pillow

global Username
Username =  sys.argv[1]

root = Tk()
root.geometry("1800x1200")
root.title("User Ratings")
title=Label(root, text ="USER PROFILE", font= ('Comic sans ms',50, 'bold', 'underline'))
title.pack(side = "left")
title.place(x=250, y=160)



connection =mysql.connect(host="localhost", user="ashna03", password="password", database ="movie_project")
cursor = connection.cursor()
query= "select username, FName, LName, gender, email, AGE from users where username = '" + str(Username) +"';"

cursor.execute(query)
result = cursor.fetchall()[0]
print(Username)
query1= "select avg(ratings) from user_ratings Inner join users on user_ratings.contact= users.contcat where users.fname = 'uname' "
connection.commit()
connection.close()

uname = Label(root, text = "Username         " + str(result[0]), font= ('Arial',20, 'bold'))
uname.place(x=320, y=270)
name = Label(root, text =  "Name             " + result[1] + " " + result[2], font= ('Arial',20, 'bold'))
name.place(x=320, y=320)

gender = Label(root, text= "Gender           " + str(result[3]), font= ('Arial',20, 'bold'))
gender.place(x=320, y=370)

email = Label(root, text = "Email            "+ str(result[4]),font= ('Arial',20, 'bold'))
email.place(x=320, y=420)

age = Label(root, text =   "Age              "+ str(result[5]),font= ('Arial',20, 'bold'))
age.place(x=320, y=470)

#avg_rating = Label(root, text ="Average Rating"+ str(result[3]),font= ('Arial',20, 'bold'))
#avg_rating.place(x=320, y=520)

title1=Label(root, text ="Previously rated movies", font= ('Comic sans ms',40, 'bold', 'italic'))
title1.pack(side = "right")
title1.place(x=850, y=250)
title2=Label(root, text ="Movie Name             Ratings", font= ('Comic sans ms',25, 'bold', 'underline' ))
title2.pack(side = "right")
title2.place(x=850, y=350)



#bg = ImageTk.PhotoImage(file="Untitled.png")
#bgL = Label(root, image=bg).place(x=0, y=0, relwidth=1, relheight=1)








searchbar = Label(root, text ="Search", font= ('comic sans ms',25, 'bold'))
searchbar.place(x=300, y=700)

e_searchbar = Entry()
e_searchbar.place(x=400, y=710)

m1name = e_searchbar.get()


Search = Button(root, text = "Search", font=('comic sans ms' , 14, 'italic'), bg = "white")
Search.place(x=500, y=750)


Rating = Button(root, text = "Ratings", font=('Arial' , 30, 'italic'), bg = "white")#, command = user)
Rating.place(x=430, y=600)

root.mainloop()
