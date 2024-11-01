"""
Python Development II Assignment 4: Palindrome Validator
Geetha Ramesh

test_palindrome.py

Unit tests for the is_palindrome function.

This module contains test cases to validate the behavior of the
is_palindrome function, which returns a boolean (True or False)
for a given string.
"""

import pytest
from palindrome import is_palindrome


def test_non_string_input():
    """
    Test to check if is_palindrome function raises
    a ValueError for any input that is not a string.
    """
    with pytest.raises(ValueError):
        is_palindrome(7.5)
    with pytest.raises(ValueError):
        is_palindrome(754)
    with pytest.raises(ValueError):
        is_palindrome(None)


def test_empty_string_input():
    """
    Test to check if is_palindrome function returns
    False when called with an empty string.
    """
    input_value = ""
    expected_result = False
    assert is_palindrome(input_value) == expected_result


def test_one_character_input():
    """
    Test to check if is_palindrome function returns
    True when called with one character
    """
    input_value = "a"
    expected_result = True
    assert is_palindrome(input_value) == expected_result


def test_two_characters_input():
    """
    Test to check if is_palindrome function returns
    True when called with two characters
    """
    input_value = "bb"
    expected_result = True
    assert is_palindrome(input_value) == expected_result


def test_three_characters_input():
    """
    Test to check if is_palindrome function returns
    False when called with three characters
    """
    input_value = "abc"
    expected_result = False
    assert is_palindrome(input_value) == expected_result


def test_multi_character_input():
    """
    Test to check if is_palindrome function returns
    True when called with multi-character palindrome
    """
    input_value = "laval"
    expected_result = True
    assert is_palindrome(input_value) == expected_result


def test_non_palindrome_input():
    """
    Test to check if is_palindrome function returns
    False when called with a non-palindrome
    """
    input_value = "toronto"
    expected_result = False
    assert is_palindrome(input_value) == expected_result


def test_is_palindrome_with_sentence():
    """
    Test to check if is_palindrome function returns
    True when called with a sentence
    """
    input_value = "Able was I ere I saw Elba"
    expected_result = True
    assert is_palindrome(input_value) == expected_result
