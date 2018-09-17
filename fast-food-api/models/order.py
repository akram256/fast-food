""" Module for orders"""
from datetime import datetime

class Order():
    """
        Class defines the order atributes
        params: user_name, order_id, order&nbsp;&nbsp;&nbsp;&nbsp;
        """
    def __init__(self, order_id, user_name, order):
        self.order_id = order_id
        self.user_name = user_name
        self.order = order
        self.order_status = "pending"
        self.order_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
