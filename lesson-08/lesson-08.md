**Testing in Python**

### Introduction

Testing is an essential part of the development process. It allows us to verify that our code is working correctly and catch any errors or bugs before releasing our software. In this lesson, we'll learn how to write tests for our Python code using the `unittest` module and explore the `assert` statement.

### Why Testing is Important

- Catching errors early: Testing allows us to catch errors and bugs early on, which can save us a lot of time and effort in the long run.
- Improved quality: Writing tests ensures that our code is working correctly and meets our expectations.
- Faster development: With a good set of tests in place, we can make changes to our code more confidently, knowing that our tests will catch any errors.

### The `assert` Statement

The `assert` statement is a built-in statement in Python used to, as the name says, assert if a given condition is true or not. If the condition is true, nothing happens, but if it's not true, an error is raised. Although, at first, it may look like the try and except clauses, they are completely different, and assert should not be used for error handling but for debugging and testing reasons.

Here's an example of how to use the `assert` statement:

```python
def add_numbers(a, b):
    assert type(a) == int and type(b) == int, "Both inputs must be integers"
    return a + b

print(add_numbers(2, 3))  # Output: 5
print(add_numbers("2", 3))  # Raises an AssertionError
```

In this example, we're using the `assert` statement to check that both inputs to the `add_numbers` function are integers. If they are not integers, an `AssertionError` is raised.

### Writing Tests

A test is a function that starts with the name `test_` followed by a descriptive name. For example:

```python
import unittest

def test_addition():
    assert 2 + 2 == 4
```

In this example, we're testing whether the addition of 2 and 2 equals 4. We use the `assert` statement to verify this.

### Running Tests

To run our tests, we'll use the `unittest.main()` function. This function will automatically discover and run all the test functions in our code.

Here's an example of how to run our tests:

```python
import unittest

def test_addition():
    assert 2 + 2 == 4

if __name__ == '__main__':
    unittest.main()
```

When we run this code, we'll see the following output:

```
....
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

This means that our test passed successfully!

### Test Cases

A test case is a class that inherits from `unittest.TestCase`. We can use test cases to group related tests together.

Here's an example of how to create a test case:

```python
import unittest

