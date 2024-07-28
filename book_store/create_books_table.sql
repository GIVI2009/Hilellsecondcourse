
CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    author_id INTEGER,
    title TEXT NOT NULL,
    price REAL,
    description TEXT,
    FOREIGN KEY (author_id) REFERENCES authors(id)
);
