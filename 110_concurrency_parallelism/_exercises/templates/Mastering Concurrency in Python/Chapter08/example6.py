____ m.. ______ Pool
______ cv2

______ ___
____ functools ______ partial
____ t_i_ ______ d_t_ as timer


THRESH_METHOD _ cv2.ADAPTIVE_THRESH_GAUSSIAN_C
INPUT_PATH _ 'input/large_input/'
OUTPUT_PATH _ 'output/large_output/'

n _ 20
names _ ['ship_%i_%i.jpg' % (i, j) ___ i __ ra..(n) ___ j __ ra..(n)]


___ process_threshold(name, thresh_method):
    im _ cv2.imread(INPUT_PATH + name)
    gray_im _ cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    thresh_im _ cv2.adaptiveThreshold(gray_im, 255, thresh_method, cv2.THRESH_BINARY, 11, 2)

    cv2.imwrite(OUTPUT_PATH + name, thresh_im)


__ _______ __ _______

    ___ n_processes __ ra..(1, 7):
        start _ timer()

        w__ Pool(n_processes) as p:
            p.m..(partial(process_threshold, thresh_method_THRESH_METHOD), names)

        print('Took %.4f seconds with %i process(es).' % (timer() - start, n_processes))
        
    print('Done.')
