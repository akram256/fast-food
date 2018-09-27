"""
 This module handles the database connection
"""
import os
import time
import datetime
import psycopg2
from werkzeug.security import generate_password_hash, check_password_hash

class Databaseconn(object):
    """
    This Class contains methods that connects to the database 
    """
    @staticmethod
    def database_connection():
        """
        This method creates a connection to the databse
        "dbname='mydb' user='mydb1' host='localhost' password='mydb123' port='5432'" @staticmethod
        :retun: connection
        """
    
        connection = psycopg2.connect("""dbname='fast-food-db' user='akram'  host='localhost'  password='12345'  port='5432'""" )
        return connection
    @staticmethod  
    def create_tables():
        """
        This method creates tables in the PostgreSQL database.
        It connects to the database and creates tables one by one
        for command in commands:
        cur.execute(command)
        """
        connection = psycopg2.connect("""dbname='fast-food-db' user='akram'  host='localhost'  password='12345'  port='5432' """ )
        commands = (
            """
            CREATE TABLE if not exists "users" (
                    user_id SERIAL PRIMARY KEY,
                    username VARCHAR(50) NOT NULL,
                    email VARCHAR(50) UNIQUE NOT NULL,
                    password VARCHAR(80) NOT NULL,
                    is_admin BOOLEAN DEFAULT TRUE,
                    is_otheruser BOOLEAN DEFAULT FALSE
                    
                )
            """,
            """
            CREATE TABLE if not exists "menus" (
                    menu_id SERIAL PRIMARY KEY,
                    menu_name VARCHAR (255) NOT NULL,
                    user_id integer,
                    FOREIGN KEY (user_id)
                    REFERENCES users(user_id),
                    menu_date DATE,
                    menu_time TIME

         
                    
                    
                )
            """,
            """
            CREATE TABLE if not exists "orders" (
                    order_id SERIAL PRIMARY KEY,
                    order_now VARCHAR (255) NOT NULL,
                    order_status VARCHAR (255) NOT NULL,
                    user_id integer,
                    FOREIGN KEY (user_id)
                    REFERENCES users(user_id),
                    menu_id integer,
                    FOREIGN KEY (menu_id)
                    REFERENCES menus(menu_id),
                    order_date DATE,
                    order_time TIME
          
                )
            """,)
         


        try:

            cur = connection.cursor()
            for command in commands:
                cur.execute(command)
            connection.commit()
            cur.close()
    
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if connection is not None:
                connection.close()
    
    # for coomand in commands
        # self.execute (command)
    # def delete_tables():
         
    

db = Databaseconn()
# Databaseconn.database_connection() 
db.create_tables()
