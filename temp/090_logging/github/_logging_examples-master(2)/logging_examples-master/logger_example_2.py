______ argparse
______ ?
______ sys

?.basicConfig(filename_'ex2_log.log', level_?.D..)


def simple_parser():
    ?.i..("Command Line inputs: " + ' '.join(sys.argv[1:]))
    
    parser _ argparse.ArgumentParser()
    
    parser.add_argument('A', type_int)
    parser.add_argument('B', type_int)
    parser.add_argument('C', type_int)
    
    args _ parser.parse_args()
    
    return args.A, args.B, args.C


def foo(A, B, C):
    """Demonstrate basic logging functionality with file output."""
    
    ?.i..(f'args: ({A}, {B}, {C})')
    
    result _ (A + B) * C
    ?.i..(f'result: {result}')
    
    return result
    
    
if  -n == '__main__':
    args _ simple_parser()
    print(foo(*args))
    