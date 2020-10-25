import os 

class Config():
    SECRET_KEY = 'farmula'
    socket_location = "/var/run/mysqld/mysqld.sock"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost/mizani"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    