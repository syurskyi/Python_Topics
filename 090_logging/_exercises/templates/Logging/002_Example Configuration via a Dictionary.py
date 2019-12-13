______ l____
from l____.config ______ dictConfig

logging_config = dict(
    version = 1,
    formatters = {
        'f': {'format':
              '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'}
        },
    handlers = {
        'h': {'class': 'logging.StreamHandler',
              'formatter': 'f',
              'level': l____.DEBUG}
        },
    root = {
        'handlers': ['h'],
        'level': l____.DEBUG,
        },
)

dictConfig(logging_config)

logger = l____.getLogger()
logger.debug('often makes a very good meal of %s', 'visiting tourists')