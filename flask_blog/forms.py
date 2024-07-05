from flask_blog.models import User, Post
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class RegistrationForm(FlaskForm):
    username = StringField('username', validators=[
        DataRequired(), Length(min=2, max=20)])
    email = StringField("email", validators=[DataRequired(), Email()])
    password = PasswordField("password", validators=[DataRequired()])
    confirm_password = PasswordField("confirm_password", validators=[
        DataRequired(), EqualTo("password")])
    submit = SubmitField("sign up")

    # if the credentials has been already in sql then handle those errors
    # it checks itself in the form before storing onto the DB
    # note this syntax => parameter takes an argument from this class
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("that is already taken")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("that is already taken")


class LoginForm(FlaskForm):
    email = StringField("email", validators=[DataRequired(), Email()])
    password = PasswordField("password", validators=[DataRequired()])
    remember = BooleanField("remember me")
    submit = SubmitField("Login")

    """
    NOTE!!!
    Make sure that you are extracting the actual value from the form field 
    (form.username.data in this case) and passing it to the 
    query instead of passing the StringField object directly.
    username = username => do pass StringField object directly.
    username = username.data => because it return from form field

    !read this
    if this block throw any kind of error submit button won't work and 
    no post operation and no db operation occur that is what i need
    """
