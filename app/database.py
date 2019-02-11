# Standard Library Imports.
import os

# Third Party Imports.
import psycopg2

DB_URL = os.getenv('DATABASE_URL')
def db_connection():
    conn = psycopg2.connect(DB_URL)
    conn.autocommit = True
    return conn

def create_tables():
    auth_table = """
        CREATE TABLE IF NOT EXISTS users(
            id SERIAL PRIMARY KEY,
            firstname VARCHAR(20) NOT NULL,
            lastname VARCHAR(20) NOT NULL,
            username VARCHAR(20) UNIQUE NOT NULL,
            email VARCHAR UNIQUE NOT NULL,
            password1 VARCHAR(20) NOT NULL,
            password2 VARCHAR(20) NOT NULL
        );
    """
    table_queries = [auth_table]
    connection = db_connection()
    for query in table_queries:
        cur = connection.cursor()
        cur.execute(query)
    connection.commit()
    connection.close()

def drop_tables():
    db = db_connection()
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS users CASCADE")
    