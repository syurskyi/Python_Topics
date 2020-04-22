______ ?2

face_cascade _ ?2.CascadeClassifier('input/haarcascade_frontalface_default.xml')

___ filename __ ['obama1.jpeg', 'obama2.jpg']:
    im _ ?2.?r..('input/' + filename)
    gray_im _ ?2.cvtColor(im, ?2.C_B..
    faces _ face_cascade.detectMultiScale(im)

    ___ (x, y, w, h) __ faces:
        ?2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 2)

    ?2.?s..('%i face(s) found' % le.(faces), im)
    ?2.wK..(0)

    #cv2.imwrite('output/' + filename, im)

print('Done.')
