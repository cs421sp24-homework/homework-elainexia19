from flask_login import UserMixin
import pymysql

# db = pymysql.connect(host='34.27.57.204', port=3306, charset='utf8', database="data", user='root', password='mysql')
# cursor = db.cursor()

class User(UserMixin):

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username

    def get_id(self):
        return self.id

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False
