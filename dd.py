import sqlite3


conn = sqlite3.connect('book_store/book_store.sqlite3')

# Створюємо об'єкт для роботи з базою даних
cursor = conn.cursor()

# Створюємо таблицю books
cursor.execute('''
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    published_date TEXT,
    price REAL
)
''')

# Зберігаємо зміни
conn.commit()

# Закриваємо з'єднання
conn.close()

print("База даних створена успішно!")
