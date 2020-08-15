# -*- coding: utf-8 -*-
from utils import logger

log = logger.define_logger(__name__)


def on_request(req_body):
    # Parse info from request body
    return "Hello"
