# -*- coding: utf-8 -*-
from utils import logger
from engines.query_engine import fetch_data_from_ghibli
log = logger.define_logger(__name__)


def on_movie_request(req_body):
    """Handle request on movie endpoint.

    Args:
        req_body (flask request obj): Flask request object

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
    return fetch_data_from_ghibli()
