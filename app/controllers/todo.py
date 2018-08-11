from flask import request
from flask_restplus import Resource
from app import api
from app.models import User


@api.route('/todo/<string:todo_id>')
class TodoSimple(Resource):
    todos = {}

    def get(self, todo_id):
        return {todo_id: self.todos[todo_id]}

    def put(self, todo_id):
        self.todos[todo_id] = request.form['data']
        return {todo_id: self.todos[todo_id]}