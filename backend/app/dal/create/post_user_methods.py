from ....db import db_connection

def create_user_with_phone(data):
    try:
        conn = db_connection()
        cursor = conn.cursor()
        query = """
        INSERT INTO users (first_name, last_name, email, phone_number, pw)
        VALUES (?, ?, ?, ?, ?)
        """
        cursor.execute(query, (data['first_name'],data['last_name'],data['email'],data['phone_number'],data['pw'],))
        conn.commit()
        conn.close()
        return f"User: {data['first_name']} {data['last_name']} was created successfully"
    except Exception as err:
        return f"An error has occurred in the DAL: {err}"
    finally:
        if conn:
            conn.close()
    
def create_user_without_phone(data):
    try:
        conn = db_connection()
        cursor = conn.cursor()
        query = """
        INSERT INTO users (first_name, last_name, email, pw)
        VALUES (?, ?, ?, ?)
        """
        cursor.execute(query, (data['first_name'],data['last_name'],data['email'],data['pw'],))
        conn.commit()
        conn.close()
        return f"User: {data['first_name']} {data['last_name']} was created successfully"
    except Exception as err:
        return f"An error has occurred in the DAL: {err}"
    finally:
        if conn:
            conn.close()