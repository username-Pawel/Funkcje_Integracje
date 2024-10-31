import pandas as pd
import requests


url = "https://www.officialcharts.com/chart-news/the-best-selling-albums-of-all-time-on-the-official-uk-chart__15551/"
response = requests.get(url)
tables = pd.read_html(response.text)

if tables:
    df = tables[0]
    df.columns = ['POZYCJA', 'TYTUŁ', 'ARTYSTA', 'ROK', 'MAX POZYCJA']
    
   
   

    # 1. Liczba unikalnych artystów
    unique_artists_count = df['ARTYSTA'].nunique()
    print(f"Liczba unikalnych artystów: {unique_artists_count}")
    
    # 2. Najczęściej pojawiające się zespoły
    frequent_artists = df['ARTYSTA'].value_counts().head(5)
    print("Najczęściej pojawiający się artyści:\n", frequent_artists)
    
    # 3. Formatowanie nagłówków
    df.columns = [col.capitalize() for col in df.columns]
    
    # 4. Usunięcie kolumny ‘Max Pozycja’
    df.drop(columns=['Max Pozycja'], inplace=True, errors='ignore')
    
    # 5. Rok, w którym wyszło najwięcej albumów
    most_albums_year = df['Rok'].value_counts().idxmax()
    print(f"Rok z największą liczbą albumów: {most_albums_year}")

    # 6. Liczba albumów wydanych między 1960 a 1990 rokiem
    df['Rok'] = pd.to_numeric(df['Rok'], errors='coerce')  
    albums_1960_1990 = df[(df['Rok'] >= 1960) & (df['Rok'] <= 1990)].shape[0]
    print(f"Liczba albumów wydanych między 1960 a 1990 rokiem: {albums_1960_1990}")
    
    # 7. Rok wydania najmłodszego albumu
    youngest_album_year = df['Rok'].max()
    print(f"Rok wydania najmłodszego albumu: {youngest_album_year}")

    # 8. Lista najwcześniej wydanych albumów każdego artysty
    df = df.dropna(subset=['Rok']) 
    earliest_albums = df.loc[df.groupby('Artysta')['Rok'].idxmin()][['Artysta', 'Tytuł', 'Rok']]
    earliest_albums.to_csv('/Users/pawelwrzesinski/desktop/Kodilla/Zadania/Funkcje_integracje/najwcześniej_wydane_albumy.csv', index=False)

    print("Lista najwcześniej wydanych albumów zapisana do 'najwcześniej_wydane_albumy.csv'.")
else:
    print("Brak tabeli na stronie.")

