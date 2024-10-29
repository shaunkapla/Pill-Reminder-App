"""
This file will deal with the exposed endpoints that the 
front end will use for all things user related.

Endpoints:
1. create_user: This endpoint will create a user in the database
2. get_user_info: This endpoint will get all the information related to the user
3. get_user_login: This endpoint will get the users username and password for validation
4. delete_user: This endpoint will remove a user from the database
5. update_user_info: This endpoint will update the users information
"""
from flask import request, jsonify
from .helper_functions.verify_user_interactions import verify_user_creation
from ..services.user_services import (
    create_user_without_phone, 
    create_user_with_phone,
    get_user_service,
    delete_user_service,
    update_user_service
    )
from ..services.common_errors import UserAlreadyExistsError, UserDoesntExistError
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
    
@api_bp.route('/get_user', methods=['GET'])
def get_user():
    """
    
    """
    email = request.args.get('email')
    user = get_user_service(email)

    return user

@api_bp.route('/delete_user', methods=['DELETE'])
def delete_user():
    """
    API endpoint to delete a user by email
    """
    user_email = request.args.get('email')
    
    if not user_email:
        return 'Error: Argument for user was passed improperly', 400
    
    try:
        deleted_user_message = delete_user_service(user_email)
        return jsonify({"message": deleted_user_message}), 200
    except UserDoesntExistError:
        return jsonify({"error": "User doesn't exist in the database."}), 409
    except Exception as e:
        print(f"Error deleting user: {e}")
        return jsonify({"error": "Failed to delete user."}), 500
    
@api_bp.route('/update_user', methods=['PATCH'])
def update_user():
    data = request.get_json()
    email = data.get('email')
    response, status = update_user_service(
        email,
        first_name=data.get('first_name'),
        last_name=data.get('last_name'),
        phone_number=data.get('phone_number'),
        password=data.get('pw')
    )
    return jsonify(response), status