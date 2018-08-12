import os
import flaskr
import unittest
import tempfile
from flask import json, jsonify


class TestControllerStatic(unittest.TestCase):
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
    def test_main_page(self):
        response = self.app.get('/index', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()