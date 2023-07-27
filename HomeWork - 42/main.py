
import sqlite3 as sq


def execute_query(query):
    conn = sq.connect('db_4.db')
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()