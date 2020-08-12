import argparse
import logging

logging.basicConfig(level=logging.DEBUG)


def simple_parser():
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument('A', type=int)
    parser.add_argument('B', type=int)
    parser.add_argument('C', type=int)
    
    args = parser.parse_args()
    
    return args.A, args.B, args.C


def foo(A, B, C):
    """Demonstrate basic logging functionality with command line output."""
    
    logging.debug(f'args: ({A}, {B}, {C})')
    
    result = (A + B) * C
    logging.debug(f'result: {result}')
    
    return result
    
    
if __name__ == '__main__':
    args = simple_parser()
    print(foo(*args))
    