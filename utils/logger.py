# -*- coding: utf-8 -*-
import os
import logging

import logmatic
ENV = os.getenv('ENV', 'dev')


def define_logger(log_component='no name'):
    """ Define a  logger with 3 default levels

    :param log_component: name of the component which generates the log
    :return: logger object
    """
    logger = logging.getLogger(log_component)

    handler = logging.StreamHandler()
    handler.setFormatter(logmatic.JsonFormatter())

    logger.addHandler(handler)
    if ENV == 'dev':
        logger.setLevel(logging.DEBUG)
    logger.setLevel(logging.INFO)

    return logger
