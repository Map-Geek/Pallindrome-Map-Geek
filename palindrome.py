"""
Python Development II Assignment 4: Palindrome Validator
Geetha Ramesh

palindrome.py

This module provides an 'is_palindrome' function that determines if a given
string is a palindrome and returns a boolean: True or False.

Functions:
    - is_palindrome(input_string: str) -> bool: Checks if the input string is a palindrome.

Exceptions:
    - Raises a ValueError for non-string inputs.
"""

from collections import deque


def is_palindrome(input_string):
    """
    Validate if the input string is a palindrome.

    :param input_string: the string to be checked if it is a palindrome
    :return: True or False
    :raises ValueError: if input is not a string
    """

    if not isinstance(input_string, str):
        raise ValueError("The input value must be a string")

    # Remove spaces, non-alpha characters and convert string to lowercase
    input_string = ''.join(c.lower() for c in input_string if c.isalpha())

    # Return False if string is empty
    if len(input_string) == 0:
        return False

    # Return True for a single character (it is always a palindrome)
    if len(input_string) == 1:
        return True

    # Create a deque from the string
    d = deque(input_string)

    # Remove and compare first and last characters, if they match it's a palindrome
    if len(d) > 1:
        if d.popleft() == d.pop():
            return True
    return False
