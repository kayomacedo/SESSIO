import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "config.db")

def create_config_table():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS config (
        id INTEGER PRIMARY KEY,
        login_url TEXT,
        home_url TEXT
    )
    """)

    # garante que exista ao menos 1 registro
    cur.execute("SELECT COUNT(*) FROM config")
    if cur.fetchone()[0] == 0:
        cur.execute("INSERT INTO config (login_url, home_url) VALUES (?, ?)", ("", ""))
        conn.commit()

    conn.close()


def save_config(login_url: str, home_url: str):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
        UPDATE config SET login_url = ?, home_url = ? WHERE id = 1
    """, (login_url, home_url))

    conn.commit()
    conn.close()


def load_config():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("SELECT login_url, home_url FROM config WHERE id = 1")
    row = cur.fetchone()

    conn.close()

    return {"login_url": row[0], "home_url": row[1]}
