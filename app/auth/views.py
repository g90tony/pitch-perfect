from flask import render_template, url_for, flash
from flask_login import login_user
from flask_login import login_user, logout_user, login_required

from . import auth
from ..models import User
from .forms import RegistrationForm, LoginForm

@auth.route('/login')
def login():
    new_login = LoginForm()
    
    if new_login.validate_on_submit():
        user = User.query.filter_by(email = new_login.email.data).first()
        
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user, login_form.remember_user.data)
            
            return redirect(request.args.get('next') or url_for('main.index'))
        
        flash('Invalid email or password')
        
    title = 'Welcome back: Pitch Perfect Login'
    
    return render_template('auth/login', login_form = new_login, title = title)

