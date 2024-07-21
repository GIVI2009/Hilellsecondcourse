from typing import Callable

db = {"login": "admin", "password": "123"}


# Decorator to filter result list based on type
def filter_result(data_type: str):
    def decorator(func: Callable):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, list):
                type_map = {
                    'str': str,
                    'int': int,
                    'float': float
                }
                if data_type in type_map:
                    result = [item for item in result if not isinstance(item, type_map[data_type])]
            return result

        return wrapper

    return decorator


# Test functions using filter_result decorator
@filter_result('str')
def test_func():
    return [1, 'a', 2.5, 'b', 3]


@filter_result('int')
def test_func2():
    return [1, 'a', 2.5, 'b', 3]


@filter_result('float')
def test_func3():
    return [1, 'a', 2.5, 'b', 3]


@filter_result('unknown')
def test_func4():
    return [1, 'a', 2.5, 'b', 3]


# Authorization decorator
def simple_decorator(func: Callable):
    def wrapper(*args, **kwargs):
        login = kwargs.get('login', '')
        password = kwargs.get('password', '')
        if login == db["login"] and password == db["password"]:
            result = func(*args, **kwargs)
            return result
        return None

    return wrapper


@simple_decorator
def add_two_numbers(number_1: float | int, number_2: float | int) -> float | int:
    result = number_1 + number_2
    return result
