import pandas as pd

# Wczytaj dane o śmiertelnych interwencjach policji
data = pd.read_csv("/Users/pawelwrzesinski/desktop/Kodilla/Zadania/Funkcje_integracje/fatal-police-shootings-data (1).csv")

# Tworzymy tabelę przestawioną
race_mental_illness = data.pivot_table(index='race', columns='signs_of_mental_illness', aggfunc='size', fill_value=0)

# Wyświetlamy tabelę
print(race_mental_illness)

# Dodajemy kolumnę procentową
race_mental_illness['mental_illness_percentage'] = (
    race_mental_illness[True] / (race_mental_illness[True] + race_mental_illness[False]) * 100
)

# Wyświetlamy tabelę z nową kolumną
print(race_mental_illness)

# Sprawdzamy, która rasa ma najwyższy odsetek
highest_percentage_race = race_mental_illness['mental_illness_percentage'].idxmax()
print(f"Rasa z najwyższym odsetkiem chorób psychicznych podczas interwencji to: {highest_percentage_race}")

# Przekształcamy kolumnę 'date' na format daty
data['date'] = pd.to_datetime(data['date'], errors='coerce')

# Dodajemy kolumnę z dniem tygodnia
data['day_of_week'] = data['date'].dt.day_name()

# Zliczamy interwencje według dnia tygodnia
day_counts = data['day_of_week'].value_counts()
print(day_counts)

# Wczytujemy dane o populacji i skrótach stanów
state_population = pd.read_html("https://simple.wikipedia.org/wiki/List_of_U.S._states_by_population")[0]
state_abbreviations = pd.read_html("https://en.wikipedia.org/wiki/List_of_U.S._state_and_territory_abbreviations")[0]

# Ujednolicenie nazw kolumn
state_population = state_population.rename(columns={"State or territory": "state", "Population estimate, July 1, 2019": "population"})
state_abbreviations = state_abbreviations.rename(columns={"Name": "state", "Postal Abbreviation": "state_abbreviation"})

# Łączenie danych o populacji i skrótach stanów
state_data = pd.merge(state_population[['state', 'population']], state_abbreviations[['state', 'state_abbreviation']], on='state')

# Łączenie z danymi o interwencjach
data = pd.merge(data, state_data, left_on='state', right_on='state_abbreviation', how='left')

# Grupa i liczenie incydentów na stan
state_counts = data['state_abbreviation'].value_counts().rename_axis('state_abbreviation').reset_index(name='incident_count')

# Łączenie z danymi populacji i obliczanie liczby incydentów na 1000 mieszkańców
state_counts = pd.merge(state_counts, state_data[['state_abbreviation', 'population']], on='state_abbreviation')
state_counts['incidents_per_1000'] = (state_counts['incident_count'] / state_counts['population']) * 1000

# Wyświetlamy wyniki
print(state_counts[['state_abbreviation', 'incident_count', 'population', 'incidents_per_1000']])


