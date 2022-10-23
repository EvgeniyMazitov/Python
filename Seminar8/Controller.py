import View
import Model


def start():
    choice = 1
    while choice != 9:
        choice = View.show_menu()
        match(choice):
            case 0:
                phone_book = Model.get_phone_book()
                View.show_phone_book(phone_book)
            case 1:
                path = View.input_path()
                Model.set_path(path)
                Model.open_file()
            case 2:
                Model.write_file()
            case 3:
                contact = View.input_contact()
                Model.new_contact(contact)
            case 4:
                contact = View.input_change()
                Model.change_contact(*contact)
            case 5:
                id_contact = View.input_delete()
                Model.delete_contact(id_contact)
            case 6:
                choise, value = View.input_search()
                search_result = Model.search_contact(choise, value)
                View.output_search(search_result)
