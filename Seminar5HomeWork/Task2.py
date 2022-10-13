# 2. Создайте программу для игры с конфетами человек против человека.

# Правила: На столе лежит 150 конфет. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# 1. Добавьте игру против бота
# 2. Подумайте как наделить бота 'интеллектом'
# Оба задания обязательны


from random import randint
import tkinter as tk
from tkinter import messagebox as mb


def StartGame():
    global count
    global maxKonf
    typeGame = ''
    if radio_GameType_var.get() == 0:
        typeGame = 'Игрок против Игрока'
        radio_GameType_PvBot['state'] = tk.DISABLED
    else:
        typeGame = 'Игрок против Бота'
        radio_GameType_PvP['state'] = tk.DISABLED
    labelNewGame = tk.Label(mainWindow, text=f'Начата новая игра {typeGame}',
                            font=('Arial', 15, 'bold'))
    buttom_GameStart['state'] = tk.DISABLED
    label_PlayerName['text'] = f'Ход игрока: {CurrentPlayer()}'
    labelNewGame.pack()
    needTake = 0
    if CurrentPlayer() == playerName[0]:
        print('Выполняется')
        needTake = maxKonf-fail[-2]
        maxKonf -= needTake
        labelNewStep = tk.Label(
            mainWindow, text=f'{count}-й ход: Игрок {CurrentPlayer()} взял [{needTake }] конфет (Осталось {maxKonf} конфет)')
        labelNewStep.pack()
        count += 1
        buttom_NextStep['text'] = f'Сделать ход {count}'
    label_PlayerName['text'] = f'Ход игрока: {CurrentPlayer()}'


def NextStep():
    global count
    global playerName
    global currentPlayer
    global maxKonf
    global maxStep
    valueEntry = entryValue.get()
    if buttom_GameStart['state'] != tk.DISABLED:
        mb.showerror('Ошибка', 'Нажмите "Начать игру"')
    else:
        if CurrentPlayer() != playerName[0]:
            if valueEntry and 0 < int(valueEntry) <= maxStep and int(valueEntry) <= maxKonf:
                maxKonf -= int(valueEntry)
                labelNewStep = tk.Label(
                    mainWindow, text=f'{count}-й ход: Игрок {CurrentPlayer()} взял [{valueEntry}] конфет (Осталось {maxKonf} конфет)')
                labelNewStep.pack()

                if maxKonf == 0:
                    labelEndGame = tk.Label(
                        mainWindow, text=f'Игрок {CurrentPlayer()} победил. Поздравляем!', background='lightgreen')
                    labelEndGame.pack()
                    buttom_NextStep['state'] = tk.DISABLED
                    entryValue['state'] = tk.DISABLED
                    mb.showinfo(
                        'Победа', f'Игрок {CurrentPlayer()} победил. Поздравляем!')
                count += 1
                buttom_NextStep['text'] = f'Сделать ход {count}'
                label_PlayerName['text'] = f'Ход игрока: {CurrentPlayer()}'

            else:
                mb.showerror(
                    'Ошибка', f'Введите количество конфет не более {min(maxStep,maxKonf)} и нажмите еще раз')
        if CurrentPlayer() == playerName[0]:
            need = 0
            for i in range(0, len(fail)):
                if maxKonf == fail[i]:
                    need = randint(1, min(maxStep-1, maxKonf))
                elif fail[i] < maxKonf < fail[i+1]:
                    need = maxKonf-fail[i]
            maxKonf -= need
            labelNewStepb = tk.Label(
                mainWindow, text=f'{count}-й ход: Игрок {CurrentPlayer()} взял [{need}] конфет (Осталось {maxKonf} конфет)')
            labelNewStepb.pack()
            if maxKonf == 0:
                labelEndGame = tk.Label(
                    mainWindow, text=f'Игрок {CurrentPlayer()} победил. Поздравляем!', background='lightgreen')
                labelEndGame.pack()
                buttom_NextStep['state'] = tk.DISABLED
                entryValue['state'] = tk.DISABLED
                mb.showinfo(
                    'Победа', f'Игрок {CurrentPlayer()} победил. Поздравляем!')
            count += 1
            buttom_NextStep['text'] = f'Сделать ход {count}'
            label_PlayerName['text'] = f'Ход игрока: {CurrentPlayer()}'


def CurrentPlayer():
    global count
    global playerName
    global first
    currentPlayer = ""
    if radio_GameType_var.get() == 1:
        currentPlayer = playerName[(count+first) % 2]
    else:
        currentPlayer = playerName[((count+first) % 2)+2]
    return currentPlayer


count = 1
first = randint(0, 2)
playerName = {0: 'Бот', 1: 'Игрок1', 2: 'Игрок1', 3: 'Игрок2'}
maxKonf = 150
maxStep = 28
fail = [0, maxKonf]
for i in range(maxKonf - maxStep-1, -1, -maxStep-1):
    fail.insert(-1, maxKonf-i)


mainWindow = tk.Tk()
photo = tk.PhotoImage(file='Seminar5HomeWork\IcoGame.png')
mainWindow.iconphoto(False, photo)
mainWindow.title('Игра с конфетами')
mainWindow.geometry("500x800+300+100")
mainWindow.resizable(False, False)

label_GameType = tk.Label(
    mainWindow, text='Выберите тип игры', font=('Arial', 15, 'bold'))
label_GameType.pack()

radio_GameType_var = tk.BooleanVar()
radio_GameType_var.set(0)
radio_GameType_PvP = tk.Radiobutton(text='Игрок против Игрока',
                                    variable=radio_GameType_var, value=0)
radio_GameType_PvBot = tk.Radiobutton(text='Игрок против Бота',
                                      variable=radio_GameType_var, value=1)
radio_GameType_PvP.pack()
radio_GameType_PvBot.pack()

currentPlayer = CurrentPlayer()

label_GameStart = tk.Label(
    mainWindow, text=f'Нажмите кнопку "Начать игру":', font=('Arial', 15, 'bold'))
label_GameStart.pack()

buttom_GameStart = tk.Button(mainWindow, text='Начать игру', command=StartGame)
buttom_GameStart.pack()

label_PlayerName = tk.Label(
    mainWindow, text=f'Ход игрока: ', font=('Arial', 15, 'bold'))
label_PlayerName.pack()

label_EntryValue = tk.Label(
    mainWindow, text=f'Введите количество конфет (не более [{maxStep}]):', font=('Arial', 15, 'bold'))
label_EntryValue.pack()

entryValue = tk.Entry(mainWindow, text='1')
entryValue.pack()

buttom_NextStep = tk.Button(
    mainWindow, text=f'Сделать ход {count}', command=NextStep)
buttom_NextStep.pack()

label_Help = tk.Label(
    mainWindow, text=f'Подсказка: Для победы 1й игрок должен взять 150-(150-(150 % 29)) = {150-(150-(150 % 29))} конфет', background='lightgreen')
label_Help.pack(side='bottom')

mainWindow.mainloop()
