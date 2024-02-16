import flask
from flask import jsonify, request, session
from flask_cors import CORS
# from flask_login import current_user, login_required, login_user, logout_user, LoginManager
import pymysql
# from models import User
from datetime import datetime
import hashlib
# import random
 
app = flask.Flask(__name__, template_folder='../frontend')
app.config['SECRET_KEY'] = '123456'

cors = CORS(app)

# login_manager = LoginManager()
# login_manager.init_app(app)

db = pymysql.connect(host='34.27.57.204', port=3306, charset='utf8', database="data", user='root', password='mysql')
cursor = db.cursor()

user = {'id' :'', 'username': ''}
event = {'id': '', 'name': '', 'description': '', 'organizer_id': '', 'date': '', 'start_time': '', 'end_time': ''}

# @login_manager.user_loader
# def load_user(id, username):
#     return User(id, username)
 
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
        events = []
        for result in results:
            event = {'event_id': result[0], 'name': result[1], 'description': result[2], 'date': result[4].strftime('%Y-%m-%d'),
                     'start_time': str(result[5])[:5], 'end_time': str(result[6])[:5], 'code': result[7]}
            events.append(event)
        ret_data = {'username': user['username'], 'events': events}
        return jsonify(ret_data)
    if request.method == 'POST':
        req_data = request.get_data()
        event_id = req_data.decode()
        # print("code:", code)
        # isValid = False
        error = ''
        sql = f"select code from events where id='{event_id}'"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
        # if not result:
        #     error = 'Invalid Code'
        #     # print("error code:", code)
        # else:
        #     isValid = True
        #     print("event name:", result[1])
        #     # event['id'], event['name'], event['description'], event['organizer_id'],
        #     # event['date'], event['start_time'], event['end_time'] = result
        ret_data = {'valid': True, 'code': result[0], 'msg': error}
        return jsonify(ret_data)

def gen_code(event_id):
    hash_code = hashlib.md5(str(event_id).encode())
    code = hash_code.hexdigest()[:6]
    return code

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
        code = gen_code(inserted_id)
        update = f"update events set code='{code}' where id={inserted_id}"
        cursor.execute(update)
        db.commit()
        ret_data = {'username': user['username'], 'code': code}
        return jsonify(ret_data)

@app.route('/code', methods=['GET'])
def code():
    ret_data = {'username': user['username']}
    return jsonify(ret_data)

@app.route('/join', methods=['GET', 'POST'])
def join():
    if request.method == 'POST':
        req_data = request.get_data()
        code = req_data.decode()
        # print("code:", code)
        isValid = False
        error = ''
        sql = f"select * from events where code='{code}'"
        cursor.execute(sql)
        result = cursor.fetchone()
        if not result:
            error = 'Invalid Code'
            # print("error code:", code)
        else:
            isValid = True
            print("event name:", result[1])
            # event['id'], event['name'], event['description'], event['organizer_id'],
            # event['date'], event['start_time'], event['end_time'] = result
        ret_data = {'valid': isValid, 'msg': error}
        return jsonify(ret_data)
    
@app.route('/event', methods=['POST'])
def event():
    is_user = False
    req_data = request.get_json()
    code = req_data['code']
    print("code:", code)
    sql = f"select * from events where code='{code}'"
    cursor.execute(sql)
    results = cursor.fetchone()
    event_id = results[0]
    form = req_data['type']
    if form == "question":
        question = req_data['question']
        if question:
            sql = f"insert into questions (question, event_id, votes, answered) values ('{question}', '{event_id}', 0, 0)"
            cursor.execute(sql)
            db.commit()
    if form == "vote":
        question_id = req_data['question_id']
        isUpvote = req_data['isUpvote']
        # print(question_id, isUpvote)
        if isUpvote:
            update = f"update questions set votes=votes+1 where id='{question_id}'"
        else:
            update = f"update questions set votes=votes-1 where id='{question_id}'"
        cursor.execute(update)
        db.commit()
    if form == "mark":
        question_id = req_data['question_id']
        isMarked = req_data['isMarked']
        print(question_id, isMarked)
        if isMarked:
            update = f"update questions set answered=0 where id='{question_id}'"
        else:
            update = f"update questions set answered=1 where id='{question_id}'"
        cursor.execute(update)
        db.commit()
    sql = f"select * from questions where event_id='{event_id}'"
    cursor.execute(sql)
    questions = cursor.fetchall()
    # print("last question:", questions[-1][1])
    sql = f"select * from event_organizer where id='{event_id}'"
    cursor.execute(sql)
    result = cursor.fetchone()
    organizer = result[8]
    event = {'name': result[1], 'description': result[2], 'date': result[4].strftime('%Y-%m-%d'),
                    'start_time': str(result[5])[:5], 'end_time': str(result[6])[:5]}
    ret_data = {'questions': questions, 'organizer': organizer, 'event': event, 'isUser': is_user}
    return jsonify(ret_data)


# @app.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return 'Logged out successfully.'


if __name__ == '__main__':
    app.run(debug=True)