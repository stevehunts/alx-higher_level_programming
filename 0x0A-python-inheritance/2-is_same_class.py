#!/usr/bin/python3
"""
Module 2-is_same_class contains a single function is_same_class.
The function checks if an object is exactly an instance of a specified class.
"""

def is_same_class(obj, a_class):
    """
    Determines if the object `obj` is exactly an instance of the class `a_class`.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of `obj`.

    Returns:
        bool: True if `obj` is exactly an instance of `a_class`, otherwise False.
    """
    return type(obj) is a_class
