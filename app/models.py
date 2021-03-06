from . import db
from . import login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Pitch(db.Model):
    __tablename__ = 'pitches'
    
    id = db.Column(db.Integer, primary_key= True)
    body = db.Column(db.String)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_on = db.Column(db.Time, default=datetime.utcnow())
    up_votes = db.Column(db.Integer)
    down_votes = db.Column(db.Integer)
    comments =  db.relationship('Comment', backref='comments', lazy='dynamic')

    def __init__(self,body,category_id,user_id,up_votes,down_votes ):
        self.body = body
        self.category_id = category_id
        self.user_id = user_id
        self.up_votes = up_votes
        self.down_votes = down_votes
        
    def save_pitch(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def get_pitches(cls, category = None):
        if category is not None:
            pitches = Pitch.query.filter_by(category_id = category).all()
        
        else :
            pitches = Pitch.query.limit(20)
        
        pitch_results = list()
        
        if pitches is not None:
            for pitch in pitches:
                pitch_result_item = dict()
                
                category_record = Category.query.filter_by(id = pitch.category_id).first()
                user_record = User.query.filter_by(id = pitch.user_id).first()
             
                
                pitch_result_item['id'] = pitch.id 
                pitch_result_item['body'] = pitch.body 
                pitch_result_item['created_on'] = pitch.created_on.strftime("%a, %d %B, %y")
                pitch_result_item['username'] = user_record.username
                pitch_result_item['avatar'] = user_record.avatar
                pitch_result_item['category'] = category_record.title
                pitch_result_item['up_votes'] = pitch.up_votes 
                pitch_result_item['down_votes'] = pitch.down_votes 
            
                
                pitch_results.append(pitch_result_item)

            return pitch_results
     
        
        
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String)
    user_email = db.Column(db.String)
    bio = db.Column(db.String)
    avatar = db.Column(db.String)
    hash_pass = db.Column(db.String(255))
    pitches = db.relationship('Pitch', backref='pitches', lazy='dynamic')
    
    
    def create_new_user(self):
        db.session.add(self)
        db.session.commit()
        
        
    def __repr__ (self):
        return f'User {self.username}'
        
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)
    
    @property
    def password(self):
        raise AttributeError('You can not read the password attribute')
    
    @password.setter
    def password(self, password):
        self.hash_pass = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.hash_pass, password)
    
    
class Category(db.Model):
    
    __tablename__ = 'categories'
    
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String)
    pitches = db.relationship('Pitch', backref='pitches_relation', lazy='dynamic')
    
    def add_category(self):
        db.session.add(self)
        db.session.commit()
    
    def __repr__ (self):
        return f'Category {self.title}'
        
    
    @classmethod
    def get_categories(cls):
        categories: Category.query.all()
        
        return categories
    
class Comment(db.Model):
    
    __tablename__ = 'comments'
    
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer)
    comment = db.Column(db.String)
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    
    
    
    def add_comment(self):
        db.session.add(self)
        db.session.commit()
        
    def __repr__ (self):
        return f'User {self.username}'

    def get_comments(pitch_id):
        comments = Comment.query.filter_by(pitch_id = pitch_id).all()
        
        comment_results = list()
        
        if comments is not None:
            comment_item = dict()
            
            for item in comments:
                
                user_details = User.query.filter_by(id = item.user_id).first()
                
                comment_item['id'] = item.id
                comment_item['comment'] = item.comment
                comment_item['username'] = user_details.username
                
                comment_results.append(comment_item)
                
        return comment_results

    def get_comment_responses(response_id):
        responses = Comment.query.filter_by(response_id = response_id).all()
        
        responses_results = list()
        
        if responses is not None:
            response_item = dict()
            
            for item in responses:
                
                user_details = User.query.filter_by(id = item.user_id).first()
                
                response_item['id'] = item.id
                response_item['comment'] = item.comment
                response_item['username'] = user_details.username
                
                responses_results.append(comment_item)
                
        return responses_results
                