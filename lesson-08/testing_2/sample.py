from math import isclose

def check_floats_equal(a, b):
    if isclose(a, b):
        return True
    else:
        return False

def check_floats_equal2(a, b):
    return round(a, 2) == round(b, 2)

print(check_floats_equal(0.1, 0.09 + 0.01))
print(check_floats_equal2(0.1, 0.09 + 0.01))
