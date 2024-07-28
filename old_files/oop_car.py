class Car:
    def __init__(self, model: str, year: int, price: int):
        self.model = model
        self.year = year
        self.price = price

    def drive(self, distance: int):
        cost_per_km = 10
        self.price -= cost_per_km * distance

    def __str__(self) -> str:
        return f"Model: {self.model}, Year: {self.year}, Price: {self.price} грн"

    __repr__ = __str__

    @property
    def category(self) -> str:
        if self.price > 10_000_000:
            return "елітне"
        elif 2_000_000 <= self.price <= 10_000_000:
            return "середнячок"
        else:
            return "економ"


# Приклад використання
car = Car("BMW M8", 2024, 50_000_000)
print(car)  # Model: BMW M8, Year: 2024, Price: 50000000 грн
print(car.category)  # середнячок

car.drive(50)
print(car)
print(car.category)