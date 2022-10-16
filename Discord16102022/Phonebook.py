from Classes import Contact


class PhoneBook:
    contact: list = []
    last_id: str = '0'

    def __init__(self):
        pass

    def add(self, name: str, phone: str, comment: str):
        user = Contact(self.last_id, name, phone, comment)
        self.last_id = str(int(self.last_id)+1)
        self.contact.append(user)


book = PhoneBook()
book.add('stone', '45641235', '345641')

print(book.contact[0].show())
print(book.contact[1].show())
print(book.contact[2].show())
