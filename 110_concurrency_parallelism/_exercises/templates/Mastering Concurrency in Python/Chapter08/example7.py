______ cv2

face_cascade _ cv2.CascadeClassifier('input/haarcascade_frontalface_default.xml')

___ filename __ ['obama1.jpeg', 'obama2.jpg']:
    im _ cv2.imread('input/' + filename)
    gray_im _ cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces _ face_cascade.detectMultiScale(im)

    ___ (x, y, w, h) __ faces:
        cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('%i face(s) found' % le.(faces), im)
    cv2.waitKey(0)

    #cv2.imwrite('output/' + filename, im)

print('Done.')
