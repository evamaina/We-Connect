from flask import Flask, jsonify, request

class Business():

    def __init__(self):
        self.businesses = []

    def add_business(self, id, name, category, location):
        new_business = {
           'id': id,
           'name': name,
           'category': category,
           'location': location,
           }

        self.users.append(new_user)

        return self.businesses