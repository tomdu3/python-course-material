def prime(num):
    for i in range(int(num ** 0.5)-1):
        if num % (i+2) == 0:
            return False
    return True


print(prime(7))
print(prime(9))
print(prime(101))
