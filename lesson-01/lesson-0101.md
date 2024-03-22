# Creating Code with Python

## Introduction

###  Machine language vs. high-level language
*From Cisco Python Essentials 1 Course*
[https://www.netacad.com/courses/programming/pcap-programming-essentials-python](https://www.netacad.com/courses/programming/pcap-programming-essentials-python)

The IL is, in fact, **the alphabet of a machine language**. This is the simplest and most primary set of symbols we can use to give commands to a computer. It's the computer's mother tongue.

Unfortunately, this mother tongue is a far cry from a human mother tongue. We both (computers and humans) need something else, a common language for computers and humans, or a bridge between the two different worlds.

We need a language in which humans can write their programs and a language that computers may use to execute the programs, one that is far more complex than machine language and yet far simpler than natural language.

Such languages are often called high-level programming languages. They are at least somewhat similar to natural ones in that they use symbols, words and conventions readable to humans. These languages enable humans to express commands to computers that are much more complex than those offered by ILs.

A program written in a high-level programming language is called a **source code** (in contrast to the machine code executed by computers). Similarly, the file containing the source code is called the **source file**.

### Compilation vs. Interpretation

**Compilation** – the source program is translated once (however, this act must be repeated each time you modify the source code) by getting a file (e.g., an .exe file if the code is intended to be run under MS Windows) containing the machine code. Now you can distribute the file worldwide; the program that performs this translation is called a compiler or translator.

**Interpretation** – you (or any user of the code) can translate the source program each time it has to be run. The program performing this kind of transformation is called an interpreter, as it interprets the code every time it is intended to be executed. It also means that you cannot just distribute the source code as-is, because the end-user also needs the interpreter to execute it.

| |Compilation|Interpretation |
|---|---|---|
| **Advantages**    | - ✓ the execution of the translated code is usually faster;<br>- ✓ only the user has to have the compiler – the end-user may use the code without it;<br>- ✓ the translated code is stored using machine language – as it is very hard to understand it, your own inventions and programming tricks are likely to remain your secret. | - ✓ you can run the code as soon as you complete it – there are no additional phases of translation;<br>- ✓ the code is stored using programming language, not machine language - this means that it can be run on computers using different machine languages; you don't compile your code separately for each different architecture. |
| **Disadvantages** | - ❌ the compilation itself may be a very time-consuming process – you may not be able to run your code immediately after making an amendment;<br>- ❌ you have to have as many compilers as hardware platforms you want your code to be run on.                              | - ❌ don't expect interpretation to ramp up your code to high speed - your code will share the computer's power with the interpreter, so it can't be really fast;<br>- ❌ both you and the end user have to have the interpreter to run your code.                      |


### What does the interpreter do?

Let's assume once more that you have written a program. Now, it exists as a computer file: a computer program is actually a piece of text, so the source code is usually placed in text files.

Note: it has to be pure text, without any decorations like different fonts, colors, embedded images or other media. Now you have to invoke the interpreter and let it read your source file.

The interpreter reads the source code in a way that is common in Western culture: from top to bottom and from left to right. There are some exceptions - they'll be covered later in the course.

First of all, the interpreter checks if all subsequent lines are correct (using the four aspects covered earlier).

If the compiler finds an error, it finishes its work immediately. The only result in this case is an error message.



You may ask now: which is better? The "compiling" model or the "interpreting" model? There is no obvious answer. If there had been, one of these models would have ceased to exist a long time ago. Both of them have their advantages and their disadvantages.

### What does this all mean for you?

Python is an **interpreted language**. This means that it inherits all the described advantages and disadvantages. Of course, it adds some of its unique features to both sets.
If you want to program in Python, you'll need the **Python interpreter**. You won't be able to run your code without it. Fortunately, **Python is free**. This is one of its most important advantages.
Due to historical reasons, languages designed to be utilized in the interpretation manner are often called **scripting languages**, while the source programs encoded using them are called **scripts**. Okay, let's meet Python.

## Python
### Short History of Python
*From geeksofgeeks.org*
[https://www.geeksforgeeks.org/history-of-python/](https://www.geeksforgeeks.org/history-of-python/)

Python was conceived in the late 1980s by **Guido van Rossum** at Centrum Wiskunde & Informatica (CWI) in the Netherlands as a successor to the ABC language (itself inspired by SETL), capable of exception handling and interfacing with the Amoeba operating system. Its implementation began in December 1989. Van Rossum shouldered sole responsibility for the project, as the lead developer, until 12 July 2018, when he announced his "permanent vacation" from his responsibilities as Python's Benevolent Dictator For Life, a title the Python community bestowed upon him to reflect his long-term commitment as the project's chief decision-maker. In January 2019, active Python core developers elected Brett Cannon, Nick Coghlan, Barry Warsaw, Carol Willing and Van Rossum to a five-member "Steering Council" to lead the project.

The inspiration for the name came from the BBC’s TV Show – ‘Monty Python’s Flying Circus’, as he was a big fan of the TV show and also he wanted a short, unique and slightly mysterious name for his invention and hence he named it Python!

he language was finally released in 1991. When it was released, it used a lot fewer codes to express the concepts, when we compare it with Java, C++ & C. Its design philosophy was quite good too. Its main objective is to provide code readability and advanced developer productivity. When it was released, it had more than enough capability to provide classes with inheritance, several core data types of exception handling and functions. 

### Python 2 vs. Python 3

*From Python 2.7.15 documentation*
[https://docs.python.org/3/whatsnew/3.7.html](https://docs.python.org/3/whatsnew/3.7.html)

Python 2.7 is the last major version in the 2.x series, and as such it will remain in long-term maintenance. The Python 2 language, i.e. Python 2.7, is officially being deprecated (i.e. no longer developed or maintained), the final 2.7 release is expected in 2020. This means that after that date there will be no further official support or bugfixes for Python 2.7.

Python 3.0, also known as "Python 3000" or "Py3K", is the first ever intentionally backwards incompatible Python release. There are more changes than in a typical release, and more that are important for all Python users. Nevertheless, after a long time in development, Python 3.0 was released on December 3, 2008. Many of its major features have been backported to the Python 2.6.x and 2.7.x series.

### Python 3.12.2

*From Python 3.12.2 documentation*
[https://docs.python.org/3/whatsnew/3.12.html](https://docs.python.org/3/whatsnew/3.12.html)

Python 3.12.2, also known as "Python 3.12", is the last major release of the 3.x series, and as such it will remain in long-term maintenance. The Python 3 language, i.e. Python 3.12, is officially being deprecated (i.e. no longer developed or maintained), the final 3.12 release is expected in 2025. This means that after that date there will be no further official support or bugfixes for Python 3.12.


## Downloading And Installing Python

### Downloading Python

*From Python 3.12.2 documentation*
[https://docs.python.org/3/whatsnew/3.12.html](https://docs.python.org/3/whatsnew/3.12.html)

You can download Python from the official Python web site at [https://www.python.org](https://www.python.org). The website provides a download link for the latest version of Python. The website will automatically detect your operating system and provide the correct download link.

### Installing Python

Once you have downloaded the latest Python version, follow the instructions below to install it on your computer.

1. **Windows**: Run the installer (the .exe file you downloaded in the previous step.) Follow the installation wizard to install Python. Be sure to check the box that says "Add Python 3.x to PATH" before you click Install Now.

2. **MacOS**: Follow the instructions in the [MacOS installation guide](https://docs.python.org/3/install/index.html#mac-os-x-installation) to install Python.

3. **Linux**: Follow the instructions in the [Linux installation guide](https://docs.python.org/3/install/index.html#installing-on-linux) to install Python.

### Verifying the Installation

To verify that Python is installed correctly, you can run the command `python --version` in the terminal. The output should be something like `Python 3.12.2` or `Python 3.10.0`. If you see a different version number, or if the command is not found, then Python is not installed correctly.

## Conclusion
Python is a powerful language that can be used to create programs that can be executed on a computer. It can be used to create programs that can be executed on a computer.

## References
*From Python 3.12.2 documentation*
[https://docs.python.org/3/whatsnew/3.12.html](https://docs.python.org/3/whatsnew/3.12.html)

