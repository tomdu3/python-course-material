# reverse a list without making a new one

norm_list = ['This', 'is', 'a', 'stupid', 'list']

print(norm_list)
for i in range(len(norm_list)//2 - 1):
    norm_list[i], norm_list[len(norm_list) - i - 1] =\
        norm_list[len(norm_list) - i - 1], norm_list[i]

print(norm_list)
