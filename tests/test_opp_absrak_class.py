from old_files.opp_absrak_class import MarvelMovie, AvengersMovie, StandaloneMovie


def test_avengers_movie_description():
    avengers1 = AvengersMovie("The Avengers", "Joss Whedon", 2012, "Loki")
    assert avengers1.description() == (
        "Title: The Avengers, Director: Joss Whedon, Year: 2012, Main Villain: Loki"
    )

    avengers2 = AvengersMovie("Avengers: Age of Ultron", "Joss Whedon", 2015, "Ultron")
    assert avengers2.description() == (
        "Title: Avengers: Age of Ultron, Director: Joss Whedon, Year: 2015, Main Villain: Ultron"
    )


def test_standalone_movie_description():
    iron_man = StandaloneMovie("Iron Man", "Jon Favreau", 2008, "Tony Stark")
    assert iron_man.description() == (
        "Title: Iron Man, Director: Jon Favreau, Year: 2008, Hero: Tony Stark"
    )

    black_widow = StandaloneMovie("Black Widow", "Cate Shortland", 2021, "Natasha Romanoff")
    assert black_widow.description() == (
        "Title: Black Widow, Director: Cate Shortland, Year: 2021, Hero: Natasha Romanoff"
    )


def test_inheritance():
    avengers1 = AvengersMovie("The Avengers", "Joss Whedon", 2012, "Loki")
    assert isinstance(avengers1, MarvelMovie)
    assert isinstance(avengers1, AvengersMovie)

    iron_man = StandaloneMovie("Iron Man", "Jon Favreau", 2008, "Tony Stark")
    assert isinstance(iron_man, MarvelMovie)
    assert isinstance(iron_man, StandaloneMovie)
