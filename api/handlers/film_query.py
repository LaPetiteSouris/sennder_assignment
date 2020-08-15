# -*- coding: utf-8 -*-
from api.utils import logger

log = logger.define_logger(__name__)


def get_film_id_from_url(url):
    return url.rsplit('films/', 1).pop()


def build_film_index(film_data):
    films_to_people_index = {}
    for film in film_data:
        films_to_people_index[film.get("id")] = film
    return films_to_people_index


def build_revert_index_from_people_to_movie(film_data, people_data):
    films_to_people_index = build_film_index(film_data)

    for person in people_data:

        person_id = person.get("id")
        person_data = {"id": person_id, "name": person.get("name")}

        involved_films = person.get("films", [])
        for film_url in involved_films:
            film_id = get_film_id_from_url(film_url)

            people_involved = films_to_people_index[film_id].get(
                "people", {})
            people_involved[person_id] = person_data
            films_to_people_index[film_id]["people"] = people_involved

    return films_to_people_index


def on_movie_request(req_body):
    # Parse info from request body
    return "Hello"
