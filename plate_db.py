import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "plates.db")

def initialize_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS authorized_plates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            plate TEXT UNIQUE NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_plate(plate):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO authorized_plates (plate) VALUES (?)", (plate,))
        conn.commit()
    except sqlite3.IntegrityError:
        print("Bu plaka zaten kayıtlı.")
    conn.close()

def is_plate_authorized(plate):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM authorized_plates WHERE plate = ?", (plate,))
    result = cursor.fetchone()
    conn.close()
    return result is not None
