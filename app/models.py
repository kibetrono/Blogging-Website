from flask_login import UserMixin
from . import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(255), index=True)
    email = db.Column(db.String(255), index=True)
    biography = db.Column(db.String(255))
    profile_pic = db.Column(db.String())
    password_secure = db.Column(db.String(255))
    posts = db.relationship('Post', backref='user', lazy='dynamic')
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    upvote = db.relationship('Upvote', backref='user', lazy='dynamic')
    downvote = db.relationship('Downvote', backref='user', lazy='dynamic')
    comment = db.relationship('Comment', backref='user', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_secure, password)

    def __repr__(self):
        return f'User: {self.username}'


@login_manager.user_loader
def load_user(user_id):
    """call back function that retrieves a user when a unique identifier is passed"""
    return User.query.get(int(user_id))


def __repr__(self):
    return f'User: {self.name}'


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    title = db.Column(db.String(255))
    category = db.Column(db.String)
    content = db.Column(db.String())
    image_path = db.Column(db.String())
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    upvote = db.relationship('Upvote', backref='post', lazy='dynamic')
    downvote = db.relationship('Downvote', backref='post', lazy='dynamic')
    comments = db.relationship('Comment', backref='post', lazy='dynamic')

    def save_post(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_posts(cls):
        posts = Post.query.all()
        return posts

    @classmethod
    def get_post(cls, id):
        post = Post.query.filter_by(id=id).first()
        return post


class Subscribe(UserMixin, db.Model):
   __tablename__="subscribes"

   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(255))
   email = db.Column(db.String(255),unique = True,index = True)


   def save_subscriber(self):
       db.session.add(self)
       db.session.commit()

   @classmethod
   def get_subscribers(cls,id):
       return Subscribe.query.all()


   def __repr__(self):
       return f'User {self.email}'

class Upvote(db.Model):
    __tablename__ = 'upvotes'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_upvotes(cls, id):
        upvote_results = Upvote.query.filter_by(post_id=id).all()
        return upvote_results

    def __repr__(self):
        return f'{self.user_id}:{self.post_id}'


class Downvote(db.Model):
    __tablename__ = 'downvotes'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_downvotes(cls, id):
        downvote_results = Downvote.query.filter_by(post_id=id).all()
        return downvote_results

    def __repr__(self):
        return f'{self.user_id}:{self.post_id}'


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Text())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls, post_id):
        comments_results = Comment.query.filter_by(post_id=post_id).all()

        return comments_results

    def __repr__(self):
        return f'comment:{self.comment}'
