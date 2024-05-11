# Lesson 2: Intro
## Data Types - Continuation

Standard Data Types in Python are:

**Simple Data Types**
- int - integer numbers, like: 0, 1, 100, -23, ...
- float - floating point numbers (decimals), like: 0.0, 1.0, 100.0, -23.0, ...
- str - string, like: "hello", "world", "123", ...
- bool - boolean, like: True, False
- NoneType - None


**Complex Data Types**
- list - list of elements, like: [1, 2, 3], ["hello", "world"], ...
- tuple - immutable list, like: (1, 2, 3), ("hello", "world"), ...
- dict - dictionary, like: {"name": "John", "age": 30}, ...
- set - set of unique elements, like: {1, 2, 3}, {"hello", "world"}, ...


We have already seen some of these data types in the previous notebook, especially ints and floats.

## Strings

- Strings are sequences of characters, using the syntax of either single quotes or double quotes.
- Strings are immutable, meaning they cannot be changed after they are created.
- Strings are ordered sequences, meaning each element in the sequence can be accessed using an index represented by the array of numbers.
- Strings can be sliced, concatenated, and formatted.
- Strings can be compared using comparison operators.
- Strings can be formatted using the `format` method or f-strings.
- Strings can be manipulated using methods like `upper`, `lower`, `strip`, `replace`, `split`, `join`, and many others.


```python
# define a string variable
my_string = "Hello, World!"
# we can use single quotes as well
my_string2 = 'Hello, World!'
# print the strings
print(my_string)
print(my_string2)
```

    Hello, World!
    Hello, World!



```python
# let us print the length of the string
# we can use len() function to find the length of the string
print(len("Tomislav"))  # prints 8
print(len(my_string))  # prints 13
```

    8
    13


- We can use the index operator [] to access an item in a string
- The index operator returns the character at the specified position
- The index must be an integer
- Negative indices count from the end of the string
- The index must be in the range 0 to len(string) - 1

