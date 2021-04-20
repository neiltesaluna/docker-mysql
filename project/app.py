from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
import os
import pymysql

app = Flask('__main__')

dbuser = os.environ.get('MYSQL_USER')
dbpassword = os.environ.get('MYSQL_PASSWORD')
dbname = os.environ.get('testdb')

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{dbuser}:{dbpassword}@database/{dbname}?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Greetings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sayhi = db.Column(db.String(20), nullable=False)

db.create_all(checkfirst=True)

@app.route('/', methods=['GET'])
def home():
    
    try:
        greetings = greetings.query.all()
        
    except:
        greetings = [{'sayhi':'I can\'t understand you'}]

    return render_template('index.html', greetings = greetings)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)