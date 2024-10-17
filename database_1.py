import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to {db_file}, sqlite version: {sqlite3.version}")
        return conn
    except Error as e:
        print(e)
        return None

def create_table(conn):
    """ create tables for customers and orders """
    try:
        cursor = conn.cursor()

        # Tworzenie tabeli Klienci
        create_customers_table = """
        CREATE TABLE IF NOT EXISTS Klienci (
        id_klienta INTEGER PRIMARY KEY,
        imie TEXT NOT NULL,
        nazwisko TEXT NOT NULL,
        email TEXT NOT NULL
        );"""
        cursor.execute(create_customers_table)
        print("Tabela 'Klienci' created successfully.")

        # Tworzenie tabeli Zamówienia
        create_orders_table = """
        CREATE TABLE IF NOT EXISTS Zamówienia (
        id_zamówienia INTEGER PRIMARY KEY,
        data_zamówienia DATE NOT NULL,
        kwota REAL NOT NULL,
        id_klienta INTEGER,
        FOREIGN KEY (id_klienta) REFERENCES Klienci(id_klienta)
        );"""
        cursor.execute(create_orders_table)
        print("Tabela 'Zamówienia' created successfully.")

    except Error as e:
        print(e) 

def insert_sample_data(conn):
    """ insert sample data into Klienci and Zamówienia tables """
    try:
        cursor = conn.cursor()

        # Wstawianie przykładowych klientów
        insert_customers = """
        INSERT INTO Klienci (imie, nazwisko, email) VALUES
        ('Jan', 'Kowalski', 'jan.kowalski@example.com'),
        ('Anna', 'Nowak', 'anna.nowak@example.com'),
        ('Piotr', 'Zielinski', 'piotr.zielinski@example.com');
        """
        cursor.execute(insert_customers)

        # Wstawianie przykładowych zamówień
        insert_orders = """
        INSERT INTO Zamówienia (data_zamówienia, kwota, id_klienta) VALUES
        ('2024-10-15', 250.75, 1),
        ('2024-10-16', 99.99, 2),
        ('2024-10-17', 150.00, 1);
        """
        cursor.execute(insert_orders)

        conn.commit()  # Zatwierdzanie zmian
        print("Przykładowe dane zostały dodane pomyślnie.")
    
    except Error as e:
        print(e)

def select_all(conn, table):
    """ Query all rows in a table """
    try:
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {table}")
        rows = cur.fetchall()
        return rows
    except Error as e:
        print(e)
        return None

def select_where(conn, table, **query):
    """ Query rows from a table based on conditions in query """
    try:
        cur = conn.cursor()
        qs = []
        values = tuple()
        for k, v in query.items():
            qs.append(f"{k}=?")
            values += (v,)
        q = " AND ".join(qs)
        cur.execute(f"SELECT * FROM {table} WHERE {q}", values)
        rows = cur.fetchall()
        return rows
    except Error as e:
        print(e)
        return None

def update(conn, table, id, **kwargs):
    """ Update rows in a table by id """
    try:
        parameters = [f"{k} = ?" for k in kwargs]
        parameters = ", ".join(parameters)
        values = tuple(kwargs.values())
        values += (id,)

        sql = f''' UPDATE {table}
                  SET {parameters}
                  WHERE id_klienta = ?'''  # assuming 'id_klienta' as ID column
        cur = conn.cursor()
        cur.execute(sql, values)
        conn.commit()
        print(f"Record updated successfully in {table}.")
    except Error as e:
        print(e)

# def delete_where(conn, table, **kwargs):
   ## """ Delete rows from a table based on conditions """
    ##try:
      ##  qs = []
      ##  values = tuple()
      ##  for k, v in kwargs.items():
      ##      qs.append(f"{k}=?")
      ##      values += (v,)
      ##  q = " AND ".join(qs)

      ##  sql = f'DELETE FROM {table} WHERE {q}'
       ## cur = conn.cursor()
      ##  cur.execute(sql, values)
      #  conn.commit()
       # print(f"Deleted from {table} where {q}.") 
   # except Error as e:
       # print(e)

# def delete_all(conn, table):
   # """ Delete all rows from a table """
    #try:
     #   sql = f'DELETE FROM {table}'
      #  cur = conn.cursor()
      #  cur.execute(sql)
       # print(f"All rows deleted from {table}.")
    #except Error as e:
      #  print(e)

if __name__ == '__main__':
    db_file = r"database_1.db"
    connection = create_connection(db_file)

    if connection is not None:
        create_table(connection)
        insert_sample_data(connection)

        # Pobieranie danych z tabeli 'Klienci'
        customers = select_all(connection, 'Klienci')
        print("Klienci:", customers)

        # Pobieranie danych z tabeli 'Zamówienia'
        orders = select_all(connection, 'Zamówienia')
        print("Zamówienia:", orders)

        # Aktualizacja danych w tabeli 'Klienci'
        update(connection, 'Klienci', 1, imie="Janusz", nazwisko="Kowalczyk")
        customers_after_update = select_all(connection, 'Klienci')
        print("Klienci po aktualizacji:", customers_after_update)

        # Usuwanie konkretnego klienta
      #  delete_where(connection, 'Klienci', id_klienta=2)

        # Usuwanie wszystkich zamówień
       # delete_all(connection, 'Zamówienia')

        connection.close()