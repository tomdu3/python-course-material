# Lesson 5a: Working with Modules and Files in Python

![Modules in Python](./docs/modules.png)

- [Python Documentation: *Modules*](https://docs.python.org/3/tutorial/modules.html)
- [Real Python: *Modules*](https://realpython.com/python-modules/)
- [Learn Python: *Python Modules, Packages, Libraries, and Frameworks*](https://learnpython.com/blog/python-modules-packages-libraries-frameworks/)
- [Ajeet Verma: *Understanding the Python Ecosystem: Modules, Packages, Libraries, and Frameworks, with a Focus on TensorFlow*](https://medium.com/@ajeet214/understanding-the-python-ecosystem-modules-packages-libraries-and-frameworks-with-a-focus-on-cb4602b5d31c)

## 5.1. Modules

Modules are a collection of functions that can be used in your program. We have already seen how to import some modules in Python like `random`, `time` and `datetime`.
We have different kind of modules in Python: Built-in modules, third-party modules, and user-defined modules.
- Built-in modules: These modules are pre-installed in the Python interpreter: `sys`, `math`, `os`, `random`, etc.
- Third-party modules: These modules are not pre-installed in the Python interpreter. We need to install them first.
- User-defined modules: These modules are created by us.

## 5.1.1. Importing Modules

- We can import modules using the `import` statement.
  - syntax: `import module_name`
  - `module_name` is the name of the module we want to import.

This way we are importing the whole module with all its functions. To call a function from a module, we need to use the module name followed by the function name.
  - syntax: `module_name.function_name()`
    - example: `random.randint(0, 100)`


```python
# import library
import math

# call the function for the square root of 16
print(math.sqrt(16))
```

    4.0


- The other way is to import all the functions in a module using the `from` statement.
  - syntax: `from module_name import *`
  - `module_name` is the name of the module we want to import.
  - `*` means we want to import all the functions in the module.
  - example: `from random import *`

This way of importing function gives us the opportunity to call a specific function and we don't need to write the module name and function name.
  - syntax: `function_name()`
    - example: `randint(0, 100)`
  - when we import all the functions there could be a problem if we want to call a specific function that could overwrite other functions in the code.


```python
# import all functions from a module
from math import *

# call the square function
print(sqrt(16))
```

    4.0


We can also import import single functions or multiple functions from a module using the `from` and `import` statements.
  - syntax: `from module_name import function_name1, function_name2, function_name3`
  - `module_name` is the name of the module we want to import.
  - `function_name1, function_name2, function_name3` are the names of the functions we want to import.
  - example: `from random import randint, choice`


```python
# import specific functions
from math import sqrt, sin

# call the square function
print(sqrt(16))

# call the sine function
print(sin(90))
```

    4.0
    0.8939966636005579


In order to shorten the syntax, we can import modules with the `as` statement.
  - syntax: `import module_name as new_name`
  - `module_name` is the name of the module we want to import.
  - `new_name` is the new name we want to give to the module.
  - example: `import pandas as pd`


```python
# import datetime module
import datetime as dt

# get today's date
today = dt.date.today()
print(today)
```

    2024-05-19


### 5.1.2. Importing different kinds of modules

#### 5.1.2.1. Built-in modules

Built-in modules are the ones that come in the Python standard library. We can import them using only the `import` statement.
These modules are `sys`, `math`, `os`, `random`, etc.

#### 5.1.2.2. Third-party modules

Third-party modules or packages are the ones that are not included in the standard library. We need to install them first and then import them. To install a third-party module, we need to use the `pip` command. We can find them on the [Python Package Manager - PyPI](https://pypi.org/).
- To install a third-party module, we need to go to the terminal and type `pip install module_name`.
- We can also install a specific version of a module using the `pip` command.
  - syntax: `pip install module_name==version` or `pip install module_name>=version`
  - `module_name` is the name of the module we want to install.
  - `version` is the version number of the module we want to install.



```python
!pip install getch
```

    Requirement already satisfied: getch in /home/tom/anaconda3/envs/myenv/lib/python3.12/site-packages (1.0)


***From the Module Documentation:***

The getch module does single-char input by providing wrappers for the conio.h library functions getch() (gets a character from user input, no output - this is useful for password input) and getche() (also outputs to the screen), if conio.h does not exist, it uses a stub-library using termios.h and other headers to emulate this behaviour:

```python
import getch
# ...
char = getch.getch() # User input, but not displayed on the screen
# or
char = getch.getche() # also displayed on the screen
```

Hint: On Windows, you can use:

```python
import msvcrt
# ...
char = msvcrt.getch()
# or, to display it on the screen
char = msvcrt.getche()
```

as a standard library alternative to this module



```python
import getch

print('press a key to continue...')
getch.getch()
```

The following code is a sophisticated example of using the getch module so that we can get a single character from the user whether they are on Linux, macOS or Windows.


```python
import sys

try:
    import getch  # Importing getch for Linux and macOS
except ImportError:
    if sys.platform.startswith('win'):
        import msvcrt  # Importing msvcrt for Windows
    else:
        raise ImportError("Unsupported platform")

def get_char():
    """
    Get a single character from the user.
    """
    if 'getch' in globals():  # Using getch module
        return getch.getch()
    elif sys.platform.startswith('win'):  # Using msvcrt for Windows
        return msvcrt.getch().decode('utf-8')
    else:
        raise NotImplementedError("get_char is not implemented for this platform")

# Example usage
print("Press any key (q to quit):")
while True:
    char = get_char()
    print("You pressed:", char)
    if char.lower() == 'q':
        break
```

#### 5.1.2.3. User-defined modules

User-defined modules are the ones that we created. They are python files that contain functions and classes. We can import them using only the `import` statement.
- the file needs to be in the same folder as the code we are executing. If we want to import a file in a different folder, we need to specify the folder path.
- syntax: `import module_name` or `from module_name import function_name`


```python
# import module from the same directory
import even

# call the function
print(even.is_even(5))

# import module from a subdirectory (1st)
import modules.prime
print(modules.prime.is_prime(5))

# import module from a subdirectory (2nd)
from  modules import prime
print(prime.is_prime(5))
```

    False
    True
    True


#### 5.1.2.4. Libraries
Libraries are the collections of similar modules grouped together under a single name. We need to install them first with `pip` and then import them.
- The most famous libraries are `numpy`, `pandas`, `matplotlib`, `seaborn`, `scikit-learn`, etc.
- Sometimes, when we need to work with multiple libraries, we need to import them all at once. We can do that using the `from` statement.


```python
!pip install pandas
```


```python
# import pandas
import pandas as pd

# make pandas dataframe from a 2d list
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]] 
df = pd.DataFrame(data, columns=['a', 'b', 'c'])
print(df)

```

        a   b   c
    0   1   2   3
    1   4   5   6
    2   7   8   9
    3  10  11  12


#### 5.1.2.5. requirements.txt file
- [Free Code Camp: *Python Requirements.txt – How to Create and Pip Install Requirements.txt in Python*](https://www.freecodecamp.org/news/python-requirementstxt-explained/)

We can install modules from the [requirements.txt](https://www.python.org/dev/peps/pep-0508/) file. This file is created by the developer of the code in order to provide the list of necessary modules to the user who uses the code.
- syntax: `pip install -r requirements.txt`
- We usually use `requirements.txt` in the same main folder of a complex project. It is not recommended to use it in subdirectories.
- when we are creating this file, we could just add the module names, or we could also give the versions of single modules.
- there's an automated way, that is to use the command `pip freeze > requirements.txt` in the terminal.

- Simple requirements.txt example
```
numpy
pandas
```

- requirements.txt with versions of the packages example
```
numpy==1.21.5
pandas==1.3.5
```



```python
!pip freeze > requirements.txt
!cat requirements.txt
```

## 5.2. Files I/O in Python

If we want to permanently store data, we need to work with files. Files can be of different kind, from a simple text to a complex object like a database, video, audio, etc.

We will first introduce the general approach to a file I/O in Python. The simplest one is to read and write to a file. We will see how to read and write to a text file.

## 5.2.1. Reading from a File

- To read a file we use the `open` function.
- `open` takes two arguments: the name of the file and a mode.
  - syntax: `open(filename, mode)`
  - `filename` is the name of the file
  - `mode` is a string that specifies how the file will be read. The default value is `r` for reading. You can also use `w` for writing. `a` for appending. If we ommit the mode, it will be `r` by default.
- it is important to know that the file exists and that we can access it. Otherwise, we will get an error.
- after we have opened the file, we need to read it. We can do that with different methods:
  - `read` method reads the whole file as a string.
  - `readline` method reads a line. 
  - `readlines` method reads all the lines and returns them as a list.
  - `next` method skips to the next line. It returns the next line and advances the cursor. It is useful when we want to read a file line by line.
- `close` method closes the file. It is very important to always close the file. Otherwise, the file will not be accessible.


```python
# open and read the file
file = open("shakespeare.txt", "r")
print(file.read())
file.close()

# open and read the file line by line
file = open("shakespeare.txt", "r")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

# open and read the file line by line
file = open("shakespeare.txt", "r")
print(file.readlines())
file.close()

```

    SONNET 54
    
    O how much more doth beauty beauteous seem,
    By that sweet ornament which truth doth give!
    The rose looks fair, but fairer we it deem
    For that sweet odour which doth in it live.
    The canker-blooms have full as deep a dye
    As the perfumed tincture of the roses,
    Hang on such thorns and play as wantonly
    When summer's breath their masked buds discloses:
    But, for their virtue only is their show,
    They live unwoo'd and unrespected fade,
    Die to themselves. Sweet roses do not so;
    Of their sweet deaths are sweetest odours made:
    And so of you, beauteous and lovely youth,
    When that shall fade, my verse distills your truth. 
    SONNET 54
    
    
    
    O how much more doth beauty beauteous seem,
    
    ['SONNET 54\n', '\n', 'O how much more doth beauty beauteous seem,\n', 'By that sweet ornament which truth doth give!\n', 'The rose looks fair, but fairer we it deem\n', 'For that sweet odour which doth in it live.\n', 'The canker-blooms have full as deep a dye\n', 'As the perfumed tincture of the roses,\n', 'Hang on such thorns and play as wantonly\n', "When summer's breath their masked buds discloses:\n", 'But, for their virtue only is their show,\n', "They live unwoo'd and unrespected fade,\n", 'Die to themselves. Sweet roses do not so;\n', 'Of their sweet deaths are sweetest odours made:\n', 'And so of you, beauteous and lovely youth,\n', 'When that shall fade, my verse distills your truth. ']


- It seems we have some problems with the printouts. We need to clean them up. Reading the whole file is a good thing for a small text files, but for larger files, we need to read line by line. And when we do that, we should also be aware that some outputs are containg new lines. We need to clean them up using the `strip` function.


```python
# read file until you arrive to the end of the file
file = open('shakespeare.txt', 'r')
for line in file:
    # print(line)  # each line will have a double newline. why?
    print(line.strip())  # remove the double newline
file.close()
```

    SONNET 54
    
    O how much more doth beauty beauteous seem,
    By that sweet ornament which truth doth give!
    The rose looks fair, but fairer we it deem
    For that sweet odour which doth in it live.
    The canker-blooms have full as deep a dye
    As the perfumed tincture of the roses,
    Hang on such thorns and play as wantonly
    When summer's breath their masked buds discloses:
    But, for their virtue only is their show,
    They live unwoo'd and unrespected fade,
    Die to themselves. Sweet roses do not so;
    Of their sweet deaths are sweetest odours made:
    And so of you, beauteous and lovely youth,
    When that shall fade, my verse distills your truth.


- we can read line by line if we use `readlines` method.


```python
# read file using readlines
file = open('shakespeare.txt', 'r')
lines = file.readlines()
for line in lines:
    print(line.strip())
file.close()
```

    SONNET 54
    
    O how much more doth beauty beauteous seem,
    By that sweet ornament which truth doth give!
    The rose looks fair, but fairer we it deem
    For that sweet odour which doth in it live.
    The canker-blooms have full as deep a dye
    As the perfumed tincture of the roses,
    Hang on such thorns and play as wantonly
    When summer's breath their masked buds discloses:
    But, for their virtue only is their show,
    They live unwoo'd and unrespected fade,
    Die to themselves. Sweet roses do not so;
    Of their sweet deaths are sweetest odours made:
    And so of you, beauteous and lovely youth,
    When that shall fade, my verse distills your truth.


- sometimes is easier to read the file by using `with` statement. The syntax is a bit different and is similar to a while loop. All the file operations are done in the `with` statement indentation. The `with` statement closes the file automatically when it is done.
- syntax: `with open(filename, mode) as file:`
- `as` is used to assign the file to a variable.
- `file` is the name of the variable.


```python
# open and read file with with
with open('shakespeare.txt', 'r') as file:
    for line in file:
        print(line.strip())

# open and read file with with
with open('shakespeare.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())

print(file.read())  # this will throw an error, beacuse file is closed now

```

    SONNET 54
    
    O how much more doth beauty beauteous seem,
    By that sweet ornament which truth doth give!
    The rose looks fair, but fairer we it deem
    For that sweet odour which doth in it live.
    The canker-blooms have full as deep a dye
    As the perfumed tincture of the roses,
    Hang on such thorns and play as wantonly
    When summer's breath their masked buds discloses:
    But, for their virtue only is their show,
    They live unwoo'd and unrespected fade,
    Die to themselves. Sweet roses do not so;
    Of their sweet deaths are sweetest odours made:
    And so of you, beauteous and lovely youth,
    When that shall fade, my verse distills your truth.
    SONNET 54
    
    O how much more doth beauty beauteous seem,
    By that sweet ornament which truth doth give!
    The rose looks fair, but fairer we it deem
    For that sweet odour which doth in it live.
    The canker-blooms have full as deep a dye
    As the perfumed tincture of the roses,
    Hang on such thorns and play as wantonly
    When summer's breath their masked buds discloses:
    But, for their virtue only is their show,
    They live unwoo'd and unrespected fade,
    Die to themselves. Sweet roses do not so;
    Of their sweet deaths are sweetest odours made:
    And so of you, beauteous and lovely youth,
    When that shall fade, my verse distills your truth.



    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    Cell In[9], line 12
          9     for line in lines:
         10         print(line.strip())
    ---> 12 print(file.read())  # this will throw an error, beacuse file is closed now


    ValueError: I/O operation on closed file.


### 5.2.2. Writing to a File

- In order to write to a file, we need to open it. We can do that with the `open` function, and we need to use the `write` method.
  - syntax: `open(filename, mode)`
- `mode` can be `w` for writing, `a` for appending. If file already exists, it will be overwritten if we use `w` mode, otherwise it will be appended.
- To write to a file we use the `write` method. It takes one argument: the string we want to write.
  - syntax: `file.write(string)`



```python
# open and write to a file
file = open('test.txt', 'w')
file.write('Hello, World!')
file.close()

# open and append to a file
file = open('test.txt', 'a')
file.write('Hello, World!')
file.close()

# open and read a file
file = open('test.txt', 'r')
print(file.read())
file.close()
```

    Hello, World!Hello, World!


- Notice that with `write()` method, the strings are written to the file as one big string.
- The other methods are `writelines()` and `seek()` to move to a specific position in the file.


```python
# writelines
lines = ['Hello, World!', 'Welcome to Python!', 'Have a nice day!']

file = open('test.txt', 'w')
file.writelines(lines)
file.close()

# seek
file = open('test.txt', 'r')
file.seek(0)
print(file.read())
file.close()
```

    Hello, World!Welcome to Python!Have a nice day!


- If we wish to write properly line by line with `write` method, we need to add `newline` argument at the end of a string(line).
  - syntax: `write(line+'\n')`


```python
# with
with open('test.txt', 'w') as file:
    file.write('Hello, World!\n')
    file.write('Welcome to Python!\n')
    file.write('Have a nice day!\n')

# read
with open('test.txt', 'r') as file:
    print(file.read())
```

    Hello, World!
    Welcome to Python!
    Have a nice day!
    


## 5.2.3. Other File I/O Methods

[Os Module](https://docs.python.org/3/library/os.html)

- Many times there's a need to perform other file I/O operations. We can use the `os` module to do that.
- `os` module provides a lot of methods that we can use to perform other file I/O operations. We will introduce them in the next section.

### 5.2.3.1. Check if File Exists

- We can check if a file exists using the `exists` method.
  - syntax: `os.path.exists(filename)`


```python
import os

# check if a file exists
if os.path.exists('test.txt'):
    print('File exists')
else:
    print('File does not exist')
```

    File exists


### 5.2.3.2. List Files

- We can list all the files in a directory using the `listdir` method.
  - syntax: `os.listdir(directory)`


```python
# list files
print(os.listdir())
```

    ['even.py', 'lesson-0501.ipynb', 'lesson-0502.ipynb', 'modules', 'shakespeare.txt', 'requirements.txt', 'lesson-0501.md', 'lesson-0502.md', 'weekly-challenge', 'lesson-csv.ipynb', 'sample_data.csv', 'test.txt']


### 5.2.3.3. Create Directory

- We can create a directory using the `mkdir` method.
  - syntax: `os.mkdir(directory)`


```python
# create a directory
os.mkdir('test')
```

### 5.2.3.4. Remove Directory

- We can remove a directory using the `rmdir` method.
  - syntax: `os.rmdir(directory)`


```python
# remove a directory
os.rmdir('test')
```

### 5.2.3.5. Change Directory and Get Current Directory

- We can change the current directory using the `chdir` method.
  - syntax: `os.chdir(directory)`
- We can get the current directory using the `getcwd` method.
  - syntax: `os.getcwd()`


```python
# get current directory
print(os.getcwd())

# change directory
os.chdir('..')
print(os.getcwd())
os.chdir('lesson-05')
print(os.getcwd())
```

    /devop/tutoring/python-course-material/lesson-05
    /devop/tutoring/python-course-material
    /devop/tutoring/python-course-material/lesson-05


### 5.2.3.6. Rename File and Rename Directory

- We can rename a file using the `rename` method.
  - syntax: `os.rename(old_filename, new_filename)`
- We can rename a directory using the `rename` method.
  - syntax: `os.rename(old_directory, new_directory)`


```python
# make a new file
with open('test.txt', 'w') as file:
    file.write('Hello, World!\n')

# check if the file exists
print(os.path.exists('test.txt'))

# rename the file
os.rename('test.txt', 'test2.txt')

# check if the old file exists
print(os.path.exists('test.txt'))
# check if the new file exists
print(os.path.exists('test2.txt'))

# remove the new file
os.remove('test2.txt')


# make a new directory
os.mkdir('test_dir')

# check if the directory exists
print(os.path.exists('test_dir'))

# rename the directory
os.rename('test_dir', 'test_dir2')

# check if the old directory exists
print(os.path.exists('test_dir'))

# check if the new directory exists
print(os.path.exists('test_dir2'))

# remove the new directory
os.rmdir('test_dir2')

```

    True
    False
    True
    True
    False
    True


### 5.2.3.7. Other useful methods of `Os` Module

The `os` module in Python provides a variety of methods for interacting with the file system. Here are some useful methods along with examples for each:

- **Listing All Files in a Directory**: Use the `listdir` method.
  ```python
  import os
  
  files = os.listdir('/path/to/directory')
  print(files)
  ```
  Example: If the directory `/path/to/directory` contains files `file1.txt` and `file2.txt`, the output will be `['file1.txt', 'file2.txt']`.

- **Creating a Directory**: Use the `mkdir` method.
  ```python
  import os
  
  os.mkdir('/path/to/new_directory')
  ```
  Example: Creates a new directory named `new_directory` at the specified path.

- **Removing a Directory**: Use the `rmdir` method.
  ```python
  import os
  
  os.rmdir('/path/to/directory_to_remove')
  ```
  Example: Removes the directory named `directory_to_remove` at the specified path. The directory must be empty.

- **Getting the Size of a File**: Use the `getsize` method.
  ```python
  import os
  
  file_size = os.path.getsize('/path/to/file.txt')
  print(file_size)
  ```
  Example: If `file.txt` is 1024 bytes, the output will be `1024`.

- **Getting the Time of Last Modification of a File**: Use the `getmtime` method.
  ```python
  import os
  import time
  
  mod_time = os.path.getmtime('/path/to/file.txt')
  print(time.ctime(mod_time))
  ```
  Example: If the file was last modified on May 19, 2024, the output will be `Sun May 19 12:34:56 2024`.

- **Getting the Time of Last Access of a File**: Use the `getatime` method.
  ```python
  import os
  import time
  
  access_time = os.path.getatime('/path/to/file.txt')
  print(time.ctime(access_time))
  ```
  Example: If the file was last accessed on May 19, 2024, the output will be `Sun May 19 12:34:56 2024`.

- **Getting the Time of Creation of a File**: Use the `getctime` method.
  ```python
  import os
  import time
  
  creation_time = os.path.getctime('/path/to/file.txt')
  print(time.ctime(creation_time))
  ```
  Example: If the file was created on May 19, 2024, the output will be `Sun May 19 12:34:56 2024`.

- **Removing a File**: Use the `remove` method.
  ```python
  import os
  
  os.remove('/path/to/file.txt')
  ```
  Example: Removes the file named `file.txt` at the specified path.
```
