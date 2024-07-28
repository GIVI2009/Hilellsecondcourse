# accepts two tapes and returns the longer one
def return_the_longer_string(string1: str, string2: str) -> str:
    if len(string1) > len(string2):
        return string1
    else:
        return string2


result1 = return_the_longer_string("item_test", "abrakadabra,")


# accepts a list and returns True if the list consists only of numbers and False otherwise
def is_list_contains_only_numbers(lst: list) -> bool:
    for item in lst:
        if not isinstance(item, (int, float)):
            return False
    return True


result2 = is_list_contains_only_numbers([1234567890, 3.14])


# a function that outputs the type ribbon to the console
# '*' * 80
def outputs() -> None:
    print('*' * 80)


print(result1)
print(result2)
outputs()
