import sqlite3


def create_groups_table(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS muslib_db(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            band_name TEXT NOT NULL,
            folder_path TEXT NOT NULL
            )
        ''')

    conn.commit()

    conn.close()

