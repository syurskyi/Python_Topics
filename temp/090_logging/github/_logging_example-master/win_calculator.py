______ math
____ collections ______ OrderedDict
____ log_config ______ get_logger

__metaclass__ _ type

payouts _ OrderedDict([
    ((1, 2), 2.0),  # Sym1
    ((1, 3), 5.0),
    ((1, 4), 20.0),
    ((1, 5), 100.0),
    ((2, 3), 5.0),  # Sym2
    ((2, 4), 20.0),
    ((2, 5), 100.0),
    ((3, 3), 5.0),  # Sym3
    ((3, 4), 40.0),
    ((3, 5), 120.0),
    ((4, 3), 5.0),  # Sym4
    ((4, 4), 40.0),
    ((4, 5), 120.0),
    ((5, 3), 10.0), # Sym5
    ((5, 4), 50.0),
    ((5, 5), 140.0),
    ((6, 3), 10.0),  # Sym6
    ((6, 4), 50.0),
    ((6, 5), 140.0),
    ((7, 2), 10.0),  # Sym7
    ((7, 3), 40.0),
    ((7, 4), 100.0),
    ((7, 5), 150.0),
    ((8, 2), 10.0),  # Sym8
    ((8, 3), 40.0),
    ((8, 4), 100.0),
    ((8, 5), 150.0),
    ((9, 2), 20.0),  # Sym9
    ((9, 3), 80.0),
    ((9, 4), 150.0),
    ((9, 5), 200.0),
    ((10, 2), 20.0),  # Sym10
    ((10, 3), 80.0),
    ((10, 4), 150.0),
    ((10, 5), 200.0),
    ((11, 2), 50.0),  # Sym11
    ((11, 3), 150.0),
    ((11, 4), 200.0),
    ((11, 5), 250.0)
])


c_ Shape:
    ___  - (self,side):
        side _ side

    ___ process_request(self,caller):
        print(getattr(self,caller))
        r_ getattr(self, caller,"Invalid Caller")(caller)
       

    ___ area(self,caller):
        print("Parent")
        r_ caller

    ___ parameter(self,caller):
        print("Parent")
        r_ caller

    

c_ Square(Shape):

    ___  - (self,side):
        side _ side
        super(Square, self). - (side)
    
    ___ area(self,caller):
        r_ side*side
    
    ___ parameter(self,caller):
        r_ 4*side

#caller area/parameter


#Result format : winning[{
#                           'symbol': 1,
#                           'offset': [[0,1],[1,0]],  
#                        }]


___ calculate_winning(symbol_grid, multiplier_1, wild_multiplier_{}):
    #symbol_list = [1,2,3,4,5,6,7,8,9,10,11]
    symbol_list _ set(symbol_grid[0])
    win _ []
    for symbol __ symbol_list:
        sym_data _ {'symbol': symbol, 'offset': []}
        for col __ range(0,len(symbol_grid)):
            col_offset _ []
            sym_found _ False
            for row __ range(len(symbol_grid[col])):
                __ symbol_grid[col][row] __ symbol:
                    col_offset.append([col,row])
                    sym_found _ True

            __ row __ len(symbol_grid[col])-1:
                __ len(col_offset) > 0:
                    sym_data['offset'].append(col_offset)
            
            __ no. sym_found:
                __ len(col_offset) > 0:
                    sym_data['offset'].append(col_offset)
                break  
            
        __ len(sym_data['offset']) > 1 :
            win.append(sym_data)
    r_ win_amount(win)

___ win_amount(wins):
    global payouts
    amount _ 0
    for win __ wins:
        symbol _ win['symbol']
        length _ len(win['offset'])
        ways _ 1
        for offset __ win['offset']:
            ways *_ len(offset)
        amount +_ payouts[(symbol,length)]*ways
    r_ amount


__  -n__'__main__':
    logger _ get_logger("win_calculator")
    logger.d..("a d.. m..")
    logger.e..("a d.. m..")
    logger.i..("a d.. m..")
    logger.critical("a d.. m..")

    '''caller = 'parameter'
    square = Square(10)
    print(caller ," : ",square.process_request(caller))
    caller = 'area'
    print(caller ," : ",square.process_request(caller))
    #print(__metaclass__)'''
    #symbol_grid = [[2, 1, 11, 5], [7, 6, 7, 10], [2, 4, 3, 1], [11, 7, 8, 9], [3, 1, 5, 6]]
    #symbol_grid = [[3, 9, 8, 11], [10, 11, 8, 7], [3, 1, 5, 2], [8, 9, 10, 11], [2, 4, 3, 1]]
    
    symbol_grid _ [[3, 11, 8, 11], [10, 11, 8, 11], [3, 1, 5, 11], [8, 9, 10, 11], [2, 4, 3, 11]]

    print(calculate_winning(symbol_grid))

    '''for win in wins:
        print(win['symbol'])
        for offset  in win['offset']:
            print(offset)'''



