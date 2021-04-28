from . import db
from . import login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask login import UserMixin

class Pitch(db.model):
    __tablename__ = 'pitches'
    
    id = db.Column(db.Integer)
    body = db.Column(db.String)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_on = db.Column(db.Integer, default=datetime.utcnow())
    up_votes = db.Column(db.Integer)
    down_votes = db.Column(db.Integer)

    def __init__(self,id,body,category_id,user_id,up_votes,down_votes, ):
        self.id = id
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
            pitches = Pitch.query.filter_by(category = category)limit(20)
        
        else :
            pitches = Pitch.query.limit(20)
        
        pitch_results = list()
        
        if pitches is not None:
            for pitch in pitches:
                category_record = Category.query.filter_by(pitch.category_id).first()
                user_record = User.query.filter_by(pitch.user_id).first()
                comments = Comment.get_comments(pitch.id)
                
                pitch_result_item['id'] = pitch.id 
                pitch_result_item['body'] = pitch.body 
                pitch_result_item['created_on'] pitch.created_on
                pitch_result_item['username'] = user_record.username
                pitch_result_item['avatar'] = user_record.avatar
                pitch_result_item['category'] = category_record.title
                pitch_result_item['up_votes'] = pitch.up_votes 
                pitch_result_item['down_votes'] = pitch.down_votes 
                pitch_result_item['comments'] = comments
                
                pitch_result.append(pitch_result_item)

            return pitch_results
     
        
        
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String)
    user_email = db.Column(db.String)
    bio = db.Column(db.String)
    avatar = db.Column(db.String)
    hash_pass = db.Column(db.String(255))
    date_joined = db.Column(db.Integer,  default=datetime.utcnow())
    pitches = db.relationships('Pitch', backref='pitches', lazy='dynamic')
    
    
    def __init__(self, id, username,user_email,bio,avatar,hash_pass):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.user_email = user_email
        self.bio = bio
        self.avatar = avatar
        self.hash_pass = hash_pass
        self.date_joined = date_joined
        self.pitches = list()
    
    def create_new_user(self):
        db.session.db(self)
        db.session.commit()
        
        
    def __repr__ (self):
        return f'User {self.username}'
        
    @login_manger.user_loader
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
    pitches = db.relationships('Pitch', backref='pitches', lazy='dynamic')
    
    def add_category(self):
        db.session.add(self)
        db.session.commit()
    
    def __repr__ (self):
        return f'Category {self.title}'
        
    
    @classmethod
    def get_categories(cls):
        categories: Category.query.all()
        
        return categories
    
