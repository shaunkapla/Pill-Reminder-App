import re

def verify_user_creation(data):
    """
    Helper function used to validate the api body data and make sure it has the following fields:
        - first_name
        - last_name
        - email
        - password (pw)
    and makes sure that the email is of a proper format

    inputs:
        - data: This is the data that is passed through the api

    outputs:
        Boolean: This boolean is only returned true if the data matches what is expected
        Message: This is the return message on what didn't validate
    """
    required_fields = ['first_name', 'last_name', 'email', 'pw']
    for field in required_fields:
        if field not in data:
            return False, f"{field} is required."
        
    if not verify_email(data['email']):
        return False, "Invalid email format."    
    
    return True, ""

def verify_email(email):
    """
    Helper function for validating that the email address is of proper format

    inputs:
        - email: The email waiting to be validated

    outputs:
        - Boolean: True is matches regular expression, False if not
    """
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None