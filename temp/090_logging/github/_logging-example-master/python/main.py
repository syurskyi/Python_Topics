______ ?
______ config
______ someothermodule

logger _ ?.gL..(__name__)

logger.debug("program started")
logger.info("Security is one of your major goals in life.")
logger.warn("Some of your aspirations tend to be pretty unrealistic.")

try:
    logger.debug("attempting to do something tricksy")
    someothermodule.foo()
except:
    logger.exception("caught unhandled exception.")
finally:
    logger.info("program exiting, cleaning up")
