# Lesson 2: Control Flow - Functions, Scopes

## 2.1. Functions
[Function in Python Documentation](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)

- function is a reusable block of code that performs a specific task.
- function can be defined in two ways:
    - function definition
    - function declaration

### 2.1.1. Function definition in Python
- syntax: `def function_name(parameters):`
- `parameters` are optional
- `return` is optional
- `:` is required
- indentation is required
- `pass` is optional


```python
# declaration of the function to print the title
def print_title():
    print('---------------------------------------------------------------')
    print('{:^63}'.format('Lesson 2: Functions'))
    print('---------------------------------------------------------------')
```

- Why nothing happened when we run the code? Because we only defined the function, but we didn't call it. Functions are like a recepie for our code. We have the instructions, but if we don't say - ok make it so, nothing happens.
- Therefore, we need make a **function** call. We do that by writing the name of the function and parentheses.


```python
# function call
print_title()
```

    ---------------------------------------------------------------
                          Lesson 2: Functions                      
    ---------------------------------------------------------------


### 2.1.2. Function definition with return value

- if a function doesn't have a return value, the default value is `None`. We call that function a void function.
- usually, we expect a function to return a value, after some data manipulation
- we use the `return` keyword to return a value from a function
- we also use the `return` keyword to exit the function

Because of this, the value of the function needs to be assigned to a variable, stored in a file or passed to another function.


```python
# weather forecast functin

def weather_forecast():
    return 'The weather will be sunny with a high of 75 degrees.'

print(weather_forecast())
```

    The weather will be sunny with a high of 75 degrees.



```python
# news
def news():
    return 'The news today is that the stock market is up 100 points.'

headline = news()
print(headline)
```

    The news today is that the stock market is up 100 points.



```python
# using Pass in a function
def check_triangle():
    pass

check_triangle()
```

We use `pass` to create an empty function. It is useful when we want to create a function that we will fill in later.


### 2.1.3 Functions with parameters

- functions can take parameters
- parameters are variables that are passed to the function when it is called
- we use the `:` operator to specify the type of a parameter (optional)
- we user the `->` operator to specify the type of the return value (optional)
- we use the `=` operator to assign a default value to a parameter if it is not specified in a function call



```python
# function with parameters
def add_two_numbers(num1, num2):
    return num1 + num2

# function with specified types of parameters
def add_three_numbers(num1: int, num2: int, num3: int) -> int:
    return num1 + num2 + num3

# function with default parameters
def multiply_by_two(num1, num2=2):
    return num1 * num2

sum_of_two = add_two_numbers(1, 2)
sum_of_three = add_three_numbers(1, 2, 3)
product_of_two_one_parameter = multiply_by_two(2)
product_of_two = multiply_by_two(2, 3)

print(sum_of_two)
print(sum_of_three)
print(product_of_two_one_parameter)
print(product_of_two)
```

    3
    6
    4
    6


### 2.1.4. Functions with default parameters

- as we saw in the previous example, we use the `=` operator to assign a default value to a parameter if it is not specified in a function call
- there is a rule that limits the use of default value of the parameters. That is, if we specify a default value of the parameter, the parameters that follow also need to have a default value, whilst the parameters that come before the one with the default value do not need to have a default value.


```python
# function with default values
def multiply_by_two(num1, num2=2):
    return num1 * num2

print(multiply_by_two(2))
print(multiply_by_two(2, 3))
```

    4
    6



```python
# function with default values folowed by undefined
def area_of_triangle(side_a=3, side_b=4, side_c):  # side_c is undefined and will cause an error
    return side_a * side_b / 2
```


      Cell In[3], line 2
        def area_of_triangle(side_a=3, side_b=4, side_c):  # side_c is undefined and will cause an error
                                                 ^
    SyntaxError: parameter without a default follows parameter with a default



## 2.2 Scope
- scope is the visibility of a variable. It determines where a variable can be accessed.
- variables can be accessed from anywhere in the program, depending on their scope

- there are 2 important types of scopes in Python:
    - local scope
    - global scope
  
### 2.2.1. Local scope

