from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgres://xbbjsspscgmysg:7f1a9f17d64c014ec4769316fe81db7cb2aa08131a84414159c3959fed22efcb@ec2-34-202-7-83.compute-1.amazonaws.com:5432/da6g60jf9f7an6?sslmode=require'
db = SQLAlchemy(app)
class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    height = db.Column(db.Integer)
    def __init__(self,email,height):
        self.email = email
        self.height = height
@app.route('/')
def index():
    return render_template("index.html")




@app.route('/success/', methods=['POST'])
def success_page():
    if request.method=='POST':
        email=request.form['email_name']
        height = request.form['height_name']
        if db.session.query(Data).filter(Data.email==email).count() == 0:
            data = Data(email,height)
            db.session.add(data)
            db.session.commit()
            avg_height = db.session.query(func.avg(Data.height)).scalar()
            avg_height = round(avg_height,1)
            cou = db.session.query(Data.height).count()
            send_email(email,height,avg_height,cou)
            return render_template("success.html")
        else:
            return render_template("index.html",text="Sorry, we have already got something from that email id!")    

if __name__ == "__main__":
    app.debug=True
    app.run(port=2008)    


