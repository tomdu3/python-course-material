numbers = [4, 5, 1, 34, 100, -1, -20, 7]

words = ['Ada', 'Loveless', 'atom', 'eon', 'p', '01', '007']


# sorting numbers

for i in range(len(numbers)-1):
    for j in range(len(numbers) - i):
        if numbers[i] > numbers[i + j]:
            numbers[i], numbers[i + j] = numbers[i + j], numbers[i]

print(numbers)


# sorting strings - case insensitive
# sorting strings

for i in range(len(words)-1):
    for j in range(len(words) - i):
        if words[i] > words[i + j]:
            words[i], words[i + j] = words[i + j], words[i]

print(words)


# sorting strings - case sensitive

for i in range(len(words)-1):
    for j in range(len(words) - i):
        if words[i].casefold() > words[i + j].casefold():
            words[i], words[i + j] = words[i + j], words[i]

print(words)

