import argparse
import logging
import sys

logging.basicConfig(filename='ex2_log.log', level=logging.DEBUG)


def simple_parser():
    logging.info("Command Line inputs: " + ' '.join(sys.argv[1:]))
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument('A', type=int)
    parser.add_argument('B', type=int)
    parser.add_argument('C', type=int)
    
    args = parser.parse_args()
    
    return args.A, args.B, args.C


def foo(A, B, C):
    """Demonstrate basic logging functionality with file output."""
    
    logging.info(f'args: ({A}, {B}, {C})')
    
    result = (A + B) * C
    logging.info(f'result: {result}')
    
    return result
    
    
if __name__ == '__main__':
    args = simple_parser()
    print(foo(*args))
    