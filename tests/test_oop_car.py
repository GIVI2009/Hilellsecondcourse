import pytest
from old_files.oop_car import Car


def test_initialization():
    car = Car("BMW M8", 2024, 50_000_000)
    assert car.model == "BMW M8"
    assert car.year == 2024
    assert car.price == 50_000_000


def test_drive():
    car = Car("BMW M8", 2024, 50_000_000)
    car.drive(50)
    assert car.price == 49_999_500


def test_category():
    car = Car("BMW M8", 2024, 50_000_000)
    assert car.category == "елітне"
    car.price = 15_000_000
    assert car.category == "елітне"
    car.price = 5_000_000
    assert car.category == "середнячок"
    car.price = 1_500_000
    assert car.category == "економ"


def test_str():
    car = Car("BMW M8", 2024, 50_000_000)
    assert str(car) == "Model: BMW M8, Year: 2024, Price: 50000000 грн"


if __name__ == '__main__':
    pytest.main()
