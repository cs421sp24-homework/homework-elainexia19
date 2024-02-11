import pymysql
import hashlib

db = pymysql.connect(host='34.27.57.204', port=3306, charset='utf8', database="data", user='root', password='mysql')
cursor = db.cursor()

class User():

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username

class Event():

    def __init__(self, name, description, organizer_id, date, start_time, end_time):
        self.name = name
        self.description = description
        self.organizer_id = organizer_id
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
    
    def createEvent(self):
        if self.description:
            sql = f"insert into events (name, description, organizer_id, date, start_time, end_time) \
                values ('{self.name}', '{self.description}', {self.organizer_id}, '{self.date}', \
                '{self.start_time}', '{self.end_time}')"
        else:
            sql = f"insert into events (name, organizer_id, date, start_time, end_time) \
                values ('{self.name}', {self.organizer_id}, '{self.date}', '{self.start_time}', '{self.end_time}')"
        cursor.execute(sql)
        self.event_id = cursor.lastrowid
        self.generateCode()
        db.commit()

    def generateCode(self):
        hash_code = hashlib.md5(str(self.event_id).encode())
        code = hash_code.hexdigest()[:6]
        self.code = code[:3] + '-' + code[3:]
