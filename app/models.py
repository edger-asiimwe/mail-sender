from . import login_manager
from flask_login import UserMixin

class User(UserMixin):
    
    def __init__(self, user):
        self.user = user

    def name(self):
        return self.user['username']

    def getId(self):
        return self.user['userID']

    @login_manager.user_loader
    def user_loader(self, user_id):
        return User().getId()