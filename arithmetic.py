"""Functions for common math operations."""


def add(num1, num2):
    add_num = num1 + num2
    """Return the sum of num1 and num2."""
    return add_num


def subtract(num1, num2):
    """Return the value of num1 minus num2."""
    sub_num = num1 - num2   
    return sub_num

def multiply(num1, num2):
    """Multiply the num1 by num2 and return the result."""
    multi_num = num1 * num2
    return multi_num

def divide(num1, num2):
    """Divide the num1 by num2, returning a floating point."""
    divide_num = num1 / num2    
    return divide_num


def square(num1):
    """Return the square of num1."""
    squared = num1 ** 2
    return squared


def cube(num1):
    """Return the cube of num1."""
    cubed = num1 ** num1
    return cubed


def power(num1, num2):
    """Raise num1 to the power of num2 and return the value."""
    power_num = num1 ** num2
    return power_num


def mod(num1, num2):
    """Return the remainder of num1 / num2."""
    mod_num = num1 % num2
    return mod_num
