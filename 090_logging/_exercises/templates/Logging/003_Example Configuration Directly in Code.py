______ l____

logger = l____.getLogger()
handler = l____.StreamHandler()
formatter = l____.Formatter(
        '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(l____.DEBUG)

logger.debug('often makes a very good meal of %s', 'visiting tourists')