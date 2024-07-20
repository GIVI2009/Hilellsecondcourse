from decorators import test_func, test_func2, test_func3, test_func4, add_two_numbers


# Tests for filter_result decorator
def test_filter_result_str():
    assert test_func() == [1, 2.5, 3]  # remove strings


def test_filter_result_int():
    assert test_func2() == ['a', 2.5, 'b']  # remove integers


def test_filter_result_float():
    assert test_func3() == [1, 'a', 'b', 3]  # remove floats


def test_filter_result_unknown():
    assert test_func4() == [1, 'a', 2.5, 'b', 3]  # keep all


# Tests for simple_decorator
def test_add_two_numbers_success(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'admin')
    assert add_two_numbers(2, 8, login='admin', password='123') == 10  # correct login


def test_add_two_numbers_fail(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'user')
    assert add_two_numbers(2, 8, login='user', password='wrong') is None  # incorrect login
