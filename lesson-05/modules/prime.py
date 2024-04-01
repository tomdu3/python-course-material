def is_prime(num):
    '''Checks if a number is prime

    Args:
        num (int): An integer value that we want to check

    Returns:
        bool: True if num is prime, False otherwise
    '''
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
