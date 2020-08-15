# -*- coding: utf-8 -*-
from utils import logger
from engines.fetch_external_api.fetch_helper import GhibliAPI
log = logger.define_logger(__name__)


def get_film_id_from_url(url):
    return url.rsplit('films/', 1).pop()


def build_film_index(film_data):
    films_to_people_index = {}
    for film in film_data:
        films_to_people_index[film.get("id")] = film
    log.debug("Parsed film data to build hashed table of films",
              extra={"data": films_to_people_index})
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
                "people_involved", {})
            people_involved[person_id] = person_data
            films_to_people_index[film_id]["people_involved"] = people_involved

    return films_to_people_index


def fetch_data_from_ghibli(params=None):
    ghibli_api = GhibliAPI(base_url="https://ghibliapi.herokuapp.com")
    # Fetch films data
    film_data = ghibli_api.get_all_films()
    # Fetch people data
    people_data = ghibli_api.get_all_people()
    log.info(
        "Successfully fetched film data and people data from external server")
    joined_film_people = build_revert_index_from_people_to_movie(
        film_data, people_data)
    return joined_film_people
