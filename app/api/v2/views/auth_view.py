# Local Imports.
from ..models.auth_model import Auth
from ..utils.serializer import AuthenticationDTO
# Standard Library Imports.
import json
# Third Party Imports.
from flask import Response
from flask_restplus import reqparse, Resource

auth_api = AuthenticationDTO.auth_namespace

# Parser.
parser = reqparse.RequestParser()
parser.add_argument('first_name', type=str, help="Enter your firstname", required=True)
parser.add_argument('last_name', type=str, help="Enter your lastname", required=True)
parser.add_argument('username', type=str, help="Enter your username", required=True)
parser.add_argument('email', type=str, help="Enter your email", required=True)
parser.add_argument('password1', type=str, help="Enter your password", required=True)
parser.add_argument('password2', type=str, help="Confirm your password", required=True)

registration_model = AuthenticationDTO.user_registration_model
login_model = AuthenticationDTO.user_login_model

@auth_api.route('/register')
class UserRegistration(Resource):
    @auth_api.expect(registration_model, validate=True)
    def post(self):
        req_data = parser.parse_args()
        user_data = dict(
            first_name=req_data["first_name"],
            last_name=req_data["last_name"],
            username=req_data["username"],
            email=req_data["email"],
            password1=req_data["password1"],
            password2=req_data["password2"]
        )
        register_user = Auth.user_registration(self, data=user_data)
        resp_payload = dict(
            status=201,
            message="User registered successfully.",
            registered_user=register_user
        )
        resp = Response(json.dumps(resp_payload), status=201, mimetype="application/json")
        return resp
@auth_api.route("/login")
class UserLogin(Resource):
    @auth_api.expect(login_model, validate=True)
    def post(self):
        login_parser = reqparse.RequestParser()
        login_parser.add_argument('username', type=str, required=True, help="Enter username")
        login_parser.add_argument('password', type=str, required=True, help="Enter password")

        req_data = login_parser.parse_args()
        check_for_user = Auth.user_login(self, username=req_data["username"])
        if check_for_user:
            resp_payload = dict(
                status=200,
                logged_in="You're logged in as {}.".format(req_data["username"]),
                message="Login successful."
            )
            resp = Response(json.dumps(resp_payload), status=200, mimetype="application/json")
            return resp
            