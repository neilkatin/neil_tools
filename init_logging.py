
import os

import logging
from logging.config import dictConfig

def init_logging(app_name):
    logging_config = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'default',
                'level': 'DEBUG',
                'stream': 'ext://sys.stderr'
            },
            #'wsgi': {
            #    'class': 'logging.StreamHandler',
            #    'formatter': 'default',
            #    'level': 'DEBUG',
            #    'stream': 'ext://flask.logging.wsgi_errors_stream'
            #},
        },
        'formatters': {
            'default': {
                'format': '%(asctime)s %(levelname)-5s %(name)-10s %(funcName)-.15s:%(lineno)d %(message)s',
                'datefmt': '%Y-%m-%d %H:%M:%S',
            },
        },
        'root': {
            'level': 'INFO',
            #'handlers': [ 'console', 'wsgi' ],
            #'handlers': [ 'wsgi' ],
            'handlers': [ 'console' ],
        },
        'loggers': {
            'urllib3': {
                'level': 'INFO',
            },
            'selenium': {
                'level': 'INFO',
            },
            'requests_oauthlib': {
                'level': 'INFO',
            },
            'O365_local.connection': {
                'level': 'WARN',
            },
            'O365.connection': {
                'level': 'WARN',
            },
        },
    }

    logging.config.dictConfig(logging_config)
    log = logging.getLogger(app_name)

    return log


