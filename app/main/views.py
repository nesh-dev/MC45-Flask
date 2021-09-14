from flask import render_template
from ..request import get_movies, get_movie
from . import main


# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    popular_movies = get_movies('popular')
    upcoming_movie = get_movies('upcoming')
    now_showing_movie = get_movies('now_playing')
    title = 'Home -'
    return render_template('index.html', popular= popular_movies, upcoming = upcoming_movie, now_showing = now_showing_movie)


@main.route('/movie/<movie_id>')
def movie(movie_id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    movie = get_movie(movie_id)
    title = f'{movie.title}'
    return render_template('movie.html', movie = movie, title=title)
