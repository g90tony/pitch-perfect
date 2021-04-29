from flask import Markup
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FileField, BooleanField, ValidationError
from wtforms.validators import Required, Email, EqualTo
from ..models import User


class RegistrationForm(FlaskForm):
    first_nameLabel = Markup(" <p class='custom-bold-body mb-0'>Enter first name</p>")
    last_nameLabel = Markup(" <p class='custom-bold-body mb-0'>Enter last name</p>")
    emailLabel = Markup(" <p class='custom-bold-body mb-0'>Enter email address</p>")
    avatarLabel = Markup(" <p class='custom-bold-body mb-0'>Upload profile picture</p>")
    passwordLabel = Markup(" <p class='custom-bold-body mb-0'>Enter new password</p>")
    password2Label = Markup(" <p class='custom-bold-body mb-0'>Confirm new password</p>")
    first_name = StringField(first_nameLabel, validators = [(Required())])
    last_name = StringField(last_nameLabel, validators = [Required()])
    email = StringField(emailLabel, validators = [Required(), Email()])
    password = PasswordField(passwordLabel, validators = [Required()])
    password2 = PasswordField(password2Label, validators = [Required()])

class LoginForm(FlaskForm):
    emailLabel = Markup(" <p class='custom-bold-body mb-0'>Enter email address</p>")
    passwordLabel = Markup(" <p class='custom-bold-body mb-0'>Enter your password</p>")
    email = StringField(emailLabel, validators = [Required(), Email()])
    password = PasswordField(passwordLabel, validators = [Required()])
    remember_user = BooleanField('Remember me')