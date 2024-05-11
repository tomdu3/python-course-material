# Lesson 2 - Control Flow Part 2 - If statements and Loops

## 2.3. If statements

An if statement is a conditional statement that runs or skips code based on whether a condition is True or False.

### 2.3.1 True or False
In order to work with if statements in Python, we need to recall our Boolean data type. A Boolean data type is a data type that has one of two possible values (usually denoted true and false), intended to represent the two truth values of logic and Boolean algebra. In Python, the two possible values are `True` and `False`. `True` is represented as `1` and `False` is represented as `0`. It is important to note that `True` and `False` are not the same as `1` and `0`.

Let us see some examples:


```python
# True or False statements with comparisons
print(5==5)
print(5!=5)
print(5>5)
print(5<5)
print(5>=5)
print(5<=5)
```

    True
    False
    False
    False
    True
    True



```python
# True or False statements with boolean operators
print(5==5 and 5!=5)
print(5==5 or 5!=5)
print(not 5==5)
```

    False
    True
    False



```python
print(bool(0))
print(bool(1))
print(bool(''))
print(bool('hello'))
print(bool(' '))
print(bool(None))
a = 0
print(bool(a))
b = 2
print(bool(b))
```

    False
    True
    False
    True
    True
    False
    False
    True


- **Truth Tables**

| Condition | True | False |
| --- | --- | --- |
| 5 == 5 | True | False |
| 5 != 5 | False | True |
| 5 > 5 | False | False |
| 5 < 5 | False | False |
| 5 >= 5 | True | False |
| 5 <= 5 | True | False |

- **Logical Operators**
- `and`, `or` and `not` (not in Python is `!`)
<br>

- **AND**
  
| A | B | A and B |
| --- | --- | --- |
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

- **OR**

| A | B | A or B |
| --- | --- | --- |
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

- **NOT**

| A | A not |
| --- | --- |
| 0 | 1 |
| 1 | 0 |

- **NOT AND**

| A | B | NOT (A and B) |
| --- | --- | --- |
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 0 |

- **NOT OR**

| A | B | NOT (A or B) |
| --- | --- | --- |
| 0 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

<br>

- `NOT AND` is equivalent to `NOT(A and B) == (NOT A) or (NOT B)`
- `NOT OR` is equivalent to `NOT(A or B) == NOT(A) and NOT(B)`

### 2.3.2 if statement

- if statement is a conditional statement that runs or skips code based on whether a condition is True or False.
- the general structure of an if statement is as follows:

    ```python
    if condition:
        # code to be executed if condition is True
    else:
        # code to be executed if condition is False
    ```



```python
# if statement
a = 5
if a == 5:
    print('a is 5')
else:
    print('a is not 5')
```

    a is 5



```python
# if else statement
a = 4
if a == 5:
    print('a is 5')
else:
    print('a is not 5')
```

    a is not 5


If we need to check more than one condition, we can use `elif` keyword. It is used to indicate the next condition if the previous condition is false. The general structure of an if statement with `elif` is as follows:

```python
    if condition1:
        # code to be executed if condition1 is True
    elif condition2:
        # code to be executed if condition1 is False and condition2 is True
    else:
        # code to be executed if condition1 and condition2 are False
```



```python
# example if elif else
a = 5
if a == 5:
    print('a is 5')  # condition is true
elif a == 4:  # condition is not true
    print('a is 4')
else:  # condition is not true
    print('a is not 5 or 4')
```

    a is 5


### 2.3.3 Nested if statements

- if statement can be nested inside another if statement. This means that an if statement can be inside another if statement.


```python
# nested if statement
a = 5
b = 10
if a == 5:
    if b == 10:
        print('a is 5 and b is 10')
    else:
        print('a is 5 but b is not 10')
else:
    print('a is not 5')

```

    a is 5 and b is 10


## 2.3.4 Match Statements

