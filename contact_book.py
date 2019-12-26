class Contact:
    def __init__(self, first_name, surname, phone_number, favorite="нет", **kwargs):
        self.first_name = first_name
        self.surname = surname
        self.phone_number = phone_number
        self.favorite = favorite
        self.keys_list = []
        self.values_list = []
        for key, value in kwargs.items():
            self.key = key
            self.keys_list.append(self.key)
            self.value = value
            self.values_list.append(self.value)

    def str(self):
        print("Имя:", self.first_name)
        print("Фамилия:", self.surname)
        print("Номер телефона:", self.phone_number)
        print("В избранных:", self.favorite)
        print("Дополнительная информация:")
        print("                     ", self.keys_list[0], ":", self.values_list[0])
        print("                     ", self.keys_list[1], ":", self.values_list[1])


jhon = Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
print(jhon.str())


class PhoneBook(Contact):
    def __init__(self, first_name, surname, phone_number, **kwargs):
        super().__init__(first_name, surname, phone_number, **kwargs)
        self.phone_book_name = self.phone_book_name
        
