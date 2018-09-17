"""
    Module for making tests on the app
"""
import unittest
import json

from run import APP

class TestViews(unittest.TestCase):
    """"
        Class for making tests
        params: unittest.testCase
    """

    def setUp(self):
        """
           Method for making the client object
        """
        self.client = APP.test_client
    def test_fetch_all_orders(self):
        """
           Method for tesing the get function which returns all orders
        """
        result = self.client().get('api/v1/orders')
        respond = json.loads(result.data.decode("utf8"))
        self.assertEqual(result.status_code, 200)
        self.assertIn('Orders', respond)
        self.assertIsInstance(respond, dict)

    def test_get_an_order(self):
        """
            Method for tesing the get function which returns one order
        """
        result = self.client().get('api/v1/orders/17')
        result2 = self.client().get('api/v1/orders/a')
        respond = json.loads(result.data.decode("utf8"))
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result2.status_code, 404)
        self.assertIsInstance(respond, dict)


    def test_post_an_order(self):
        """
            Method for tesing the post function which posts an order
        """
        result = self.client().post('api/v1/orders',
                                    content_type="application/json",
                                    data=json.dumps(dict(order_id=18, user_name="Akram",
                                                         order=
                                                         "chips and chicken")))
        respond = json.loads(result.data.decode("utf8"))
        self.assertIn('New order', respond)
        self.assertIsInstance(respond, dict)
        self.assertEqual(result.status_code, 200)
        self.assertTrue(result.json["New order"])

    def test_put_an_order(self):
        """
            Method for tesing the post function which updates an order
        """
        result1 = self.client().put('api/v1/orders/1',
                                    content_type="application/json",
                                    data=json.dumps(dict(order_id=18,
                                                         order_status=
                                                         "Pending")))
        result2 = self.client().put('api/v1/orders/1',
                                    content_type="application/json",
                                    data=json.dumps(dict(order_id=18,
                                                         order_status=
                                                         "Ready")))
        respond = json.loads(result2.data.decode("utf8"))
        self.assertIn('Updated order', respond)
        self.assertIsInstance(respond, dict)
        self.assertEqual(result1.status_code, 200)
        self.assertTrue(result1.json["Updated order"])
        self.assertEqual(result2.status_code, 200)
        self.assertTrue(result2.json["Updated order"])
    def test_inputs(self):
        result = self.client().post('api/v1/orders',
                                    content_type="application/json",
                                    data=json.dumps(dict(order_id=18
                                                         )))
        result_response = json.loads(result.data.decode("utf8"))
        print(result_response)
        self.assertTrue(result_response['New order'], 'Your request has empty fields')
        self.assertTrue(result.content_type, 'application/json')
        self.assertEqual(result.status_code, 400)

    def test_input_order(self):
        result = self.client().post('api/v1/orders',
                                    content_type="application/json",
                                    data=json.dumps(dict(order_id=18, user_name="Akram",
                                                         order=
                                                         "")))
        result_response = json.loads(result.data.decode())
        self.assertTrue(result_response['order'], 'Order missing, please enter Order')
        self.assertTrue(result.content_type, 'application/json')
        self.assertEqual(result.status_code, 400)

    def test_input_user_name(self):
        result = self.client().post('api/v1/orders',
                                    content_type="application/json",
                                    data=json.dumps(dict(order_id=18, user_name="",
                                                         order=
                                                         "All food and beef")))
        result_response = json.loads(result.data.decode())
        self.assertTrue(result_response['user_name'], 'user_name missing, please enter                                    user_name')
        self.assertTrue(result.content_type, 'application/json')
        self.assertEqual(result.status_code, 400)
        