![String indexing](https://res.cloudinary.com/practicaldev/image/fetch/s--A7oqOWqx--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/1wr90mjnil60r7226bgq.png)




```python

""" 'Hello' is a string with 5 characters (length is 5)
The indices and characters are:
0: H
1: e
2: l
3: l
4: o
"""
word = 'Hello'
# print the first character of the string
print(word[0])  # prints H  -> we could also do it like: 'Hello'[0]
# print the last character of the string
print(word[-1])  # prints o
# print the character at index 3
print(word[3])  # prints l

```

    H
    o
    l


## Slicing Strings
When we take only a part of a string, we are slicing it. We can use the slice operator `:` to get a range of characters from the string.
When slicing, the first index is included, while the last given index is excluded.
![Slicing strings](https://prepinstadotcom.s3.ap-south-1.amazonaws.com/wp-content/uploads/2020/07/Slicing-in-python.webp)


```python
# slicing
s = 'hello world'
print(s[2:])  # prints llo world
print(s[:5])  # prints hello
print(s[2:5])  # prints llo
print(s[-5:])  # prints world
print(s[:-5])  # prints hello

# slicing with step
print(s[::2])  # prints hlowrd
print(s[1::2])  # prints el ol
print(s[::-1])  # prints dlrow olleh - this is reversing a string
# reversing a string with step -2
print(s[::-2])  # prints dlrow olleh


```

    llo world
    hello
    llo
    world
    hello 
    hlowrd
    el ol
    dlrow olleh
    drwolh


## Concatenate Strings
We can concatenate strings using the `+` operator. What it does is it joins the two strings together.
We can also use the `*` operator to repeat a string a given number of times.
Let us see some examples.


```python
# define two string variables and concatenate them
f_name = 'Mark'
l_name = 'Twain'

full_name = f_name + l_name
print(full_name)  # prints MarkTwain
# is this what we wanted? No, we need a space between the first and last name
full_name = f_name + ' ' + l_name
print(full_name)  # prints Mark Twain

```

    MarkTwain
    Mark Twain


**Multi Line Strings**
- We can create multi-line strings using triple quotes `'''` or `"""`.
- We can also use the escape character `\n` to create multi-line strings.


```python
# multi-line string using triple quotes
multiline_string = '''This is a
multiline string.
As you can see, it spans
multiple lines.
'''
print(multiline_string)
```

    This is a
    multiline string.
    As you can see, it spans
    multiple lines.
    


**Escaping Characters**
- We can use the escape character `\` to escape characters that have a special meaning in Python, like `"` or `\`.
- We can also use the escape character `\` to create new lines, tabs, and other special characters.
  - Examples: `\\`, `\'`, `\"`, `\n`, `\t`, ...

**<p style="color:red;">Attention:</p>**
- When we are using single quotes `'` to define a string, we can use double quotes `"` inside the string without escaping them.
- When we are using double quotes `"` to define a string, we can use single quotes `'` inside the string without escaping them.
- When we are using triple quotes `'''` or `"""` to define a string, we can use both single and double quotes inside the string without escaping them.
- We can also use the escape character `\` to escape the quotes inside the string, e.g. `\'`, `\"`.


```python
# escape characters
name = 'Hermione'
print('My name is \\', name )  # prints My name is \ Hermion
print('My name is \n', name)  # prints My name is and then goes to the next line and prints my name

print('My name is \'Tomislav\'')  # prints My name is 'Tomislav'
print('My name is "Tomislav"')  # prints My name is "Tomislav"
print('My name is \t', name)  # prints My name is <tab space> Hermione
```

    My name is \ Hermione
    My name is 
     Hermione
    My name is 'Tomislav'
    My name is "Tomislav"
    My name is 	 Hermione


## Printing Strings, numbers and string formatting

- We can use the `print` function to print strings, numbers, and other objects.
- We can use the `+` operator to concatenate strings and the `*` operator to repeat strings.
- But, we cannot concatenate strings with numbers or other objects.
- if we want to combine strings with numbers, we need first to convert the numbers to strings using the `str` function.


```python
name = 'Charles Dickens'
age = 58
print(name + ' is ' + str(age) + ' years old')  # prints Charles Dickens is 58 years old
```

    Charles Dickens is 58 years old


- if we use comma to separate the strings and numbers in the `print` function, it will automatically add a space between them. Therefore, we don't need to add a space manually, and we don't have to convert numbers to strings.


```python
print(name, 'is', age, 'years old.')
```

    Charles Dickens is 58 years old.


- we can use the formatting string or f-string to format strings and numbers in a more readable way.
- that way, we can use placeholders `{}` inside the string, and then pass the values to be formatted as arguments to the `f` string.


```python
print(f'Hello, {name}. You are {age} years old.')
```

    Hello, Charles Dickens. You are 58 years old.


## String Methods

Strings have many methods that can be used to manipulate and format them:
- `upper`, `lower`, `capitalize`, `title`, `swapcase`
- `strip`, `lstrip`, `rstrip`
- `replace`, `count`
- `find`, `index`
- `startswith`, `endswith`
- `split`, `join`
- `format`
- `isalnum`, `isalpha`, `isdigit`, `isnumeric`, `isdecimal`, `isspace`, `islower`, `isupper`, `istitle`, `isidentifier`, `isprintable`
- `encode`, `decode`
- `zfill`
- `center`, `ljust`, `rjust`
- `expandtabs`

We will not go through all of them (there are too many), but we will see some of the most important ones.


```python
title = 'this is a nice title of a book'
title2 = 'NOBODY SHOULD READ THIS BOOK'

# upper
print(title.upper())
# lower
print(title2.lower())
# capitalize
print(title.capitalize())
# title
print(title.title())

# startswith
print(title.startswith('this'))  # prints True
print(title.startswith('This'))  # prints False

# count
print(title.count('i'))  # prints 4
```

    THIS IS A NICE TITLE OF A BOOK
    nobody should read this book
    This is a nice title of a book
    This Is A Nice Title Of A Book
    True
    False
    4


Some formating perks


```python
# we can print a number with commas for thousands separator
print(f'{123456789:,}')  # prints 123,456,789
# we can print a number with commas for thousands separator and decimal separator
print(f'{123456789:,.2f}')  # prints 123,456,789.00

```

    123,456,789
    123,456,789.00


---

### F-string

F-string is an advanced version of the `format` method. It allows us to format strings and numbers in a more readable way.
- We can use the `f` or `F` prefix before the string.
- Then, we can use placeholders `{}` inside the string, and then pass the values to be formatted as arguments to the `f` string.
- We can use the `:=^10` specifier(here `=`) to align the string to the center and fill it with spaces to the left and right (here 10, but it can be any number).
- to center the string on the left we use `:=<10` and to the right we use `:=>10`



```python
name = 'Hermione'
age = 58
print(f'Hello, {name}. You are {age:-^10} years old.')
print(f'Hello, {name}. You are {age:=<10} years old.')
print(f'Hello, {name}. You are {age:*>10} years old.')

```

    Hello, Hermione. You are ----58---- years old.
    Hello, Hermione. You are 58======== years old.
    Hello, Hermione. You are ********58 years old.


- We can use f-string to output the values of the expressions in curly brackets.


```python
# f-string with expressions
name = 'Hermione'
age = 58
print(f'Hello, {name}. You are {age*2} years old.')

```

    Hello, Hermione. You are 116 years old.


### Multiline Strings

- We can use triple quotes to create multiline strings.
- F-strings can also be multiline.


```python
# multiline strings

multiline_string = '''This is a
multiline string.
As you can see, it spans
multiple lines.
'''
print(multiline_string)
```

    This is a
    multiline string.
    As you can see, it spans
    multiple lines.
    



```python
# multiline f-string
name = 'Hermione'
age = 58
print(f'''Hello, {name}.
You are {age} years old.''')
```

    Hello, Hermione.
    You are 58 years old.


### Strings and Numbers

When we are combining strings and numbers in a print statemente, we have to convert the numbers to strings using the `str` function. We cannot concatenate strings with numbers.


```python
# printing strings and numbers
print('Hello, World!')  # prints Hello, World!
print('Hello, World!', 123)  # prints Hello, World! 123
print('Hello, World!'+ 123)  # throws error
```

    Hello, World!
    Hello, World! 123



    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In[17], line 4
          2 print('Hello, World!')  # prints Hello, World!
          3 print('Hello, World!', 123)  # prints Hello, World! 123
    ----> 4 print('Hello, World!'+ 123)  # throws error


    TypeError: can only concatenate str (not "int") to str



```python
print('Hello, World!'+ str(123))  # prints Hello, World!123
```

    Hello, World!123


But we can "multipy" strings and numbers by using operator `*`. It is not multiplication in mathematical sense. It is merly a concatenation of the same string by `n` times.


```python
# print twice 'Hello world!'
print('Hello, World!')
print('Hello, World!')

# or
print('Hello, World!\n'*2)  # prints Hello, World! two times - here we added a new line character
```

    Hello, World!
    Hello, World!
    Hello, World!
    Hello, World!
    

