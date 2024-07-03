import json
from person import Person
from datetime import date
from colorama import Fore


class StudentControl:
    def __init__(self):
        self.students = self.import_json()

    @staticmethod
    def import_json():
        i_data = []
        with open("data.json") as file:
            content = json.load(file)["students"]

        for key in content.keys():
            s_data = Student(
                content[key]["name"],
                content[key]["surname"],
                content[key]["birth_year"],
                content[key]["password"],
                content[key]["grade"],
                content[key]["clas"],
                content[key]["clas_num"],
                content[key]["scores"],
            )
            i_data.append(s_data)
        return i_data

    @staticmethod
    def get_curriculum(c: int):
        with open("data.json") as file:
            content = json.load(file)
            return content["curriculums"][str(c)]

    @staticmethod
    def add_to_json(student):
        s_data = {"name": student.get_name(),
                  "surname": student.get_surname(),
                  "birth_year": student.get_birth_year(),
                  "password": student.get_password(),
                  "grade": student.get_grade(),
                  "clas": student.get_clas(),
                  "clas_num": student.get_clas_num(),
                  "scores": student.get_scores(s=True)}

        with open("data.json") as file:
            content = json.load(file)
            content["students"][s_data["name"]] = s_data

        with open("data.json", "w") as file:
            json.dump(content, file, indent=2)

    def get_student(self, num=None, *args):
        if num:
            for student in self.students:
                if str(student.get_clas_num()) == str(num):
                    return student

        name = f"{args[0].title()} {args[1].title()}"
        for student in self.students:
            if name == student.get_fullname():
                return student

        return None

    def new_student(self, name: str, surname: str, birth_year: int, password: str, grade: int, clas: str, clas_num: int,
                    scores=None):
        if scores is None:
            scores = self.get_curriculum(grade)

        n = f"{name.title()} {surname.title()}"
        for student in self.students:
            if student.get_fullname() == n:
                pass

        student = Student(
            name,
            surname,
            birth_year,
            password,
            grade,
            clas,
            clas_num,
            scores
        )
        self.add_to_json(student)
        self.students = self.import_json()


class Student(Person):
    """A class of Student object"""

    def __init__(self, name: str, surname: str, birth_year: int, password: str, grade: int, clas: str, clas_num: int,
                 scores: dict):
        super().__init__(name, surname, birth_year, password)
        self.__name = name.title()
        self.__surname = surname.title()
        self.__birth_year = birth_year
        self.__age = date.today().year - birth_year
        self.__password = password
        self.__grade = grade
        self.__clas = clas.upper()
        self.__clas_num = clas_num
        self.__scores = scores

    # General getters
    @staticmethod
    def get_type():
        return "s"

    def define(self, write=False):
        scores = ""
        for key, value in self.__scores.items():
            x = f"--{key}: {value}\n"
            scores += x

        define = (Fore.CYAN + f"{self.__name} {self.__surname} - {self.__grade}/{self.__clas}"
                  f"\nAge: {self.__age}"
                  f"\n{scores}"
                  f"\n average: "f"{self.get_average()}")

        if write:
            print(define)
        else:
            return define

    def get_grade(self):
        return self.__grade

    def get_clas(self):
        return self.__clas

    def get_clas_num(self):
        return self.__clas_num

    # General setters
    def set_grade(self, value: int, plus=False):
        if plus:
            self.__age += value
        else:
            self.__age = value

    def set_clas(self, value: str):
        self.__clas = value.upper()

    def set_clas_num(self, value: int):
        self.__clas_num = value

    # Scores
    def get_scores(self, s=False):
        if s:
            return self.__scores

        scores = ""
        for key, value in self.__scores.items():
            scores += f"{key}: {value}\n"

        return scores

    def get_score(self, area: str):
        if area in self.__scores:
            return f"{area}: {self.__scores[area]}"

    def set_score(self, area: str, value: float):
        if area in self.__scores:
            self.__scores[area] = float(value)

    def get_average(self):
        total = sum(self.__scores.values())
        average = total / len(self.__scores)
        return average
