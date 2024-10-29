from werkzeug.security import generate_password_hash
from ....db import db_connection

def update_user_information(email, first_name=None, last_name=None, phone_number=None, password=None):
    """
    
    """
    fields = []
    params = []

    if first_name is not None:
        fields.append("first_name = ?")
        params.append(first_name)
    if last_name is not None:
        fields.append("last_name = ?")
        params.append(last_name)
    if phone_number is not None:
        fields.append("phone_number = ?")
        params.append(phone_number)
    if password is not None:
        hashed_password = generate_password_hash(password)
        fields.append("pw = ?")
        params.append(hashed_password)

    params.append(email)
    
    if fields:
        try:
            conn = db_connection()
            cursor = conn.cursor()
            query = f"UPDATE users SET {', '.join(fields)} WHERE email = ?"
            cursor.execute(query, params)
            conn.commit()

            if cursor.rowcount == 0:
                return {'message': 'User not found'}, 404
            return {'message': 'User information updated successfully'}, 200
        except Exception as e:
            return {'message': str(e)}, 500
        finally:
            conn.close()
