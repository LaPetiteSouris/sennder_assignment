# -*- coding: utf-8 -*-
from flask_caching import Cache
from utils.config import CACHE_CONFIG

# Flask cache object
cache = Cache(config=CACHE_CONFIG)