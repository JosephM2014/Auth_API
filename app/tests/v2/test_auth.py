from .basecase import TestBaseCase as base

# Standard Import.
import json

class TestAuthentication(base):
    def setUp(self):
        base.setUp(self)

    def test_user_registration(self):
        req = self.client.post("/api/v2/laicare/auth/register", data=json.dumps(self.registration_payload), content_type=self.content_type)
        resp_data = json.loads(req.data.decode())
        self.assertEqual(req.status_code, 201)
        self.assertEqual(resp_data["message"], "User created successfully.")

    def test_user_login(self):
        req = self.client.post("/api/v2/laicare/auth/login", data=json.dumps(self.login_payload), content_type=self.content_type)
        resp_data = json.loads(req.data.decode())
        self.assertEqual(req.status_code, 200)
        self.assertEqual(resp_data["message"], "Login Successful.")

    def tearDown(self):
        base.tearDown(self)
        