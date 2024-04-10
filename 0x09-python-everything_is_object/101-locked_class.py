#!/usr/bin/python3
"""Defines a locked class."""

class LockedClass:
    """
    Prevent the user from dynamically creating new instance attributes,
    except if the new instance attribute is called 'first_name'.
    """
    __slots__ = ["first_name"]

# Below code is for testing the functionality.
# It's not part of the class definition.
if __name__ == "__main__":
    lc = LockedClass()
    lc.first_name = "John"
    try:
        lc.last_name = "Snow"
    except AttributeError as e:
        print("[{}] {}".format(e.__class__.__name__, e))
