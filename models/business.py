from flask import Flask, jsonify, request

class Business():

    def __init__(self):
        self.businesses = []

    def add_business(self, id, name, category, country):
        new_business = {
           'id': id,
           'name': name,
           'category': category,
           'country': country,
           }

        self.users.append(new_user)

        return self.businesses