class TestMathFunctions(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(2 + 2, 4)

    def test_subtraction(self):
        self.assertEqual(5 - 3, 2)
```

In this example, we've created a test case called `TestMathFunctions` that contains two test methods: `test_addition` and `test_subtraction`.

### Test Fixtures

A test fixture is a setup and teardown routine that is run before and after each test. We can use fixtures to create a controlled environment for our tests.

Here's an example of how to create a fixture:

```python
import unittest
from tempfile import TemporaryDirectory

class TestMathFunctions(unittest.TestCase):
    def setUp(self):
        self.temp_dir = TemporaryDirectory()

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_addition(self):
        self.assertEqual(2 + 2, 4)

    def test_subtraction(self):
        self.assertEqual(5 - 3, 2)
```

In this example, we've created a fixture that creates a temporary directory before each test and cleans it up after each test.

### Best Practices

- Keep your tests simple and focused on one specific behavior.
- Use descriptive names for your tests.
- Use the `assert` statement to verify the expected behavior.
- Use fixtures to create a controlled environment for your tests.
- Run your tests regularly to catch any errors or bugs early on.

### Conclusion

In this lesson, we've learned how to write tests for our Python code using the `unittest` module and explored the `assert` statement. We've also covered why testing is important, how to set up testing, and some best practices for writing tests. With testing, we can ensure that our code is working correctly and catch any errors or bugs early on.

## 8.2. Project Documentation

- [Readme Guide](https://youtu.be/l1DE7L-4eKQ)
- [How to write a kickass README](https://dev.to/scottydocs/how-to-write-a-kickass-readme-5af9)
- [How to Write a Good README File for Your GitHub Project](https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/)
- [Writing good README files](https://coderefinery.github.io/documentation/writing-readme-files/)
- [How to create a stunning README.md](https://medium.com/@sagarganiga468/how-to-create-a-stunning-readme-md-edf1c74b6a46)
  - [Sample README.md](https://github.com/SagarGaniga/How-to-Create-A-Stunning-README.md)

### 8.2.1. Why Documentation Is Important

The `README.md` file is the first file that is visible to others when you push your project to a GitHub repository. It is a great way to introduce your project to others and show them how to use your code. It also helps others understand your project. You can easily say that a `README.md` is a calling card for your project. It should be a summary of your project and its features.

For many smaller and mid-size project, this is a good enough documentation. For larger projects, it should be accompanied by a detailed documentation. Nevertheless, if we browse through many of the open source projects, we can find that most of them have a good and complete `README.md` file.

The `README.md` file is also a great way to document our project from it's conception to the final product for ourselves. It will happen in the future, that we would return to one of our projects, only to find ourselves reading the code and trying to understand what it does.

### 8.2.2. MarkDown Syntax
- [Writing on GitHub](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github)
- [MarkDown Guide: *Basic Syntax*](https://www.markdownguide.org/basic-syntax/)
- [MarkDown Guide: *Cheet Sheet*](https://www.markdownguide.org/cheat-sheet/)
- [John Gruber: *MarkDown: Basics*](https://daringfireball.net/projects/markdown/basics)

`README.md` file is written in `MarkDown`. Markdown is a simple, easy-to-use syntax for formatting text. It is a great way to document our project. We will not got too much into details here. Here is a demonstration of the basic syntax of `MarkDown`:

Here is the Markdown syntax demonstration in two parts:

**Headings**
```
# Heading 1
## Heading 2
### Heading 3
```
**Text Formatting**
```
**Bold text**
*Italic text*
___Underlined text___
```

**Links**
```
[Link to Google](https://www.google.com)
[Link to Google](https://www.google.com "Title of link")

```

**Lists**
- ordered lists
```
1. Item 1
2. Item 2
3. Item 3
```

1. Item 1
2. Item 2
3. Item 3

- unordered lists

```
- Item 1
- Item 2
- Item 3
```

- Item 1
- Item 2
- Item 3

**Code**
For code quotes we use triple backticks. If we want to have syntax highlighting we can write the name of the coding language immediately after the backticks.

\`\`\`python
print("Hello, world!")
\`\`\`

```python
print("Hello, world!")
```

```
| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Cell 1   | Cell 2   | Cell 3   |
|----------|----------|----------|
| Cell 4   | Cell 5   | Cell 6   |
```

```
> This is a quote
> That's all folks!
```

```
Term: Definition
:   Description
```

```
<h1>Heading</h1>
<p>This is a paragraph</p>
```
***Example Outputs***

**Bold text** and *Italic text* are used to emphasize certain words.

[Link to Google](https://www.google.com) and [Link to Google](https://www.google.com "Title of link") are used to create links.


```python
print("Hello, world!")
```


The following table shows the structure of a Markdown document:

| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Cell 1   | Cell 2   | Cell 3   |
| Cell 4   | Cell 5   | Cell 6   |
---

**Quotes**
```
> This is a quote
```

> This is a quote

**Definition lists** are used to define technical terms:

```
Term: Definition
:   Description
```

Term: Definition
:   Description

**Image**
```
![Image Text](link-to-the-image)
```

![Image](https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png)

Finally, **HTML code** is used to format the text:

```html
<h1>Heading</h1>
<p>This is a paragraph</p>
```
<h1>Heading</h1>
<p>This is a paragraph</p>


### 8.2.3. How to Write a Good README File for Your GitHub Project

For the documentation, we can have more different `md`, but the one that is the primary is `README.md`. When we put that file in the root directory of our project, it is rendered on our GitHub project repo. GitHub automatically converts our headings into working links and it makes it easier to navigate through our project. It also can automatically generate the table of contents.

Here is the list of sections and brief descriptions of each:

**1. Introduction**
A brief description of the project, including its purpose and main features.

**2. Overview**
A high-level overview of the project, including its features, functionalities, and technologies used.

**3. Flowchart**
A visual representation of the project's workflow, showing the steps involved in using the project.

**4. Technologies**
A list of the technologies and dependencies used in the project, including libraries, frameworks, and tools.

**5. Getting Started**
Step-by-step instructions for getting started with the project, including cloning the repository, installing dependencies, and creating a `.env` file.


**6. Usage**
Instructions for using the project, including step-by-step guides and configuration options.

**7. Changelog**
A list of significant changes made to the project, including bug fixes, new features, and improvements.


**8. Contributing**
Instructions for contributing to the project, including how to fork the repository, create a new branch, and submit a pull request.

**9. License**
Information about the license under which the project is released, including terms and conditions.

**10. Credits**
Acknowledgments to contributors and sponsors who have helped make the project possible.

**11. Links**
Additional resources and links for more information about the project, including its website, documentation, and social media channels.

Here is the provided sample you can use: [Sample README.md](./README-sample.md)

### 8.2.4. Some Auxiliary Resources

- [GitHub Markdown Guide](https://guides.github.com/features/mastering-markdown/) - a good MarkDown Tutorial from GitHub
- [Readme.so](https://readme.so/) - as the website says - the easiest way to create a README. It is an interactive `README.md` editor.
- [Example of a good GitHub README](https://github.com/SagarGaniga/How-to-Create-A-Stunning-README.md) - a good README example with different elements.
- VS Code extension for Automatically Generated Markdown Table of Contents - [Auto Markdown TOC](https://marketplace.visualstudio.com/items?itemName=joffreykern.markdown-toc)

## 8.3. Project Directory Structure

- [The Hitchhiker's Guide to Python: *Structuring Your Project*](https://docs.python-guide.org/writing/structure/)
- [Tech with Tim: *How To Structure A Programming Project*](https://youtu.be/CAeWjoP525M)
- [Programming 101: File Structures](https://medium.com/@deshayk/programming-101-file-structures-2e4699ac0fc2)
- [Guide to Python Project Structure and Packaging](https://medium.com/@joshuale/a-practical-guide-to-python-project-structure-and-packaging-90c7f7a04f95)

### 8.3.1. Recommended Project Structure

There are different ways how to organise your project and you can check the links above to learn more. For your final project, I would propose the following structure:


>.
├── app.py
├── aux
│   ├── end.txt
│   ├── highscores.json
│   ├── highscores.py
│   ├── intro.txt
│   ├── questions.json
│   ├── quiz.py
│   └── retrieve_api.py
├── docs
│   ├── img
│   │   └── image.png
│   └── pdf
│       └── doc.pdf
├── README.md
└── requirements.txt

- in the project's root directory (`/`):
  - `app.py` - is the main file of your project
  - `README.md` - is our main project documentation file
  - `requirements.txt` - contains all the dependencies of your project
- `aux/` - directory, contains auxiliary scripts and data files
- `docs/` - directory, contains documentation files (images, PDFs, etc.)

### 8.3.2. Importing Modules from different directories

- [Python Import Module From Different Directory](https://www.geeksforgeeks.org/python-import-module-from-different-directory/)

- general syntax:
  - `from directory_name import module_name` - import module from a directory. We call then functions by using `module_name.function_name()`
  - `from directory_name.subdirectory_name import module_name` - import module from a subdirectory. We call then functions by using `module_name.function_name()`
  - `from directory_name.module_name import function_name` - import specific function from a module in a directory
  - `from directory_name.module_name import *` - import all functions from a module in a directory

If we take into consideration the structure we presented in [Recommended Project Structure](#831-recommended-project-structure), we can import modules from a subdirectory this way.

```python
import aux.highscores as highscores
```
- in this case we need to call functions by using `highscores.function_name()`
or

```python
from aux import highscores
```
- also, in this case we need to call functions by using `highscores.function_name()`
- 
or

```python
from aux.highscores import *
```

- in this case we need to call functions by using only `function_name()`


