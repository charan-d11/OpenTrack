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

    conn.commit()
    conn.close()

def add_student(name, branch):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO students (name, branch) VALUES (?, ?)",
        (name, branch)
    )
    conn.commit()
    conn.close()

def view_students():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    conn.close()
    return rows
