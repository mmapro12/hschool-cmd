import data

students_data = data.import_data("s")
teachers_data = data.import_data("t")
admin_passwords = ("1", "6t7yui", "534rytf")

def login(name, surname, password):
    if password in admin_passwords:
        return "admin"

    for u in students_data:
        if u.get_name() == name and u.get_surname() == surname and u.get_password() == password:
            return "student"

    for u in teachers_data:
        if u.get_name() == name and u.get_surname() == surname and u.get_password() == password:
            return "teacher"

    return "none"
