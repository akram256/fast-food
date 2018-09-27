"""
This module handels requests to urls.
"""

from models.user_views import RegisterUser, LoginUser ,Logout
from models.db_link import linkdb


class Urls(object):
    """
    Class to generate urls
    """
      
    @staticmethod
    def generate_url(app):
        """
         Generates urls on the app context
        :param: app: takes in the app variable
        :return: urls
        """
       

        app.add_url_rule('/api/v1/signup/', view_func=RegisterUser.as_view('register_user'),methods=["POST",])
        app.add_url_rule('/api/v1/login/', view_func=LoginUser.as_view('login_user'),
                          methods=["POST",])
        app.add_url_rule('/api/v1/users/logout',view_func=Logout.as_view('logout_user'),
                         methods=["POST",])