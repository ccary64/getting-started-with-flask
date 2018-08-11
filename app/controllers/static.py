from flask import render_template, g, request, redirect, url_for
from flask_restplus import Resource
from flask_login import current_user, login_user
from app import app
from app.models import User


@app.route('/login', methods=['GET'])
def login():
    user = User.query.get(1)
    return render_template('index.html', title='Home', user=user)


@app.route('/index', methods=['GET'])
def index():
    user = User.query.get(1)
    return render_template('index.html', title='Home', user=user)