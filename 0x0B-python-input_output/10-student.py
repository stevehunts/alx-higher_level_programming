#!/usr/bin/python3
class Student:
    """Defines a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student.

        If attrs is a list of strings, represents only those attributes
        included in the list. Raises ValueError if attrs is not a list of strings.

        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if attrs is not None:
            if not isinstance(attrs, list) or not all(isinstance(ele, str) for ele in attrs):
                raise ValueError("attrs must be a list of strings")
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}

        return self.__dict__
