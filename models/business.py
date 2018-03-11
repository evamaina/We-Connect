from flask import Flask, jsonify, request

class Business(object):

    def __init__(self):
        self.businesses = []

    def add_business(self, id, name, category, country,userid):
        new_business = {
           'id': id,
           'name': name,
           'category': category,
           'country': country,
           'userid':userid
           }

        self.users.append(new_user)

        return self.businesses
