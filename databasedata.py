# Imports
from usertype import UserType
from users import Users
from courses import Courses
from profesorscourses import ProfesorsCourses
from studentscourses import StudentsCourses

class DatabaseData:
    # Import user type data
    def UserTypeData(self):
        ut = UserType()
        ut.insert("Student")
        ut.insert("Profesor")

    # Import users data
    def UsersData(self):
        u = Users()
        u.insert(1, "Student 1", "student1@gmail.com", "7fa242fc775fc88106462384f4456131") # Password "ma635xd"
        u.insert(1, "Student 2", "student2@gmail.com", "7fa242fc775fc88106462384f4456131") # Password "ma635xd"
        u.insert(2, "Profesor 1", "profesor1@gmail.com", "7fa242fc775fc88106462384f4456131") # Password "ma635xd"

    # Import user type data
    def CoursesData(self):
        c = Courses()
        c.insert("Predmet 1", "Opis predmeta 1", "course.html")
        c.insert("Predmet 2", "Opis predmeta 2", "course.html")

    # Import profesors courses data
    def ProfesorsCoursesData(self):
        pc = ProfesorsCourses()
        pc.insert(3, 1)

    # Import students courses data
    def StudentsCoursesData(self):
        sc = StudentsCourses()
        sc.insert(1, 1, 10)
        sc.insert(1, 2, 10)
        sc.insert(2, 1, 7)
        sc.insert(2, 2, 8)