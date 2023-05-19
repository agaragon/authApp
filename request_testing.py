import unittest
import requests
import jwt

class JWTTokenVerificationTest(unittest.TestCase):
    base_url = 'http://localhost:5000'
    token = None

    @classmethod
    def setUpClass(cls):
        # Generate the JWT token with the username and password information
        payload = {'username': 'andre', 'password': '123456'}
        cls.token = jwt.encode(payload, 'secret_key', algorithm='HS256')

    def test_check_user_exists(self):
        # Send a POST request to the /check_user endpoint with the JWT token
        response = requests.post(f'{self.base_url}/check_user', json={'token': self.token})

        # Assert that the response status code is 200
        self.assertEqual(response.status_code, 200)
        # Assert that the response message indicates the user is present
        self.assertEqual(response.json()['message'], 'User is present')

    def test_check_user_not_exists(self):
        # Modify the JWT token payload to simulate a non-existent user
        payload = {'username': 'nonexistent_user', 'password': '123456'}
        token = jwt.encode(payload, 'secret_key', algorithm='HS256')

        # Send a POST request to the /check_user endpoint with the modified JWT token
        response = requests.post(f'{self.base_url}/check_user', json={'token': token})

        # Assert that the response status code is 404
        self.assertEqual(response.status_code, 404)
        # Assert that the response message indicates the user is not present
        self.assertEqual(response.json()['message'], 'User is not present')

if __name__ == '__main__':
    unittest.main()
