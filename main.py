from student import StudentControl
from teacher import TeacherControl
from settings import *

usr = "t"

SPanel = StudentControl()
TPanel = TeacherControl()

while usr == "t":
    cmd = input(hc + hsc)
    cmd = cmd_filter(cmd)

    if cmd in new_s:
        name = input(inpc + "Enter student's name:")
        surname = input(inpc + "Enter student's surname:")
        birth_year = int(input(inpc + "Enter student's birth year:"))
        password = input(inpc + "Enter student's password:")
        grade = int(input(inpc + "Enter student's grade:"))
        clas = input(inpc + "Enter student's clas:")
        clas_num = int(input(inpc + "Enter student's clas_num:"))

        SPanel.new_student(name, surname, birth_year, password, grade, clas, clas_num)

    if cmd in get_s:
        n = input(inpc + "Enter student's name: ")
        s = input(inpc + "Enter student's surname: ")
        num = input(inpc + "Enter student's number(optional): ")

        student = SPanel.get_student(num, n, s)
        student.define(True)

    if cmd in q:
        quit(oc + "--Program End")

    print(sc + "-"*14)
