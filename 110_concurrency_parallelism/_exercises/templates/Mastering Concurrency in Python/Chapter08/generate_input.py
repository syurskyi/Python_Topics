______ cv2

n _ 20

im _ cv2.imread('input/ship.jpg')
h, w, a _ im.shape
h_unit _ h // n; w_unit _ w // n

___ i __ ra..(n):
    start_x _ h_unit * i
    ___ j __ ra..(n):
        #print(i, j)
        start_y _ w_unit * j
        cv2.imwrite(
            'input/large_input/ship_%i_%i.jpg' % (i, j),
            im[start_x : start_x + h_unit, start_y : start_y + w_unit, :]
        )

print('Done.')
