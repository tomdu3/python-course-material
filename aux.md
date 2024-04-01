## Simplifying the code

```python
while number != 0: and while number:
```

The condition that checks if a number is odd can be coded in these equivalent forms, too:

```python
if number % 2 == 1: and if number % 2:
```

## Using counter in a loop
```python
counter = 5
while counter != 0:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)
```

different approach:

```python
counter = 5
while counter:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)
```

## Challenge

Scenario
A junior magician has picked a secret number. He has hidden it in a variable named secret_number. He wants everyone who runs his program to play the Guess the secret number game, and guess what number he has picked for them. Those who don't guess the number will be stuck in an endless loop forever! Unfortunately, he does not know how to complete the code.

Your task is to help the magician complete the code in the editor in such a way so that the code:

will ask the user to enter an integer number;
will use a while loop;
will check whether the number entered by the user is the same as the number picked by the magician. If the number chosen by the user is different than the magician's secret number, the user should see the message "Ha ha! You're stuck in my loop!" and be prompted to enter a number again. If the number entered by the user matches the number picked by the magician, the number should be printed to the screen, and the magician should say the following words: "Well done, muggle! You are free now."
The magician is counting on you! Don't disappoint him.


# Quiz
Question 1: Create a for loop that counts from 0 to 10, and prints odd numbers to the screen. Use the skeleton below:

for i in range(1, 11):
    # Line of code.
        # Line of code.


Question 2: Create a while loop that counts from 0 to 10, and prints odd numbers to the screen. Use the skeleton below:

x = 1
while x < 11:
    # Line of code.
        # Line of code.
    # Line of code.
 
 Question 3: Create a program with a for loop and a break statement. The program should iterate over characters in an email address, exit the loop when it reaches the @ symbol, and print the part before @ on one line. Use the skeleton below:

for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        # Line of code.
    # Line of code.

Question 4: Create a program with a for loop and a continue statement. The program should iterate over a string of digits, replace each 0 with x, and print the modified string to the screen. Use the skeleton below:

for digit in "0165031806510":
    if digit == "0":
        # Line of code.
        # Line of code.
    # Line of code.

Question 5: What is the output of the following code?

n = 3
 
while n > 0:
    print(n + 1)
    n -= 1
else:
    print(n)

Question 7: What is the output of the following code?

for i in range(0, 6, 3):
    print(i)


## Logical expressions
You may be familiar with De Morgan's laws. They say that:

The negation of a conjunction is the disjunction of the negations.
The negation of a disjunction is the conjunction of the negations.

```python
not (a and b) == (not a) or (not b)
```

```python
not (a or b) == (not a) and (not b)
```

## SECTION SUMMARY
1. Python supports the following logical operators:

and → if both operands are true, the condition is true, e.g., (True and True) is True,
or → if any of the operands are true, the condition is true, e.g., (True or False) is True,
not → returns false if the result is true, and returns true if the result is false, e.g., not True is False.
2. You can use bitwise operators to manipulate single bits of data. The following sample data:

x = 15, which is 0000 1111 in binary,
y = 16, which is 0001 0000 in binary.
will be used to illustrate the meaning of bitwise operators in Python. Analyze the examples below:

& does a bitwise and, e.g., x & y = 0, which is 0000 0000 in binary,
| does a bitwise or, e.g., x | y = 31, which is 0001 1111 in binary,
˜  does a bitwise not, e.g., ˜ x = 240*, which is 1111 0000 in binary,
^ does a bitwise xor, e.g., x ^ y = 31, which is 0001 1111 in binary,
`>>` does a bitwise right shift, e.g., `y >> 1 = 8`, which is 0000 1000 in binary,
`<<` does a bitwise left shift, e.g., `y << 3 = 128`, which is 1000 0000 in binary.
* -16 (decimal from signed 2's complement) -- read more about the Two's complement operation.

## Functions vs. methods
A method is a specific kind of function ‒ it behaves like a function and looks like a function, but differs in the way in which it acts, and in its invocation style.

A function doesn't belong to any data ‒ it gets data, it may create new data and it (generally) produces a result.

A method does all these things, but is also able to change the state of a selected entity.

A method is owned by the data it works for, while a function is owned by the whole code.

This also means that invoking a method requires some specification of the data from which the method is invoked.

It may sound puzzling here, but we'll deal with it in depth when we delve into object-oriented programming.

In general, a typical function invocation may look like this:

result = function(arg)
 
The function takes an argument, does something, and returns a result.

A typical method invocation usually looks like this:

result = data.method(arg)
 
Note: the name of the method is preceded by the name of the data which owns the method. Next, you add a dot, followed by the method name, and a pair of parenthesis enclosing the arguments.

The method will behave like a function, but can do something more ‒ it can change the internal state of the data from which it has been invoked.

You may ask: why are we talking about methods, not about lists?

This is an essential issue right now, as we're going to show you how to add new elements to an existing list. This can be done with methods owned by all the lists, not by functions.