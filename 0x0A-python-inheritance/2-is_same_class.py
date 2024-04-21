#!/usr/bin/python3
"""
Module 2-is_same_class contains a single function is_same_class.
The function checks if an object is exactly an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Determine if 'obj' is exactly an instance of 'a_class'.

    Args:
        obj (any): The object to check.
        a_class (type): The class type to compare against.

    Returns:
        bool: True if 'obj' is exactly of 'a_class', otherwise False.
    """
    return type(obj) is a_class
