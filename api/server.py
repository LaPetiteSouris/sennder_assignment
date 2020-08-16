# -*- coding: utf-8 -*-
from flask import Flask

from api.errors.error_handler import error_handler_api
from api.routes import ghibli
from api.cache import cache
from utils import logger

log = logger.define_logger('API started')

app = Flask(__name__)
app.register_blueprint(ghibli)
app.register_blueprint(error_handler_api)

# Initialize cache
cache.init_app(app)
