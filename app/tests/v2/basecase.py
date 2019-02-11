# Local Import.
from ... import create_app
from ...database import create_tables, drop_tables
# Standard Library Import.
import unittest

class TestBaseCase(unittest.TestCase):
    def setUp(self):
        self.client = create_app(config_name="testing").test_client()
        create_tables()
        self.content_type = 'application/json'
        self.registration_payload = dict(
            first_name="Test",
            last_name="User",
            username="test_user",
            email="testuser@gmail.com",
            password1="Test@123",
            password2="Test@123"
        )
        self.login_payload = dict(
            username="test_user",
            password="Test@123"
        )
    
    def tearDown(self):
        self.client = None
        self.content_type = None
        self.registration_payload = None
        self.login_payload = None
        drop_tables( )
        