import pytest
from functions.palindrome_number import palindrome_number

def test_for_palindrome():
    assert palindrome("racecar") == True
    
def test_for_empty_string():
    assert palindrome("") == False
