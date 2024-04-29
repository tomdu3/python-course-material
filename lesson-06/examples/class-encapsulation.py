# encapsulation example
class Person:
    def __init__(self, name, age):
        self._name = name
        self.age = age
    

    def person_details(self):
        print(f"{self._name} is a {self.age} year old person.")

    def get_name(self):
        return self._name

p1 = Person("John", 36)
p1.person_details()
print(p1._name)  # not a good practice
print(p1.get_name())

class Teacher(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.__salary = salary

    def get_salary(self):
        return self.__salary
    
    def teacher_details(self):
        # print(f"{self._name} is a {self.age} year old teacher with salary {self.__salary}.")  # doesn't work
        print(f"{self._name} is a {self.age} year old teacher with salary {self.get_salary()}.")


t1 = Teacher("Jane", 30, 50000)
t1.person_details()
t1.teacher_details()
# print(t1.__salary)  # doesn't work
print(t1._Teacher__salary)  # works but not recommended
print(t1.get_salary())
