from ....db import db_connection

def delete_user_by_email(email):
    try:
        conn = db_connection()
        cursor = conn.cursor()

        # Check if the user exists first
        check_query = "SELECT 1 FROM users WHERE email = ?"
        cursor.execute(check_query, (email,))
        user_exists = cursor.fetchone()

        if not user_exists:
            return f"No user found with email {email}", False

        
        # if user does exist, we will delete them
        delete_query = """
        DELETE FROM users WHERE email = ?
        """
        cursor.execute(delete_query, (email,))
        conn.commit()
        conn.close()

        return f"User with email {email} has been successfully deleted", True
    except Exception as e:
        return f"Error occurred while deleting user: {str(e)}", False
    finally:
        if conn:
            conn.close()