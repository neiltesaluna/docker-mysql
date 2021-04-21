from flask import Flask,render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
import pymysql

app = Flask('__main__')

dbuser = os.environ.get('MYSQL_USER')
dbpassword = os.environ.get('MYSQL_PASSWORD')
dbname = os.environ.get('MYSQL_DATABASE')

dbpath = f'mysql+pymysql://{dbuser}:{dbpassword}@database:3306/{dbname}?charset=utf8mb4'

app.config['SQLALCHEMY_DATABASE_URI'] = dbpath
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Greetings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sayhi = db.Column(db.String(20), nullable=False)

# creating database tables
db.create_all()


def receive_response(param):

    # check if json data
    try:
        data = request.get_json(force=True)
        data = data.get(param)

    except:
        # check if form data
        if request.form.get(param):
            data = request.form.get(param)

        #check if query string data
        elif request.args.get(param):
            data = request.args.get(param)

        else:
            data = 'data not found!'

    return data



@app.route('/', methods=['GET'])
def home():
    
    try:
        greetings = Greetings.query.all()
        
    except:
        greetings = [{'sayhi':'I can\'t understand you, seems like the database is empty'}]


    return render_template('index.html', greetings = greetings)


@app.route('/add', methods=['POST'])
def add():

    data = receive_response('greeting')

    greeting = Greetings(sayhi=data)
    db.session.add(greeting)
    db.session.commit()

    return f'The database has been updated with {data}\n'

@app.route('/methods', methods=['GET', 'POST', 'PUT', 'DELETE'])
def methods():
    
    data = receive_response('greeting')

    return f'You\'ve sent a {request.method} request\nwith some data:\n{data}\n'



@app.route('/api', methods=['GET'])
def api():
    try:
        greetings = [greetings.__dict__ for greetings in Greetings.query.all()]
        for item in greetings:
            item.pop('_sa_instance_state')
        
    except:
        greetings = [{'sayhi':'I can\'t understand you, seems like the database is empty'}]

    json = jsonify(greetings)
    return json



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)