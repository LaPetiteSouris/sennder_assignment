# -*- coding: utf-8 -*-
from api.handlers.film_query import join_movies_and_people

sample_get_all_films_response = [{
    "id": "2baf70d1-42bb-4437-b551-e5fed5a87abe",
    "title": "One Piece",
    "description": "Kaizoku Ou ni, ore wa naru",
    "director": "Eiichiro Oda",
    "producer": "Tohei Animation",
    "release_date": "2010",
    "rt_score": "95"
}, {
    "id": "2baf70d1-42bb-4437-b551-efghiklm",
    "title": "Harry Potter",
    "description": "Witch craft",
    "director": "J.K Rowling",
    "producer": "Hollywood",
    "release_date": "2010",
    "rt_score": "95"
}]

sample_get_all_people_response = [{
    "id":
    "ba924631-068e-4436-b6de-f3283fa848f0",
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
    "films": [
        "https://ghibliapi.herokuapp.com/films/2baf70d1-42bb-4437-b551-e5fed5a87abe"
    ],
}, {
    "id":
    "ba924631-068e-4436-b6de-f3283fa848g7",
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
    "films": [
        "https://ghibliapi.herokuapp.com/films/2baf70d1-42bb-4437-b551-e5fed5a87abe"
    ],
}, {
    "id":
    "ba924631-068e-4436-b6de-f3283fa848f9",
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
    "films":
    ["https://ghibliapi.herokuapp.com/films/2baf70d1-42bb-4437-b551-efghiklm"],
}]


def _search_for_person_in_list(person, list_of_people):
    try:
        return next(item for item in list_of_people if item["name"] == person)
    except StopIteration:
        return None


def test_search_for_person_in_list():
    # Given a list of people Vinsmoke Sanji and Monkey D. Luffy
    list_of_people = [{
        "id": "ba924631-068e-4436-b6de-f3283fa848f0",
        "name": "Monkey D. Luffy",
    }, {
        "id": "a924631-068e-4436-b6de-f3283fa848g7",
        "name": "Vinsmoke Sanji",
    }]

    # Search for Luffy
    person = _search_for_person_in_list("Monkey D. Luffy", list_of_people)
    assert person == {
        "id": "ba924631-068e-4436-b6de-f3283fa848f0",
        "name": "Monkey D. Luffy",
    }

    # Search for Sanji
    person = _search_for_person_in_list("Vinsmoke Sanji", list_of_people)
    assert person == {
        "id": "a924631-068e-4436-b6de-f3283fa848g7",
        "name": "Vinsmoke Sanji",
    }

    # Search for Mr.Totoro (not in list)
    person = _search_for_person_in_list("Mr.Totoro", list_of_people)
    assert person is None


def test_join_movies_with_people():
    # Given sample data set
    # Films data set contain 2 films One Piece and Harry Potter
    # People data set contains 3 people, Monkey D.Luffy , Vinsmoke Sanji
    # and Harry Potter

    # Perform the join of 2 datasets
    joined_movies_people_data = join_movies_and_people(
        sample_get_all_films_response, sample_get_all_people_response)

    # Expect that Vinsmoke Sanji and Monkey D.Luffy are in One Piece movie
    # Harry Potter is in Harry Potter movie

    # Expected result should be in form of a dict (hashtable)
    # with key is the ID of movie and content is the movie data
    # included related people
    expected_results = {
        "2baf70d1-42bb-4437-b551-e5fed5a87abe": {
            "id":
            "2baf70d1-42bb-4437-b551-e5fed5a87abe",
            "title":
            "One Piece",
            "description":
            "Kaizoku Ou ni, ore wa naru",
            "director":
            "Eiichiro Oda",
            "producer":
            "Tohei Animation",
            "release_date":
            "2010",
            "rt_score":
            "95",
            # Expect field people to be filled with
            # Monkey D.Luffy and Vinsmoke Sanji
            "people": [{
                "id": "ba924631-068e-4436-b6de-f3283fa848f0",
                "name": "Monkey D. Luffy",
            }, {
                "id": "a924631-068e-4436-b6de-f3283fa848g7",
                "name": "Vinsmoke Sanji",
            }]
        },
        "2baf70d1-42bb-4437-b551-efghiklm": {
            "id":
            "2baf70d1-42bb-4437-b551-efghiklm",
            "title":
            "Harry Potter",
            "description":
            "Witch craft",
            "director":
            "J.K Rowling",
            "producer":
            "Hollywood",
            "release_date":
            "2010",
            "rt_score":
            "95",
            # Expect field people to be filled with
            # Harry Potter
            "people": [{
                "id": "ba924631-068e-4436-b6de-f3283fa848f9",
                "name": "Harry Potter",
            }]
        }
    }

    # Expect the joined data set to contain identical amount of information
    # with expected results (e.g : there should be 2 and ONLY 2 movies,
    # one of them is Harry Potter and the other is One Piece)
    assert set(joined_movies_people_data.keys()) == set(
        expected_results.keys())

    # Expect field people to be filled with
    # Monkey D.Luffy and Vinsmoke Sanji
    # Search for Luffy
    list_of_people = joined_movies_people_data.get(
        "2baf70d1-42bb-4437-b551-e5fed5a87abe", {}).get("people")

    person = _search_for_person_in_list("Monkey D. Luffy", list_of_people)
    # Luffy should be in the list
    assert person == {
        "id": "ba924631-068e-4436-b6de-f3283fa848f0",
        "name": "Monkey D. Luffy",
    }

    # Search for Sanji
    person = _search_for_person_in_list("Vinsmoke Sanji", list_of_people)
    # Sanji should be in the list
    assert person == {
        "id": "a924631-068e-4436-b6de-f3283fa848g7",
        "name": "Vinsmoke Sanji",
    }

    # Expect field people to be filled with
    # Harry Potter
    list_of_people = joined_movies_people_data.get(
        "2baf70d1-42bb-4437-b551-efghiklm", {}).get("people")
    person = _search_for_person_in_list("Harry Potter", list_of_people)
    # Mr.Potter should be in the list
    assert person == {
        "id": "ba924631-068e-4436-b6de-f3283fa848f9",
        "name": "Harry Potter",
    }
