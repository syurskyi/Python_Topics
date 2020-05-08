import os
root = os.path.dirname(__file__)

icons = dict(
    # create=QIcon(os.path.join(root, 'create.png')), # eto ne verno. QIcon ili QPixmap, kotoruj sozdajotsja vnytri ikonki
                                                      # mozet rabotat' tol'ko v srede QApplication. Na moment importa etogo modulja
                                                      # QApplication echjo ne sozdan. Poetomy v etom modyle mu ne mozem
                                                      # sozdavat' ikonki, mu mozem hranit' zdes' tol'ko pyti k nim
    create=os.path.join(root, 'create.png'),
    clear=os.path.join(root, 'clear.png'),
    open=os.path.join(root, 'open.png'),
    close=os.path.join(root, 'close.png'),
    save=os.path.join(root, 'save.png'),
    item1=os.path.join(root, 'item1.png'),
    item2=os.path.join(root, 'item2.png'),
    item3=os.path.join(root, 'item3.png'),
    sphere=os.path.join(root, 'sphere.png')
)

print(icons)