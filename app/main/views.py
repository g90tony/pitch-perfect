from datetime import datetime
from flask import render_template, request, redirect, url_for, flash
from . import main
from .forms import BioUpdateForm, PitchForm, UpdatePasswordForm, NewCommentForm
from .. import db, photos
from ..models import User, Category, Pitch, Comment
from flask_login import login_required, current_user


@main.route('/', methods=['POST', 'GET'])
def index():
    title = 'Pitch Perfect: Perfect your pitches'
    if current_user.is_authenticated:
        authenticated = True
    else:
        authenticated = False
        
    new_pitch = PitchForm()
    
    categories = Category.query.all()
    
    new_pitch.category.choices = [(category.id, category.title) for category in  Category.query.all()] 
    
    if authenticated:
        if new_pitch.validate_on_submit():

            pitch = Pitch(body=new_pitch.new_pitch.data, category_id = new_pitch.category.data, user_id = current_user.id, up_votes = 0, down_votes=0)
            
            pitch.save_pitch()
            db.session.commit()
            
            return redirect( url_for('main.index'))
    
    pitches = Pitch.get_pitches()
    
    
    return render_template('index.html', title=title, pitches= pitches, authenticated=authenticated, form = new_pitch, categories = categories, user=current_user)

@main.route('/filter/<int:category_id>')
def filter(category_id):
    if current_user.is_authenticated:
        authenticated = True
    else:
        authenticated = False
    
    categories = Category.query.all()
    selected_category = Category.query.filter_by(id = category_id).first()
    new_pitch = PitchForm()
    pitches = Pitch.get_pitches(category_id)
    
    title = f'{selected_category.title} Pitches'
    
    return render_template('index.html', title=title, pitches= pitches, authenticated=authenticated, form = new_pitch, categories = categories, user=current_user)    


@main.route('/pitch/<int:pitch_id>', methods=['POST','GET'])
@login_required
def comments(pitch_id):
    pitch = Pitch.query.filter_by(id = pitch_id).first()
    category = Category.query.filter_by(id = pitch.category_id).first()
    user = User.query.filter_by(id = pitch.user_id).first()
    
    formatted_date = pitch.created_on.strftime("%a, %d %B, %y")
    
    comment_form = NewCommentForm()
    
    if comment_form.validate_on_submit():
        new_comment = comment_form.new_comment.data
        
        comment = Comment(user_id= user.id, comment= new_comment, pitch_id= pitch.id)
        comment.add_comment()
        db.session.commit()
        
        return redirect( url_for('main.comments', pitch_id = pitch_id))

    
    comments = Comment.query.filter_by(pitch_id = pitch.id).all()
    
    comment_results = list()
    
    for comment in comments:
        user = User.query.filter_by(id = comment.user_id).first()
        temp = dict()
        temp['username'] = user.username
        temp['comment'] = comment.comment
        
        comment_results.append(temp)
        
        
        
    comment_count = len(comments)
    
    title = f"Comments for {user.username}'s pitch"
    
    return render_template('comment-view.html', comments = comment_results, comment_count = comment_count, pitch = pitch , user= user, category = category, authenticated = True, title=title, form = comment_form, formatted_date = formatted_date)    
    


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
                userdata.password = new_password
                flash('Password changed successfully')
                redirect(url_for('main.profile'))
            else: 
                flash('Passwords do not match')
                
    if update_bio.validate_on_submit():
        new_bio = update_bio.new_biography.data
        userdata.bio = new_bio 
        db.session.add(userdata)
        db.session.commit() 
        
        
    pitch_results = list()
        
    if own_pitches is not None:
        for pitch in own_pitches:
            pitch_result_item = dict()
            
            category_record = Category.query.filter_by(id = pitch.category_id).first()
            comments = Comment.query.filter_by(pitch_id = pitch.id).all()
            
            pitch_result_item['id'] = pitch.id 
            pitch_result_item['body'] = pitch.body 
            pitch_result_item['created_on'] = pitch.created_on
            pitch_result_item['username'] = userdata.username
            pitch_result_item['avatar'] = userdata.avatar
            pitch_result_item['category'] = category_record.title
            pitch_result_item['up_votes'] = pitch.up_votes 
            pitch_result_item['down_votes'] = pitch.down_votes 
            
            pitch_results.append(pitch_result_item)
    
    title = f"{userdata.username}'s Profile"
    pitches_count = len(pitch_results)
    
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'images/{filename}'
        userdata.avatar = path
        db.session.commit()

    return render_template('profile.html', form =update_password, bio_form =update_bio, pitches = pitch_results, user = current_user, pitches_count = pitches_count, title = title, authenticated = True )
    
    