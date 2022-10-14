# 3. Создайте программу для игры в 'Крестики-нолики'.

from tkinter import *
import random
mainWindow = Tk()
mainWindow.title('Крестики-нолики')
game_run = True
field = []
cross_count = 0
photo = PhotoImage(file='Seminar5HomeWork\IcoGame.png')
mainWindow.iconphoto(False, photo)


def New_game():
    for row in range(3):
        for col in range(3):
            field[row][col]['text'] = ' '
            field[row][col]['background'] = 'lavender'
    global game_run
    game_run = True
    global cross_count
    cross_count = 0


def Click(row, col):
    if game_run and field[row][col]['text'] == ' ':
        field[row][col]['text'] = 'X'
        global cross_count
        cross_count += 1
        Check_win('X')
        if game_run and cross_count < 5:
            Computer_move()
            Check_win('O')


def Check_win(smb):
    for n in range(3):
        Check_line(field[n][0], field[n][1], field[n][2], smb)
        Check_line(field[0][n], field[1][n], field[2][n], smb)
    Check_line(field[0][0], field[1][1], field[2][2], smb)
    Check_line(field[2][0], field[1][1], field[0][2], smb)


def Check_line(a1, a2, a3, smb):
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == smb:
        a1['background'] = a2['background'] = a3['background'] = 'lightgreen'
        global game_run
        game_run = False


def Can_win(a1, a2, a3, smb):
    res = False
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == ' ':
        a3['text'] = 'O'
        res = True
    if a1['text'] == smb and a2['text'] == ' ' and a3['text'] == smb:
        a2['text'] = 'O'
        res = True
    if a1['text'] == ' ' and a2['text'] == smb and a3['text'] == smb:
        a1['text'] = 'O'
        res = True
    return res


def Computer_move():
    for n in range(3):
        if Can_win(field[n][0], field[n][1], field[n][2], 'O'):
            return
        if Can_win(field[0][n], field[1][n], field[2][n], 'O'):
            return
    if Can_win(field[0][0], field[1][1], field[2][2], 'O'):
        return
    if Can_win(field[2][0], field[1][1], field[0][2], 'O'):
        return
    for n in range(3):
        if Can_win(field[n][0], field[n][1], field[n][2], 'X'):
            return
        if Can_win(field[0][n], field[1][n], field[2][n], 'X'):
            return
    if Can_win(field[0][0], field[1][1], field[2][2], 'X'):
        return
    if Can_win(field[2][0], field[1][1], field[0][2], 'X'):
        return
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if field[row][col]['text'] == ' ':
            field[row][col]['text'] = 'O'
            break


for row in range(3):
    line = []
    for col in range(3):
        button = Button(mainWindow, text=' ', width=4, height=2,
                        font=('Verdana', 30, 'bold'),
                        background='lavender',
                        command=lambda row=row, col=col: Click(row, col))
        button.grid(row=row, column=col, sticky='nsew')
        line.append(button)
    field.append(line)
button_NewGame = Button(mainWindow, text='Начать новую игру', command=New_game)
button_NewGame.grid(row=3, column=0, columnspan=3, sticky='nsew')
mainWindow.mainloop()
