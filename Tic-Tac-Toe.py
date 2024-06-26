from tkinter import *

root = Tk()   #creates the main window of the application using the Tk() constructor
root.geometry("320x500") #px
root.title("Tic Tac Toe")
frame1 = Frame(root)
frame1.pack()

titleLabel = Label(frame1, text = "Tic Tac Toe", font = ("Arial", 26), bg = "orange", width=16)
titleLabel.grid(row=0, column=0)

frame2 = Frame(root)
frame2.pack()

board = {1: " ", 2: " ", 3:" ",
         4: " ", 5: " ", 6:" ",
         7: " ", 8: " ", 9:" " }

turn = "x"
game_end = False

def checkForWin(player):
    #rows
    if board[1] == board[2] and board[2] == board[3] and board[3] == player:
        return True
    
    elif board[4] == board[5] and board[5] == board[6] and board[6] == player:
        return True

    elif board[7] == board[8] and board[8] == board[9] and board[9] == player:
        return True

    #columns
    if board[1] == board[4] and board[4] == board[7] and board[7] == player:
        return True
    
    elif board[2] == board[5] and board[5] == board[8] and board[8] == player:
        return True

    elif board[3] == board[6] and board[6] == board[9] and board[9] == player:
        return True

    #diagonals
    elif board[1] == board[5] and board[5] == board[9] and board[9] == player:
        return True

    elif board[3] == board[5] and board[5] == board[7] and board[7] == player:
        return True
    return False

def checkForDraw():
    for i in board.keys():
        if board[i] == " ":
            return False

    return True

def restartGame():
    global game_end
    game_end = False
    for button in buttons:
        button["text"] = " "

    for i in board.keys():
        board[i]= " "

    titleLabel = Label(frame1, text = "Tic Tac Toe", font = ("Arial", 30), bg = "orange", width=15)
    titleLabel.grid(row=0, column=0)

#Function to play

def play(event):
    global turn, game_end
    if game_end:
        return

    button = event.widget
    buttonText = str(button)
    clicked = buttonText[-1]

    if clicked == "n":
        clicked = 1
    else:
        clicked = int(clicked)

    if button["text"] == " ":
        if turn == "x":
            button["text"]="X"
            board[clicked] = turn
            if checkForWin(turn):
                winningLabel = Label(frame1, text=f"{turn} wins the game!", bg = "orange", font=("Arial", 26), width=16)
                winningLabel.grid(row = 0, column=0, columnspan=3)
                game_end = True
            turn = "o"

        else:
            button["text"]= "O"
            board[clicked] = turn
            if checkForWin(turn):
                winningLabel = Label(frame1, text=f"{turn} wins the game!", bg="orange", font=("Arial", 30), width=20)
                winningLabel.grid(row = 0, column=0, columnspan=3)
                game_end = True
            turn="x"

        if checkForDraw():
            drawLabel = Label(frame1, text=f"Game Draw!", bg="orange", font=("Arial", 26), width=16)
            drawLabel.grid(row = 0, column=0, columnspan=3)

#Tic Tac Toe board

#first row
button1 = Button(frame2, text = " ", width = 4, height = 2, font=("Arial", 30), bg = "gray", relief= RAISED, borderwidth=5)
button1.grid(row=0, column=0)
button1.bind("<Button-1>", play)

button2 = Button(frame2, text = " ", width = 4, height = 2, font=("Arial", 30), bg = "gray", relief= RAISED, borderwidth=5)
button2.grid(row=0, column=1)
button2.bind("<Button-1>", play)

button3 = Button(frame2, text = " ", width = 4, height = 2, font=("Arial", 30), bg = "gray", relief= RAISED, borderwidth=5)
button3.grid(row=0, column=2)
button3.bind("<Button-1>", play)

#second row
button4 = Button(frame2, text = " ", width = 4, height = 2, font=("Arial", 30), bg = "gray", relief= RAISED, borderwidth=5)
button4.grid(row=1, column=0)
button4.bind("<Button-1>", play)

button5 = Button(frame2, text = " ", width = 4, height = 2, font=("Arial", 30), bg = "gray", relief= RAISED, borderwidth=5)
button5.grid(row=1, column=1)
button5.bind("<Button-1>", play)

button6 = Button(frame2, text = " ", width = 4, height = 2, font=("Arial", 30), bg = "gray", relief= RAISED, borderwidth=5)
button6.grid(row=1, column=2)
button6.bind("<Button-1>", play)

#Third row
button7 = Button(frame2, text = " ", width = 4, height = 2, font=("Arial", 30), bg = "gray", relief= RAISED, borderwidth=5)
button7.grid(row=2, column=0)
button7.bind("<Button-1>", play)

button8 = Button(frame2, text = " ", width = 4, height = 2, font=("Arial", 30), bg = "gray", relief= RAISED, borderwidth=5)
button8.grid(row=2, column=1)
button8.bind("<Button-1>", play)

button9 = Button(frame2, text = " ", width = 4, height = 2, font=("Arial", 30), bg = "gray", relief= RAISED, borderwidth=5)
button9.grid(row=2, column=2)
button9.bind("<Button-1>", play)

restartButton = Button(frame2, text="Restart Game!", width=19, height=1, font=("Arial",20), bg="Green", relief=RAISED, 
borderwidth=5, command=restartGame )
restartButton.grid(row=4, column=0, columnspan=3)

buttons = [button1, button2, button3, button4, button5, button6, button7, button8, button9


]
root.mainloop() # This line starts the Tkinter event loop.
                # The event loop is an infinite loop that listens for events such as button clicks, key presses, etc.
                # It keeps the GUI application running until the user closes the main window.
                # The program will remain in this loop until the window is closed by the user.