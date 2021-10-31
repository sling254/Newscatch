from flask import render_template, url_for
from . import main
from ..request import get_news_source, get_articles



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



@main.route('/articles/<id>')
def display_article(id):
    '''
	articles  page function that returns the articles page 
	'''
    article = get_articles(id)
    title = f'News Room articles | {id}'
    return render_template('articles.html',title= title,articles= article)