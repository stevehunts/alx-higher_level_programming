#!/usr/bin/python3
"""
This module contains the function is_same_class
"""

def is_same_class(obj, a_class):
    """Return True if obj is exactly an instance of a_class; otherwise False."""
    return type(obj) == a_class
