"""
   Class for defining url / routes
"""
from controllers.main_viewsorders import GetOrder
class Urls():
    """
       GetRoutes defines urls
       params:urls
    """
    @staticmethod
    def fetch_urls(order):
        """
           Add url rule defines the routes for http requests
        """
        order_view = GetOrder.as_view('orders')
        order.add_url_rule('/api/v1/orders', view_func=order_view,
                           defaults={'order_id': None}, methods=['GET',])
        order.add_url_rule('/api/v1/orders/<int:order_id>',
                           view_func=order_view, methods=['GET',])
        order_post = GetOrder.as_view('post_orders')
        order.add_url_rule('/api/v1/orders',
                           view_func=order_post, methods=['POST',])
        order.add_url_rule('/api/v1/orders/<int:order_id>', 
                            view_func=order_post, methods=['PUT',])
