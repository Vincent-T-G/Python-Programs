# This code is written in the learning and practice of class variables in OOP in Python

class Student:

    num_of_students = 0
    class_year = 2024

    def __init__(self,name,age):
        self.name = name
        self.age = age
        Student.num_of_students += 1


student1 = Student("Spongebob", 30)
student2 = Student("Patric", 35)
student3 = Student("Squidward", 55)
student4 = Student("Sandy", 27)

print(student1.name)
print(student1.age)

print(f"My graduating class of {Student.class_year} has {Student.num_of_students} students")