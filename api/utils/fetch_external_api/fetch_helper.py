# -*- coding: utf-8 -*-
import json
import requests
from urllib.parse import urljoin
from api.errors.api_exception import ExternalAPIFetchError


class GhibliAPI(object):
    def __init__(self, base_url, auth=None):
        self.base_url = base_url
        self.auth = auth

    @staticmethod
    def get_data_from_url(url, params):
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return json.loads(response.text)
        raise ExternalAPIFetchError(
            "An error occurs upon fetching data from external service")

    def get_all_films(self, film_url="/films"):
        all_films_url = urljoin(self.base_url, film_url)
        return self.get_data_from_url(all_films_url)

    def get_all_people(self, film_url="/people"):
        all_people_url = urljoin(self.base_url, film_url)
        return self.get_data_from_url(all_people_url)
