import os 

class Config():
    SECRET_KEY = 'farmula'
    socket_location = "/var/run/mysqld/mysqld.sock"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost/mizani"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:ahmed@12345@159.203.0.249/mizani"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    