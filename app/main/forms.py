from flask import Markup
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SelectField
from wtforms.validators import Required


class BioUpdateForm(FlaskForm):
    bioLabel = Markup(" <p class='custom-bold-body mb-0'>Update your bios</p>") 
    new_biography = TextAreaField(bioLabel)



class PitchForm(FlaskForm):
    pitchLabel = Markup(" <p class='custom-bold-body mb-0'>Post new pitch</p>")
    categoryLabel = Markup(" <p class='custom-bold-body mb-0'>Post new pitch</p>")
    new_pitch = TextAreaField(pitchLabel)
    category = SelectField(categoryLabel, choices=[], coerce = int, validators=[Required()])

class UpdatePasswordForm(FlaskForm):
    old_passwordLabel = Markup(" <p class='custom-bold-body mb-0'>Enter new password</p>")
    new_passwordLabel = Markup(" <p class='custom-bold-body mb-0'>Enter new password</p>")
    new_password2Label = Markup(" <p class='custom-bold-body mb-0'>Confirm new password</p>")
    old_password = PasswordField(old_passwordLabel, validators = [Required()])
    new_password = PasswordField(new_passwordLabel, validators = [Required()])
    new_password2 = PasswordField(new_password2Label, validators = [Required()])
