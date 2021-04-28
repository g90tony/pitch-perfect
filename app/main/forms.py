from flask_wtf import FlaskForm
from wtforms import StringField, PasswordFields, TextAreaField, EmailField,  SelectField, SubmitField
from wtforms.validators import Required


class BioUpdateForm(FlaskForm):
    new_biography = TextAreaField('Update your bios')
    submit_button = SubmitField('save')


class PitchForm(FlaskForm):
    new_pitch = TextAreaField('Enter your pitch here')
    category = SelectField('Select a category', coerce='unicode', validators=[InputRequired])
    submit_button = SubmitField('save')