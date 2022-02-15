from . import category
from flask import render_template, url_for, abort, request, redirect
from flask_login import login_required, current_user
from ..models import User, Post, Upvote, Downvote, Comment
from .. import db, photos
from ..requests import get_random_quote,get_quote



@category.route('/')
def index():
    """category view function"""
    all_pitches = Post.query.all()
    title = "Flask Pitch Application"
    return render_template("index.html", all_pitches=all_pitches, title=title)


#######################################Categories##################################
@category.route('/food')
def food():
    quotes = get_random_quote()
    title="Food category"
    food = Post.query.filter_by(category='food').all()
    return render_template('categories/food.html', all_posts=food,title=title,quote=quotes)


@category.route('/lifestyle')
def lifestyle():
    quotes = get_random_quote()
    title="Lifestyle category"
    lifestyle = Post.query.filter_by(category='lifestyle').all()
    return render_template('categories/lifestyle.html', all_posts=lifestyle,title=title,quote=quotes)

@category.route('/fashion')
def fashion():
    quotes = get_random_quote()
    title="fashion category"
    fashion = Post.query.filter_by(category='fashion').all()
    return render_template('categories/fashion.html', all_posts=fashion,title=title,quote=quotes)

@category.route('/health')
def health():
    quotes = get_random_quote()
    title="Health category"
    health = Post.query.filter_by(category='health').all()
    return render_template('categories/health.html', all_posts=health,title=title,quote=quotes)

@category.route('/promotion')
def promotion():
    quotes = get_random_quote()
    title="Promotion category"
    promotion = Post.query.filter_by(category='promotion').all()
    return render_template('categories/promotion.html', all_posts=promotion,title=title,quote=quotes)

@category.route('/photography')
def photography():
    quotes = get_random_quote()
    title="Photography category"
    photography = Post.query.filter_by(category='photography').all()
    return render_template('categories/photography.html', all_posts=photography,title=title,quote=quotes)

@category.route('/travel')
def travel():
    quotes = get_random_quote()
    title="Travel category"
    travel = Post.query.filter_by(category='travel').all()
    return render_template('categories/travel.html', all_posts=travel,title=title,quote=quotes)