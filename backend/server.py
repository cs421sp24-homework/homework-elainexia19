import flask
import pymysql
 
app = flask.Flask(__name__, template_folder='../frontend')

db = pymysql.connect(host='34.27.57.204', port=3306, charset='utf8', database="data", user='root', password='mysql')
cursor = db.cursor()
 
@app.route('/', methods=['GET'])
def hello_world():
    sql = 'select example from test'
    cursor.execute(sql)
    result = cursor.fetchone()
    # print(result)
    return flask.render_template('index.html', msg=result)
 
if __name__ == '__main__':
    app.run(debug=True)