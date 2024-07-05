from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_bcrypt import Bcrypt
# from flask_login import LoginManager

# from sqlalchemy import create_engine
# engine = create_engine('sqlite:///site.db', echo=True)

# Replace 'sqlite:///site.db' with your actual database connection string
# For SQLite, the connection string is typically in the format 'sqlite:///your_database_file.db'

app = Flask(__name__)
app.config["SECRET_KEY"] = "83e1252582507840982f44504c216e28"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"

# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the Flask app and the database
db = SQLAlchemy(app)
# (or)db.init_app(app)
# db = SQLAlchemy()
# db.init_app(app)
bcrypt = Bcrypt(app)
# login_manager = LoginManager(app)
"""
In Flask, the flask_login module is part of the Flask-Login extension, which provides "user session management for Flask applications."
 It simplifies the process of handling user authentication, user sessions, and managing user login/logout states.
"""

# because @app are in route_file
# NOTE don't put this at top it cause circular import
from flask_blog import routes
