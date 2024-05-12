# Lesson 3 - Complex Data Structures in Python: Lists

## Excursus I - Flowchart Diagram

- Flowchart diagram is a visual representation of the flow of data in a program
- It is used to visualize the flow of data in a program
- Software Developers use flowchart to map the flow of data in a program and the way certain actions should be performed.
- Usually, flowchart can be modified over the course of the development of the program, when some more functionalities are added, updated, or removed.
<br>

- We will use [`drawio.io`](https://drawio-app.com/) to draw flowchart diagram

- Here are some instructions **Version 1**: [How to create flowcharts in draw.io](https://drawio-app.com/blog/flowcharts/)
**The different shapes used in flowcharts**

![Shapes for flowcharts](./docs/drawio-flowchart-shapes.png)

- **Start/End** – circles are sometimes used to indicate start and end points.
- **Steps** – a rectangle or square (often with rounded corners).
- **Decisions** – usually represented by a diamond.
- **A sub-process** – a normal step shape with borders on the left and right edges.
- **Manual input** – where a step requires someone to enter something manually, you can use this step ‘rectangle’ with a sloped ‘roof’.
- **Document or multiple documents** – where a step results in one or more documents, you can use these shapes
- **Data** – a parallelogram is used to indicate where information enters or leaves the process. For example, when an invoice is sent to a customer.
- **Delay** – this is used to show there is a delay before the next step.
- **Preparation** – used to indicate there are setup conditions required for the next step.

- Instruction - **Version 2**: [Draw a basic flow chart in draw.io
](https://www.drawio.com/doc/getting-started-basic-flow-chart)

Here are many different shapes used to visualise processes in a flow chart.

![Shapes for flowcharts](./docs/flow-chart-shapes.png)
- **Rectangle** - Basic steps in your process.
- **Diamond (rhombus)** - Decisions, usually yes/no questions, that split the process into two or more branches.
- **Circle or oval** - Optional start and stop points in your process.
- **Parallelogram** - Input or output, where your process needs or gives information to an external party or system.
- **Cylinder** - Disk drives, used to indicate that data is stored during that step in the process.
- **Rectangle with a wavy bottom line** - Documents that are produced as a result of a process step.

### Excursus - Example Flowchart Diagram

- Let us see a simple Python code:


```python
a = 10
b = 20
if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")
```

- We can see this flowchart in the image below:

![Flowchart](./docs/Python-example.png)

[Link to the diagram](https://drive.google.com/file/d/1ddxGKsL0oe2jDy19ji2BnvzF_ZWIUEsf/view?usp=sharing)


- Here's an interesting link about using `Draw.io` and `VS Code`: [Flow charts and process diagrams with Draw.io & VS Code](https://paulvanderlaken.com/2020/12/22/draw-io-flow-chart-process-diagram-vscode/)

## 3.1 - Complex Data Structures - Lists

- Complex Data Structures in Python are: **Lists**, **Tuples**, **Sets**, **Dictionaries**.
- To these we should add **strings**, because they are sequences of characters, but we prefere to categorize them as basic data structures.
- Generally, we understand as a Complex Data Structure a type of data that contains more different type of data.
- They can be sequential or contain sequential data.

<br>

**Lists**

- **Lists are mutable and ordered collections of items.**

<br>

- Lists are used to store multiple items in a single variable.
- The items in a list do not need to be of the same data type.
- it is an ordered collection or sequence of items. Therefore, we can access items by referring to their position in the list.
- We can use indexing to access items in a list.
- We put elements inside square brackets: `[ el1, el2, el3 ]`


```python
# list with the same type of elements
shopping_list = ['bread', 'milk', 'oil', 'eggs']
math_marks = [78, 89, 90, 100]
hiking_coordinates = [(40.7128, -74.0060), (34.0522, -118.2437)]
voting_for_president_Tom = [True, False, True, True, False]

# lists with different types of elements
mixed_list = ['a', 10, 10.5, True]
```

### 3.2 **Accessing the items in a list**
- we use the index number and square bracket notation to access the items in a list
- the index number starts from 0

Syntax:
- `list_name[index_number]`


```python
  shopping_list = ['bread', 'milk', 'oil', 'eggs']
  print(shopping_list[0])
  print(shopping_list[1])
  print(shopping_list[2])
  print(shopping_list[3])
```

    bread
    milk
    oil
    eggs



```python
# negative index
shopping_list = ['bread', 'milk', 'oil', 'eggs']

print(shopping_list[-1])
print(shopping_list[-2])
print(shopping_list[-3])
print(shopping_list[-4])
```

    eggs
    oil
    milk
    bread


- if we use an index number that is out of the range of the list, we will get an error message


```python
# out of range error
friends_list = ['Tom', 'Jerry', 'Spike']

print(friends_list[3])
```


    ---------------------------------------------------------------------------


    IndexError                                Traceback (most recent call last)


    Cell In[3], line 4


          1 # out of range error


          2 friends_list = ['Tom', 'Jerry', 'Spike']


    ----> 4 print(friends_list[3])


    


    IndexError: list index out of range


- we can also use slicing to get the part of the list
- slicing can be also used to reverse the list


```python
# slicing
shopping_list = ['bread', 'milk', 'oil', 'eggs']

print(shopping_list[0:2])
```

    ['bread', 'milk']


- we can also use negative indexes


```python
# reverse slicing - reversing of the list
shopping_list = ['bread', 'milk', 'oil', 'eggs']

print(shopping_list[::-1])
```

    ['eggs', 'oil', 'milk', 'bread']


### 3.3 **Changing the value of an item**
- we can change the value of an item in a list
- we use the index number to change the value of an item


```python
# change values
shopping_list = ['bread', 'milk', 'oil', 'eggs']
print(shopping_list)
shopping_list[0] = 'butter'
print(shopping_list)
  
```

    ['bread', 'milk', 'oil', 'eggs']
    ['butter', 'milk', 'oil', 'eggs']


### 3.4 **len() function**
- we can use the len() function to get the length of the list
- it returns the number of items in the list
- syntax: `len(list_name)`


```python
# length of a list

shopping_list = ['bread', 'milk', 'oil', 'eggs']

print(len(shopping_list))

```

    4


### 3.5 **Removing items from a list**

- `clear()` function removes all the items from the list
    - syntax: `list_name.clear()`
- `pop()` function removes the last item from the list and returns it
  - syntax: `list_name.pop()`
  - we can also remove an item by specifying the index number and recieve the removed item
  - syntax: `list_name.pop(index_number)`
- `remove(value)` function removes the item with specified value from the list 
  - syntax: `list_name.remove(value)`
- `del` function removes the item at the specified index, or a slice from the list
  - syntax: `del list_name[index_number]` - removes item
  - syntax: `del list_name[start_index:end_index]` - removes items from start_index to end_index


```python
# clear
shopping_list = ['bread', 'milk', 'oil', 'eggs']

shopping_list.clear()
print(shopping_list)
```

    []



```python
# pop
shopping_list = ['bread', 'milk', 'oil', 'eggs']

shopping_list.pop()
print(shopping_list)
```

    ['bread', 'milk', 'oil']



```python
# remove
shopping_list = ['bread', 'milk', 'oil', 'eggs']

shopping_list.remove('oil')
print(shopping_list)

# example 2 - only first occurrence will be removed
test_marks = [78, 89, 90, 100, 89, 67, 89]

test_marks.remove(89)
print(test_marks)
```

    ['bread', 'milk', 'eggs']
    [78, 90, 100, 89, 67, 89]



```python
# del
shopping_list = ['bread', 'milk', 'oil', 'eggs']

del shopping_list[0]
print(shopping_list)

# example 2
test_marks = [78, 89, 90, 100, 89, 67, 89]

del test_marks[1:3]
print(test_marks)
```

    ['milk', 'oil', 'eggs']
    [78, 100, 89, 67, 89]


### 3.6 **Adding elements to a list**
- `append()` function adds an item to the end of the list
  - syntax: `list_name.append(value)`
- `insert()` function adds an item at the specified index
  - syntax: `list_name.insert(index_number, value)`
  - we can also insert multiple items
  - syntax: `list_name.insert(index_number, value1, value2, value3, ...)`


```python
# append item to a list
shopping_list = ['bread', 'milk', 'oil', 'eggs']

shopping_list.append('chocolate')
print(shopping_list)
```

    ['bread', 'milk', 'oil', 'eggs', 'chocolate']



```python
# insert item to a list
shopping_list = ['bread', 'milk', 'oil', 'eggs']

shopping_list.insert(0, 'chocolate')  # inserts 'chocolate' at index 0, and moves the rest of the items to the right
print(shopping_list)
```

    ['chocolate', 'bread', 'milk', 'oil', 'eggs']


### 3.7 **Checking if an item is in a list**
- `in` keyword - if the value is in the list
  - syntax: `value in list`
- `not in` keyword - if the value is not in the list
  - syntax: `value not in list`


```python
# check value in the list
shopping_list = ['bread', 'milk', 'oil', 'eggs']

if 'oil' in shopping_list:
    print('yes, the oil is in the list')
else:
    print(shopping_list)
    print('oh, no! you have forgotten to buy oil')
    # shopping_list.append('oil')
    # print(shopping_list)
    # print('we have added oil to your list. now it is all fine!')
    # print(shopping_list)
```

    yes, the oil is in the list


### 3.8 **Sorting a list**

- `sort()` function sorts the list
  - syntax: `list_name.sort()`
- `reverse()` function reverses the list
  - syntax: `list_name.reverse()`
- these functions do not return any value, but they change the original list


```python
# sort

shopping_list = ['bread', 'milk', 'oil', 'eggs']
shopping_list.sort()
print(shopping_list)

# reverse with sort
shopping_list.sort(reverse=True)
print(shopping_list)
```

    ['bread', 'eggs', 'milk', 'oil']
    ['oil', 'milk', 'eggs', 'bread']



```python
# reverse()

shopping_list = ['bread', 'milk', 'oil', 'eggs']
shopping_list.reverse()
print(shopping_list)
```

    ['eggs', 'oil', 'milk', 'bread']


- if we want to sort the list, but don't want to change the original list we can use sorted() function
  - syntax: `sorted(list_name)`
- if we want to reverse the list, we can use `sorted(list_name, reverse=True)`


```python
# sorted

shopping_list = ['bread', 'milk', 'oil', 'eggs']

print("sorted list:", sorted(shopping_list))
print("original list:", shopping_list)


# reverse with sorted

print("reverse sorted list:", sorted(shopping_list, reverse=True))
print("original list:", shopping_list)
```

    sorted list: ['bread', 'eggs', 'milk', 'oil']
    original list: ['bread', 'milk', 'oil', 'eggs']
    reverse sorted list: ['oil', 'milk', 'eggs', 'bread']
    original list: ['bread', 'milk', 'oil', 'eggs']


### 3.9 **Finding the index of an item**

- `index()` function returns the index of the first occurrence of the specified value
  - syntax: `list_name.index(value)`
- `count()` function returns the number of times the specified value appears in the list
  - syntax: `list_name.count(value)`


```python
# find the index of an item
shopping_list = ['bread', 'milk', 'oil', 'eggs']

# print(shopping_list.index('oil'))
# print(shopping_list.index('milk'))
# print(shopping_list.index('bread'))
# print(shopping_list.index('eggs'))

# find and index of a repeating item
test_marks = [78, 89, 90, 100, 89, 67, 89]

print(test_marks.index(89))

# if we want to find a second occurence, we need to start from the index that comes after the first occurence
print(test_marks.index(89, 2))

# if we want to find the last occurence
print(test_marks.index(89, -2))
```

    1
    4
    6


### 3.10 **Looping/iterating through a list**

- we can loop/iterate through a list by using a for loop in different ways:
  - looping through the indices of the list:
    ```python
    for index in range(len(my_list)):
        print(my_list[index])
    ```

  - looping through the list items:
    ```python
    for item in my_list:
        print(item)
    ```

  - looping through the list items and indices - we use a function called `enumerate()`. It gives us the index and the value:
    ```python
    for index, item in enumerate(my_list):
        print(index, item)
    ```


```python
# looping through indices of a list

shopping_list = ['bread', 'milk', 'oil', 'eggs']

for i in range(len(shopping_list)):
    print(i, shopping_list[i])
```

    0 bread
    1 milk
    2 oil
    3 eggs



```python
# looping through a list items

shopping_list = ['bread', 'milk', 'oil', 'eggs']

for item in shopping_list:
    print(item)
```

    bread
    milk
    oil
    eggs



```python
# looping through a list items and indices

shopping_list = ['bread', 'milk', 'oil', 'eggs']

for i, item in enumerate(shopping_list):
    print(i, item)
```

    0 bread
    1 milk
    2 oil
    3 eggs


- we can also loop through a list with a while loop
    ```python
    index = 0

    while index < len(my_list):
        print(my_list[index])
        index += 1
    ```

### 3.10.a **Paralel loops**

Sometimes we need to loop through two or more lists in parallel.
- we can use the `zip()` function to loop through lists in parallel
  - syntax: `zip(list1, list2)`
  - if the lists have different lengths, the longer list will be truncated


```python
# loop through two lists together

shopping_list = ['bread', 'milk', 'oil', 'eggs']
test_marks = [78, 89, 90, 100, 89, 67, 89]

for item, mark in zip(shopping_list, test_marks):
    print(item, mark)
print()
# loop through three lists of different lengths

shopping_list = ['bread', 'milk', 'oil', 'eggs']
test_marks = [78, 89, 90, 100, 89, 67, 89, 89]
validation_marks = [True, True, True, True, False, True, True, False]

for item, mark, valid in zip(shopping_list, test_marks, validation_marks):
    print(item, mark, valid)

```

    bread 78
    milk 89
    oil 90
    eggs 100
    
    bread 78 True
    milk 89 True
    oil 90 True
    eggs 100 True


### 3.11 **Copying a list**

- there's one issue with the lists. Let us consider the following code:


```python
a = 3
b = a
print(f"a={a}, b={b}")

a = 5
print(f"a={a}, b={b}")
```

    a=3, b=3
    a=5, b=3


If we do the same with a list, it will not work the same:


```python
list_a = [1, 2, 3]
list_b = list_a
print(f"list_a={list_a}, list_b={list_b}")

list_a[0] = 5
print(f"list_a={list_a}, list_b={list_b}")
```

    list_a=[1, 2, 3], list_b=[1, 2, 3]
    list_a=[5, 2, 3], list_b=[5, 2, 3]


What happened here? The problem is that the list `list_b` is a reference to the list `list_a`. Therefore, if we change the value of `list_a[0]` then the value of `list_b` will also change.
If we wish to take the same list and then change the value of the new variable that contains the list, without changing the original list, we can use the `copy()` function:

- syntax: `list_name.copy()`


```python
# copy of a list

list_a = [1, 2, 3]
list_b = list_a.copy()
print(f"list_a={list_a}, list_b={list_b}")

list_a[0] = 5
print(f"list_a={list_a}, list_b={list_b}")
```

    list_a=[1, 2, 3], list_b=[1, 2, 3]
    list_a=[5, 2, 3], list_b=[1, 2, 3]


- We can also make a copy of a list with the `list()` function:
- syntax: `list(list_name)`


```python
# copy a list with list()

list_a = [1, 2, 3]
list_b = list(list_a)
print(f"list_a={list_a}, list_b={list_b}")

list_a[0] = 5
print(f"list_a={list_a}, list_b={list_b}")
```

    list_a=[1, 2, 3], list_b=[1, 2, 3]
    list_a=[5, 2, 3], list_b=[1, 2, 3]


- there's another way to make a copy of a list. We can use list slicing operator `[:]`:
  - syntax: `list_name[:]`


```python
# copy list with [:]
list_a = [1, 2, 3]
list_b = list_a[:]
print(f"list_a={list_a}, list_b={list_b}")

list_a[0] = 5
print(f"list_a={list_a}, list_b={list_b}")
```

    list_a=[1, 2, 3], list_b=[1, 2, 3]
    list_a=[5, 2, 3], list_b=[1, 2, 3]


### 3.12 **Converting list to string**

- we can convert a list to a string with the `.join()` function:
  - syntax: `"x".join(list_name)` - where `x` is a joing string/character, but only if all elements in the list are strings.


```python
# convert list to a string with join()

list_a = ['1', '2', '3']
list_b = '*'.join(list_a)

print(list_b)
```

    1*2*3


### 3.13 **Converting string to list**

- we can convert a string to a list with the `.split()` function:
  - syntax: `list_name.split("x")` - where `x` is a split string/character. If it is not specified, the default value is any white space.
- we can also specify the number of splits
  - syntax: `list_name.split("x", number_of_splits)`


```python
# split string with split()

list_a = '1*2*3'
list_b = list_a.split('*')
print(list_b)
print(type(list_b))

# split a sentence
sentence = 'I am learning Python'
list_c = sentence.split()
print(list_c)
print(type(list_c))
```

    ['1', '2', '3']
    <class 'list'>
    ['I', 'am', 'learning', 'Python']
    <class 'list'>


### 3.14 **Merging two lists**

- we can merge/concatenate two lists with the `+` operator:
  - syntax: `list_a + list_b`


```python
# concatenation of two lists

list_a = [1, 2, 3]
list_b = [4, 5, 6]

list_c = list_a + list_b
print(list_c)
print(type(list_c))
```

    [1, 2, 3, 4, 5, 6]
    <class 'list'>


- we can also use the `extend()` function:
  - syntax: `list_name.extend(list_name)`


```python
# merging two lists with extend()

list_a = [1, 2, 3]
list_b = [4, 5, 6]

list_a.extend(list_b)
print(list_a)
print(type(list_a))
```

    [1, 2, 3, 4, 5, 6]
    <class 'list'>


### 3.15 **Nested Lists**

- we can create a nested list with the `[]` brackets:
  - syntax: `[ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]`
- to access elements in a nested list we use the `[]` brackets and the indices
- first index is for the outer list, second index is for the inner list


```python
# nested list
my_nested_list = [1, 2, 3, [4, 5, 6], 7, 8, 9]
print(my_nested_list)  # prints the outer list
print(my_nested_list[3])  # prints the list on index 3 of the outer list
print(my_nested_list[3][0])  # prints element on index 0 of the list on index 3 of the outer list
```

    [1, 2, 3, [4, 5, 6], 7, 8, 9]
    [4, 5, 6]
    4

