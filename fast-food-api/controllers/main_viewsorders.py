"""
   Module defines views
"""
from flask import jsonify, request
from flask.views import MethodView
from models.view_order import UsersOrders


class GetOrder(MethodView):
    """
       Class to run the views using method view
       params: routes
       respone: json data
    """

    @staticmethod
    def get(order_id):
        """
           get method for get requests
           param: route /api/v1/orders and /api/v1/orders/<int:order_id>
           response: json data get_all_orders() and self.get_one_order(order_id)
        """
        if order_id is None:
            if UsersOrders.get_all_orders() is True:
                return jsonify({'Orders':'No orders available at the moment,Please make an order'})
            return jsonify({'Orders': UsersOrders.get_all_orders()})
        return jsonify(UsersOrders.get_one_order(order_id))

    @staticmethod
    def post(order_id=None):
        """
           post method for post requests
           param: route /api/orders
           response: json data
        """
        if order_id is None:
            keys = ("user_name", "order")
            if not set(keys).issubset(set(request.json)):
                return jsonify({'New order': 'Your request has Empty feilds'}), 400

            if not request.json['user_name']:
                
                # if request.json['order']=="":
                #     return jsonify({"order": 'Order missing, please enter Order'}),400
                return jsonify({"user_name": 'User_name missing, please enter User-name'}),400
            if request.json['order']=="":
                return jsonify({"order": 'Order missing, please enter Order'}),400
            if not isinstance(request.json["order"],str):
                return jsonify({'message':'order should be a string'}),400

            return jsonify(UsersOrders.post_an_order(request.json['user_name'],
                                                     request.json['order']))
    @staticmethod
    def put(order_id):
        """
           post method for puts requests
           param: route /api/orders/<int:order_id>
           response: json data
        """
        
        return jsonify({'Updated order': UsersOrders.put_an_order(order_id)})
        