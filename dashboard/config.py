import os 

class Config():
    SECRET_KEY = 'farmula'
    socket_location = "/var/run/mysqld/mysqld.sock"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost/eawa"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    