"""
This module contains tests for user account creatiom
and signing in.
"""
import uuid
from unittest import TestCase
from flask import json
import psycopg2
from auth.user import User
from run import APP
from controllers.database_connection import Databaseconn


class TestUserAuthTestCase(TestCase):
    """
    Tests run for the api end pints.
    """
    user1 = User("akram", 
                 "a4a@gmail.com",  "8888")
    empty_user = User("", 
                      "a4aboss@gmail.com","7777")
    def setUp(self):
        """
        Define test variables and initialize app.
        """
        APP.config['TESTING'] = True
        self.app = APP
        self.client = self.app.test_client
        Databaseconn.create_tables()

    def test_app_is_development(self):
        """
        This method tests configuration variables such that they are set correctly
        """
        self.assertNotEqual(APP.config['SECRET_KEY'], "my-key")
        self.assertTrue(APP.config['DEBUG'] is False)
        self.assertTrue(APP.config['TESTING'] is True)

    def test_user_registration(self):
        """
        Test a user is successfully created through the api
        :return:
        """
        response = self.client().post('/api/v1/signup/', data=json.dumps(
            self.user1.__dict__), content_type='application/json')
        print(response)

        self.assertEqual(response.status_code, 201)
        self.assertTrue(response.content_type == 'application/json')
        self.assertIn("user", response.json)
        self.assertEqual("Successfully registered", response.json['message'])
        self.assertTrue(response.json['user'])

    def test_content_type_not_json(self):
        """
        Test that the content type that is not application/json
        returns an error message
        :return:
        """
        response = self.client().post('/api/v1/signup/', data=json.dumps(
            self.user1.__dict__), content_type='text/plain')

        self.assertEqual(response.status_code, 400)
        self.assertEqual("Failed Content-type must be json", response.json['error_message'])

    def test_empty_attributes_not_sent(self):
        """
        This method tests that data is not sent with empty fields
        """
        response = self.client().post('/api/v1/signup/', data=json.dumps(
            self.empty_user.__dict__), content_type='application/json')

        self.assertEqual(response.status_code, 400)
        self.assertTrue(response.json)
        self.assertEqual("Some fields are not defined", response.json['error_message'])

    def test_partial_fields_not_sent(self):
        """
        This method tests that data with partial fields is not send
        on creating a ride offer
        """
        response = self.client().post('/api/v1/signup/', data=json.dumps(
            dict(
                  email=self.user1.email)),
                                      content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual("Some fields are missing, all fields are required",
                         response.json['error_message'])

    def test_user_login(self):
        """
        Test for login of a registered user
        """
        self.client().post('/api/v1/signup/', data=json.dumps(
            self.user1.__dict__), content_type='application/json')

        response = self.client().post(
            '/api/v1/login/',
            data=json.dumps(dict(
                email=self.user1.email,
                password=self.user1.password
            )),
            content_type='application/json'
        )

        self.assertTrue(response.json['status'] == 'success')
        self.assertTrue(response.json['message'] == 'Successfully logged in.')
        self.assertTrue(response.json['auth_token'])
        self.assertTrue(response.content_type == 'application/json')
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        sql_commands = (
            """DROP TABLE IF EXISTS "users" CASCADE;""",
            """DROP TABLE IF EXISTS "orders" CASCADE;""")
           
        conn = None
        try:
            conn = Databaseconn.database_connection()
            cur = conn.cursor()
            for sql_command in sql_commands:
                cur.execute(sql_command)
            cur.close()
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                