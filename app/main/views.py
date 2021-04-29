from flask import render_template, request, redirect, url_for
from . import main
from .forms import BioUpdateForm, PitchForm, UpdatePasswordForm
from .. import db
from ..models import User, Category, Pitch
from flask_login import login_required, current_user

@main.route('/', methods=['POST', 'GET'])
def index():
    title = 'Pitch Perfect: Perfect your pitches'
    new_pitch = PitchForm()
        if current_user.is_authenticated:
        authenticated = True
    else:
        authenticated = False
    
    if authenticated:
        if new_pitch.validate_on_submit():
            category_id = Category.query.filter_by(title = new_pitch.category).first()
            pitch = Pitch(body=new_pitch.new_pitch, category_id = category_id, user_id = current_user.id, up_votes = 0, down_votes=0)
            
            db.session.add(pitch)
            db.session.commit()
            
            return redirect( url_for('main.index'))
    
    pitches = Pitch.get_pitches()

    
    return render_template('index.html', title=title, pitches= pitches, authenticated=authenticated, form = new_pitch)

@main.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    
    userdata = User.query.filter_by(id = current_user.id).first()
    own_pitches = Pitch.query.filter_by(user_id = current_user.id).all()
    update_password = UpdatePasswordForm()
    update_bio = BioUpdateForm()
    
    if update_password.validate_on_submit():
        if userdata is not None and userdata.verify_password(update_password.old_password.data):
            if update_password.new_password == update_password.new_password2:
                userdata.password(new_password)
                flash('Password changed successfully')
                redirect(url_for('main.profile'))
            else: 
                flash('Passwords do not match')
                
    if update_bio.validate_on_submit():
        new_bio = update_bio.new_biography.data
        userdata['bio'] = new_bio
        db.session.add(userdata)
        db.session.commit() 
        
        
    pitch_results = list()
        
    if own_pitches is not None:
        for pitch in own_pitches:
            category_record = Category.query.filter_by(pitch.category_id).first()
            comments = Comment.get_comments(pitch.id)
            
            pitch_result_item['id'] = pitch.id 
            pitch_result_item['body'] = pitch.body 
            pitch_result_item['created_on'] = pitch.created_on
            pitch_result_item['username'] = userdata.username
            pitch_result_item['avatar'] = userdata.avatar
            pitch_result_item['category'] = category_record.title
            pitch_result_item['up_votes'] = pitch.up_votes 
            pitch_result_item['down_votes'] = pitch.down_votes 
            pitch_result_item['comments'] = comments
            
            pitch_result.append(pitch_result_item)
    
    title = f"{userdata.first_name} {userdata.last_name}'s Profile"
    
    return render_template('profile.html', pitches = pitch_results, userdata = userdata)
    return render_template('profile.html', form =update_password, bio_form =update_bio )
    
    