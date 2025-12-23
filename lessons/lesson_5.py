import sqlite3


def create_tables(connection):
    connection.execute("""" 
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT
        name TEXT
        author TEXT
        publication_year INTEGER
        genre TEXT
        number_of_pages INTEGER
        number_of_copies INTEGER
    )
    """)


def add_books(connection,name, author, publication_year, genre,
              number_of_pages, number_of_copies):
    connection.execute(""""
    INSERT INTO books
    VALUES (?, ?, ?)
    """,
                        (name, author, publication_year, genre,
              number_of_pages, number_of_copies ))
    connection.commit()


if __name__=="__main__":
    conn = sqlite3.connect('databass.db')

    create_tables(conn)
    add_books(conn,"Война и мир", "Лев Толстой", 1869, "Роман",
              1600, 30000000)
    add_books(conn, 'Преступление и наказание', 'Фёдор Достоевский',
              1866, 'Роман', 672, 10000000)
