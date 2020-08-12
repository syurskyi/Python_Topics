"""Demonstrate basic logging functionality with multiple modules."""

______ argparse
______ ?
______ sys

from ex3_sub_module ______ foo


___ simple_parser():
    
    # principal logger
    logger _ ?.gL..( -n)
    logger.sL..(?.I..)
    
    # set a file handler to write output to file
    fh _ ?.FH..("ex3_log.log.log")
    
    # specify a format for the log output
    formatter _ ?.F..('%(a_t_)s - %(name)s - %(l..)s - %(m..)s')
    fh.sF..(formatter)
    
    # assign the formatted file handler to the logger
    logger.aH..(fh)
    
    logger.i..("Command Line inputs: " + ' '.join(sys.argv[1:]))
    
    parser _ argparse.ArgumentParser()
    
    parser.add_argument('A', type_int)
    parser.add_argument('B', type_int)
    parser.add_argument('C', type_int)
    
    args _ parser.parse_args()
    
    r_ args.A, args.B, args.C


__  -n == '__main__':
    args _ simple_parser()
    print(foo(*args))
    