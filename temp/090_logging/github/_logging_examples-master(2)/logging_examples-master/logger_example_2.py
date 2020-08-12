______ argparse
______ ?
______ sys

?.bC..(filename_'ex2_log.log', level_?.D..)


___ simple_parser():
    ?.i..("Command Line inputs: " + ' '.j..(sys.argv[1:]))
    
    parser _ argparse.ArgumentParser()
    
    parser.add_argument('A', type_int)
    parser.add_argument('B', type_int)
    parser.add_argument('C', type_int)
    
    args _ parser.parse_args()
    
    r_ args.A, args.B, args.C


___ foo(A, B, C):
    """Demonstrate basic logging functionality with file output."""
    
    ?.i..(f'args: ({A}, {B}, {C})')
    
    result _ (A + B) * C
    ?.i..(f'result: {result}')
    
    r_ result
    
    
__  -n __ '__main__':
    args _ simple_parser()
    print(foo(*args))
    