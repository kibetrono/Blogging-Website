from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField, SelectField,PasswordField
from wtforms.validators import input_required
categories = ['lifestyle','fashion','food','promotion','photography','travel','health']


class UpdateForm(FlaskForm):
    biography = TextAreaField("Your Biography", validators=[input_required(message='Biography field is required')])
    submit = SubmitField("Update Profile")


class PostForm(FlaskForm):
    title = StringField("post title", validators=[input_required(message='Post title is required')],render_kw={"placeholder":"Post Title"})
    category = SelectField("Post category", validators=[input_required(message="Post Category required")],choices=categories)
    post = TextAreaField("Post description", validators=[input_required(message="Post required")],render_kw={"placeholder":"Post description"})
    submit = SubmitField("Post Post")


class CommentForm(FlaskForm):
    comment = TextAreaField('Post comment', validators=[input_required(message="Comment field is required")],render_kw={"placeholder": "Your Comment"})
    submit = SubmitField('Comment')

class SubscribeForm(FlaskForm):

    email = StringField('Your Email Address...',validators=[input_required(message="Email field required")],render_kw={"placeholder":"Your email address "})
    name = StringField('Enter your name',validators=[input_required(message="Name required")],render_kw={"placeholder":"Your name"})
    submit = SubmitField('Subscribe')