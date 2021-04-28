from flask import render_template, url_for, flash
from flask_login import login_user, logout_user, login_required

from . import auth
from ..models import User
from .forms import RegistrationForm, LoginForm

@auth.route('/login', methods=['GET', 'POST'])
def login():
    new_login = LoginForm()
    
    if new_login.validate_on_submit():
        user = User.query.filter_by(email = new_login.email.data).first()
        
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user, login_form.remember_user.data)
            
            return redirect(request.args.get('next') or url_for('main.index'))
        
        flash('Invalid email or password')
        
    title = 'Welcome back: Pitch Perfect Sign-in'
    
    return render_template('auth/signin.html', form = new_login, title = title)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    new_user = RegistrationForm()
    
    if new_user.validate_on_submit():
        user = User(first_name = new_user.first_name.data,last_name = new_user.last_name.data ,user_email = new_user.email.data ,bio = '' ,avatar = new_user.avatar ,hash_pass = new_user.password) 
        db.session.add(user)
        db.session.commit()
        
        welcome_email('Welcome to Pitch Perfect', 'email/welcome_user', user.email, user= user)
        
        return redirect(url_for('auth.login'))
    
    title = 'Create an account: Pitch Perfect Sign-up'     
    
    return render_template('auth/signup.html', form = new_user, title= title)

@auth.route('/logout')
def logout():
    logout()
    return redirect(url_for('main.index'))