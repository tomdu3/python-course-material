# Advanced Class

class Animal:

    # constructor
    def __init__(self, name, says_what):
        self.name = name
        self.says_what = says_what

    # method - 
    def says(self):
        return self.says_what + " " + self.name


# object or instance of a class
animal = Animal("Dog", "Woof")

print(animal.says())
print(animal.name)