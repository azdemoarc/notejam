import os
basedir = os.path.abspath(os.path.dirname(__file__))

import urllib
from sqlalchemy import create_engine


driver = "{ODBC Driver 17 for SQL Server}"
server = os.environ['server']
database = os.environ['database']
user = os.environ['user']
password = os.environ['password']

conn = f"""Driver={driver};Server=tcp:{server},1433;Database={database};
Uid={user};Pwd={password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"""

params = urllib.parse.quote_plus(conn)
conn_str = 'mssql+pyodbc:///?autocommit=true&odbc_connect={}'.format(params)
engine = create_engine(conn_str, echo=True)
engine.execute("SELECT 1")


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ['secret_key']
    WTF_CSRF_ENABLED = True
    CSRF_SESSION_KEY = os.environ['csrf_key']
    SQLALCHEMY_DATABASE_URI = conn_str
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True



class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
