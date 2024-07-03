import json
from student import Student
from teacher import Teacher

data_file = "data.json"
blank_data = {
  "students": {

  },
  "teachers": {

  },
  "curriculums": {
    "9": {"English": 0.0, "Physic": 0.0},
    "10": {"English": 0.0, "Physic": 0.0},
    "11": {"English": 0.0, "Physic": 0.0},
    "12": {"English": 0.0, "Physic": 0.0}
  }
}

# Loading all data or special(spec) type of data
def load_data(spec="no"):
    with open(data_file) as file:
        content = json.load(file)
    if spec != "no":
        return content[spec]
    else:
        return content


# Saving data to data file
def save_data(data):
    with open(data_file, "w") as file:
        json.dump(data, file)


# Load all students data formatted
def import_data(type):
    data = []
    if type == "s":
        content: dict = load_data("students")

        for student in content.values():
            name = student["name"]
            surname = student["surname"]
            birth_year = student["birth_year"]
            password = student["password"]
            grade = student["grade"]
            clas = student["clas"]
            clas_num = student["clas_num"]
            scores = student["scores"]

            data.append(Student(name, surname, birth_year, password, grade, clas, clas_num, scores))

        return data

    elif type == "t":
        content: dict = load_data("teachers")

        for teacher in content.values():
            name = teacher["name"]
            surname = teacher["surname"]
            birth_year = teacher["birth_year"]
            password = teacher["password"]
            area = teacher["area"]
            salary = teacher["salary"]

            data.append(Teacher(name, surname, birth_year, password, area, salary))

        return data


# Load a curriculum
def get_curriculum(curriculum):
    with open(data_file) as file:
        content = json.load(file)["curriculums"]

    return content[str(curriculum)]


# Adding a new student and saving for data
def add_student(name: str, surname: str, birth_year: int, password: str, grade: int, clas: str, clas_num: int, scores):
    student = {"name": name.title(),
               "surname": surname.title(),
               "birth_year": birth_year,
               "password": password,
               "grade": grade,
               "clas": clas.title(),
               "clas_num": clas_num,
               "scores": scores}

    content = load_data()
    content["students"][name] = student

    save_data(content)


# Adding a new student and saving for data
def add_teacher(name: str, surname: str, birth_year: int, password: str, area: str, salary: int):
    teacher = {"name": name.title(),
               "surname": surname.title(),
               "birth_year": birth_year,
               "password": password,
               "area": area.title(),
               "salary": salary}

    content = load_data()
    content["teachers"][name] = teacher

    save_data(content)


# Convert Student and Teacher class to json file
def built_data(built_s_data: list, built_t_data: list):
    data = blank_data
    for item in built_s_data:
        student = {"name": item.get_name(),
                   "surname": item.get_surname(),
                   "birth_year": item.get_birth_year(),
                   "password": item.get_password(),
                   "grade": item.get_grade(),
                   "clas": item.get_clas(),
                   "clas_num": item.get_clas_num(),
                   "scores": item.get_scores()}

        data["students"][student["name"]] = student

    for item in built_t_data:
        teacher = {"name": item.get_name(),
                   "surname": item.get_surname(),
                   "birth_year": item.get_birth_year(),
                   "password": item.get_password(),
                   "grade": item.get_grade(),
                   "clas": item.get_clas(),
                   "clas_num": item.get_clas_num(),
                   "scores": item.get_scores()}

        data["teachers"][teacher["name"]] = teacher

    return data
