# Python - Lesson 02

## Interpreted language
Python is an **interpreted language**. This means that it inherits all the described advantages and disadvantages. Of course, it adds some of its unique features to both sets.

Python is a **scripting language**. The interpreter reads the source code in a way that is common in Western culture: from top to bottom and from left to right. There are some exceptions - they'll be covered later in the course. 


### Advantages

*The execution of the translated code is usually faster;
*only the user has to have the compiler – the end-user may use the code without it;
*the translated code is stored using machine language – as it is very hard to understand it, your own inventions and programming tricks are likely to remain your secret.

### Disadvantages

*the compilation itself may be a very time-consuming process – you may not be able to run your code immediately after making an amendment;
*you have to have as many compilers as hardware platforms you want your code to be run on.

### What does the interpreter do?

Let's assume once more that you have written a program. Now, it exists as a computer file: a computer program is actually a piece of text, so the source code is usually placed in text files.

Note: it has to be pure text, without any decorations like different fonts, colors, embedded images or other media. Now you have to invoke the interpreter and let it read your source file.

The interpreter reads the source code in a way that is common in Western culture: from top to bottom and from left to right. There are some exceptions - they'll be covered later in the course.

First of all, the interpreter checks if all subsequent lines are correct (using the four aspects covered earlier).

If the compiler finds an error, it finishes its work immediately. The only result in this case is an error message.


## Python and Terminal (Command Line)

In the terminal (or on Windows) you can execute Python code. The interpreter reads the code in the same way as it would in the shell. Let's try to execute some code in the terminal.

- let us check the python version

```bash
python --version
```

or

```bash
python3 -V
```

To execute a script of Python code, we need to use the special command `python` or `python3` (depending on the version) and the name of the script. 

```bash
python hello.py
```


## Python Shell
Python has a shell. It's a special environment, which allows you to execute Python commands and see the results immediately. It's a very good place to test your code and to learn Python.

The shell is also a very good place to test small code snippets, to check how some functions work, or to experiment with new features.

Let us try to execute some code in the shell.


To enter the Python shell, we need to use the special command `python3`.

```bash
python3
```
or

```bash
python
```

To exit the Python shell, we need to use the special command `exit()`.

```python
exit()
```

