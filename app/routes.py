from flask import render_template, g, request, redirect, url_for
from flask_restplus import Resource
from flask_login import current_user, login_user
from app import api
from app.models import User

todos = {}

@api.route('/todo/<string:todo_id>')
class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

@api.route('/login')
class UserLogin(Resource):
    def get(self):
        print(current_user.is_authenticated)
        return redirect(url_for('index'))

@api.route('/')
@api.route('/index')
class UserLogin(Resource):
    def get(self):
        user = User.query.get(1)
        return render_template('index.html', title='Home', user=user)