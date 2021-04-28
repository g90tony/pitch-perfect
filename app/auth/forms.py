from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField, BooleanField, ValidationError
from wtforms.validators import Required, Email, EqualTo
from ..models import User

class RegistrationForm(FlaskForm):
    first_name = StringField('Enter first name', validators = [(Required())])
    last_name = StringField('Enter last name', validators = [Required()])
    email = StringField('Enter email address', validators = [Required(), Email()])
    avatar = FileField('Upload Profile Picture', validators = [Required()])
    password = PasswordField('Enter new password', validators = [Required()])
    password2 = PasswordField('Confrim new password', validators = [Required()])
    submit = SubmitField('Create account')

class LoginForm(FlaskForm):
    email = StringField('Enter email address', validators = [Required(), Email()])
    password = PasswordField('Enter your password', validators = [Required()])
    remember_user = BooleanField('Remember me')
    submit = SubmitField('Login')