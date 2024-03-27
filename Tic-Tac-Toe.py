from tkinter import *

root = Tk()   #creates the main window of the application using the Tk() constructor
root.geometry("500x500") #px
root.title("Tic Tac Toe")
frame1 = Frame(root)
frame1.pack()

titleLabel = Label(frame1, text = "Tic Tac Toe", font = ("Arial", 26), bg = "orange")
titleLabel.pack()

frame2 = Frame(root)
frame2.pack()

turn = "x"

def play(event):
    global turn
    button = event.widget

    if turn == "x":
        button["text"]="X"
        turn = "o"

    else:
        button["text"]= "O"
        turn="x"
#Tic Tac Toe board

#first row
button1 = Button(frame2, text = " ", width = 4, height = 2, font=("Arial", 30), bg = "gray", relief= RAISED, borderwidth=5)
button1.grid(row=0, column=0)
button1.bind("<Button-1>", play)

button1 = Button(frame2, text = " ", width = 4, height = 2, font=("Arial", 30), bg = "gray", relief= RAISED, borderwidth=5)
button1.grid(row=0, column=1)
button1.bind("<Button-1>", play)

button1 = Button(frame2, text = " ", width = 4, height = 2, font=("Arial", 30), bg = "gray", relief= RAISED, borderwidth=5)
button1.grid(row=0, column=2)
button1.bind("<Button-1>", play)

#second row
button1 = Button(frame2, text = " ", width = 4, height = 2, font=("Arial", 30), bg = "gray", relief= RAISED, borderwidth=5)
button1.grid(row=1, column=0)
button1.bind("<Button-1>", play)

button1 = Button(frame2, text = " ", width = 4, height = 2, font=("Arial", 30), bg = "gray", relief= RAISED, borderwidth=5)
button1.grid(row=1, column=1)
button1.bind("<Button-1>", play)

button1 = Button(frame2, text = " ", width = 4, height = 2, font=("Arial", 30), bg = "gray", relief= RAISED, borderwidth=5)
button1.grid(row=1, column=2)
button1.bind("<Button-1>", play)

#Third row
button1 = Button(frame2, text = " ", width = 4, height = 2, font=("Arial", 30), bg = "gray", relief= RAISED, borderwidth=5)
button1.grid(row=2, column=0)
button1.bind("<Button-1>", play)

button1 = Button(frame2, text = " ", width = 4, height = 2, font=("Arial", 30), bg = "gray", relief= RAISED, borderwidth=5)
button1.grid(row=2, column=1)
button1.bind("<Button-1>", play)

button1 = Button(frame2, text = " ", width = 4, height = 2, font=("Arial", 30), bg = "gray", relief= RAISED, borderwidth=5)
button1.grid(row=2, column=2)
button1.bind("<Button-1>", play)


root.mainloop() # This line starts the Tkinter event loop.
                # The event loop is an infinite loop that listens for events such as button clicks, key presses, etc.
                # It keeps the GUI application running until the user closes the main window.
                # The program will remain in this loop until the window is closed by the user.