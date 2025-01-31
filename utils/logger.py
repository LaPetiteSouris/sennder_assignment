# -*- coding: utf-8 -*-
import os
import logging

import structlog
from utils.config import LOG_DEFAULT_LEVEL


def _log_factory(handler, level, namespace):
    """ Opinionated logger factory. """
    logger = logging.getLogger(namespace)
    logger.setLevel(level)
    if not logger.handlers:
        logger.addHandler(handler)

    return structlog.wrap_logger(
        logger,
        processors=[
            structlog.stdlib.filter_by_level, structlog.stdlib.add_log_level,
            structlog.stdlib.add_logger_name,
            structlog.processors.TimeStamper(fmt='iso',
                                             utc=True,
                                             key='created_at'),
            structlog.processors.JSONRenderer()
        ])


def define_logger(namespace=__name__, level=None):
    """ Configure and provide a structured logger. """
    level = level or os.environ.get('LOG_LEVEL', LOG_DEFAULT_LEVEL)
    return _log_factory(logging.StreamHandler(), level.upper(), namespace)
