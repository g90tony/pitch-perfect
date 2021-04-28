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
     
        
        
