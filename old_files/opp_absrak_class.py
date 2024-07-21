from abc import ABC, abstractmethod


class MarvelMovie(ABC):
    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year

    @abstractmethod
    def description(self):
        return f"Title: {self.title}, Director: {self.director}, Year: {self.year}"


class AvengersMovie(MarvelMovie):
    def __init__(self, title, director, year, main_villain):
        super().__init__(title, director, year)
        self.main_villain = main_villain

    def description(self):
        return f"{super().description()}, Main Villain: {self.main_villain}"


class StandaloneMovie(MarvelMovie):
    def __init__(self, title, director, year, hero):
        super().__init__(title, director, year)
        self.hero = hero

    def description(self):
        return f"{super().description()}, Hero: {self.hero}"


avengers1 = AvengersMovie("The Avengers", "Joss Whedon", 2012, "Loki")
avengers2 = AvengersMovie("Avengers: Age of Ultron", "Joss Whedon", 2015, "Ultron")
iron_man = StandaloneMovie("Iron Man", "Jon Favreau", 2008, "Tony Stark")
black_widow = StandaloneMovie("Black Widow", "Cate Shortland", 2021, "Natasha Romanoff")

print(avengers1.description())
print(avengers2.description())
print(iron_man.description())
print(black_widow.description())
