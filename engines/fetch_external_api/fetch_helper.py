# -*- coding: utf-8 -*-
import json
import requests
from urllib.parse import urljoin
from api.errors.api_exception import ExternalAPIFetchError


class GhibliAPI(object):
    """ GhibliAPI is the helper class to retrieve information from Ghibli
    Args:
        base_url (str): Base URL of the Ghibli API
        auth (bool): Enable authentication

    Attributes:
        base_url (str): Base URL of the Ghibli API
        auth (bool): Enable authentication
    """
    def __init__(self, base_url, auth=None):
        self.base_url = base_url
        # Implement authentication if neccessary
        self.auth = auth

    @staticmethod
    def get_data_from_url(url, params=None):
        """ get_data_from_url is the helper function to retrieve
        information from a given URL

        Args:
            url (str): URL to perform GET request
            params (dict): Dictionry containing request's params

        Returns:
            response(json object): response of the endpoint in JSON format.

        Raises:
            ExternalAPIFetchError:  if the request fails, the exeption is
            raised
        """
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return json.loads(response.text)
        raise ExternalAPIFetchError(
            "An error occurs upon fetching data from external service")

    def get_all_films(self, film_url="/films"):
        """ Fetch all films from Ghilib Studio endpoints

        Args:
            film_url (str): relative path to Ghilib Studio
            endpoint to get all films

        Returns:
            response(json object): information of all films on Ghilib studio
            in JSON format.
        """
        all_films_url = urljoin(self.base_url, film_url)
        return self.get_data_from_url(all_films_url)

    def get_all_people(self, film_url="/people"):
        """ Fetch all people from Ghilib Studio endpoints

        Args:
            people_url (str): relative path to Ghilib Studio
            endpoint to get all people

        Returns:
            response(json object): information of all people on Ghilib studio
            in JSON format.
        """
        all_people_url = urljoin(self.base_url, film_url)
        return self.get_data_from_url(all_people_url)