[Match Statement](https://medium.com/@sabcan.uy/python-match-case-statement-63d01477e1c0)

- Match statements are a new feature in Python 3.10. They are used to match a value of the certain data.
- Every match statement can be rewritten as if-elif-else statements.
- we use `case` keyword to indicate the case with certain condition.

- the syntax is as follow:
  ```python
  match value:
    case value1:
        # code to be executed if value is value1
    case value2:
        # code to be executed if value is value2
    case _:
        # code to be executed if value is not value1 or value2
  ```
<br>

Let us first see an example in if-elif-else statement that we will then convert into match statement.


```python
# example with if elif else
user_input = int(input('Enter a number: '))

if user_input == 1:
    print('You entered 1')
elif user_input == 2:
    print('You entered 2')
else:
    print('You did not enter 1 or 2')
```

    You did not enter 1 or 2



```python
# same code with match
user_input = int(input('Enter a number: '))

match user_input:
    case 1:
        print('You entered 1')
    case 2:
        print('You entered 2')
    case _:
        print('You did not enter 1 or 2')
```

    You entered 2


**Using Match with conditionals**
- We can use match statement with conditionals.
- we will use `_` in the match statement to indicate the case with certain condition.
- we also use `|` to indicate `OR` condition.
- we also use `&` to indicate `AND` condition.
- we also use `not` to indicate `NOT` condition.


```python
# example with if elif else
user_input = int(input('Enter a number: '))

if user_input == 1 | 2:
    print('You entered 1 or 2')
else:
    print('You did not enter 1 or 2')
```


```python
# same code with match
user_input = int(input('Enter a number: '))

match user_input:
    case 1 | 2:
        print('You entered 1 or 2')
    case _:
        print('You did not enter 1 or 2')
```


```python
# example with if elif else
user_input = int(input('Enter a number: '))

if user_input == 0:
    print('You entered 0')
elif user_input > 0:
    print('You entered a positive number')
elif user_input < 0:
    print('You entered a negative number')
else:
    print('You did not enter a number')
```


```python
# same code with match
user_input = int(input('Enter a number: '))

match user_input:
    case 0:
        print('You entered 0')
    case _ if user_input > 0:
        print('You entered a positive number')
    case _ if user_input < 0:
        print('You entered a negative number')
    case _:
        print('You did not enter a number')
```

Let use show now another beautiful example.


```python
# example with match
def process_data(data):
    match data:
        case str():
            return data.upper()
        case list() as l if len(l) > 2:
            return l[0], l[-1]
        case int() | float():
            return data * 2
        case _:
            return "Unknown data type"


print(process_data('hello'))
print(process_data([1, 2, 3, 4, 5]))
print(process_data(5))
print(process_data(5.5))
```

    HELLO
    (1, 5)
    10
    11.0



```python
# rewritten with if elif else
def process_data(data):
    if isinstance(data, str):
        return data.upper()
    elif isinstance(data, list) and len(data) > 2:
        return data[0], data[-1]
    elif isinstance(data, (int, float)):
        return data * 2
    else:
        return "Unknown data type"


print(process_data('hello'))
print(process_data([1, 2, 3, 4, 5]))
print(process_data(5))
print(process_data(5.5))
```

    HELLO
    (1, 5)
    10
    11.0


## 2.4 Loops

- A loop is a sequence of instructions that is repeated until a specific condition is met.
- We have different types of loops in Python:
    - for loop
    - while loop

### 2.4.1 for loop

[For Loop](https://www.w3schools.com/python/python_for_loops.asp)

- A for loop is used to iterate over a sequence (list, tuple, string, dictionary, set, etc.) and execute a block of code for each element in the sequence.
- The general structure of a for loop is as follows:

```python
for item in sequence:
    # code to be executed for each item in the sequence
```

- there's a special sequence called `range` that can be used to generate a sequence of numbers. The general structure of a range is as follows:

[Range Function](https://www.w3schools.com/python/ref_func_range.asp)

```python
range(start, stop, step)
```

- `start` is the starting number of the sequence (optional, default is 0)
- `stop` is the ending number of the sequence (mandatory, exclusive)
- `step` is the difference between each number in the sequence (optional, default is 1)


```python
# basic for loop with range
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4
```

    0
    1
    2
    3
    4



```python
# for loop with start and end range
for i in range(2, 5):
    print(i)  # 2, 3, 4
```

    2
    3
    4



```python
# for loop with start, end and step
for i in range(2, 5, 2):
    print(i)  # 2, 4
```

    2
    4



```python
# we can go backwards
for i in range(5, 2, -1):
    print(i)  # 5, 4, 3
```

    5
    4
    3


We will get back to for loops later, when we learn about other sequences.

### 2.4.2 while loop

[While Loop](https://www.w3schools.com/python/python_while_loops.asp)

- A while loop is used to execute a block of code until a certain condition is met.
- The general structure of a while loop is as follows:
    
```python
    while condition:
        # code to be executed
```


```python
# while loop
i = 0
while i < 5:
    print(i)  # 0, 1, 2, 3, 4
    i += 1  # increments i by 1. it corresponds to i = i + 1
```

This example is quite similar to a for loop. In fact, every for loop can be transformed into a while loop. However, there are some cases where a while loop is more appropriate than a for loop. For example, when we don't know the number of iterations in advance.

General rule of thumb:
- when the number of iterations is known, that is when we need to loop throug a defined sequence,use a for loop
- when the number of iterations is unknown, use a while loop


```python
# while loop without knowing the number of iterations
user_input = ''

while not user_input:
    user_input = input('Enter something: ')  # if empty string, while loop continues

print(user_input)

```

    e


Many times we need to count the number of iterations that a while loop performs. This can be done using a `counter` variable. It is usually initialized to 0 and then incremented by 1 each time the loop iterates.



```python
count = 0
user_input = ''

while not user_input:
    user_input = input('Enter something: ')
    count += 1

print(f'You entered {user_input} after {count} times')

```

    You entered 1 after 3 times


## 2.4.3 Continue, Break and Pass

- The `continue` statement is used to skip the rest of the current iteration of a loop.
- The `break` statement is used to exit a loop.
- The `pass` statement is used to do nothing at all.

### 2.4.3.1 continue

[continue](https://www.w3schools.com/python/python_while_continue.asp)

- The `continue` statement is used to skip the rest of the current iteration of a loop.


```python
# continue in a for loop
# skips the rest of the code in the current iteration

for i in range(5):
    if i == 2:  # if i == 2, it will go to the next iteration
        continue
    print(i)  # 0, 1, 3, 4
```

    0
    1
    3
    4



```python
# continue in a while loop
# skips the rest of the code in the current iteration

i = 0
while i < 5:
    if i == 2:  # if i == 2, it will go to the next iteration
        i += 1
        continue
    print(i)  # 0, 1, 3, 4
```

### 2.4.3.2 break

[break](https://www.w3schools.com/python/python_while_break.asp)

- The `break` statement is used to immediately exit a loop.


```python
# break in a for loop
# terminates the loop

for i in range(5):
    if i == 2:  # if i == 2, it will terminate the loop
        break
    print(i)  # 0, 1
```

    0
    1



```python
# break in a while loop
# terminates the loop

i = 0
while i < 5:
    if i == 2:  # if i == 2, it will terminate the loop
        break
    print(i)  # 0, 1
    i += 1
```

    0
    1


### 2.4.3.3 pass

[pass](https://www.w3schools.com/python/python_while_pass.asp)

- The `pass` statement is used to do nothing at all.
- It is used when you don't want to do anything in a particular iteration of a loop.
- We use it as a temporary placeholder when we don't want to do anything at the moment in a particular iteration.


```python
# pass in a for loop
# terminates the loop

for i in range(5):
    pass
```


```python
# pass in a while loop

i = 0
while i < 5:
    pass
```

Sometimes we need to combine different conditions in a loop to skip, break, or do nothing, depending on the singe condition.


```python
# example using break, continue, pass in one loop

for i in range (10):
    if i % 2 == 0:  # skips even numbers
        continue
    elif i == 7:  # exits the loop if i == 3
        break
    print(i)
```

    1
    3
    5


### 2.5. Random Module

https://docs.python.org/3/library/random.html

- The `random` library in Python is used to generate random numbers. The `randint()` function from this library is often used when an integer needs to be randomly selected within a certain range.
- The `randint()` function takes two arguments: the start and the end of the range (both inclusive). It returns a random integer within this range.
<br>
Here's how you can use it:

In this example, `random.randint(1, 10)` will generate a random integer between 1 and 10 (1 and 10 included).


```python
import random

random_number = random.randint(1, 10)
print(random_number)

```


```python
import random

# generate a random number
random_number = random.randint(1, 10)
print(random_number)  # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
```

    9


Here's another example:


```python
import random

for _ in range(5):
    print(random.randint(1, 100))
```

    21
    46
    57
    29
    63


In this example, we generate and print five random integers between 1 and 100.
<br>

The `random` library is not just limited to the `randint()` function. There are also other functions available that provide more flexibility and control over the randomization process.
For example, the `random()` function returns a random floating point number in the range [0.0, 1.0). Here's an example:


```python
import random

random_float = random.random()
print(random_float)
```

    0.6294152416500041


In this code, `random.random()` generates a random float between 0 (inclusive) and 1 (exclusive).
