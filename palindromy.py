def is_it_palindrome (word):
    # Usunięcie zbędnych spacji oraz zamiana liter na małe, żeby nie zwracać uwagi na wielkość liter
    word = word.replace(" ", "").lower()
    
    # Sprawdzenie, czy słowo jest takie samo jak jego odwrócona wersja
    if word == word[::-1]:
        return f'"{word}" jest palindromem.'
    else:
        return f'"{word}" nie jest palindromem.'

# Pobranie słowa od użytkownika
uzytkownik_input = input("Wpisz słowo do sprawdzenia, czy jest palindromem: ")
# Wywołanie funkcji i wydrukowanie wyniku
wynik = is_it_palindrome(uzytkownik_input)
print(wynik)