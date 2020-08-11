import logging
import argparse
from ez_log import parse_log_args, conf_logging


parser = parse_log_args(argparse.ArgumentParser())
args = parser.parse_args()
logger = conf_logging(logging.getLogger(__name__),
                      args.loglevel, args.no_stdout, args.logfile)

logger.debug("What")
logger.info("okay")
