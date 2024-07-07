# test_remove_spaces.py

import pytest
from remove_spaces import remove_spaces

def test_remove_spaces_with_spaces():
    assert remove_spaces("hello world") == "helloworld"

def test_remove_spaces_with_multiple_spaces():
    assert remove_spaces("  hello   world  ") == "helloworld"

def test_remove_spaces_without_spaces():
    assert remove_spaces("helloworld") == "helloworld"

def test_remove_spaces_empty_string():
    assert remove_spaces("") == ""
