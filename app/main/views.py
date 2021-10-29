from flask import render_template, url_for
from . import main



@main.route('/')
def index():
    return render_template('index.html')



@main.route('/articles')
def display_article():
    return render_template('articles.html')