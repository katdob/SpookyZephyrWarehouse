import os
from flask import Flask
from flask_cors import CORS
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy_session import flask_scoped_session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db_user = 'root'
db_pw = 'rootroot'
db_port = '3306'
db_name = 'SpookyZephyrWarehouse'

uri = 'mysql+pymysql://{}:{}@localhost:{}/{}?charset=UTF8MB4'.format(
    db_user, db_pw, db_port, db_name)

app = Flask(__name__)
app.secret_key = 'secret'
CORS(app, support_credentials=True)
ENGINE = create_engine(
    'mysql+pymysql://',
    pool_size=10,
    pool_timeout=1000,
    pool_recycle=280,
    max_overflow=10,
    pool_pre_ping=True,
    encoding='UTF8',
    echo=True
)
SESSON_FACTORY = sessionmaker(bind=ENGINE)
SESSION = flask_scoped_session(SESSON_FACTORY, app)
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_BINDS'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

SQLALCHEMY_DATABASE_URI = uri
SQLALCHEMY_BINDS = ''
SQLALCHEMY_TRACK_MODIFICATIONS = False

db = SQLAlchemy(app, session_options={'expire_on_commit': False, })
db.metadata.bind = db.engine
db.metadata.reflect = True
db_session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False, bind=db.engine
    )
)
Base = declarative_base()
Base.query = db_session.query_property()
db.create_all()
migrate = Migrate(app, db)

# DB = SQLAlchemy(APP, session_options={'expire_on_commit': False, })
# DB.metadata.bind = DB.engine
# DB.metadata.reflect = True
# DB_SESSION = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=DB.engine))
# Base = declarative_base()
# Base.query = DB_SESSION.query_property()
# DB.create_all()
# MIGRATE = Migrate(APP, DB)

from . import routes, models
