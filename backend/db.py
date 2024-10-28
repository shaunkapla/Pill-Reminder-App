import sqlite3


db_loc = './database/pill_reminder_db.db'

def db_connection():
    conn = sqlite3.connect(db_loc, timeout=10)
    conn.row_factory = sqlite3.Row
    return conn