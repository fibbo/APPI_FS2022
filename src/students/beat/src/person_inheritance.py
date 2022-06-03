class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I'm an abstract person which is {self.age} years old and my name is {self.name}.")

class Student(Person):
    def __init__(self, name, age, grades, lectures):
        super().__init__(name, age)
        self.grades = grades
        self.lectures = lectures

    def info(self):
        print(f"I'm a stundent, my name is {self.name}, I'm {self.age} years old, my grades are {self.grades} and I study {self.lectures}.")

class Teacher(Person):
    def __init__(self, name, age, salary, lectures):
        super().__init__(name, age)
        self.salary = salary
        self.lectures = lectures

    def info(self):
        print(f"I'm a teacher, my name is {self.name}, I'm {self.age} years old, my salary is {self.salary} and I lecture {self.lectures}.")


# Probably it's better to keep lecture in singular. Then it's easier:
# A lecture as one teacher and many students.

class Lecture:
    def __init__(self, topic, teacher, students):
        self.topic = topic
        self.teacher = teacher
        self.students = students

    def info(self):
        print(f"I'm a lecture, my topic is {self.topic}, my teacher is {self.teacher}, and my students are {self.students}.")
# class Lectures:
#     def __init__(self, topic, teacher, students):
#         self.topic = topic
#         self.teacher = teacher
#         self.students = students

#     def lecture_list_teacher(self):
#         self.lecture = {}
#         lecture[self.topic] = self.teacher

#     def lecture_list_student(self):
#         self.lecture = {}
#         count = 0
#         lecture[self.topic] = str(count += 1)


list_of_person = [Student("Max", 17, 5, "Maths"), Teacher("Dr. Jekyll", 54, 100000, "Chemistry"), Student("Sophie", 19, 5.5, "Chemistry"), Teacher("Mr. Hyde", 55, 120000, "Maths")]
for person in list_of_person:
    person.info()

# for person in list_of_person:
#     if person of class Student:
#         take lectures student



