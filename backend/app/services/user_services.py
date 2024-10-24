from .common_errors import UserAlreadyExistsError, UserDoesntExistError
from ..dal.read.get_user_methods import get_user_by_email
from ..dal.create.post_user_methods import create_user_without_phone, create_user_with_phone

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

def get_user_service(email):
    user = get_user_by_email(email)
    if user == None:
        raise UserDoesntExistError(f"{email} doesn't exist in the database.")
    
    return {
        'first_name': user['first_name'],
        'last_name': user['last_name'],
        'email': user['email'],
        'phone': user['phone_number'],
        'password': user['pw']
    }

if __name__ == "__main__":
    info = {
        "first_name": "Shaun",
        "last_name": "Kapla",
        "email": "email@email.com",
        "pw": "password"
    }
    print(create_user_wo_phone(info))