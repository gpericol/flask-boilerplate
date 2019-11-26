from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, SelectField
from wtforms.validators import Required, Email, EqualTo, Regexp
from app.utilities.validators import Unique
from app.mod_dummy.models import User


class LoginForm(FlaskForm):
    email    = TextField('Email Address', [Email(),
                Required(message='Forgot your email address?')])
    password = PasswordField('Password', [
                Required(message='Must provide a password. ;-)')])

class CreateForm(FlaskForm):
    name = TextField('Name', [
        Required(message='Forgot your name'),
        Regexp(u'[A-Za-z]+', message="a-z")])
    
    email = TextField('Email Address', [
        Email(), 
        Required(message='Forgot your email address?'), 
        Unique(User, User.email, message="Esiste Già")])
    
    password = PasswordField('Password', [
            Required(message='Must provide a password. ;-)'), 
            EqualTo('password_repeat', message='Passwords must match')
            ])

    password_repeat = PasswordField('Password', [Required(message='Must repeat the password')])

    role = SelectField("Role", choices=[
                ("1", "Internal"),
                ("2", "External")
            ])
    status = SelectField("Status", choices=[
                ("1", "Active"),
                ("-1", "Not Active")
            ])