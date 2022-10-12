# 2. Создайте программу для игры с конфетами человек против человека.

# Правила: На столе лежит 150 конфет. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# 1. Добавьте игру против бота
# 2. Подумайте как наделить бота 'интеллектом'
# Оба задания обязательны


import tkinter as tk


def StartGame():
    label123 = tk.Label(mainWindow, text=f'Начата новая игра {count}',
                        font=('Arial', 15, 'bold'))
    buttom_GameStart['state'] = tk.DISABLED

    label123.pack()


def NextStep():
    global count
    count += 1
    buttom_NextStep['text'] = f'Сделать ход {count}'
    valueEntry = entryValue.get()
    if valueEntry:
        print(valueEntry)
    else:
        print('Введите количество конфет и нажмите еще раз')


count = 1
mainWindow = tk.Tk()
photo = tk.PhotoImage(file='Seminar5HomeWork\IcoGame.png')
mainWindow.iconphoto(False, photo)
mainWindow.title('Игра с конфетами')
mainWindow.geometry("500x600+300+100")
mainWindow.resizable(False, False)


radioOption = tk.StringVar(value='PvP')

label_GameType = tk.Label(
    mainWindow, text='Выберите тип игры', font=('Arial', 15, 'bold'))
label_GameType.pack()


radio_GameType_PvP = tk.Radiobutton(mainWindow,
                                    text='PvP', value='PvP', textvariable=radioOption)
radio_GameType_PvP.pack()

radio_GameType_PvBot = tk.Radiobutton(mainWindow,
                                      text='PvBot', value='PvBot', textvariable=radioOption)
radio_GameType_PvBot.pack()


label_GameStart = tk.Label(
    mainWindow, text=f'Нажмите кнопку "Начать игру":', font=('Arial', 15, 'bold'))
label_GameStart.pack()

buttom_GameStart = tk.Button(mainWindow, text='Начать игру', command=StartGame)
buttom_GameStart.pack()

label_PlayerName = tk.Label(
    mainWindow, text=f'Ход игрока: ', font=('Arial', 15, 'bold'))
label_PlayerName.pack()

label_EntryValue = tk.Label(
    mainWindow, text='Введите количество конфет', font=('Arial', 15, 'bold'))
label_EntryValue.pack()

entryValue = tk.Entry(mainWindow, text='1')
entryValue.pack()

buttom_NextStep = tk.Button(
    mainWindow, text=f'Сделать ход {count}', command=NextStep)
buttom_NextStep.pack()

mainWindow.mainloop()
