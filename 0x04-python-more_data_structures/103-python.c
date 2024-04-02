import ctypes

# Load the shared library
libPython = ctypes.CDLL('./libPython.so')

# Create ctypes prototype for our functions
libPython.print_python_list.argtypes = [ctypes.py_object]
libPython.print_python_bytes.argtypes = [ctypes.py_object]

# Create test objects
s = b"Hello"
b = b'\xff\xf8\x00\x00\x00\x00\x00\x00'
l = [b'Hello', b'World']

# Call our C functions
libPython.print_python_bytes(s)
libPython.print_python_bytes(b)
libPython.print_python_list(l)
