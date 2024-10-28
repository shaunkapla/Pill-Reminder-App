from ....db import db_connection

def get_user_by_email(email):
    try:
        conn = db_connection()
        cursor = conn.cursor()
        query = """
        SELECT * FROM users WHERE email = ?
        """
        cursor.execute(query, (email,))
        user = cursor.fetchone()
        conn.close()
        return user
    finally:
        if conn:
            conn.close()