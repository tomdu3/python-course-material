from math import pi, sqrt

def circle_area(radius):
    """
    Calculate the area of a circle given its radius.

    Parameters:
        radius (float): The radius of the circle.

    Returns:
        float: The area of the circle.
    """

    return pi * radius**2

def circle_circumference(radius):
    """
    Calculate the circumference of a circle given its radius.

    Parameters:
        radius (float): The radius of the circle.

    Returns:
        float: The circumference of the circle.
    """

    return 2 * pi * radius


def triangle_area(side1, side2, side3):
    """
    Calculate the area of a triangle given its base and height.

    Parameters:
        base (float): The base of the triangle.
        height (float): The height of the triangle.

    Returns:
        float: The area of the triangle.
    """
    if not triangle_check(side1, side2, side3):
        return None
    
    semi_para = (side1 + side2 + side3) / 2

    area = sqrt(semi_para * (semi_para - side1) * (semi_para - side2) * (semi_para - side3))
    return area


def triangle_check(side1, side2, side3):
    """
    Check if a triangle is valid.

    Parameters:
        side1 (float): The length of the first side.
        side2 (float): The length of the second side.
        side3 (float): The length of the third side.

    Returns:
        bool: True if the triangle is valid, False otherwise.
    """
    return side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1

if __name__ == "__main__":
    print(triangle_area(4, 5, 6))
    print(triangle_check(4, 5, 6))
    print(triangle_area(4, 5, 1))
    print(circle_area(4))
    print(circle_circumference(4))