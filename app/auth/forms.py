from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordFields, SubmitField, FileField, BooleanField, ValidationErrors
from wtforms.validators import Required, Email, EqualTo
from ..models import User

class RegistrationForm(FlaskForm):
    first_name = StringField('Enter first name', validators = [(Required())])
    last_name = StringField('Enter last name', validators = [Required()])
    email = EmailField('Enter email address', validators = [(Required(), Email())])
    avatar = FileField('Upload Profile Picture', validators = [Required()])
    password = PasswordFields('Enter new password', validators = [Required()])
    password2 = PasswordFields('Confrim new password', validators = [Required()])
    submit = SubmitField('Create account')

class LoginForm(FlaskForm):
    email = EmailField('Enter email address', validators = [(Required(), Email())])
    password = PasswordFields('Enter your password', validators = [Required()])
    remember_user =     BooleanField('Remember me')
    submit = SubmitField('Login')