# accessing private attributes with getters and setters
class Person:
    def __init__(self, name, age):
        self._name = name
        self.age = age

    def person_details(self):
        print(f"{self._name} is a {self.age} year old person.")

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name


p1 = Person("John", 36)
p1.person_details()
p1.get_name()
p1.set_name("Jane")
p1.person_details()
p1.get_name()