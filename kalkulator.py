import logging

# Konfiguracja logowania
logging.basicConfig(level=logging.INFO, format='%(message)s')

def dodawanie(a, b):
    return a + b

def odejmowanie(a, b):
    return a - b

def mnozenie(a, b):
    return a * b

def dzielenie(a, b):
    return a / b

def kalkulator():
    # Pobieranie wyboru od użytkownika
    dzialanie = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
    
    # Pobieranie argumentów od użytkownika
    a = float(input("Podaj składnik 1: "))
    b = float(input("Podaj składnik 2: "))

    # Sprawdzenie wybranego działania i jego wykonanie
    if dzialanie == '1':
        logging.info(f"Dodaję {a:.2f} i {b:.2f}")
        wynik = dodawanie(a, b)
    elif dzialanie == '2':
        logging.info(f"Odejmuję {a:.2f} od {b:.2f}")
        wynik = odejmowanie(a, b)
    elif dzialanie == '3':
        logging.info(f"Mnożę {a:.2f} przez {b:.2f}")
        wynik = mnozenie(a, b)
    elif dzialanie == '4':
        logging.info(f"Dzielę {a:.2f} przez {b:.2f}")
        wynik = dzielenie(a, b)
    else:
        print("Niepoprawny wybór działania!")
        return

    # Wyświetlenie wyniku
    print(f"Wynik to {wynik:.2f}")

if __name__ == "__main__":
    kalkulator()


