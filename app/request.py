
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
        poster = movie.get('poster_path') 
        vote_average = movie.get('vote_average') 
        vote_count = movie.get('vote_count') 

        if poster: 
            movie_object = Movie(id, title, overview, poster, vote_average, vote_count)
            movie_results.append(movie_object)
    return movie_results

