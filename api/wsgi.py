# -*- coding: utf-8 -*-
from api import config
from api.server import app
from api.utils import logger

log = logger.define_logger(__name__)

if __name__ == "__main__":
    log.info('service ready',
             extra={'server': {
                 'host': config.HOST,
                 'port': config.PORT
             }})
    app.run(debug=False, host=config.HOST, port=config.PORT)
