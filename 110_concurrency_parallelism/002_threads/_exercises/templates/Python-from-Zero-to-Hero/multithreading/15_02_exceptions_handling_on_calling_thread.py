_______ t___
_______ c__.f__
____ c__.f__ _______ CancelledError


___ div(divisor, limit):
    print(f'started div = {divisor}')

    result = 0
    ___ x __ r..(1, limit):
        __ x % divisor == 0:
            result += x
            print(f'divisor={divisor}, x={x}')
        t___.s(0.2)

    print('raise exception')
    raise Exception('bad things happen!')

    r_ result


__ _____ __ _____
    print('started main')

    w___ c__.f__.T...(max_workers = 2) __ executor:
        res_list = executor.m..(div, (3, 5), (15, 25))
        w.... res_list:
            try:
                cur_res = next(res_list)
            except StopIteration:
                print('stop iteration excepted')
                break
            except Exception __ ex:
                print('generalized exception')
                print(repr(ex))

    print('main ended')


# if __name__ == '__main__':
#     print('started main')
#     with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
#         future = executor.submit(div, 3, 15)
#
#         time.sleep(5)
#         print('Nothing happens until...')
#
#         try:
#             res = future.result()
#         except CancelledError as ex:
#             print(repr(ex))
#         except TimeoutError as ex:
#             print(repr(ex))
#         except Exception as ex:
#             print(repr(ex))
#
#     print('main ended')
