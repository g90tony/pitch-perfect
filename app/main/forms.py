from flask import Markup
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SelectField
from wtforms.validators import Required


class BioUpdateForm(FlaskForm):
    bioLabel = Markup(" <p class='custom-bold-body mb-0'>Enter first name</p>") 
    new_biography = TextAreaField('Update your bios')



class PitchForm(FlaskForm):
    pitchLabel = Markup(" <p class='custom-bold-body mb-0'>Post new pitch</p>")
    categoryLabel = Markup(" <p class='custom-bold-body mb-0'>Post new pitch</p>")
    new_pitch = TextAreaField(pitchLabel)
    category = SelectField(categoryLabel, coerce='unicode', validators=[Required()])
