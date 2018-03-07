class User(object):
    """The class data models. storea application data in data structures"""
    self.users = {}
    self.user_token = {}

    def __init__(self, username, email, password):
        self.username = username
        self.email=email
        self.password=password

    def add_user(self, username, password, first_name, last_name, admin=False):
        """Creates a new user and append to the list of users"""
        data = {'id': uuid.uuid4(), 'username': username, 'password': password,
                'first_name': first_name, "last_name": last_name, "admin": admin}
        self.users[username] = data
        return self.users