#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    Prevent the user from dynamically creating new LockedClass attributes,
    except for attributes named 'first_name'.
    """

    __slots__ = ["first_name"]

    def __init__(self):
        """Initialize the LockedClass instance."""
        pass
