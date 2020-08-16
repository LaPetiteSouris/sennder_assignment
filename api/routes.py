# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, request
from api.handlers.film_query import on_movie_request
from api.cache import cache

from utils import logger

ghibli = Blueprint('sennder', __name__)
log = logger.define_logger(__name__)


@ghibli.before_request
def pre_request_logging():
    # Logging statement for every request
    log.info("Processing request",
             remote_addr=request.remote_addr,
             url=request.url,
             data=request.data,
             method=request.method)


@ghibli.route('/v1/ping', methods=['GET'])
def index():
    """ API Handshake """
    return jsonify({'response': 'pong'}), 200


@ghibli.route('/v1/movies', methods=['GET'])
@cache.cached(timeout=60)
def movies():
    """ Handle get all movies request """
    log.info("Processing request on movies")
    response = on_movie_request(request)
    return jsonify(response), 200