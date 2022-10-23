import Controller

phone_book = []
path = 'Seminar8/data/'
flag = 0


def get_phone_book():
    global phone_book
    return phone_book


def set_path(file):
    global path
    global flag
    if file not in path:
        path += file


def open_file():
    global phone_book
    global path
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


def delete_contact(id):
    global phone_book
    phone_book.pop(id)


def search_contact(choise, value):
    global phone_book
    search_result = []
    for id, item in enumerate(phone_book):
        if value in item[int(choise)]:
            search_result.append(id)
            search_result.append(item)
    return search_result


def write_file():
    global path
    with open(path, 'w', encoding='UTF-8') as data:
        phone_book_write = phone_book_data_maker()
        print(phone_book_write)
        data.write(phone_book_write)


def phone_book_data_maker():
    global phone_book
    phone_book_write = phone_book
    for index, item in enumerate(phone_book_write):
        phone_book_write[index] = ';'.join(item)
    phone_book_write = '\n'.join(phone_book_write)
    return phone_book_write
