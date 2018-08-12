from flask import request
from flask_restplus import Resource
from app import api
from app.models import User

parser = api.parser()
parser.add_argument('data', type=str, help='todo title', location='form')


@api.route('/todo/<string:todo_id>')
@api.doc(params={'todo_id': 'the todo identifier'})
class TodoSimple(Resource):
    todos = {}

    def get(self, todo_id):
        return {todo_id: self.todos[todo_id]}

    @api.doc(parser=parser)
    def put(self, todo_id):
        self.todos[todo_id] = request.form['data']
        return {todo_id: self.todos[todo_id]}