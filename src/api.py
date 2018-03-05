from flask import Flask, request, jsonify
import uuid
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisissecret'

users = []
business_list = []


@app.route('/api/auth/register', methods=['POST'])
def register_user():
    request_data = request.get_json()
    user = {'username': request_data['username'], 'password': request_data['password'], 'id': len(users) + 1}
    username = request_data['username']

    if (len(users) > 0):
        for x, k in enumerate(users):
            if k['username'] == username:
                return jsonify({'Message': "Username already exists : " + username}), 200
            else:
                users.append(user)
                return jsonify({'Message': 'User registered successfully'}), 201
    else:
        users.append(user)
        return jsonify({'Message': 'User registered successfully'}), 201


@app.route('/api/auth/login', methods=['POST'])
def login_user():
    request_data = request.get_json()
    username = request_data['username']
    password = request_data['password']

    for x, k in enumerate(users):
        if k['username'] == username and k['password'] == password:
            return jsonify({'Message': "User :" + username + " logged in Successifuly"}), 201
    else:
        return jsonify({'Message': 'User does not exist or wrong username/password.'}), 404






if __name__ == '__main__':
    app.run(debug=True)
    