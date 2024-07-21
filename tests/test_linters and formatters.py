from old_files.linters_and_formatters import (is_list_contains_only_numbers, outputs, return_the_longer_string)


def test_return_the_longer_string():
    assert return_the_longer_string("item_test", "abrakadabra,") == "abrakadabra,"
    assert return_the_longer_string("abrakadabra,", "item_test") == "abrakadabra,"
    assert return_the_longer_string("same", "same") == "same"


def test_is_list_contains_only_numbers():
    assert is_list_contains_only_numbers([1, 2, 3, 4, 5])
    assert not is_list_contains_only_numbers([1, 2, "three", 4, 5])
    assert is_list_contains_only_numbers([])


def test_outputs(capsys):
    outputs()
    captured = capsys.readouterr()
    assert captured.out == '*' * 80 + '\n'
