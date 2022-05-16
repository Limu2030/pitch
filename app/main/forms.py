from email import contentmanager
from flask_wtf import FlaskForm 
from wtforms import StringField,PasswordField,SubmitField,TextAreaField
from wtforms.validators import DataRequired,Length,Email,EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('username',validators=[DataRequired(),Length(min=5,max=20)])
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    confirm_password = PasswordField('Password',validators =[DataRequired(),EqualTo('password')])
    submit = SubmitField('Sign up')

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    login= SubmitField('Login')


class PitchForm(FlaskForm):
    title = StringField('title',validators=[DataRequired()])
    category = StringField('category',validators=[DataRequired()])
    content = TextAreaField('content',validators=[DataRequired()])
    submit = SubmitField('pitch')

class CommentForm(FlaskForm):
    content = TextAreaField('comment',validators=[DataRequired()])
    submit = SubmitField('comment')