from .. import app
from flask import render_template, redirect, request
from .mysqlconnection import connectToMySQL
from friends_module.controllers.friends import Friends

friends = Friends()


@app.route('/')
def index():
    return friends.index()

@app.route('/friends', methods=['POST'])
def create():
    return friends.create(request.form)

@app.route('/clear_db')
def clear_db():
    return friends.clear_db()
