from .common_errors import UserAlreadyExistsError, UserDoesntExistError
from ..dal.read.get_user_methods import (
    get_user_by_email,
    get_user_credentials_by_email
)
from ..dal.create.post_user_methods import (
    create_user_without_phone, 
    create_user_with_phone
)
from ..dal.delete.delete_user_methods import delete_user_by_email
from ..dal.update.update_user_methods import update_user_information
from werkzeug.security import check_password_hash

def create_user_wo_phone(data):
    user_exists = get_user_by_email(data['email'])
    if user_exists:
        raise UserAlreadyExistsError(f"{data['email']} is already an email in the database.")
    
    message = create_user_without_phone(data)

    return message

def create_user_w_phone(data):
    user_exists = get_user_by_email(data['email'])
    if user_exists:
        raise UserAlreadyExistsError(f"{data['email']} is already an email in the database.")
    
    message = create_user_with_phone(data)
    return message

def validate_user_login(email, password):
    user_credentials = get_user_credentials_by_email(email)
    if user_credentials is None:
        return {'message': 'Invalid email or password'}, 401

    if check_password_hash(user_credentials[1], password):

        user_info = get_user_by_email(email)
        return {
            'user_id': user_info[0],
            'first_name': user_info[1],
            'last_name': user_info[2],
            'email': user_info[3],
            'phone_number': user_info[4],
            'message': 'Login successful'
        }, 200
    else:
        return {'message': 'Invalid email or password'}, 401

def delete_user_service(email):
    message, success = delete_user_by_email(email)
    
    if not success and "No user found" in message:
        raise UserDoesntExistError(message)
    
    if not success:
        raise Exception(message)
    
    return message

def update_user_service(email, first_name=None, last_name=None, phone_number=None, password=None):
    res, status = update_user_information(email, first_name, last_name, phone_number, password)
    return res, status