import Controller


def show_menu():
    print('------------------------------------')
    print('0. Показать все контакты')
    print('1. Открыть файл с контактами')
    print('2. Записать файл с контактами')
    print('3. Добавить контакт')
    print('4. Изменить контакт')
    print('5. Удалить контакт')
    print('6. Поиск по контактам')
    choice = int(input('Выберите пункт меню: '))
    print('------------------------------------')
    return choice


def show_phone_book(phone_book):
    if len(phone_book) < 1:
        print('Телефонная книга пуста')
    else:
        for id, item in enumerate(phone_book):
            print(id, *item)


def input_path():
    global path
    path = ''
    path = input('Введите имя файла: ')
    return path


def input_contact():
    name_contact = input('Введите ФИО контакта: ')
    phone_contact = input('Введите Телефон контакта: ')
    comment_contact = input('Введите Описание контакта: ')
    return (name_contact, phone_contact, comment_contact)


def input_change():
    id = int(input('Введите номер контакта: '))
    print('Что изменить?')
    choise = input('0 - ФИО, 1 - Телефон, 2 - Комментарий: ')
    value = input('Введите изменения: ')
    return (id, choise, value)


def input_delete():
    id = int(input('Введите номер контакта для удаления: '))
    return id


def input_search():
    print('По какому полю выполнить поиск?')
    choise = input('0 - ФИО, 1 - Телефон, 2 - Комментарий: ')
    value = input('Введите искомое значение: ')
    return (choise, value)


def output_search(search_result):
    print('Результаты поиска: ')
    for i in range(0, len(search_result)-1, 2):
        print(search_result[i], *search_result[i+1])
