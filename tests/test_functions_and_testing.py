from functions_and_testing import remove_spaces


def test_remove_spaces_no_spaces():
    assert remove_spaces("hello") == "hello"


def test_remove_spaces_with_spaces():
    assert remove_spaces("h e l l o") == "hello"


def test_remove_spaces_empty_string():
    assert remove_spaces("") == ""


def test_remove_spaces_only_spaces():
    assert remove_spaces("     ") == ""


def test_remove_spaces_leading_trailing_spaces():
    assert remove_spaces("  hello  ") == "hello"
