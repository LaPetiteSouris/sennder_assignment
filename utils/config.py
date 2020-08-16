# -*- coding: utf-8 -*-
import os

CACHE_CONFIG = {
    "CACHE_TYPE": "simple",
}

# REDIS should be activated explicitly
if os.environ.get("CACHE") == "REDIS":
    CACHE_CONFIG = {
        "CACHE_REDIS_HOST": os.environ.get("CACHE_REDIS_HOST"),
        "CACHE_REDIS_PORT": os.environ.get("CACHE_REDIS_PORT"),
        "CACHE_REDIS_PASSWORD": os.environ.get("CACHE_REDIS_PORT", ""),
        "CACHE_KEY_PREFIX": os.environ.get("CACHE_KEY_PREFIX", "sennder"),
        "CACHE_TYPE": "redis",
    }

LOG_DEFAULT_LEVEL = "info"

if os.environ.get("ENV") == "DEV":
    LOG_DEFAULT_LEVEL = "debug"
