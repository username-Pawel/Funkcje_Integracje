import random

class Film:
    def __init__(self, title, release_year, genre):
        self.title = title
        self.release_year = release_year
        self.genre = genre
        self.views = 0

    def play(self):
        self.views += 1

    def __str__(self):
        return f"{self.title} ({self.release_year})"

class Serial:
    def __init__(self, title, release_year, genre, episode_number, season_number):
        self.title = title
        self.release_year = release_year
        self.genre = genre
        self.episode_number = episode_number
        self.season_number = season_number
        self.views = 0

    def play(self):
        self.views += 1

    def __str__(self):
        return f"{self.title} S{self.season_number:02}E{self.episode_number:02}"

class Library:
    def __init__(self):
        self.contents = []

    def add_item(self, item):
        self.contents.append(item)

    def get_movies(self):
        # Zwraca tylko filmy, posortowane alfabetycznie
        return sorted([item for item in self.contents if isinstance(item, Film)], key=lambda x: x.title)

    def get_series(self):
        # Zwraca tylko seriale, posortowane alfabetycznie
        return sorted([item for item in self.contents if isinstance(item, Serial)], key=lambda x: x.title)

    def search(self, title):
        # Wyszukuje film lub serial po tytule
        results = [item for item in self.contents if title.lower() in item.title.lower()]
        return sorted(results, key=lambda x: x.title)

    def generate_views(self):
        if self.contents:
            random_item = random.choice(self.contents)
            random_views = random.randint(1, 100)
            random_item.views += random_views

    def add_random_views(self, times):
        for _ in range(times):
            self.generate_views()

    def top_titles(self, count, content_type=None):
        # Zwraca najpopularniejsze tytuły
        if content_type == "movie":
            items = [item for item in self.contents if isinstance(item, Film)]
        elif content_type == "series":
            items = [item for item in self.contents if isinstance(item, Serial)]
        else:
            items = self.contents

        # Sortuje wg liczby odtworzeń malejąco i zwraca wybrane tytuły
        return sorted(items, key=lambda x: x.views, reverse=True)[:count]

# Przykładowe użycie
if __name__ == "__main__":
    library = Library()

    # Dodawanie filmów
    library.add_item(Film("Pulp Fiction", 1994, "Crime"))
    library.add_item(Film("The Godfather", 1972, "Crime"))
    library.add_item(Film("Inception", 2010, "Sci-Fi"))

    # Dodawanie seriali
    library.add_item(Serial("The Simpsons", 1989, "Comedy", 5, 1))
    library.add_item(Serial("Breaking Bad", 2008, "Drama", 1, 1))
    library.add_item(Serial("Game of Thrones", 2011, "Fantasy", 10, 7))

    # Odtwarzanie filmów i seriali
    library.contents[0].play()  # Odtwarzanie Pulp Fiction
    library.contents[1].play()  # Odtwarzanie The Godfather
    library.contents[3].play()  # Odtwarzanie The Simpsons

    # Generowanie losowych odtworzeń
    library.add_random_views(10)

    # Wyświetlenie wszystkich filmów
    print("Filmy:")
    for movie in library.get_movies():
        print(movie, f"- Odtworzenia: {movie.views}")

    # Wyświetlenie wszystkich seriali
    print("\nSeriale:")
    for series in library.get_series():
        print(series, f"- Odtworzenia: {series.views}")

    # Wyszukiwanie
    print("\nWyniki wyszukiwania 'The':")
    for result in library.search("The"):
        print(result)

    # Najpopularniejsze tytuły
    print("\nNajpopularniejsze tytuły (ogólnie):")
    for title in library.top_titles(3):
        print(title, f"- Odtworzenia: {title.views}")

    print("\nNajpopularniejsze filmy:")
    for title in library.top_titles(2, content_type="movie"):
        print(title, f"- Odtworzenia: {title.views}")

    print("\nNajpopularniejsze seriale:")
    for title in library.top_titles(2, content_type="series"):
        print(title, f"- Odtworzenia: {title.views}")