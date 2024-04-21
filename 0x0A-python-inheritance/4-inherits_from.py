#!/usr/bin/python3
"""
This module defines the inherits_from function. It checks if an object is an
instance of a class that inherited (directly or indirectly) from another class,
but is not the class itself.
"""


def inherits_from(obj, a_class):
    """
    Determine if 'obj' is an instance of a class that inherited (either
    directly or indirectly) from 'a_class' but is not 'a_class' itself.

    Args:
        obj (any): The object to check.
        a_class (type): The reference class.

    Returns:
        bool: True if 'obj' is an instance of a subclass of 'a_class' but not
        the class itself, otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
