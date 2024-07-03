from datetime import date

class Person:
    """A class of common things at Student and Teacher objects"""

    def __init__(self, name: str, surname: str, birth_year: int, password: str):
        self.__name = name.title()
        self.__surname = surname.title()
        self.__birth_year = birth_year
        self.__age = date.today().year - birth_year
        self.__password = password

    # General getters
    def define(self, write=False):
        pass

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_fullname(self, write=False):
        if write:
            print(f"{self.__name} {self.__surname}")
        else:
            return f"{self.__name} {self.__surname}"

    def get_birth_year(self):
        return self.__birth_year

    def get_age(self):
        return self.__age

    def get_password(self):
        return self.__password

    # General setters
    def set_name(self, value: str):
        self.__name = value.title()

    def set_surname(self, value: str):
        self.__surname = value.title()

    def set_birth_year(self, value: int, plus=True):
        if plus:
            self.__birth_year += value
        else:
            self.__birth_year = value

    def set_age(self, value: int, plus=False):
        if plus:
            self.__age += value
        else:
            self.__age = value

    def set_password(self, value: str):
        self.__password = value

    @staticmethod
    def generate_date(birthdate):
        birthdate = birthdate.split("-")
        day = birthdate[0]
        month = birthdate[1]
        year = birthdate[2]
        return day, month, year
