from gg import return_the_longer_string, is_list_contains_only_numbers, outputs


def test_return_the_longer_string():
    assert return_the_longer_string("item_test", "abrakadabra,") == "abrakadabra,"
    assert return_the_longer_string("abrakadabra,", "item_test") == "abrakadabra,"
    assert return_the_longer_string("same", "same") == "same"


def test_is_list_contains_only_numbers():
    assert is_list_contains_only_numbers([1, 2, 3, 4, 5]) == True
    assert is_list_contains_only_numbers([1, 2, "three", 4, 5]) == False
    assert is_list_contains_only_numbers([]) == True


def test_outputs(capsys):
    outputs()
    captured = capsys.readouterr()
    assert captured.out == '*' * 80 + '\n'
