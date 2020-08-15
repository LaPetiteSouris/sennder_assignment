# -*- coding: utf-8 -*-
from utils import logger

log = logger.define_logger(__name__)


def get_film_id_from_url(url):
    return url.rsplit('films/', 1).pop()


def build_film_index(film_data):
    films_to_people_index = {}
    for film in film_data:
        films_to_people_index[film.get("id")] = film
    return films_to_people_index


def build_revert_index_from_people_to_movie(people_data, film_data):
    films_to_people_index = {}
    for film in film_data:
        films_to_people_index[film.get("id")] = film

    for person in people_data:
        # person_data = {"id": person.get("id"), "name": person.get("name")}
        involved_films = person.get("films", [])
        for film_url in involved_films:
            film_id = get_film_id_from_url(film_url)

            # build reverted indexation from film to people
            # if film exists in film_data
            if film_data.get(film_id):
                # append person data to film
                return


def join_movies_and_people(films, people):
    return {}


def on_movie_request(req_body):
    # Parse info from request body
    return "Hello"
