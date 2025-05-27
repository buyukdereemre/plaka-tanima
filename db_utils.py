import sqlite3

DB_PATH = "database/plates.db"

def create_table():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS plates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            plate TEXT UNIQUE
        )
    ''')
    conn.commit()
    conn.close()

def add_plate(plate):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    try:
        c.execute('INSERT INTO plates (plate) VALUES (?)', (plate,))
        conn.commit()
    except sqlite3.IntegrityError:
        pass  # Plaka zaten varsa hata verme
    conn.close()

def is_plate_allowed(plate):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('SELECT * FROM plates WHERE plate = ?', (plate,))
    result = c.fetchone()
    conn.close()
    return result is not None
