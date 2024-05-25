# 6. Object oriented progamming, Lambda Functions and APIs 

## 6.1 Object oriented progamming

- [W3Schools: *Python Classes*](https://www.w3schools.com/python/python_classes.asp)
- [GeekForGeeks: *Classes*](https://www.geeksforgeeks.org/python-oops-concepts/)
- [Real Python: *Object-Oriented Programming (OOP) in Python 3*](https://realpython.com/python3-object-oriented-programming/)
- [Programiz: *Python Object Oriented Programming*](https://www.programiz.com/python-programming/object-oriented-programming)

![Python OOP](./python-objects-ai.png)

### 6.1.1. Introduction

Object oriented programming is a programming paradigm that uses objects and their interactions to design applications. It is an ultimate approach to software development and reusability.

Object Oriented Programming is a fundamental concept in Python, empowering developers to build modular, maintainable, and scalable applications. By understanding the core OOP principles—classes, objects, inheritance, encapsulation, polymorphism, and abstraction—programmers can leverage the full potential of Python’s OOP capabilities to design elegant and efficient solutions to complex problems.


### 6.1.2. What is Object-Oriented Programming in Python?

In Python object-oriented Programming (OOPs) is a programming paradigm that uses objects and classes in programming. It aims to implement real-world entities like inheritance, polymorphisms, encapsulation, etc. in the programming. The main concept of object-oriented Programming (OOPs) or oops concepts in Python is to bind the data and the functions that work together as a single unit so that no other part of the code can access this data. 

We use objects and classes in Python to define the real-world entities like inheritance, polymorphisms, encapsulation, etc.

### 6.1.3. Classes
[Classes from GeekForGeeks](https://www.geeksforgeeks.org/python-oops-concepts/)

A class is a collection of objects. A class contains the blueprints or the prototype from which the objects are being created. It is a logical entity that contains some attributes and methods. 

To understand the need for creating a class let’s consider an example, let’s say you wanted to track the number of dogs that may have different attributes like breed, and age. If a list is used, the first element could be the dog’s breed while the second element could represent its age. Let’s suppose there are 100 different dogs, then how would you know which element is supposed to be which? What if you wanted to add other properties to these dogs? This lacks organization and it’s the exact need for classes. 

Some points on Python class:  

    Classes are created by keyword class.
    Attributes are the variables that belong to a class.
    Attributes are always public and can be accessed using the dot (.) operator. Eg.: Myclass.Myattribute

Class Definition Syntax:

```python
    class Name(parameters):
        ...
```

    


```python
# class example
class Human:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def display(self):
            print(f'{self.name} is {self.age} years old.')
        
# object creation
h1 = Human('John', 36)
h1.display()


```

    John is 36 years old.


- let us explain the code
- `class` is defining a class
- `Human` is the name of the class
- `def __init__(self, name, age)` is the constructor of the class. It is called automatically when an object is created.
- `self` is the instance of the class - it refers to the object itself
- `name` and `age` are the attributes of the class - these are the variables we receive when we create an object
- `display(self)` is the method of the class
- `f'{self.name} is {self.age} years old.'` is the output of the method
- `h1` is an object made on the blueprint of the class Human

#### 6.1.4. Static variables vs instance variables

- Static variables - variables that are shared by all objects of the class
- Instance variables - variables that are unique to each object 


```python
# Make a class with static and instance variables

class Book:

    # static variable
    num_books = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.num_books += 1

    def display(self):
        print(f'Title: {self.title}')
        print(f'Author: {self.author}')

# object creation
b1 = Book('Title 1', 'Author 1')
b1.display()

b2 = Book('Title 2', 'Author 2')
b2.display()

b3 = Book('Title 3', 'Author 3')
b3.display()

print(f'Total number of books: {Book.num_books}')
```

    Title: Title 1
    Author: Author 1
    Title: Title 2
    Author: Author 2
    Title: Title 3
    Author: Author 3
    Total number of books: 3


### 6.1.5. Inheritance

Let us see one other example.


```python
# make a class that will inherit from the Human class
class Student(Human):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school

    def display(self):
        print(f'{self.name} is {self.age} years old and goes to {self.school}.')

# object creation
s1 = Student('John', 36, 'MIT')
s1.display()
```

    John is 36 years old and goes to MIT.


- here we have a class with 3 attributes and 1 method
- `super()` is a function that is used to access the attributes and methods of the parent class
- `self` is an instance of the class
- `school` is an attribute of the class Student
- `f'{self.name} is {self.age} years old and goes to {self.school}.'` is the output of the method

- here we have an example of the concept we call inheritance.

**Inheritance** is a concept that allows us to define a class that inherits the properties from another class.
- **Parent class** is the class being inherited from, also called base class.
- **Child class** is the class that inherits from another class, also called derived class.



```python
# Child class
class Employee(Human):
    def __init__(self, name, age, salary):  # overrides the parent class initialization
        super().__init__(name, age)  # inherits the parent class initialization
        self.salary = salary

    def display(self):
        print(f'{self.name} is {self.age} years old.')
        print(f'Salary: {self.salary}')

# object creation
e1 = Employee('John', 36, 50000)
e1.display()
```

    John is 36 years old.
    Salary: 50000


Let us see one example of the class that will contain all the objects that are created from the class.


```python
class Client:
    clients = []

    def __init__(self, fname, lname, age, subscription=False):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.subscription = subscription
        self.clients.append(self)

    def display(self):
        print(f'{self.fname} {self.lname} {self.age} {self.subscription}')

    def __str__(self):
        return f'{self.fname} {self.lname} {self.age} {self.subscription}'


c1 = Client('John', 'Smith', 35)
c1.display()

c2 = Client('Jane', 'Doe', 30, True)
c2.display()

print(c1)
print(c2)


print(Client.clients)  # list of objects - we receive the type details and the address

for client in Client.clients:  # we are accessing the objects
    print(client)

```

    John Smith 35 False
    Jane Doe 30 True
    John Smith 35 False
    Jane Doe 30 True
    [<__main__.Client object at 0x7f4c941039b0>, <__main__.Client object at 0x7f4c94103b00>]
    John Smith 35 False
    Jane Doe 30 True


- `__str__(self)` is a special method that is called when we print an object. Let us see the case when we print an object without and with this method.


```python
class CreditCard:

    def __init__(self, card_number, expiration_date, cvv):
        self.card_number = card_number
        self.expiration_date = expiration_date
        self.cvv = cvv

card = CreditCard('1234 5678 9012 3456', '02/25', '123')
print(card)
```

    <__main__.CreditCard object at 0x7f4c94103800>


Now, with the `__str__(self)` method


```python
class CreditCard:

    def __init__(self, card_number, expiration_date, cvv):
        self.card_number = card_number
        self.expiration_date = expiration_date
        self.cvv = cvv

    def __str__(self):
        return f'card number: {self.card_number}, exp: {self.expiration_date}, CVV: {self.cvv}'

card = CreditCard('1234 5678 9012 3456', '02/25', '123')
print(card)

```

    card number: 1234 5678 9012 3456, exp: 02/25, CVV: 123


### 6.1.6. Polymorphism

Polymorphism is the ability of an object to take on many forms. In Python, polymorphism is achieved using the concept of inheritance.
Practically, polymorphism is achieved using method overriding.
- That means we can create a method in a child class that has the same name as that of the method in the parent class, but it will have a different implementation.


```python
# Polymorphism example
class Car:

    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

    def __str__(self):
        return f'Car color is {self.color} and brand is {self.brand}'
    
    def speed(self):
        print('210 km/h')

class Truck(Car):

    def __init__(self, color, brand, payload):
        super().__init__(color, brand)
        self.payload = payload
    
    def speed(self):
        print('120 km/h')

    def __str__(self):
        return f'Truck color is {self.color} and brand is {self.brand} and payload is {self.payload}'


c1 = Car('Red', 'Toyota')
print(c1)
c1.speed()

t1 = Truck('Blue', 'Ford', 1000)
print(t1)
t1.speed()

print(type(c1))
print(type(t1))
print(isinstance(c1, Car))
print(isinstance(t1, Car))
print(isinstance(t1, Truck))
```

    Car color is Red and brand is Toyota
    210 km/h
    Truck color is Blue and brand is Ford and payload is 1000
    120 km/h
    <class '__main__.Car'>
    <class '__main__.Truck'>
    True
    True
    True


Compile time polymorphism or Method Overloading

- We can create a method in a parent class that has the same name as that of the method in the child class, but it will have a different implementation.


```python
# Compile time polymorphism - static polymorphism - not a valid Python example
class Area:

    def area(self, x, y):
        return f'Area of a rectangle is {x * y}'
    
    def area(self, x, y, z):
        return f'Area of a triangle is {x * y * z}'


area = Area()
print(area.area(10))
print(area.area(10, 20))
print(area.area(10, 20, 30))
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In[9], line 12
          8         return f'Area of a triangle is {x * y * z}'
         11 area = Area()
    ---> 12 print(area.area(10))
         13 print(area.area(10, 20))
         14 print(area.area(10, 20, 30))


    TypeError: Area.area() missing 2 required positional arguments: 'y' and 'z'



```python
# Compile time polymorphism - static polymorphism - a valid Python example
class Area:
    def area(self, x, y=None, z=None):
        if z is not None:
            return f'Area of a triangle is {x * y * z}'
        elif y is not None:
            return f'Area of a rectangle is {x * y}'
        else:
            return f'Invalid number of arguments'

area = Area()
print(area.area(10))          # Output: Invalid number of arguments
print(area.area(10, 20))      # Output: Area of a rectangle is 200
print(area.area(10, 20, 30))  # Output: Area of a triangle is 6000
```

    Invalid number of arguments
    Area of a rectangle is 200
    Area of a triangle is 6000


### 6.1.7 Encapsulation

- Encapsulation is the process of binding data and methods together in a single unit. In Python, encapsulation is achieved using the concept of attributes (data) and methods (functions).
- The reason behind encapsulation is to achieve data hiding.
- The data inside the class is private and the methods are public. The data and methods inside the class are accessible to the class and its subclasses.
- syntax for encapsulation:
    - private attributes and methods are using single underscores `_`
    - protected attributes and methods are using double underscores `__`


```python
# Encapsulation example
class Car:

    def __init__(self, color, brand):
        self.__color = color
        self.__brand = brand

    def __str__(self):  # private method
        return f'Car color is {self.__color} and brand is {self.__brand}'
    
    def _price_(self):  # protected method
        return '210 km/h' 

    def get_price(self):  # calling the protected method
        return self._price_()  # accessing the private method

c1 = Car('Red', 'Toyota')
print(c1)

print(c1.get_price())  # Now get_price() returns a value, so it can be printed

```

    Car color is Red and brand is Toyota
    210 km/h


- When we are dealing with private or protected variables, we need to use the getter and setter methods to access or modify them.
- The getter method is used to access the private variable and the setter method is used to modify the private variable.


```python
# private variables, getter and setter methods
class Animal:

    def __init__(self, name, says_what):
        self.__name = name
        self.__says_what = says_what

    def __str__(self):
        return f'{self.__name} says {self.__says_what}'

    def get_name(self):
        return self.__name

    def get_says_what(self):
        return self.__says_what

    def set_says_what(self, says_what):
        self.__says_what = says_what


a1 = Animal('Dog', 'woof')
print(a1)
print(a1.get_name())
print(a1.get_says_what())
a1.set_says_what('arf')
print(a1.get_says_what())
print(a1)
a2 = Animal('Cat', 'meow')
print(a2)
print(a2.get_name())
print(a2.get_says_what())
a2.set_says_what('purr')
print(a2.get_says_what())
print(a2)
```

    Dog says woof
    Dog
    woof
    arf
    Dog says arf
    Cat says meow
    Cat
    meow
    purr
    Cat says purr


## 6.2. Lambda functions and use cases

Sometimes we need to create a function without a name. In this case, we can use lambda functions. They are useful when we need to pass a function as an argument to another function, or when we want to create a function that is useful only in one place of the code, and never called again.

### 6.2.1. Lambda functions
- [https://www.programiz.com/python-programming/anonymous-function](https://www.programiz.com/python-programming/anonymous-function)
- [https://www.freecodecamp.org/news/python-lambda-function-explained/](https://www.freecodecamp.org/news/python-lambda-function-explained/)

<br>

- A lambda function is a small anonymous function.
- It can take any number of arguments, but can only have one expression.
- It is used when we want to create a function without a name.
- It is useful when we want to pass a function as an argument to another function.
- It is also used when we want to create a function that is called only once.
- sytax:
    ```python
    lambda argument(s) : expression  
    ```


```python

# lambda function example
hello = lambda name: f'Hello, {name}!'

print(hello('John'))
print(hello('Jane'))
```

    Hello, John!
    Hello, Jane!



```python
# lambda function with multiple arguments
say_hello = lambda name, age: f'Hello, {name}! You are {age} years old.'

print(say_hello('John', 30))
print(say_hello('Jane', 25))
```

    Hello, John! You are 30 years old.
    Hello, Jane! You are 25 years old.



```python
# lambda function called only once in a complex program

def get_sum(num1, num2):
    return lambda num3: num1 + num2 + num3

print(get_sum(10, 20)(30))  # Output: 60, because 10 + 20 + 30 = 60
```

    60


This code defines a function called get_sum that takes two arguments num1 and num2. The function returns another function defined as a lambda function which takes a single argument num3 and returns the sum of num1, num2, and num3.

When the get_sum function is called with arguments 10 and 20, it returns a lambda function. Then, the returned lambda function is immediately called with argument 30 using (30) which calculates the sum of 10, 20, and 30. The output of the code will be 60.

### 6.2.2. Lambda functions and map, filter, and reduce

- Map, filter, and reduce are functions that are used in functional programming. They are used to apply a function to each element of a list, filter out elements based on a condition, and reduce the elements into a single value.
- we use lambda functions in these functions to perform these tasks.

#### Map

- Map function applies a function to each element of a list. It returns a new list with the modified elements.
- It is used to transform the elements of a list.

- syntax: `map(function, iterable)`


```python
# map function example
numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x**2, numbers))

print(squares)  # Output: [1, 4, 9, 16, 25]

```

    [1, 4, 9, 16, 25]



```python
# map function using external function
def my_square(x):
    return x**2

numbers = [1, 2, 3, 4, 5]

squares = list(map(my_square, numbers))

print(squares)  # Output: [1, 4, 9, 16, 25]
```

    [1, 4, 9, 16, 25]


#### Filter

- Filter function filters out elements from a list based on a condition. It returns a new list with the filtered elements.
- It is used to remove elements from a list based on a condition.

- syntax: `filter(function, iterable)`


```python
# filter function example
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)  # Output: [2, 4, 6, 8, 10]
```

    [2, 4, 6, 8, 10]


#### Reduce

- Reduce function reduces the elements of a list into a single value. It returns a single value.
- It is used to combine the elements of a list into a single value.
- e.g. to calculate the sum of a list of numbers.
- syntax: `reduce(function, iterable)`


```python
# reduce function example
from functools import reduce

numbers = [1, 2, 3, 4, 5]

product = reduce(lambda x, y: x * y, numbers)

print(product)  # Output: 120
```

    120

