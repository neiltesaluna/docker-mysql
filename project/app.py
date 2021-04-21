from flask import Flask,render_template, request
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

db.create_all()


def receive_response():
    try:
        data = request.get_json(force=True)
    except:
        data = request.args
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

    data = receive_response()
    greeting = data.get('greeting')

    new_greeting = Greetings(sayhi=greeting)
    db.session.add(new_greeting)
    db.session.commit()

    return f'The database has been updated with {greeting}\n'

@app.route('/methods', methods=['GET', 'POST', 'PUT', 'DELETE'])
def methods():
    
    data = receive_response()
    data = data.get('greeting')


    return f'You\'ve sent a {request.method} request\nwith some data:\n{data}\n'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)