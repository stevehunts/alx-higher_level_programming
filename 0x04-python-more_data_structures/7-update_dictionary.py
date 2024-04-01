#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    Replaces or adds a key/value in a dictionary.

    Args:
        a_dictionary (dict): The dictionary to update.
        key (str): The key to update or add.
        value: The new value for the key.

    Returns:
        dict: The updated dictionary.
    """
    a_dictionary[key] = value
    return a_dictionary

# Assuming print_sorted_dictionary is a function that prints dictionaries sorted by keys
def print_sorted_dictionary(a_dictionary):
    for key in sorted(a_dictionary.keys()):
        print(f"{key}: {a_dictionary[key]}")

# Testing the function
a_dictionary = {'language': "C", 'number': 89, 'track': "Low level"}
update_dictionary(a_dictionary, 'language', "Python")
print_sorted_dictionary(a_dictionary)
print("--")

update_dictionary(a_dictionary, 'city', "San Francisco")
print_sorted_dictionary(a_dictionary)
