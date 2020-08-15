# -*- coding: utf-8 -*-
from engines.query_engine import build_revert_index_from_people_to_movie, \
    get_film_id_from_url, build_film_index

sample_get_all_films_response = [{
    "id": "if_of_film_one_piece",
    "title": "One Piece",
    "description": "Kaizoku Ou ni, ore wa naru",
    "director": "Eiichiro Oda",
    "producer": "Tohei Animation",
    "release_date": "2010",
    "rt_score": "95"
}, {
    "id": "id_of_film_harry_potter",
    "title": "Harry Potter",
    "description": "Witch craft",
    "director": "J.K Rowling",
    "producer": "Hollywood",
    "release_date": "2010",
    "rt_score": "95"
}, {
    "id": "id_of_a_random_film",
    "title": "Somthing that should not be made",
    "description": "This film should have not been made",
    "director": "Just a random guy",
    "producer": "Just a random producer",
    "release_date": "1320",
    "rt_score": "0.00001"
}]

sample_get_all_people_response = [{
    "id":
    "id_of_monkey_dluffy",
    "name":
    "Monkey D. Luffy",
    "gender":
    "male",
    "age":
    "late teens",
    "eye_color":
    "brown",
    "hair_color":
    "brown",
    "films": ["https://ghibliapi.herokuapp.com/films/if_of_film_one_piece"],
}, {
    "id":
    "id_of_vinsmoke_sanji",
    "name":
    "Vinsmoke Sanji",
    "gender":
    "male",
    "age":
    "late teens",
    "eye_color":
    "brown",
    "hair_color":
    "brown",
    "films": ["https://ghibliapi.herokuapp.com/films/if_of_film_one_piece"],
}, {
    "id":
    "id_of_harry_potter",
    "name":
    "Harry Potter",
    "gender":
    "male",
    "age":
    "late teens",
    "eye_color":
    "brown",
    "hair_color":
    "brown",
    "films": ["https://ghibliapi.herokuapp.com/films/id_of_film_harry_potter"],
}, {
    "id": "id_of_mr_john_smith",
    "name": "John Smith",
    "gender": "male",
    "age": "late teens",
    "eye_color": "brown",
    "hair_color": "brown",
    "films": [],
}]


def test_get_movie_id_from_url():
    # Given an url to person
    url_movie = "https://ghibliapi.herokuapp.com/films/if_of_film_one_piece"

    # Expect the film ID to be parsed correctly
    movie_id = get_film_id_from_url(url_movie)
    assert movie_id == "if_of_film_one_piece"


def test_build_film_index():
    # given sample film data
    # build hash table refer to film ID
    index = build_film_index(sample_get_all_films_response)
    expected_results = {
        "id_of_film_harry_potter": {
            "id": "id_of_film_harry_potter",
            "title": "Harry Potter",
            "description": "Witch craft",
            "director": "J.K Rowling",
            "producer": "Hollywood",
            "release_date": "2010",
            "rt_score": "95"
        },
        "if_of_film_one_piece": {
            "id": "if_of_film_one_piece",
            "title": "One Piece",
            "description": "Kaizoku Ou ni, ore wa naru",
            "director": "Eiichiro Oda",
            "producer": "Tohei Animation",
            "release_date": "2010",
            "rt_score": "95"
        },
        "id_of_a_random_film": {
            "id": "id_of_a_random_film",
            "title": "Somthing that should not be made",
            "description": "This film should have not been made",
            "director": "Just a random guy",
            "producer": "Just a random producer",
            "release_date": "1320",
            "rt_score": "0.00001"
        }
    }
    assert index == expected_results


def test_join_movies_with_people():
    # Given sample data set
    # Films data set contain 2 films One Piece and Harry Potter
    # People data set contains 3 people, Monkey D.Luffy , Vinsmoke Sanji
    # and Harry Potter

    # Perform the join of 2 datasets
    joined_movies_people_data = build_revert_index_from_people_to_movie(
        sample_get_all_films_response, sample_get_all_people_response)

    # Expect that Vinsmoke Sanji and Monkey D.Luffy are in One Piece film
    # Harry Potter is in Harry Potter film

    # Expected result should be in form of a dict (hashtable)
    # with key is the ID of film and content is the film data
    # included related people
    expected_results = {
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
        },
        # The film does not have any related people involved
        # no data
        "id_of_a_random_film": {
            "id": "id_of_a_random_film",
            "title": "Somthing that should not be made",
            "description": "This film should have not been made",
            "director": "Just a random guy",
            "producer": "Just a random producer",
            "release_date": "1320",
            "rt_score": "0.00001",
            # There is no people field for this one
            # as there is no people involved
        }
    }

    # Expect the joined data set to contain identical amount of information
    # with expected results (e.g : there should be 2 and ONLY 2 films,
    # one of them is Harry Potter and the other is One Piece)
    assert set(joined_movies_people_data.keys()) == set(
        expected_results.keys())

    # Expect field people to be filled with
    # Monkey D.Luffy and Vinsmoke Sanji
    # Search for Luffy
    set_of_people = joined_movies_people_data.get("if_of_film_one_piece",
                                                  {}).get("people_involved")

    person = set_of_people.get("id_of_monkey_dluffy")
    # Luffy should be in the list
    assert person == {
        "id": "id_of_monkey_dluffy",
        "name": "Monkey D. Luffy",
    }

    # Search for Sanji
    person = set_of_people.get("id_of_vinsmoke_sanji")
    # Sanji should be in the list
    assert person == {
        "id": "id_of_vinsmoke_sanji",
        "name": "Vinsmoke Sanji",
    }

    # Expect field people to be filled with
    # Harry Potter
    set_of_people = joined_movies_people_data.get("id_of_film_harry_potter",
                                                  {}).get("people_involved")
    person = set_of_people.get("id_of_harry_potter")
    # Mr.Potter should be in the list
    assert person == {
        "id": "id_of_harry_potter",
        "name": "Harry Potter",
    }

    # Expect no people data  is filled in for
    # the film that has no related data
    set_of_people = joined_movies_people_data.get("id_of_a_random_film",
                                                  {}).get("people_involved")

    assert set_of_people is None

    # Expect that Mr.John Smith is NOT present
    # in any film

    for _, film in joined_movies_people_data.items():
        assert film.get("people_involved", {}).get("id_of_mr_john_smith") is None