- local scope is the scope of a variable in a function or class
- local scope is defined by indentation
- local scope is only accessible within the function or class


```python
# function with variable definition
def sum_numbers(num1, num2):
    total = num1 + num2
    return total

print(sum_numbers(1,3))

print(total)
```

    4



    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    Cell In[16], line 8
          4     return total
          6 print(sum_numbers(1,3))
    ----> 8 print(total)


    NameError: name 'total' is not defined


### 2.2.2. Global scope

- global scope is the scope of a variable in the program
- global scope is defined by the `global` keyword
- global scope is accessible from anywhere in the program
- global scope is not limited to a function or class
- global scope can be overwritten by a local scope


```python
name = 'John'
def print_name():
    # we can use name in our function, but that will not change the global variable value
    name = 'Jane'
    print(name)

print_name()
print(name)
```

    Jane
    John



```python
# we can access a global variable in a function
name = 'John'
def print_name():
    global name
    name = 'Jane' # this will change the global variable value
    print(name)

print_name()
print(name)
```

    Jane
    Jane


We have to be careful when we overwrite a global variable with a local variable. It can lead to unexpected behavior of our program.


## 2.3 Docstrings
- docstrings are used to document functions
- docstrings are used to provide information about the function
- they are written in triple quotes


```python
# example of docstring
def print_title():
    """Prints the title of the lesson"""
    print('---------------------------------------------------------------')
    print('{:^63}'.format('Lesson 2: Functions'))
    print('---------------------------------------------------------------')

print_title.__doc__

```




    'Prints the title of the lesson'



- We can also give the explanation of the function input and output



```python
# docstring with explanation of input and output
def check_triangle(side1, side2, side3):
    """Checks if a triangle is valid
    Parameters
    ----------
    side1 : int
        The length of the first side
    side2 : int
        The length of the second side
    side3 : int
        The length of the third side
    Returns
    -------
    bool
        True if the triangle is valid, False otherwise
    """
    return side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1

print(check_triangle.__doc__)
```

    Checks if a triangle is valid
        Parameters
        ----------
        side1 : int
            The length of the first side
        side2 : int
            The length of the second side
        side3 : int
            The length of the third side
        Returns
        -------
        bool
            True if the triangle is valid, False otherwise
        


# 2.4 Type Conversion

- type conversion is the process of converting a value from one type to another
- we use the `type()` function to get the type of a value
- we use the `int()` function to convert a value to an integer
- we use the `str()` function to convert a value to a string
- we use the `float()` function to convert a value to a float
- we use the `bool()` function to convert a value to a boolean

We have already seen that we can use the `type()` function to get the type of a value. And when we were talking about input, we have also used the `int()` function to convert a value to an integer. Let us combine this knowledge with functions.


```python
# make a function that requires an input of a number from the user
def get_number():
    return int(input('Enter a number: '))

print(get_number())
```

    34



```python
# let as reverse a number backwards
num = 123456789

#first we need to make it a string
str_num = str(num)

#now we can reverse it with a slice
str_num = str_num[::-1]

# now we can convert it back to an int
num2 = int(str_num)

print(num2)



```

    987654321


We will often convert from floats to integers and vice versa in order to do some calculations.

For example, if we want to take the half of a string, we need to take the length of the string, divide it by two and then slice the string, but the index can be only an integer.


```python
# slice a string in half
str = 'Let us slice this string in half'

half = len(str)/2
print(half)  # this is not an int
print(int(half))

half_index = int(half)
print(str[:half_index])
print(str[half_index:])
```

    16.0
    16
    Let us slice thi
    s string in half



```python
# Different approach
str = 'Let us slice this string in half'

half = len(str)//2  # this is an int, result of floor division
print(half)  # this is not an int

print(str[:half])
print(str[half:])
```

    16
    Let us slice thi
    s string in half


Sometimes we need from the user the input of a decimal number. We can use the `float()` function.


```python
# let us calculate the total price based on a purchase
purchase = float(input('Enter the amount of the purchase: '))
tax = 0.08
total = purchase * (1 + tax)
print(total)

```

    108.0

