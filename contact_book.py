class Contact:
    contacts = {}

    def __init__(self, *args, favorite="Нет", **kwargs):
        name = args[0]
        surname = args[1]
        phone_number = args[2]
        favorite_1 = favorite
        kwargs_dict = {}
        print("Имя:", args[0])
        print("Фамилия:", args[1])
        print("Номер телефона:", args[2])
        print("В избранных:", favorite)
        print("Дополнительная информация:")
        for key, value in kwargs.items():
            print("         ", key, ":", value)
        self.contacts[name] = [name, surname, phone_number, favorite_1, kwargs_dict]


jhon = Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
print(jhon)


class PhoneBook(Contact):
    PhoneBook = "Contacts and Data"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def adding(self):
        while True:
            first_name_new = input("Введите имя ")
            surname_new = input("Введите фамилию ")
            phone_number_new = input("Введите номер телефона ")
            favorites = input("Внести в избранные?(Y/N) ")
            if favorites == "Y":
                favorites = "Да"
            else:
                favorites = "Нет"
            telegram_new = input("Имя пользователя Telegram начиная с @ ")
            email_new = input("Введите адрес электронной почты ")
            other = Contact(first_name_new, surname_new, phone_number_new, favorites, telegram=telegram_new,
                            email=email_new)
            print(other)

    @classmethod
    def __delitem__(cls, phone_number):
        phone_number = input("Введите номер телефона ")
        if phone_number == Contact(phone_number):
            print("1")

    @classmethod
    def find(cls, favorite, contacts):
        if favorite == "Да":
            print(contacts)
    @classmethod
    def find_by_name(cls, name, surname,  contacts):
        name_1 = input("Введите имя")
        surname_1 = input("Введите фамилию")
        if name_1 and surname_1 == name and surname:
            print(contacts)



q = PhoneBook("q", "q", "798", "1", "q")
del q["798"]
print("DONE!")
