"""
This file will deal with the exposed endpoints that the 
front end will use for all things user related.

Endpoints:
1. create_user: This endpoint will create a user in the database
2. get_user_info: This endpoint will get all the information related to the user
3. get_user_login: This endpoint will get the users username and password for validation
4. delete_user: This endpoint will remove a user from the database
5. update_user_info: This endpoint will update the users information
6. update_user_username: This endpoint will update the users username
7. update_user_password: This endpoint will update the users password
"""
from flask import request, jsonify
from .helper_functions.verify_user_interactions import verify_user_creation
from ..services.user_services import create_user_without_phone, create_user_with_phone
from ..services.common_errors import UserAlreadyExistsError
from . import api_bp

@api_bp.route('/create_user', methods=["POST"])
def create_user():
    data = request.json
    is_valid_data, message = verify_user_creation(data)

    if not is_valid_data:
        return jsonify({"error": message}), 400
    if 'phone_number' not in data:
        try:
            user = create_user_without_phone(data)
            return jsonify(user), 200
        except UserAlreadyExistsError:
            return jsonify({"error": "Email already exists."}), 409
        except Exception as e:
            print(f"Error creating user: {e}")
            return jsonify({"error": "Failed to create user."}), 500
    try:
        user = create_user_with_phone(data)
        return jsonify(user), 200
    except UserAlreadyExistsError:
        return jsonify({"error": "Email already exists."}), 409
    except Exception as e:
        print(f"Error creating user: {e}")
        return jsonify({"error": "Failed to create user."}), 500