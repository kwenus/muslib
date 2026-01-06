import sqlite3


def write_groups(db_file, groups_list):

    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()


    cursor.executemany('''
            INSERT INTO muslib_db (
                band_name, folder_path)
                VALUES (?, ?)''',
                groups_list)

    conn.commit()

    conn.close()

