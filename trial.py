from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import pymysql
from tkinter import ttk
from PIL import ImageTk
from PIL import Image

main_win = Tk()
ws = main_win.winfo_screenwidth()  # width of the screen
hs = main_win.winfo_screenheight()  # height of the screen

# find position where tkinter window is to be centered
xcenter = (ws / 2) - (700 / 2)  # 700 is the width and height of the tkinter window
ycenter = (hs / 2) - (700 / 2)
main_win.geometry("700x700+%d+%d"%(xcenter,(ycenter)))  # size and placement of the tkinter window WxH+X+Y
main_win.configure(bg='#ffffff') # background color of tkinter window

heading_cw3 = Label(main_win, text = 'Browse Movies',bg = 'white', fg = 'blue', font=('monotype corsiva', 15))
heading_cw3.place(relx = 0, rely = 0)
search = Entry(main_win, bg = 'white', fg = 'blue')
search.insert(0,'Search Movies')
search.place(relx = 0, rely = 0.15)

popular = Label(main_win, text = 'Popular Movies:',bg = 'white', fg = 'blue', font=('monotype corsiva', 15))
popular.place(relx = 0, rely = 0.3)

    #Movie catalog


canvas = Canvas(main_win, width = 250,  
                        height = 500)
canvas.place()   


movie1 = ImageTk.PhotoImage(Image.open('movie1.jpg').resize((250,500),Image. ANTIALIAS))
canvas.create_image(135, 20, anchor = NW, 
                   image = movie1)  
movie2 = ImageTk.PhotoImage(Image.open('movie2.jpg'))
movie3 = ImageTk.PhotoImage(Image.open('movie3.jpg'))
movie4 = ImageTk.PhotoImage(Image.open('movie4.jpg'))
movie5 = ImageTk.PhotoImage(Image.open('movie5.jpg'))

img_list = [movie1, movie2, movie3, movie4, movie5]

img_label = Label(image = movie1)
img_label.grid(row = 0, column = 0, columnspan = 3)

def forward(img_no):
    global img_label
    global btn_fwd
    global btn_back
    img_label.grid_forget()
    img_label = Label(image = img_list[img_no-1])
    btn_fwd = Button(main_win, text = '>>', command = lambda:forward(img_no))
    btn_back = Button(main_win, text = '<<', command = lambda:back(img_no-1))

    if img_no == 5:
        btn_fwd = Button(main_win, text = '>>', state = DISABLED)

    img_label.grid(row = 0, column = 0, columnspan = 3)
    btn_back.grid(row = 1, column = 0)
    btn_fwd.grid(row = 1, column = 2)

def back(img_no):
    global img_label
    global btn_fwd
    global btn_back
    img_label.grid_forget()
    img_label = Label(image = img_list[img_no-1])
    btn_fwd = Button(main_win, text = '>>', command = lambda: forward(img_no))
    btn_back = Button(main_win, text = '<<', command = lambda: back(img_no-1))

    if img_no == 1:
        btn_back = Button(main_win, text = '<<', state = DISABLED)

    img_label.grid(row = 0, column = 0, columnspan = 3)
    btn_back.grid(row = 1, column = 0)
    btn_fwd.grid(row = 1, column = 2)

btn_back = Button(main_win, text = '<<',command = back ,state = DISABLED)
btn_exit = Button(main_win, text = 'EXIT', command = main_win.quit)
btn_fwd = Button(main_win, text = '>>', command = lambda: forward(2))

btn_back.grid(row = 1,column = 0)
btn_exit.grid(row = 1,column = 1)
btn_fwd.grid(row = 1,column = 2)

main_win.mainloop()
