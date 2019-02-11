# Local Imports.
from app import create_app
# Standard Library Import.
import os

APP = create_app(os.getenv("APP_SETTINGS"))

if __name__ == '__main__':
    APP.run()
    