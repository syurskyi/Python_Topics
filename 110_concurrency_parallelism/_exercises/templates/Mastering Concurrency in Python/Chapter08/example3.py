# ch8/example3.py

______ cv2

im _ cv2.imread('input/ship.jpg')
gray_im _ cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

ret, custom_thresh_im _ cv2.threshold(gray_im, 127, 255, cv2.THRESH_BINARY)
cv2.imwrite('output/custom_thresh_ship.jpg', custom_thresh_im)

print('Done.')
