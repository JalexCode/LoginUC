class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    def is_username(self, value):
        return self.username == value 