import logging
import os
from logging.config import dictConfig

from app.core.config import settings

DEFAULT_FORMATTER = 'default'
DETAILED_FORMATTER = 'detailed'
DEFAULT_FORMAT = '[%(asctime)s] %(levelname)s %(name)s - %(message)s'
DETAILED_FORMAT = '[%(asctime)s] %(levelname)s %(name)s in %(pathname)s:%(lineno)d - %(message)s'
LOG_HANDLERS = ['console', 'file']
UVICORN_LOGGER_CONFIG = {'level': settings.LOG_LEVEL,
                         'handlers': LOG_HANDLERS,
                         'propagate': False}

os.makedirs(settings.LOG_DIR, exist_ok=True)
log_file = os.path.join(settings.LOG_DIR, settings.LOG_FILE_NAME)

LOGGING_CONFIG = {'version': 1,
                  'disable_existing_loggers': False,
                  'formatters': {DEFAULT_FORMATTER: {'format': DEFAULT_FORMAT},
                                 DETAILED_FORMATTER: {'format': DETAILED_FORMAT}},

                  'handlers': {'console': {'class': 'logging.StreamHandler',
                                           'formatter': DEFAULT_FORMATTER},
                               'file': {'class': 'logging.handlers.RotatingFileHandler',
                                        'filename': log_file,
                                        'formatter': DETAILED_FORMATTER,
                                        'maxBytes': settings.MAX_LOG_SIZE,
                                        'backupCount': settings.LOG_BACKUP_COUNT,
                                        'encoding': 'utf-8'}},

                  'root': {'level': settings.LOG_LEVEL,
                           'handlers': LOG_HANDLERS},
                  'loggers': {'uvicorn.error': UVICORN_LOGGER_CONFIG,
                              'uvicorn.access': UVICORN_LOGGER_CONFIG}}

dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)
