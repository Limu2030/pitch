from flask import render_template

from app.requests import get_news
from . import main

@main.route('/')
def index(): 
    return render_template('index.html', news = news)
    