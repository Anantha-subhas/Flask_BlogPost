from flask_blog import db
from flask_blog import bcrypt
from flask import render_template, url_for, flash, redirect
from flask_blog.forms import RegistrationForm, LoginForm
from flask_blog.models import User, Post
from flask_blog import app

posts = [
    {
        'author': 'corey schafer',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'April 24,2024'
    },
    dict(author='anantha subhas', title='Blog post 2',
         content='second post content', date_posted='April 24,2024')
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)

#
# @app.route("/home")
# def index():
#     # no-need to specify templates/imdex.html
#     return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html", title="About page")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode("utf-8")
        user = User(username=form.username.data,
                    email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"Account created for {form.username.data} !", "success")
        return redirect(url_for('home'))
    return render_template("register.html", title="register", form=form)


"""
methods=["GET", "POST"]
first: GET /login HTTP/1.1" 200
after posting data
second:POST /login HTTP/1.1" 302
"""


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.email.data == "admin@blog.com" and form.password.data == 'password':
        flash('you have been logged in!!', "success")
        return redirect(url_for('home'))
    else:
        flash("Login unsuccessful,please check username and password", 'danger')

    return render_template("login.html", title="login", form=form)
