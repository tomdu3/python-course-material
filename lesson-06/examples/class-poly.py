# class Polymorphism

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def person_details(self):
        print(f"{self.name} is a {self.age} year old person.")

class Employee(Person):

    def __init__(self, name, age, employee_id, position, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.position = position
        self.salary = salary

    def employee_details(self):
        print(f"{self.name} is a {self.age} year old {self.position} with employee id {self.employee_id}.")


p = Person("John", 30)
p.person_details()

e = Employee("Jane", 25, 12345, "Manager", 50000)
e.person_details()
e.employee_details()

