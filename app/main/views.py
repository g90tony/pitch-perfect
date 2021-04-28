from flask import render_template, request, redirect, url_for
from . import main
from .forms import BioUpdateForm, PitchForm
from .. import db
from ..models import Category, Pitch
from flask_login import login_required, current_user

@main.route('/', methods=['POST', 'GET'])
def index():
    title = 'Pitch Perfect: Perfect your pitches'
    new_pitch = PitchForm()
    
    if new_pitch.validate_on_submit():
        category_id = Category.query.filter_by(title = new_pitch.category).first()
        pitch = Pitch(body=new_pitch.new_pitch, category_id = category_id, user_id = current_user.id, up_votes = 0, down_votes=0)
        
        db.session.add(pitch)
        db.session.commit()
        
        return redirect( url_for('main.index'))
    
    pitches = Pitch.get_pitches()
    if current_user.is_authenticated:
        authenticated = True
    else:
        authenticated = False
    
    return render_template('index.html', title=title, pitches= pitches, authenticated=authenticated, form = new_pitch)