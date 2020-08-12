"""Demonstrate basic logging functionality with multiple modules."""

import argparse
import logging
import sys

from ex3_sub_module import foo


def simple_parser():
    
    # principal logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    
    # set a file handler to write output to file
    fh = logging.FileHandler("ex3_log.log.log")
    
    # specify a format for the log output
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    
    # assign the formatted file handler to the logger
    logger.addHandler(fh)
    
    logger.info("Command Line inputs: " + ' '.join(sys.argv[1:]))
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument('A', type=int)
    parser.add_argument('B', type=int)
    parser.add_argument('C', type=int)
    
    args = parser.parse_args()
    
    return args.A, args.B, args.C


if __name__ == '__main__':
    args = simple_parser()
    print(foo(*args))
    