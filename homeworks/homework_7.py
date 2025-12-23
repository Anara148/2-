import sqlite3


def create_tables(conn):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            author TEXT, 
            publication_yer INTEGER,
            genre TEXT,
            number_of_pages INTEGER,
            number_of_copies INTEGER
        )
     """)

def insert_books(conn):
    books = [
        ('Война и мир', 'Лев Толстой', 1869, 'Роман-эпопея', 1225,10000),
        ('Преступление и наказание', 'Фёдор Достоевский', 1866, 'Роман', 672,500000),
        ('Мастер и Маргарита', 'Михаил Булгаков', 1967, 'Роман', 480,300000),
        ('Евгений Онегин', 'Александр Пушкин', 1833, 'Роман в стихах', 224, 150000),
        ('1984', 'Джордж Оруэлл', 1949, 'Антиутопия', 328, 200000),
        ('Маленький принц', 'Антуан де Сент-Экзюпери', 1943, 'Сказка-притча', 112, 100000),
        ('Мертвые души', 'Николай Гоголь', 1842, 'Поэма', 352, 700000),
        ('Отцы и дети', 'Иван Тургенев', 1862, 'Роман', 288, 600000),
        ('Три товарища', 'Эрих Мария Ремарк', 1936, 'Роман', 480, 950000),
        ('Герой нашего времени', 'Михаил Лермонтов', 1840, 'Роман', 224, 1123000)
    ]




    conn.executemany("""
        INSERT INTO books
        (name, author, publication_yer, genre, number_of_pages, number_of_copies)
        VALUES (?, ?, ?, ?, ?, ?)
    """, books)

    conn.commit()
if __name__ == '__main__':
    conn = sqlite3.connect('database.db')

    create_tables(conn)
    insert_books(conn)
    conn.close()






