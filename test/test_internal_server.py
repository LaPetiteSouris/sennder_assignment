# -*- coding: utf-8 -*-
import os
import vcr
import requests
from urllib.parse import urljoin
from flask_testing import LiveServerTestCase

from api.server import app

fixtures_path = os.path.join(os.path.dirname(__file__), '__fixtures__')


class TestInternalAPI(LiveServerTestCase):
    def create_app(self):
        app.config['TESTING'] = True
        # Default port is 5000
        app.config['LIVESERVER_PORT'] = 8943
        # Default timeout is 5 seconds
        app.config['LIVESERVER_TIMEOUT'] = 10
        return app

    @vcr.use_cassette(cassette_library_dir=fixtures_path)
    def test_server_is_up_and_running(self):
        # Movie endpoint
        base_url = self.get_server_url()
        movie_endpoint = "/v1/movies"
        full_url_movie = urljoin(base_url, movie_endpoint)

        response = requests.get(full_url_movie)
        self.assertEqual(response.status_code, 200)