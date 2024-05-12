```python
# Lesson 3
```

## Excursus II
### a. Time Module

- [Time in Python Docs](https://docs.python.org/3/library/time.html)
- [Python Time Moduel in *Real Python*](https://realpython.com/python-time-module/)
- we will use time module only to suspend the execution of the code
- syntax:
  - `import time` - we import the time module
  - `time.sleep(x)` - where `x` is the number of seconds to suspend the execution of the code


```python
# suspend execution of the code for 2 seconds

import time
print('I will sleep for 2 seconds')
time.sleep(2)
print('hello! I am awake!')
```

    I will sleep for 2 seconds
    hello! I am awake!


### b. Datetime Module

- [Datetime in Python Docs](https://docs.python.org/3/library/datetime.html)
- [Python Datetime Module in *GeeksforGeeks*](https://www.geeksforgeeks.org/python-datetime-module/)
<br>
- we will use datetime module only to get the current date and time
- syntax:
  - `import datetime` - we import the datetime module
  - `datetime.datetime.now()` - we get the current date and time
  - `datetime.datetime.now().year` - we get the current year
  - `datetime.datetime.now().month` - we get the current month
  - `datetime.datetime.now().day` - we get the current day
  - `datetime.datetime.now().hour` - we get the current hour
  - `datetime.datetime.now().minute` - we get the current minute
  - `datetime.datetime.now().second` - we get the current second
  - `datetime.datetime.today()` - we get the current date and time
  - `datetime.date.today()` - we get the date only


```python
import datetime
# print today date

print(datetime.date.today())

# print current time
print(datetime.datetime.now())

# print only current time
print(datetime.datetime.now().time())

# print only current hour and minute
print(f'{datetime.datetime.now().time().hour}:{datetime.datetime.now().time().minute:0>2}')

```

    2024-03-27
    2024-03-27 21:06:52.610645
    21:06:52.610717
    21:06

