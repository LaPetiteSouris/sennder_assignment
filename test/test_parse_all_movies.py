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
    # Expect field people to be filled with
    # Monkey D.Luffy and Vinsmoke Sanji
    assert expected_results.get("2baf70d1-42bb-4437-b551-e5fed5a87abe"
                                ) == joined_movies_people_data.get(
                                    "2baf70d1-42bb-4437-b551-e5fed5a87abe")
                                    
    # Expect field people to be filled with
    # Harry Potter
    assert expected_results.get(
        "2baf70d1-42bb-4437-b551-efghiklm"
    ) == joined_movies_people_data.get(
        "2baf70d1-42bb-4437-b551-e5fed5a87abe2baf70d1-42bb-4437-b551-efghiklm")
