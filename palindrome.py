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


def is_palindrome(input_string):
    """
    Validate if the input string is a palindrome.

    :param input_string: the string to be checked if it is a palindrome
    :return: True or False
    :raises ValueError: if input is not a string
    """

    if not isinstance(input_string, str):
        raise ValueError("The input value must be a string")
