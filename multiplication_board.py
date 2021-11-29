#Program to draw Multiplication Board in Python
#By Ahmad Shirzadi

import turtle
import tkinter as tk

FONT = ('Arial', 15, 'normal')
COLOR = ('black','deep pink')
WIDTH, HEIGHT = 450, 450

window = tk.Tk()
screen_resolution = str(WIDTH)+'x'+str(HEIGHT)
window.geometry(screen_resolution)
window.title("Program to draw Multiplication Board in Python")
label = tk.Label(window, text = "Multiplication Table")
label.pack(padx = 5, pady = 5)
window.resizable(False, False) 

canvas = tk.Canvas(master=None,width=450,height=450)
canvas.pack()
canvas.create_rectangle(500, 500, 0, 0, fill="black")

mulBoard = turtle.RawTurtle(canvas)
mulBoard.speed(100) #for speedily drawing Multiplication Board

for i in range(1, 10): #for loop will run 10 times as there are 10 rows in the Multiplication Board
    for j in range(1, 10): #for loop will run 10 times as there are 10 columns in the Multiplication Board
        mulBoard.penup()
        mulBoard.goto((window.winfo_width()/2*(-1)) + (j*40), (window.winfo_height()/2) + (i*40*(-1)) )
        mulBoard.pendown()
        for k in range(4):
            mulBoard.forward(40)
            mulBoard.right(90)
        mulBoard.penup()
        mulBoard.goto( (window.winfo_width()/2*(-1)) + (j*40)+15, (window.winfo_height()/2) + (((i+1)*40*(-1))+6) )
        mulBoard.pendown()
        if (i == 1 or j == 1):
            mulBoard.color(COLOR[1])
        mulBoard.write(i*j, font = FONT)
        mulBoard.color(COLOR[0])

window.mainloop()