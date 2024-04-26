class Animal:
    # Static variable
    num_animals = 0

    def __init__(self, name, says_what):
        self.name = name
        self.says_what = says_what

        # Increment number of animals
        Animal.num_animals += 1

    def says(self):
        return self.says_what + " " + self.name

# object or instance of a class
animal1 = Animal("Dog", "Woof")
animal2 = Animal("Cat", "Meow")
animal3 = Animal("Cow", "Moo")


print(animal1.says())
print(animal2.says())
print(animal3.says())

print(Animal.num_animals)