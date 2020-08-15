# -*- coding: utf-8 -*-
from utils import logger
from engines.query_engine import fetch_data_from_ghibli
log = logger.define_logger(__name__)


def on_movie_request(req_body):
    return fetch_data_from_ghibli()
