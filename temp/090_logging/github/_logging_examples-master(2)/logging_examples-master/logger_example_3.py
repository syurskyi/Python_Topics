"""Demonstrate basic logging functionality with multiple modules."""

______ argparse
______ ?
______ sys

from ex3_sub_module ______ foo


def simple_parser():
    
    # principal logger
    logger _ ?.gL..(__name__)
    logger.sL..(?.I..)
    
    # set a file handler to write output to file
    fh _ ?.FH..("ex3_log.log.log")
    
    # specify a format for the log output
    formatter _ ?.F..('%(asctime)s - %(name)s - %(l..)s - %(m..)s')
    fh.sF..(formatter)
    
    # assign the formatted file handler to the logger
    logger.aH..(fh)
    
    logger.info("Command Line inputs: " + ' '.join(sys.argv[1:]))
    
    parser _ argparse.ArgumentParser()
    
    parser.add_argument('A', type_int)
    parser.add_argument('B', type_int)
    parser.add_argument('C', type_int)
    
    args _ parser.parse_args()
    
    return args.A, args.B, args.C


if __name__ == '__main__':
    args _ simple_parser()
    print(foo(*args))
    