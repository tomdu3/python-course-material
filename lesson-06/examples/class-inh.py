# Class Inheritance 

# Base class
class Person:

    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method
    def person_details(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Derived class
class Student(Person):
    number_of_students = 0

    # Constructor
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

        # Increment number of students
        Student.number_of_students += 1

    # Method
    def student_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Student ID: {self.student_id}")


# Derived class
class Employee(Person):
    number_of_employees = 0
    # Constructor
    def __init__(self, name, age, employee_id, position, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.position = position
        self.salary = salary

        # Increment number of employees
        Employee.number_of_employees += 1

    # Method
    def employee_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Employee ID: {self.employee_id}, Position: {self.position}")

        print(f"Salary: {self.salary}")


person = Person("John", 25)
person.person_details()

student = Student("Jane", 20, 12345)
student.person_details()
student.student_details()
print(Student.number_of_students)

employee = Employee("Bob", 30, 67890, "Janitor", 25000)
employee.person_details()
employee.employee_details()

professor = Employee("Albert Einstein", 60, 12345, "Professor", 100000)
professor.person_details()
professor.employee_details()

director = Employee("William Shakespeare", 70, 12345, "Director", 250000)
director.person_details()
director.employee_details()
print(Employee.number_of_employees)