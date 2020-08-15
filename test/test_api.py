# -*- coding: utf-8 -*-
import vcr
from engines.fetch_external_api.fetch_helper import GhibliAPI


def _assert_correct_film_format(film):
    assert film.get("id") is not None
    assert film.get("title") is not None


def _assert_correct_people_format(person):
    assert person.get("id") is not None
    assert person.get("title") is not None
    assert type(person.get("films")) == list


@vcr.use_cassette()
def test_fetch_movie_from_external_api():
    ghibli_api = GhibliAPI(base_url="https://ghibliapi.herokuapp.com")
    all_films = ghibli_api.get_all_films()
    map(_assert_correct_film_format, all_films)


@vcr.use_cassette()
def test_fetch_people_from_external_api():
    ghibli_api = GhibliAPI(base_url="https://ghibliapi.herokuapp.com")
    all_people = ghibli_api.get_all_people()
    map(_assert_correct_people_format, all_people)