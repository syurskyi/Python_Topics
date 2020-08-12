______ argparse
______ ?

?.basicConfig(level_?.D..)


def simple_parser():
    
    parser _ argparse.ArgumentParser()
    
    parser.add_argument('A', type_int)
    parser.add_argument('B', type_int)
    parser.add_argument('C', type_int)
    
    args _ parser.parse_args()
    
    return args.A, args.B, args.C


def foo(A, B, C):
    """Demonstrate basic logging functionality with command line output."""
    
    ?.debug(f'args: ({A}, {B}, {C})')
    
    result _ (A + B) * C
    ?.debug(f'result: {result}')
    
    return result
    
    
if __name__ == '__main__':
    args _ simple_parser()
    print(foo(*args))
    