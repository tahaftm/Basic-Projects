from tkinter import *
import random

def next_turn(row,column):
    global player

    buttons[row][column].config(bg = '#FDC89D')

    if buttons[row][column]['text'] == "" and check_winner() is False:
        if player == players[0]:
            buttons[row][column]['text'] = player 

            if check_winner() is False:
                player = players[1]
                label.config(text = player + ' turn')

            elif check_winner() is True:
                label.config(text= player + " wins")

            elif check_winner == "Tie":
                label.config(text = "Tie")

        else:
            if player == players[1]:
                buttons[row][column]['text'] = player

                if check_winner() is False:
                    player = players[0]
                    label.config(text = player + ' turn')

                elif check_winner() is True:
                    label.config(text= player + " wins")

                elif check_winner == "Tie":
                    label.config(text = "Tie")

def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg = 'green', fg = 'white')
            buttons[row][1].config(bg = 'green', fg = 'white')
            buttons[row][2].config(bg = 'green', fg = 'white')
            return True
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg = 'green', fg = 'white')
            buttons[1][column].config(bg = 'green', fg = 'white')
            buttons[2][column].config(bg = 'green', fg = 'white')
            return True
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg = 'green', fg = 'white')
        buttons[1][1].config(bg = 'green', fg = 'white')
        buttons[2][2].config(bg = 'green', fg = 'white')
        return True
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg = 'green', fg = 'white')
        buttons[1][1].config(bg = 'green', fg = 'white')
        buttons[2][0].config(bg = 'green', fg = 'white')
        return True
    elif empty_spaces() is False:
        return 'Tie'
    else: 
        return False

def empty_spaces():
    spaces = 9
    for row in range(3):
        for column in range(3):
            spaces -= 1
        if buttons[row][column] == "":
            return False
        else:
            return True 
        
def new_game():
    global player
    player = random.choice(players)
    label.config(text = player + " turn")
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text = "", bg = 'white')

window = Tk()
icon = PhotoImage(file='C:\\Users\\USER\\Desktop\\microsoft\\module 1\\basic projects\\tic tac toe project\\tic_tac_toe.png')
window.iconphoto(True, icon)
window.title("Tic Tac Toe")
players = ['X','O']

player = random.choice(players)
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

label = Label(text=player + ' turn', font = ('consolas', 40))
label.pack()

reset_button = Button(window,text = "reset", font = ('consolas', 20), command = new_game)
reset_button.pack()

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3): 
        buttons[row][column] = Button(frame, text = "", font = ('consolas', 40),width = 5, height=2
                                      ,command = lambda row = row, column = column : next_turn(row, column))     
        buttons[row][column].grid(row = row, column = column)
window.mainloop()