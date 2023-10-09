import os
from flask import Flask
from book_routes import book_blueprint
from customer_routes import customer_blueprint
from customer_routes import db
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm import Mapped, mapped_column
# from sqlalchemy import Integer, String
from dotenv import load_dotenv                # Loading Env Variables

load_dotenv()                                    # Loading Env Variables
app = Flask(__name__)
db_user = os.environ['DB_USER']                 # Env
db_pass = os.environ['DB_PASSWORD']             # Env
db_host = os.environ['DB_HOST']                 # Env
db_name = os.environ['DB_NAME']                 # Env
app.register_blueprint(book_blueprint)           # Blueprints for proper URL
app.register_blueprint(customer_blueprint)       # Blueprints for proper URL

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@{}/{}'.format(db_user, db_pass, db_host, db_name)
db.init_app(app)
