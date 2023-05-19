import jwt
import mysql.connector
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Database connection configuration
db_config = {
    'user': os.getenv('MYSQL_USER'),
    'password': os.getenv('MYSQL_PASSWORD'),
    'host': os.getenv('MYSQL_HOST'),
    'database': os.getenv('MYSQL_DATABASE'),
    'port': os.getenv('MYSQL_PORT')
}

secret_key = os.getenv('SECRET_KEY')

def verify_token(token):
    try:
        # Decode the JWT token
        decoded_token = jwt.decode(token, secret_key, algorithms=['HS256'])
        username = decoded_token.get('username')
        password = decoded_token.get('password')
        # Connect to the MySQL database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Execute the SQL query to check if the username and password combination exists
        query = "SELECT * FROM users WHERE name = %s AND password = %s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()

        # Close the database connection
        cursor.close()
        conn.close()

        # Check the result and return the appropriate response
        if result:
            return True
        else:
            return False
    except jwt.DecodeError:
        return False

@app.route('/check_user', methods=['POST'])
def check_user():
    request_body = request.get_json()

    if 'token' not in request_body:
        return jsonify({'message': 'Token is missing'}), 400
    token = request_body['token']

    if verify_token(token):
        return jsonify({'message': 'User is present'}), 200
    else:
        return jsonify({'message': 'User is not present'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=True)

