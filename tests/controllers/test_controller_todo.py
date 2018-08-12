import os
import flaskr
import unittest
import tempfile
from flask import json, jsonify


class TestControllerTodo(unittest.TestCase):
    ###############
    #### setup ####
    ###############
    def setUp(self):
        self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
        flaskr.app.testing = True
        self.app = flaskr.app.test_client()

    ##################
    #### teardown ####
    ##################
    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(flaskr.app.config['DATABASE'])

    ###############
    #### tests ####
    ###############
    def test_api_todo_post(self):
        response = self.app.put(
            '/todo/todo1',
            data=dict(data='Remember the milk'),
            follow_redirects=True)
        self.assertEqual(response.status_code, 201)
        data = response.json
        self.assertEqual(data['todo1'], 'Remember the milk')

    def test_api_todo_get(self):
        self.app.put(
            '/todo/todo1',
            data=dict(data='Remember the milk'),
            follow_redirects=True)
        response = self.app.get('/todo/todo1', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertEqual(data['todo1'], 'Remember the milk')


if __name__ == '__main__':
    unittest.main()