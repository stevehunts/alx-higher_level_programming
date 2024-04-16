#!/usr/bin/python3
import sys  # Required for command-line arguments
import os  # Required for file existence check

# Assuming 5-save_to_json_file.py and 6-load_from_json_file.py are in the same directory and provide the following functions:
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

file_name = "add_item.json"

# Check if the file exists and load the existing data if it does
try:
    items = load_from_json_file(file_name)
except FileNotFoundError:
    items = []

# Extend the list with arguments passed to the script (excluding the script name itself)
items.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(items, file_name)
