# -*- coding: utf-8 -*-
from utils import logger
from engines.fetch_external_api.fetch_helper import GhibliAPI
log = logger.define_logger(__name__)

BASE_URL = "https://ghibliapi.herokuapp.com"
MOVIE_URL = "/films"
PEOPLE_URL = "/people"


def get_film_id_from_url(url):
    """ Stripe out the film ID from a film URL.
    Args:
        url (str): A complete film URL that contains film ID

    Returns:
        film_id (str): ID of the film

    Examples:
        >>> get_film_id_from_url('https://ghibliapi.herokuapp.com/films/0440483e-ca0e-4120-8c50-4c8cd9b965d6')
        '0440483e-ca0e-4120-8c50-4c8cd9b965d6'
    """
    return url.rsplit('films/', 1).pop()


def build_film_index(film_data):
    """ Given the raw data of all films, build a hash table (dict)
    which each key is the film ID and content is the data of the film.
    Hash table has O(1) time complexity when querying, which is convenient in
    searching for relation between films and people.

    Args:
        film_data (dict): Dictionary contains raw data of all films, parsed
        from Ghibli studio

    Returns:
        dict: a hash table (dict) which each key is the film ID and content
        is the data of the film
    """
    films_to_people_index = {}
    for film in film_data:
        films_to_people_index[film.get("id")] = film
    log.debug("Parsed film data to build hashed table of films",
              extra={"data": films_to_people_index})
    return films_to_people_index


def build_revert_index_from_people_to_movie(film_data, people_data):
    """ Given the raw data of all films and all people build a hash table
    (dict) which each key is the film ID and content is the data of the film.

    The data of each film should contain a field named 'people_invovled'. This
    field in turn is a hash table (dict), where each key is the id of the
    person involved in the films and the content is the data of that person

    Hash table has O(1) time complexity when querying, which is convenient in
    searching for relation between films and people.

    Args:
        film_data (dict): Dictionary contains raw data of all films, parsed
        from Ghibli studio
        people_data (dict): Dictionary contains raw data of all people, parsed
        from Ghibli studio

    Returns:
        dict: a hash table (dict) which each key is the film ID and content
        is the data of the film. The data of each film should contain a
        field named 'people_invovled'. This field in turn is a hash table
        (dict), where each key is the id of the person involved in the
        films and the content is the data of that person
    """
    # First, from raw data of films, build
    # a dict table to facilitate the query
    films_to_people_index = build_film_index(film_data)

    for person in people_data:
        # Get relevant information of each person.
        # This piece of information will be included
        # in the film dataset as reference
        person_id = person.get("id")
        person_data = {"id": person_id, "name": person.get("name")}

        # Each person data set contains a field named
        # 'film'. This field is a list, contains URI to
        # the film this person involved. E.g
        # "films": [
        #   "https://ghibliapi.herokuapp.com/films/0440483e-ca0e-4120-8c50-4c8cd9b965d6"
        # ]

        involved_films = person.get("films", [])
        for film_url in involved_films:
            # stripe only the film ID
            film_id = get_film_id_from_url(film_url)
            # With this ID, trace back to the film index
            # and get the people_involved field of the
            # corresponding film
            people_involved = films_to_people_index[film_id].get(
                "people_involved", {})
            # Add this person to the `people_involved` field of
            # the corresponding film
            people_involved[person_id] = person_data
            films_to_people_index[film_id]["people_involved"] = people_involved

    return films_to_people_index


def fetch_data_from_ghibli(params=None):
    """Fetch films data and the people involved
    from Ghibli Studio

    Args:
        params (dict):

    Returns:
        movie_data(dict): The full dataset of all movies, each movie
        should contains informtion on people involved.
        Each movie is stored in key/value form, where the key is
        the id of the movie.

    Example:
    {
        "if_of_film_one_piece": {
            "id": "if_of_film_one_piece",
            "title": "One Piece",
            "description": "Kaizoku Ou ni, ore wa naru",
            "director": "Eiichiro Oda",
            "producer": "Tohei Animation",
            "release_date": "2010",
            "rt_score": "95",
            # Expect field people to be filled with
            # Monkey D.Luffy and Vinsmoke Sanji
            "people_involved": {
                "id_of_monkey_dluffy": {
                    "id": "id_of_monkey_dluffy",
                    "name": "Monkey D. Luffy",
                },
                "id_of_vinsmoke_sanji": {
                    "id": "id_of_vinsmoke_sanji",
                    "name": "Vinsmoke Sanji",
                }
            }
        },
        "id_of_film_harry_potter": {
            "id": "id_of_film_harry_potter",
            "title": "Harry Potter",
            "description": "Witch craft",
            "director": "J.K Rowling",
            "producer": "Hollywood",
            "release_date": "2010",
            "rt_score": "95",
            # Expect field people to be filled with
            # Harry Potter
            "people_involved": {
                "id_of_harry_potter": {
                    "id": "id_of_harry_potter",
                    "name": "Harry Potter",
                }
            }
        }
    }
    """
    ghibli_api = GhibliAPI(base_url=BASE_URL)
    # Fetch films data
    film_data = ghibli_api.get_all_films(film_url=MOVIE_URL)
    # Fetch people data
    people_data = ghibli_api.get_all_people(people_url=PEOPLE_URL)
    log.info(
        "Successfully fetched film data and people data from external server")
    joined_film_people = build_revert_index_from_people_to_movie(
        film_data, people_data)
    return joined_film_people
