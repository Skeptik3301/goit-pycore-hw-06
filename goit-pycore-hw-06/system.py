from collections import UserDict


class Field:
    """Базовий клас для всіх полів (Name, Phone тощо)"""
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    """Ім’я контакту — обов’язкове поле"""
    pass


class Phone(Field):
    """Клас для зберігання номера телефону з валідацією"""
    def __init__(self, value):
        if not self.validate(value):
            raise ValueError("Phone number must have exactly 10 digits.")
        super().__init__(value)

    @staticmethod
    def validate(value):
        return value.isdigit() and len(value) == 10



class Record:
    """Клас для зберігання інформації про контакт"""
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        """Додає новий телефон"""
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        """Видаляє телефон"""
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                return True
        return False

    def edit_phone(self, old_phone, new_phone):
        """Редагує номер телефону"""
        for i, p in enumerate(self.phones):
            if p.value == old_phone:
                self.phones[i] = Phone(new_phone)
                return True
        return False

    def find_phone(self, phone):
        """Знаходить телефон"""
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        phones_str = "; ".join(p.value for p in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones_str}"




class AddressBook(UserDict):
    """Клас для зберігання записів"""
    def add_record(self, record):
        """Додає запис до книги"""
        self.data[record.name.value] = record

    def find(self, name):
        """Знаходить запис за ім’ям"""
        return self.data.get(name)

    def delete(self, name):
        """Видаляє запис за ім’ям"""
        if name in self.data:
            del self.data[name]
            return True
        return False


