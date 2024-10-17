import pandas as pd
from sqlalchemy import create_engine, Table, Column, Integer, String, Float, DateTime, MetaData

# Tworzenie silnika do bazy danych SQLite
engine = create_engine('sqlite:///database.db', echo=True)
meta = MetaData()

# Definicja tabeli stations
stations = Table(
    'stations', meta,
    Column('station_id', String, primary_key=True),  # Zmiana na String
    Column('station_name', String),
    Column('latitude', Float),
    Column('longitude', Float),
    Column('elevation', Float),
    Column('country', String),
    Column('state', String),
)

# Definicja tabeli measures
measures = Table(
    'measures', meta,
    Column('measure_id', Integer, primary_key=True),  # Dodajemy primary key
    Column('station', String),
    Column('date', String),  # Możesz użyć DateTime, jeśli to potrzebne
    Column('precip', Float),
    Column('tobs', Float),
)

# Tworzenie tabel w bazie danych
meta.create_all(engine)

# Odczyt danych z plików CSV
stations_df = pd.read_csv('clean_stations.csv')
measures_df = pd.read_csv('clean_measure.csv')

# Wstawianie danych do tabeli stations
with engine.connect() as conn:
    for index, row in stations_df.iterrows():
        conn.execute(stations.insert().values(
            station_id=row['station'],
            station_name=row['name'],
            latitude=row['latitude'],
            longitude=row['longitude'],
            elevation=row['elevation'],
            country=row['country'],
            state=row['state']
        ))

    # Wstawianie danych do tabeli measures
    for index, row in measures_df.iterrows():
        conn.execute(measures.insert().values(
            station=row['station'],
            date=row['date'],
            precip=row['precip'],
            tobs=row['tobs']
        ))