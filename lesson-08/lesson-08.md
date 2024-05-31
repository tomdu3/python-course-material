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
- 

