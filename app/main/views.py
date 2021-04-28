from flask import render_template, request, redirect, url_for
from . import main
from .forms import BioUpdateForm, CategoriesFilterForm
from ..db import db
from ..models import Category, Pitch
from flask_login import login_required, current_user

@main.route('/')
def index():
    title = 'Pitch Perfect: Perfect your pitches'
    
    pitches = Pitch.get_pitches()
    if user_is_authenticated():
        authenticated = True
    else:
        authenticated = False
    
    return render_template('index.html', title=title, pitches= pitches, authenticated=authenticated)