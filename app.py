# from flask import Flask
# from flask import request
# from flask import redirect, url_for, Markup
# from flask_sqlalchemy import SQLAlchemy

from application import app

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1:3306/rps'

# db = SQLAlchemy(app)

# class Winlose(db.Model):
#     matchid = db.Column(db.Integer, primary_key=True)
#     player = db.Column(db.String(40), nullable=False)
#     opponent = db.Column(db.String(40), nullable=False)
#     result = db.Column(db.String(40), nullable=False) 

# @app.route('/')
# def hello_internet():
#     return "Hello Internet!"

# @app.route('/home', methods=["GET"])
# def hello_home():
#     if request.method == "GET":
#         return Markup("Hello Homepage! This is a GET request." + "<br>" + "This url is: " + str(url_for('hello_home')))

# @app.route('/gobackhome')
# def gobackhome():
#     return redirect('/home')

# @app.route('/home/<word>.<int:number>.upperplus')
# def home(word, number):
#     return word.upper() + "'s" + " " + str(number) + " " + "plus ten is: " + str(number+10)

# @app.route('/about')
# def about():
#     return Markup("<h1> My name is Hassan. I am a developer. </h1>")

# @app.route('/squarenumber/<int:number>')
# def squarenumber(number):
#     msg = []
#     msg.append("The URL to this is: " + str(url_for('squarenumber', number=number)))
#     msg.append("This program squares the number you entered in")
#     msg.append(str(number*number))
#     return "<br>".join(msg)

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)