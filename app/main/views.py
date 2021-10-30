from flask import render_template, url_for
from . import main
from ..request import get_news_source




@main.route('/')
def index():
    """
    a function to view  the home page 
    """
    technology = get_news_source('technology')
    sports = get_news_source('sports')
    business = get_news_source('business')
    science = get_news_source('science')
    title = "News Home Source"
    return render_template('index.html', title=title, technology=technology, sports=sports,business=business, science=science)



@main.route('/articles')
def display_article():
    return render_template('articles.html')