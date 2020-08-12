______ argparse
______ ?
______ sys

?.basicConfig(filename_'ex2_log.log', level_?.D..)


def simple_parser():
    ?.info("Command Line inputs: " + ' '.join(sys.argv[1:]))
    
    parser _ argparse.ArgumentParser()
    
    parser.add_argument('A', type_int)
    parser.add_argument('B', type_int)
    parser.add_argument('C', type_int)
    
    args _ parser.parse_args()
    
    return args.A, args.B, args.C


def foo(A, B, C):
    """Demonstrate basic logging functionality with file output."""
    
    ?.info(f'args: ({A}, {B}, {C})')
    
    result _ (A + B) * C
    ?.info(f'result: {result}')
    
    return result
    
    
if __name__ == '__main__':
    args _ simple_parser()
    print(foo(*args))
    