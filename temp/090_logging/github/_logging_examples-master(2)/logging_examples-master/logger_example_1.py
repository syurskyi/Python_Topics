______ argparse
______ ?

?.bC..(level_?.D..)


___ simple_parser():
    
    parser _ argparse.ArgumentParser()
    
    parser.add_argument('A', type_int)
    parser.add_argument('B', type_int)
    parser.add_argument('C', type_int)
    
    args _ parser.parse_args()
    
    r_ args.A, args.B, args.C


___ foo(A, B, C):
    """Demonstrate basic logging functionality with command line output."""
    
    ?.d..(f'args: ({A}, {B}, {C})')
    
    result _ (A + B) * C
    ?.d..(f'result: {result}')
    
    r_ result
    
    
__  -n __ '__main__':
    args _ simple_parser()
    print(foo(*args))
    