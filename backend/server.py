import flask
from flask import jsonify, request, session, render_template
from flask_cors import CORS
from flask_login import current_user, login_required, login_user, logout_user, LoginManager
import pymysql
from models import User
from datetime import datetime
import random
 
app = flask.Flask(__name__, template_folder='../frontend')
app.config['SECRET_KEY'] = '123456'

cors = CORS(app)

login_manager = LoginManager()
login_manager.init_app(app)

db = pymysql.connect(host='34.27.57.204', port=3306, charset='utf8', database="data", user='root', password='mysql')
cursor = db.cursor()

user = {'id' :'', 'username': ''}

@login_manager.user_loader
def load_user(id, username):
    return User(id, username)
 
@app.route('/', methods=['GET'])
def hello_world():
    # sql = 'select example from test'
    # cursor.execute(sql)
    # result = cursor.fetchone()
    # print(result)
    return "Hello World"

@app.route('/login', methods=['GET', 'POST'])
def login():
    # if request.method == 'GET':
    #     return render_template('index.html')
    if request.method == 'POST':
        req_data = request.get_json()
        username = req_data['username']
        password = req_data['password']
        isLoggedIn = False
        error = ''
        sql = f"select * from organizer where username='{username}' and password='{password}'"
        cursor.execute(sql)
        result = cursor.fetchone()
        if result:
            # print(result[0], result[1])
            user['id'] = result[0]
            user['username'] = result[1]
            # user = load_user(result[0], result[1])
            # login_user(user)
            isLoggedIn = True
        else:
            error = 'Incorrect username or password'
        ret_data = {'loggedin': isLoggedIn, 'msg': error}
        return jsonify(ret_data)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    # if request.method == 'GET':
    #     return render_template('index.html')
    if request.method == 'POST':
        req_data = request.get_json()
        username = req_data['username']
        password = req_data['password']
        email = req_data['email']
        isSignedUp = False
        error = ''
        sql = f"select * from organizer where username='{username}'"
        cursor.execute(sql)
        result = cursor.fetchone()
        if result:
            error = 'Username already exists'
        else:
            isSignedUp = True
            if email:
                sql1 = f"insert into organizer (username, password, email) values ('{username}', '{password}', '{email}')"
            else:
                sql1 = f"insert into organizer (username, password) values ('{username}', '{password}')"
            cursor.execute(sql1)
            db.commit()
            print("account created", username, password, email)
        ret_data = {'signedup': isSignedUp, 'msg': error}
        return jsonify(ret_data)
    
@app.route('/home', methods=['GET', 'POST'])
# @login_required
def home():
    if request.method == 'GET':
        if user['id'] == '':
            ret_data = {'username': user['username']}
            return jsonify(ret_data)
        sql = f"select * from events where organizer_id='{user['id']}'"
        cursor.execute(sql)
        results = cursor.fetchall()
        # print("events:", results)
        # event = results[0]
        # print(event[4])
        # print(event[4].strftime(fd))
        # print(event[5])
        # print(str(event[5]))
        events = []
        for result in results:
            event = {'name': result[1], 'description': result[2], 'date': result[4].strftime('%Y-%m-%d'),
                     'start_time': str(result[5])[:5], 'end_time': str(result[6])[:5], 'code': result[7]}
            events.append(event)
        ret_data = {'username': user['username'], 'events': events}
        return jsonify(ret_data)
    
@app.route('/create_event', methods=['GET', 'POST'])
def create_event():
    if request.method == 'GET':
        ret_data = {'username': user['username']}
        return jsonify(ret_data)
    if request.method == 'POST':
        req_data = request.get_json()
        name = req_data['name']
        description = req_data['description']
        date = req_data['date']
        start_time = req_data['start_time']
        end_time = req_data['end_time']
        print("event created", date, start_time, end_time, description)
        if description:
            sql = f"insert into events (name, description, organizer_id, date, start_time, end_time) \
                values ('{name}', '{description}', {user['id']}, '{date}', '{start_time}', '{end_time}')"
        else:
            sql = f"insert into events (name, organizer_id, date, start_time, end_time) \
                values ('{name}', {user['id']}, '{date}', '{start_time}', '{end_time}')"
        cursor.execute(sql)
        inserted_id = cursor.lastrowid
        db.commit()
        digits = len(str(inserted_id))
        event_id = '0' * (3 - digits) + str(inserted_id)
        code = ''
        for i in range(3):
            code += str(random.randint(0, 9))
            code += event_id[i]
        formatted_code = code[:3] + '-' + code[3:]
        print(formatted_code)
        update = f"update events set code='{formatted_code}' where id={inserted_id}"
        cursor.execute(update)
        db.commit()
        ret_data = {'username': user['username'], 'code': formatted_code}
        return jsonify(ret_data)

@app.route('/code', methods=['GET', 'POST'])
def code():
    if request.method == 'GET':
        ret_data = {'username': user['username']}
        return jsonify(ret_data)

# @app.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return 'Logged out successfully.'


if __name__ == '__main__':
    app.run(debug=True)