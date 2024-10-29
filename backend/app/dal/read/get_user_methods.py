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

        return user if user else None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    finally:
        if conn:
            conn.close()

def get_user_credentials_by_email(email):
    try:
        conn = db_connection()
        cursor = conn.cursor()
        query = """
        SELECT email, pw FROM users WHERE email = ?
        """
        cursor.execute(query, (email,))
        user_credentials = cursor.fetchone()

        return user_credentials if user_credentials else None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    finally:
        if conn:
            conn.close()
