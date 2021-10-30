from flask import render_template, url_for
from . import main
from ..request import get_news_source




@main.route('/')
def index():
    """
    a function to view  the home page 
    """
    technology = get_news_source('technology')
    title = "News Home Source"
    return render_template('index.html', title=title, technology=technology)



@main.route('/articles')
def display_article():
    return render_template('articles.html')