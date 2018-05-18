#/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask,render_template


app=Flask(__name__)

print('Hello,world')

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/user/<name>')
def user(name):
	return render_template('user.html',name=name)


if __name__=="main":
	app.run(debug=True)