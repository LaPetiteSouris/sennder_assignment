# -*- coding: utf-8 -*-
import os
import vcr
from unittest.mock import patch
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
        self.client = app.test_client()
        return app

    @vcr.use_cassette(cassette_library_dir=fixtures_path)
    def test_server_is_up_and_running(self):
        # Movie endpoint
        base_url = self.get_server_url()
        movie_endpoint = "/v1/movies"
        full_url_movie = urljoin(base_url, movie_endpoint)

        response = self.client.get(full_url_movie)
        self.assertEqual(response.status_code, 200)

    @patch("api.routes.on_movie_request", return_value="mock")
    @vcr.use_cassette(cassette_library_dir=fixtures_path)
    def test_cache_is_working(self, mock_on_movie_request):
        # Movie endpoint
        base_url = self.get_server_url()
        movie_endpoint = "/v1/movies"
        full_url_movie = urljoin(base_url, movie_endpoint)

        # First hit should not be cached
        _ = self.client.get(full_url_movie)
        mock_on_movie_request.assert_called_once()

        # Second hit should be cached so the function
        # on_movie_request should NOT be called
        _ = self.client.get(full_url_movie)
        mock_on_movie_request.assert_called_once()