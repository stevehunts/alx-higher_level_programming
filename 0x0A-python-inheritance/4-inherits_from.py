#!/usr/bin/python3
"""
This module defines the inherits_from function which checks if an object is an
instance of a class that inherited (directly or indirectly) from a specified
class.
"""


def inherits_from(obj, a_class):
    """
    Check if 'obj' is an instance of a class that inherited (directly or
    indirectly) from 'a_class'.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if 'obj' is an instance of a subclass of 'a_class' and not
        directly 'a_class', otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
