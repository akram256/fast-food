"""
   Module for processing logic for endpoints
"""

from models.order import Order
from flask import request
class UsersOrders:
    """
       Class for processing logic for endpoints
       """
    orders = []


    @staticmethod
    def get_all_orders():
        """
           method for getting all orders
           params: none
           response: dictionary
        """
        if not UsersOrders.orders:
            return True
        order_dict = [order.__dict__ for order in UsersOrders.orders]
        return order_dict

    @staticmethod
    def get_one_order(order_id):
        """
           method for fetting one specific order
           params: order_id
           response: dictionary
        """
        if not UsersOrders.orders:
            return {'Orders':'No orders available at the moment, Please make an Order'}
        available_order_id = [
            order.__dict__ for order in UsersOrders.orders
            if order.__dict__['order_id'] == order_id]
        if not available_order_id:
            return {order_id:"Order_id doesnot exist"}
        return {'requested order': [
            order.__dict__
            for order in UsersOrders.orders
            if order.__dict__['order_id'] == order_id]}

    @staticmethod
    def post_an_order(user_name, order):
        """
           method for posting orders
           params: user_name and order
           response: dictionary
        """
        size = [order.__dict__ for order in UsersOrders.orders]
        counter = len(size) + 1
        add_order = Order(counter, user_name, order)
        UsersOrders.orders.append(add_order)
        return {'New order': [
            order.__dict__ for order in UsersOrders.orders]}

    @staticmethod
    def put_an_order(order_id):
        """
           method for updating order status
           params:order_id
           response: dictionary
        """
        if order_id:
            for order in UsersOrders.orders:
                if order.__dict__['order_id'] == order_id:
                    order_jason = request.get_json ()   
                    order.__dict__['user_name'] = order_jason['user_name']
                    order.__dict__['order'] = order_jason['order']
                    return {'Updated order': [ order.__dict__
                            for order in UsersOrders.orders
                            if order.__dict__['order_id'] == order_id]}
                            
                
                   