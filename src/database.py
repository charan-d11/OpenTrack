import sqlite3

def connect_db():
    return sqlite3.connect("db/opentrack.db")

def create_tables():
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        branch TEXT
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        task TEXT,
        status TEXT,
        FOREIGN KEY (student_id) REFERENCES students(id)
    );
    """)

    conn.commit()
    conn.close()
