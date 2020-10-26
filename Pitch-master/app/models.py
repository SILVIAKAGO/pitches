from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    '''
    @login_manager.user_loader Passes in a user_id to this function
    Function queries the database and gets a user's id as a response
    '''
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    # role_id e= db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    # reviews = db.relationship('Review',backref = 'user',lazy = "dynamic")
    pitches = db.relationship("Pitch", backref="user", lazy = "dynamic")
    comment = db.relationship("Comments", backref="user", lazy = "dynamic")
    vote = db.relationship("Votes", backref="user", lazy = "dynamic")

    def __repr__(self):
        return f'User {self.username}'

    # pass_secure = db.Column(db.String(255))
 
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter 
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

class Category(db.Model):
    __tablename__ = 'categories'
        #columns
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))

        #save pitch
    def save_category(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_categories(cls):
        categories = Category.query.all()
        return categories

#pitches class
class Pitch(db.Model):
    """ List of pitches in each category """

    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    content = db.Column(db.String)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    comment = db.relationship("Comments", backref="pitches", lazy = "dynamic")
    vote = db.relationship("Votes", backref="pitches", lazy = "dynamic")



    def save_pitch(self):
        ''' Save the pitches '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def clear_pitches(cls):
        Pitch.all_pitches.clear()

    # display pitches

    def get_pitches(id):

        pitches = Pitch.query.filter_by(category_id=id).all()

      
        return pitches


# comments
class Comments(db.Model):
    '''User comment model for each pitch '''

    __tablename__ = 'comments'

    # add columns
    id = db.Column(db. Integer, primary_key=True)
    opinion = db.Column(db.String(255))
    time_posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    pitches_id = db.Column(db.Integer, db.ForeignKey("pitches.id"))


    def save_comment(self):
        '''
        Save the Comments/comments per pitch
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(self, id):
        comment = Comments.query.order_by(
            Comments.time_posted.desc()).filter_by(pitches_id=id).all()
        return comment

#votes
class Votes(db.Model):
    '''class to model votes '''
    __tablename__='votes'

    id = db.Column(db. Integer, primary_key=True)
    vote = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    pitches_id = db.Column(db.Integer, db.ForeignKey("pitches.id"))

    def save_vote(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_votes(cls,user_id,pitches_id):
        votes = Votes.query.filter_by(user_id=user_id, pitches_id=pitches_id).all()
        return votes
