from flask_restplus import Namespace, fields

class AuthenticationDTO():
    """Authentication Data Transfer Object."""
    
    auth_namespace = Namespace("Authentication Endpoint", description="Deals with user registration and user login.")
    user_registration_model = auth_namespace.model("User Registration Model", {
        "first_name": fields.String(description="User's first name."),
        "last_name": fields.String(description="User's last name."),
        "username": fields.String(description="Username."),
        "email": fields.String(description="User's email."),
        "password1": fields.String(description="Entered password."),
        "password2": fields.String(description="Confirm password")
    })
    user_login_model = auth_namespace.model("User Login Model", {
        "username": fields.String(description="Username."),
        "password": fields.String(description="Username password.")
    })
