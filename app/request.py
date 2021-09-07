
from os import path
import pdb
from app import app
import urllib, json
from .models.movie import Movie

api_key = app.config['MOVIE_API_KEY']
base_url = app.config['MOVIE_API_BASE_URL']

# f strings 
# format 

def get_movies(category): 

    get_movies_url = base_url.format(category, api_key)
    
    with urllib.request.urlopen(get_movies_url) as url: 

        get_movies_data = url.read()
        get_movies_response = json.loads(get_movies_data)

        movie_results = None 

        if get_movies_response['results']: 
            movie_results_list = get_movies_response['results']
            movie_results = process_results(movie_results_list)

    return movie_results


def process_results(movie_lists): 

    movie_results = [] 

    for movie in movie_lists: 
        id = movie.get('id')
        title = movie.get('title')
        overview = movie.get('overview')
        poster =  construct_image_url(movie.get('poster_path'))
        vote_average = movie.get('vote_average') 
        vote_count = movie.get('vote_count') 

        if poster: 
            movie_object = Movie(id, title, overview, poster, vote_average, vote_count)
            movie_results.append(movie_object)
    return movie_results

def get_movie(id):
    get_movie_details_url = base_url.format(id,api_key)
    with urllib.request.urlopen(get_movie_details_url) as url:
        movie_details_data = url.read()
        movie_details_response = json.loads(movie_details_data)

        movie_object = None
        if movie_details_response:
            id = movie_details_response.get('id')
            title = movie_details_response.get('original_title')
            overview = movie_details_response.get('overview')
            poster = construct_image_url(movie_details_response.get('poster_path'))
            vote_average = movie_details_response.get('vote_average')
            vote_count = movie_details_response.get('vote_count')
            movie_object = Movie(id,title,overview,poster,vote_average,vote_count)

    return movie_object

def construct_image_url(path): 
    return 'https://image.tmdb.org/t/p/w500{}'.format(path)

