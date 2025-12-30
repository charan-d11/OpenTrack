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
        status TEXT DEFAULT 'Pending',
        FOREIGN KEY (student_id) REFERENCES students(id)
    );
    """)

    conn.commit()
    conn.close()

# ---------- STUDENT FUNCTIONS ----------
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

# ---------- TASK FUNCTIONS ----------
def add_task(student_id, task):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO tasks (student_id, task) VALUES (?, ?)",
        (student_id, task)
    )
    conn.commit()
    conn.close()

def view_tasks(student_id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute(
        "SELECT id, task, status FROM tasks WHERE student_id = ?",
        (student_id,)
    )
    rows = cur.fetchall()
    conn.close()
    return rows
def mark_task_completed(task_id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute(
        "UPDATE tasks SET status = 'Completed' WHERE id = ?",
        (task_id,)
    )
    conn.commit()
    conn.close()
