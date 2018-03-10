from flask import Flask, jsonify, request


class User(object):

  def __init__(self):
    self.users=[]
    
  def create_user(self, id, username, email, password):
    new_user = {
           'id': id,
           'username': username,
           'email': email,
           'password': password,
           'login_status':False
           }

    self.users.append(new_user)

    return self.users
