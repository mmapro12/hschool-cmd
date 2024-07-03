from person import Person
from datetime import date
import json


class TeacherControl:
    def __init__(self):
        self.teachers = self.import_json()

    @staticmethod
    def import_json():
        i_data = []
        with open("data.json") as file:
            content = json.load(file)["teachers"]

        for key in content.keys():
            t_data = Teacher(
                content[key]["name"],
                content[key]["surname"],
                content[key]["birth_year"],
                content[key]["password"],
                content[key]["area"],
                content[key]["salary"],
            )
            i_data.append(t_data)
        return i_data

    @staticmethod
    def add_to_json(teacher):
        t_data = {"name": teacher.get_name(),
                  "surname": teacher.get_surname(),
                  "birth_year": teacher.get_birth_year(),
                  "password": teacher.get_password(),
                  "area": teacher.get_area(),
                  "salary": teacher.get_salary()}

        with open("data.json") as file:
            content = json.load(file)
            content["teachers"][t_data["name"]] = t_data

        with open("data.json", "w") as file:
            json.dump(content, file, indent=2)

    def get_teacher(self, *args):
        name = f"{args[0].title()} {args[1].title()}"
        for teacher in self.teachers:
            if name == teacher.get_fullname():
                return teacher

        return None

    def new_teacher(self, name: str, surname: str, birth_year: int, password: str, area: str, salary: float):
        n = f"{name.title()} {surname.title()}"
        for teacher in self.teachers:
            if teacher.get_fullname() == n:
                pass

        student = Teacher(
            name,
            surname,
            birth_year,
            password,
            area,
            salary
        )
        self.add_to_json(student)
        self.teachers = self.import_json()


class Teacher(Person, TeacherControl):
    """A class of student object"""
    def __init__(self, name: str, surname: str, birth_year: int, password: str, area: str, salary: float):
        super().__init__(name, surname, birth_year, password)
        self.__name = name.title()
        self.__surname = surname.title()
        self.__birth_year = birth_year
        self.__age = date.today().year - birth_year
        self.__password = password
        self.__area = area
        self.__salary = salary

    # General getters
    @staticmethod
    def get_type():
        return "s"

    def define(self, write=False):
        define = (f"{self.__name} {self.__surname} - {self.__area}"
                  f"\nAge: {self.__age}"
                  f"\nSalary: {self.__salary}")

        if write:
            print(define)
        else:
            return define

    def get_area(self):
        return self.__area

    def get_salary(self):
        return self.__salary

    # General setters
    def set_area(self, value: str):
        self.__area = value

    def set_salary(self, value: float):
        self.__salary = float(value)
