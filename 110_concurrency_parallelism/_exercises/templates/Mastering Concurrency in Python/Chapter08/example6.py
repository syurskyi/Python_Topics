____ m.. ______ Pool
______ ?2

______ ___
____ functools ______ partial
____ t_i_ ______ d_t_ as timer


THRESH_METHOD _ ?2.ADAPTIVE_THRESH_GAUSSIAN_C
INPUT_PATH _ 'input/large_input/'
OUTPUT_PATH _ 'output/large_output/'

n _ 20
names _ ['ship_%i_%i.jpg' % (i, j) ___ i __ ra..(n) ___ j __ ra..(n)]


___ process_threshold(name, thresh_method):
    im _ ?2.?r..(INPUT_PATH + name)
    gray_im _ ?2.cvtColor(im, ?2.C_B..
    thresh_im _ ?2.aT..(gray_im, 255, thresh_method, ?2.THRESH_BINARY, 11, 2)

    ?2.?w..(OUTPUT_PATH + name, thresh_im)


__ _______ __ _______

    ___ n_processes __ ra..(1, 7):
        start _ timer()

        w__ Pool(n_processes) as p:
            p.m..(partial(process_threshold, thresh_method_THRESH_METHOD), names)

        print('Took %.4f seconds with %i process(es).' % (timer() - start, n_processes))
        
    print('Done.')
