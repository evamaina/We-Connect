from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import uuid

app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisissecret'

users = []
business_list = []

"""
Register route and function 
register user: a method that adds a user to the system
"""

@app.route('/api/auth/register', methods=['POST'])
def register_user():
    request_data = request.get_json()
    user = {'username': request_data['username'], 'password': request_data['password'], 'id': len(users) + 1}
    username = request_data['username']

    if (len(users) > 0):
        for x, k in enumerate(users):
            if k['username'] == username:
                return jsonify({'Message': "Username already exists : " + username}), 409
            else:
                users.append(user)
                return jsonify({'Message': 'User registered successfully'}), 201
    else:
        users.append(user)
        return jsonify({'Message': 'User registered successfully'}), 201

        """
    Login route and function 
    login: a method that allws user to login
    """


@app.route('/api/auth/login', methods=['POST'])
def login_user():
    request_data = request.get_json()
    username = request_data['username']
    password = request_data['password']

    for x, k in enumerate(users):
        if k['username'] == username and k['password'] == password:
            return jsonify({'Message': "User :" + username + " logged in Successfuly"}), 201
    else:
        return jsonify({'Message': 'User does not exist or wrong username/password.'}), 401


    """
    Business route and function 
    register business: a method that adds a busness to the list.
    """


@app.route('/api/business', methods=['POST'])
def register_business():
    request_data = request.get_json()
    business = {'business_name': request_data['business_name'], 'country': request_data['country'],
                'id': len(business_list) + 1}
    business_name = request_data['business_name']


    if (len(business_list) > 0):
        for x, k in enumerate(business_list):
            if k['business_name'] == business_name:
                return jsonify({'Message': "business already exists, use a different name from : " + business_name}), 200
            else:
                business_list.append(business)
                return jsonify({'Message': 'Business registered successfully'}), 201
    else:
        business_list.append(business)
        return jsonify({'Message': 'business registered successfully'}), 201

         """
        tests that a business can be updated by the user
        """

@app.route('/api/businesses/<businessId>', methods=['PUT'])
def update_business(businessId):
    request_data = request.get_json()
    business_Id=businessId
    if (len(business_list) > 0):
        for k in range(0,len(business_list)):
            if business_list[k]['id'] == business_Id:
                business_list[k]['business_name']=request_data['business_name']
                business_list[k]['country']=request_data['country']
                return jsonify({'Message': "business updated" }), 200

        return jsonify({'Message': 'Business does not exist'}), 404
    else:
        return jsonify({'Message': 'No business record in the system'}), 404



@app.route('/api/auth/reset-password', methods=['POST'])
def reset_password():
    request_data = request.get_json()
    username = request_data['username']
    old_password = request_data['old_password']
    new_password = request_data['new_password']

    for x, k in enumerate(users):
        if k['username'] == username and k['password'] == old_password:
            k['password']=new_password

            return jsonify({'Message': "User :" + username + " password-reset done Successifuly"}), 200
    else:
        return jsonify({'Message': 'Enter the new password and try again.'}), 401





if __name__ == '__main__':
    app.run(debug=True)






