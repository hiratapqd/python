from flask import Flask, render_template, request, send_file
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func
from werkzeug import secure_filename


app=Flask(__name__)
#esta configuracao para acessar o postgres na aws
#app.config['SQLALCHEMY_DATABASE_URI']='postgresql://solve1:Solve123!@awspgdb.cp3x4epfttnq.us-east-2.rds.amazonaws.com/arcserve'
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://solve1:Solve123!@172.16.18.162/arcserve'
#app.config['SQLALCHEMY_DATABASE_URI']='postgres://ejwuclujctbntz:2ZvGfcHUFzmasNYi-TwQH6lMgf@ec2-50-17-206-164.compute-1.amazonaws.com:5432/d425fslp62inet?sslmode=require'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__="hchktbl"
    id=db.Column(db.Integer, autoincrement=True, primary_key=True)
    date=db.Column(db.String(10))
    server_=db.Column(db.String(20))
    app_=db.Column(db.String(50))
    bkp_size=db.Column(db.Integer)
    written_size=db.Column(db.Integer)
    start_time=db.Column(db.String(50))
    end_time=db.Column(db.String(50))
    bkp_time=db.Column(db.String(50))
    clone_size=db.Column(db.Integer)
    company=db.Column(db.String(50))
    compression=db.Column(db.Float())
    savings=db.Column(db.Integer)

    def __init__(self, email_, height_):
        self.email_=email_
        self.height_=height_

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():
    global file
    if request.method=='POST':
        file=request.files["file"]
        file.save(secure_filename("uploaded"+file.filename))
        with open("uploaded"+file.filename,"a") as f:
            f.write("This was added later!")
        print(file)
        print(type(file))
        return render_template("index.html", btn="download.html")

@app.route("/download")
def download():
    return send_file("uploaded"+file.filename, attachment_filename="yourfile.csv", as_attachment=True)


if __name__ == '__main__':
    app.debug=True
    app.run()
