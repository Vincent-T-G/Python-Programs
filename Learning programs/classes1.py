#This code is written in the process of learning how to uses classes in python

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point(10,20)
print(point1.x)


class Person:
    def __init__(self,name):
        self.name = name

    def talk(self):
        print(f"Hi I am {self.name}")


Kevin = Person("Kevin Kamau")
Bob = Person("Bob Smith")

Kevin.talk()
Bob.talk()