import os 

class Config():
    SECRET_KEY = 'farmula'
    socket_location = "/var/run/mysqld/mysqld.sock"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:ahmed@12345@localhost/eawa"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    