import os 
import pymysql


PASSWORD ="ahmed@12345"
PUBLIC_IP_ADDRESS ="34.89.80.180:3306"
DBNAME ="mizani"
PROJECT_ID ="mizani-301713:europe-west2"
INSTANCE_NAME ="mysql-mizani"

class Config():
    SECRET_KEY = 'farmula'
    socket_location = "/var/run/mysqld/mysqld.sock"
    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost/mizani"
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:ahmed@12345@127.0.0.1/mizani?unix_socket=/cloudsql/mizani-301713:europe-west2:mysql-mizani'
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:ahmed@209.97.135.130/mizani"
    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root@/mizani?unix_socket=/cloudsql/mizani-301713:mysql-mizani "
    # SQLALCHEMY_DATABASE_URI =  "mysql+gaerdbms:///mizani?instance=mizani:mysql-mizani"
    # SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://root:{PASSWORD}@/{DBNAME}?unix_socket=/cloudsql/{PROJECT_ID}:{INSTANCE_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    