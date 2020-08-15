# -*- coding: utf-8 -*-
import os

CACHE_CONFIG = {
    "CACHE_REDIS_HOST": os.environ.get("CACHE_REDIS_HOST"),
    "CACHE_REDIS_PORT": os.environ.get("CACHE_REDIS_PORT"),
    "CACHE_KEY_PREFIX": os.environ.get("CACHE_KEY_PREFIX", "sennder"),
    "CACHE_TYPE": "redis",
}

if os.environ.get("CACHE") == "IN_MEMORY":
    CACHE_CONFIG = {
        "CACHE_TYPE": "simple",
    }

EXTERNAL_API_CONFIG = {
    "URL": os.environ.get("STUDIO_URL", "https://ghibliapi.herokuapp.com"),
    "MOVIE_URL": os.environ.get("MOVIE_URL", "/films"),
    "PEOPLE_URL": os.environ.get("PEOPLE_URL", "/people"),
}

LOG_DEFAULT_LEVEL = "info"
if os.environ.get("ENV") == "DEV":
    LOG_DEFAULT_LEVEL = "debug"
