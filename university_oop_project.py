import random
import re
from abc import ABC, abstractmethod
from datetime import datetime

class UserOfUniversity(ABC):
    def __init__(self, name, surname, date_of_birth,phone_number):
        self.name = name
        self.surname = surname
        self.__date_of_birth = date_of_birth
        self.__id = self.generate_id(date_of_birth)
        self.phone_number = phone_number
        self.validate_phone_number()

    @abstractmethod
    def create_corporate_email(self):
        pass

    def introduce(self):
        return f"My name is {self.name} {self.surname}, born on {self.__date_of_birth}."

    def get_id(self):
        return f"ID: {self.__id}"

    @staticmethod
    def generate_id(date_of_birth):
        year_of_birth = datetime.now().year - int(date_of_birth.split('-')[2])
        random_number = random.randint(1000, 9999)
        return f"{year_of_birth}{random_number}"

    def validate_phone_number(self):

        if not re.match(r'^\+\d{10}$', self.phone_number):
            raise ValueError("Phone number must start with '+' and contain exactly 10 digits.")

class Student(UserOfUniversity):
    def __init__(self, name, surname, date_of_birth,phone_number, major):
        UserOfUniversity.__init__(self, name, surname, date_of_birth,phone_number)
        self.major = major

    def create_corporate_email(self):
        return f"{self.name.lower()}.{self.surname.lower()}.{self.get_id().split(': ')[1]}@student.university.com"

    def enroll_in_course(self, course_name):
        return f"{self.name} enrolled in {course_name}."

    def introduce(self):
        base_intro = super().introduce()
        return f"{base_intro} I am a student majoring in {self.major}."

    def update_major(self, new_major):
        self.major = new_major
        return f"{self.name} has updated their major to {self.major}."

class Teacher(UserOfUniversity):
    def __init__(self, name, surname, date_of_birth,phone_number, subject):
        UserOfUniversity.__init__(self, name, surname, date_of_birth,phone_number)
        self.subject = subject

    def create_corporate_email(self):
        return f"{self.name.lower()}.{self.surname.lower()}.{self.get_id().split(': ')[1]}@teacher.university.com"

    def assign_course(self, course_name):
        return f"{self.name} assigned to teach {course_name}."

    def introduce(self):
        base_intro = super().introduce()
        return f"{base_intro} I am a teacher and I teach {self.subject}."

    def update_subject(self, new_subject):
        self.subject = new_subject
        return f"{self.name} now teaches {self.subject}."

class StudentTeacher(Student, Teacher):
    def __init__(self, name, surname, date_of_birth,phone_number, major, subject):
        Student.__init__(self, name, surname, date_of_birth, phone_number, major)
        Teacher.__init__(self, name, surname, date_of_birth, phone_number,subject)

    def introduce(self):
        base_intro = UserOfUniversity.introduce(self)

        student_info = f"I am a student majoring in {self.major}."
        teacher_info = f"I am also a teacher and I teach {self.subject}."

        return f"{base_intro} {student_info} {teacher_info}"

    def perform_dual_role(self, student_course_name, teacher_course_name):

        as_teacher = self.assign_course(teacher_course_name)

        as_student = self.enroll_in_course(student_course_name)
        return f"{as_teacher}\n{as_student}"


if __name__ == "__main__":

    student = Student("Alice", "Johnson", "15-04-2003", "+5643789207","Mathematics")
    teacher = Teacher("Bob", "Smith", "10-06-1983", "+3425164759","Physics")
    student_teacher = StudentTeacher("Charlie", "Brown", "05-05-1995", "+8564739208","Computer Science", "Programming")


    print(student.introduce())
    print(student.create_corporate_email())
    print(student.enroll_in_course("Math 101"))
    print(student.update_major("Data Science"))

    print(teacher.introduce())
    print(teacher.create_corporate_email())
    print(teacher.assign_course("Physics 101"))
    print(teacher.update_subject("Quantum Mechanics"))

    print(student_teacher.introduce())
    print(student_teacher.perform_dual_role("Advanced Algorithms", "Programming Basics"))
