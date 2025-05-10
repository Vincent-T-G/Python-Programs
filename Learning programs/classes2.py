
from car_class import Car


car1 = Car("Mustang", 2025, "red", False)
car2 = Car("Corvette", 2023, "blue", True)
car3 = Car("Chager", 2026, "yellow", True)


print(car1.color)
car1.stop()
car2.drive()
car3.describe()