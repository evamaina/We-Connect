from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from validate_email import validate_email
import os
import sys
import inspect


currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from models.users import User
from models.business import Business
from models.reviews import Reviews


app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisissecret'


"""
Register route and function
register user: a method that adds a user to the system
"""
user = User()
reviews = Reviews()
users = user.users
business = Business()
business_list = business.businesses
review = Reviews()
reviews = review.reviews

@app.route('/api/auth/register', methods=['POST'])
def register_user():
    request_data = request.get_json()
    id = len(user.users) + 1
    username = request_data['username']
    email = request_data['email']
    is_valid_email = validate_email(email)
    if not (is_valid_email):
        return jsonify({'Message': 'Please enter correct emaill and try again '}),401

    password = request_data['password']

    for x, k in enumerate(users):
        if (k['username'] == username or k['email'] == email):
            return jsonify({'Message': 'User already exist'}), 200
    user.create_user(id, username, email, password)


    return jsonify({
        'Message': 'User created',
        'user': user.users[-1]
        }), 201


@app.route('/api/auth/login', methods=['POST'])
def login_user():
    request_data = request.get_json()
    username_or_email = request_data['username_or_email']
    password = request_data['password']

    for x, k in enumerate(users):
        if (k['username'] == username_or_email or k['email'] == username_or_email) and k['password'] == password:
            if k['login_status']==True:
                return jsonify({'Message': "User :" + username_or_email + " is already logged in"}), 201

            k['login_status'] = True
            return jsonify({'Message': "User :" + username_or_email + " logged in Successfuly"}), 201
    return jsonify({'Message': 'User does not exist or wrong username/password.'}), 401


@app.route('/api/auth/logout', methods=['POST'])
def logout_user():
    request_data = request.get_json()
    username_or_email = request_data['username_or_email']
    for x, k in enumerate(users):
        if (k['username'] == username_or_email or k['email'] == username_or_email) and k['login_status']==True:
            k['login_status'] = False
            return jsonify({'Message': 'User logged out successfully.'}), 200
    return jsonify({'Message': 'User is not logged in, please login.'}), 401


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
    business_Id = businessId
    if (len(business_list) > 0):
        for k in range(0, len(business_list)):
            if business_list[k]['id'] == business_Id:
                business_list[k]['business_name'] = request_data['business_name']
                business_list[k]['country'] = request_data['country']
                return jsonify({'Message': "business updated"}), 200

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
            k['password'] = new_password

            return jsonify({'Message': "User :" + username + " password-reset done Successifuly"}), 200
    else:
        return jsonify({'Message': 'Enter the new password and try again.'}), 401


@app.route('/api/auth/users', methods=['GET'])
def get_all_users():
    return jsonify(user.users), 200


@app.route('/api/businesses/<businessId>/reviews', methods=['POST'])
def add_review():
    request_data = request.get_json()
    id = len(review.reviews) + 1
    username = request_data['username']
    title = request_data['title']
    review = request_data['review']

    for x, k in enumerate(users):
        if (k['username'] == username or k['review'] == review):
            return jsonify({'Message': 'Review added successfully'}), 200
    review.add_review(id, username, title, review)

    return jsonify({
        'Message': 'review created',
        'user': review.reviews[-1]
        }), 201

@app.route('/api/businesses/<businessId>/reviews', methods=['GET'])
def get_all_reviews():
    return jsonify(review.reviews), 200

@app.route('/api/businesses', methods=['GET'])
def retrive_all_businesses():
    return jsonify(business.businesses), 200



# @app.route('/api/businesses/<businessId>', methods=['DELETE'])
# def remove_business(businessId):
#     business_id = request_data(businessId)

#     for x, k in enumerate(business_list):
#             if k['business_id'] == business_id:
#                 del business.businesses[business['name']] 
#                 return jsonify({'Message': "Business deleted successfully from : " + business_name}), 200
#     return jsonify({"Message": "Business not found"}), 401

        


if __name__ == '__main__':
     app.run(debug=True)


