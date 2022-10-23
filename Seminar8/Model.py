# from dataclasses import replace
import Controller

phone_book = []
path = 'Seminar8/data/'


def get_phone_book():
    global phone_book
    return phone_book


def set_path(file):
    global path
    path += file
    # return path


def open_file():
    global phone_book
    global path
    # path = ''
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for item in data:
        contact = item.replace('\n', '').split(';')
        phone_book.append(contact)


def new_contact(contact):
    global phone_book
    phone_book.append(list(contact))


def change_contact(id, choise, value):
    global phone_book
    phone_book[int(id)][int(choise)] = value
