#/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required


app=Flask(__name__)

bootstrap=Bootstrap(app)


@app.route('/')
def index():
	return render_template("index.html")

@app.route('/user/<name>')
def user(name):
	return render_template('user.html',name=name)

if __name__=='__main__':
	app.run(debug=True)