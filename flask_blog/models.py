from flask_blog import db
from datetime import datetime
# from flask_blog import login_manager


# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))


class User(db.Model):  # Subclass this to define database models.
    id = db.Column(db.Integer, primary_key=True)  # auto-increment
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False,
                           default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    # In SQLAlchemy, the backref parameter is used to establish a bidirectional relationship between two tables/models.
    # When you define a relationship between two models, you can use backref to create a reference from the related model back to the original model.
    # 'author' stores the obj of a user

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


"""
logic of model or table(User and Post)
one user can have multiple post but a post have one author(who created the post)
"""


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.today())
    content = db.Column(db.Text, nullable=False)
    # no unique means user can have multiple posts
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # user.id either upper case or lower case it consider in either ways because table are usually in lower case

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
