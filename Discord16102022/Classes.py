class Contact:
    id: str = None
    name: str = None
    phone: str = None
    comment: str = ''
    text: str = ''

    def __init__(self, id: str, name: str, phone: str, comment: str, *args, **kwargs):
        self.id = id
        self.name = name
        self.phone = phone
        self.comment = comment

    def show(self):
        return (self.id, self.name, self.phone, self.comment)

    def set_name(self, name: str):
        self.name = name


# stone = Contact('1', 'STONE', '89854450738', 'Work')
# andrey = Contact('2', 'Andrey', '123-123-123', 'Home')
# irina = Contact('5', 'IRINA', '80-8800', 'Не брать')


# print(stone.name)
# print(stone.show())

# stone.second_phone = '2123132'

# print(stone.second_phone)
# print(stone.show())
# stone.set_name('STONEE')
# print(stone.show())
