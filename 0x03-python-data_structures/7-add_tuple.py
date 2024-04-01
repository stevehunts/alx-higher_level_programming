#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure tuple_a and tuple_b are only 2 elements long
    tuple_1 = tuple_a[:2] + (0, 0)
    tuple_2 = tuple_b[:2] + (0, 0)
    new_tuple = tuple_1[0] + tuple_2[0], tuple_1[1] + tuple_2[1]
    return new_tuple
