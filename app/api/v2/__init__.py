# Third party imports
from flask_restplus import Api
from flask import Blueprint

# Local Imports
from .views.auth_view import auth_api

version2 = Blueprint('Authentication', __name__, url_prefix="/api/v2/laicare")

api = Api(version2, version="2.0", title="Authentication",
          description="Authentication API.", doc="/docs")


api.add_namespace(auth_api, path="/auth")
