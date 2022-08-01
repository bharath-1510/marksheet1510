from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

#postgres://nyremosawaihgz:7cb13261df2a46f95e1731b3c925c1638409d4a50340095d0b297a9fde22282d@ec2-44-205-112-253.compute-1.amazonaws.com:5432/d833eaqpcp0q57

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:bharath@localhost/names'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://nyremosawaihgz:7cb13261df2a46f95e1731b3c925c1638409d4a50340095d0b297a9fde22282d@ec2-44-205-112-253.compute-1.amazonaws.com:5432/d833eaqpcp0q57'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Names(db.Model):
    id = db.Column(db.Integer,primary_key= True)
    name = db.Column(db.String(30))
    mark = db.Column(db.Integer)
@app.route('/')
def index():
    result = Names.query.all()
    return render_template('main.html',result=result)

@app.route('/display')
def display():
    return render_template('index.html')

@app.route('/process',methods =['POST'])
def process():
    name = request.form['name']
    mark = request.form['mark']
    data = Names(name =name,mark=mark)
    db.session.add(data)
    db.session.commit()

    return redirect(url_for('index'))
