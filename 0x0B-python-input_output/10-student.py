#!/usr/bin/python3
class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is not None:
            if not isinstance(attrs, list) or not all(isinstance(ele, str) for ele in attrs):
                raise ValueError("attrs must be a list of strings")
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
