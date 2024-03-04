# factorial function

def factorial(n):
    # base case
    if n == 0:
        return 1
    else:
        # in return statement, n is multiplied by factorial(n-1)
        return n * factorial(n - 1)

print(factorial(5))


# factorial function non recursive
def factorial_non_recursive(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact

print(factorial_non_recursive(5))
