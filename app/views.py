from flask import render_template
from flask.json.tag import PassDict
from .request import get_movies
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    popular_movies = get_movies('popular')
    title = 'Home -'
    return render_template('index.html', popular= popular_movies)


@app.route('/movie/<movie_id>')
def movie(movie_id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('movie.html', movie_id = movie_id)
