from . import main
from flask import render_template, url_for, abort, request, redirect, flash
from flask_login import login_required, current_user
from ..models import User, Post, Comment, Subscribe
from .forms import UpdateForm, PostForm, CommentForm, SubscribeForm
from .. import db, photos
from ..requests import get_random_quote, get_quote
from ..email import mail_message


@main.route('/')
def index():
    """main view function"""
    quotes = get_random_quote()
    received_posts = Post.query.order_by(Post.created_at.desc()).all()

    # all_posts = Post.query.all()
    title = "Flask personal blog"
    return render_template("index.html", all_posts=received_posts, title=title, quote=quotes)


@main.route('/profile/<my_name>')
@login_required
def profile(my_name):
    user = User.query.filter_by(username=my_name).first()
    if user is None:
        abort(404)

    return render_template("profile/profile.html", user=user)


@main.route('/upquery.get(date/<my_name>', methods=['GET', 'POST'])
@login_required
def edit_profile(my_name):
    title = "Edit profile"
    user = User.query.filter_by(username=my_name).first()
    if user is None:
        abort(404)
    update_form = UpdateForm()
    if update_form.validate_on_submit():
        user.biography = update_form.biography.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('.profile', my_name=user.username))

    return render_template("profile/update.html", update_form=update_form, title=title)


@main.route('/updateImage/<my_name>', methods=['POST'])
@login_required
def update_image(my_name):
    title = "Update image"
    user = User.query.filter_by(username=my_name).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic = path
        db.session.commit()
    return redirect(url_for('main.profile', my_name=my_name, title=title))


@main.route('/new-post/<id>', methods=['GET', 'POST'])
@login_required
def post(id):
    """New post function"""
    title = "New post"
    post_form = PostForm()
    if post_form.validate_on_submit():
        title = post_form.title.data
        category = post_form.category.data
        post = post_form.post.data

        new_post = Post(title=title, category=category, post=post, user=current_user)

        new_post.save_post()
        return redirect(url_for('.index'))

    return render_template('post.html', post_form=post_form, title=title)


@main.route('/comment/<id>', methods=['GET', 'POST'])
@login_required
def comment(id):
    comment_form = CommentForm()
    post = Post.query.get(id)
    fetch_all_comments = Comment.query.filter_by(post_id=id).all()
    if comment_form.validate_on_submit():
        comment = comment_form.comment.data
        post_id = id
        user_id = current_user._get_current_object().id
        new_comment = Comment(comment=comment, user_id=user_id, post_id=post_id)
        new_comment.save_comment()
        return redirect(url_for('.comment', id=post_id))
    return render_template('comments.html', comment_form=comment_form, post=post, all_comments=fetch_all_comments)


#######################################CRUD####################################

@main.route('/crud')
def index2():
    all_posts = Post.query.order_by(Post.created_at.desc()).all()

    return render_template('index2.html', all_posts=all_posts)


@main.route('/add', methods=["GET", "POST"])
def addpost():
    """Add post function"""
    all_pizzas = Post.query.all()

    if request.method == 'POST':
        post_title = request.form['title']
        post_category = request.form['category']
        post_content = request.form['content']
        new_post = Post(title=post_title, category=post_category, content=post_content)
        if 'image' in request.files:
            filename = photos.save(request.files['image'])
            path = f'photos/{filename}'
            new_post.image_path = path
            db.session.commit()

        db.session.add(new_post)
        db.session.commit()
        flash("Post added successfully")
        return redirect(url_for(".index2"))

    return render_template('CRUD/create.html')


@main.route('/pizza/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    """Edit pizza function"""

    all_data = Post.query.get(id)
    if request.method == 'POST':
        all_data.title = request.form['title']
        all_data.category = request.form['category']
        all_data.content = request.form['content']

        db.session.commit()
        flash("Post successfully updated")
        return redirect(url_for(".index2"))

    return render_template("CRUD/update.html", data=all_data)


@main.route("/post/<int:id>/<int:comment_id>/delete")
def delete_comment(id, comment_id):
    post = Post.query.filter_by(id=id).first()
    comment = Comment.query.filter_by(id=comment_id).first()
    db.session.delete(comment)
    db.session.commit()
    return redirect(url_for("main.comment", id=post.id))


@main.route('/delete/<id>', methods=["GET", "POST"])
def delete(id):
    """Delete post function"""
    data = Post.query.get(id)
    db.session.delete(data)
    db.session.commit()

    flash("Post successfully deleted")

    return redirect(url_for(".index2"))


@main.route('/subscribe', methods=['GET', 'POST'])
def subscribe():
    sub_form = SubscribeForm()

    if sub_form.validate_on_submit():
        client = Subscribe(email=sub_form.email.data, name=sub_form.name.data)

        db.session.add(client)
        db.session.commit()

        mail_message("Hello, Welcome To KibRono's Blog.", "email/welcome", client.email, subscriber=client)
        return redirect(url_for('main.index'))

    return render_template('subscribe.html', sub_form=sub_form)
