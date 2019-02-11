"""Authentication Model."""
# Local Imports.
from ....database import db_connection

# Third Party Imports.
from psycopg2.extras import RealDictCursor
conn = db_connection()
cursor = conn.cursor(cursor_factory=RealDictCursor)

class Auth():
   
    def user_registration(self, data=None):
        query = """
        INSERT INTO users (firstname, lastname, username, email, password1, password2) VALUES (%(first_name)s, %(last_name)s, %(username)s, %(email)s, %(password1)s, %(password2)s);"""
        cursor.execute(query, data)
        conn.commit()
        return data

    def retrieve_all_users(self):
        query = "SELECT * FROM users;"
        cursor.execute(query)
        users_record = cursor.fetch_all()
        return users_record

    def user_login(self, username=None):
        query = "SELECT * FROM users WHERE username = '{}';".format(username)
        cursor.execute(query)
        user = cursor.fetchone()
        if user:
            return True
        return False