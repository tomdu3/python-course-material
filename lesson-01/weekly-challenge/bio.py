# task: bio.py
# Create a program that takes the user's first name, last name, age, country, place, hobbies, and money. Then print the following message using the user's input.
# Hello! I am [first name] [last name]. I am [age]. I am living in [place], [country]. I love [hobbies]. It has passed [days] days since I was born. I have [$] in my bank account. (2 decimal places)

# Write your code below this line.
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")
country = input("Enter your country: ")
place = input("Enter your place: ")
hobbies = input("Enter your hobbies: ")
money = input("Enter your money: ")

# calculate days from age
days = int(age) * 365

# print with f string
print(f"Hello! I am {first_name} {last_name}. I am {age}. I am living in {place}, {country}. I love {hobbies}.")
print(f"It has passed {days} days since I was born. I have ${float(money):.3f} in my bank account.")   # 2 decimal places

# # print without f string
# print("Hello! I am " + first_name + " " + last_name + ". I am " + age + ". I am living in " + place + ", " + country + ". I love " + hobbies + ".")
# print("It has passed " + str(days) + " days since I was born. I have $" + money + " in my bank account.")   # 2 decimal places
