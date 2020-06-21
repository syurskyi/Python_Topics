# Pered tem kak naznochat' ikonki, mozno sozdat'  slovar' , kyda mu polozim vse pyti i bydem potom dostovat'
# po imeni

##############################################################################################################
# WRONG
#############################################################################################################

# esli mu importiryem paket a ne modul mu ne mozem importirovat' ----- import [name of packet]
# mu dolznu ispol'zovat' "from"

# Ispolzyja modul' nize, mu polychim oshibky
# "QPixmap: Must construct a QApplication before a QPaintDevice
# Delo v tom shto QIcon ili QPixmap, kotoruj sozdajotsja vnytri ikonki, on mozet rabotat' tol'ko v srede Application
# a na moment importa etogo modulja Application y nas echjo ne sozdan. On sozdatsja tol'ko v samom nizy.
# Poetomy v module icons, mu ne mozem sozdavat' ikonki, mu mozem hranit tol'ko pyt' k nashim fajlam



from PySide2.QtGui import QIcon
import os
root = os.path.dirname(__file__)

icons = dict(
    create=QIcon(os.path.join(root, 'create.png'),
    create=os.path.join(root, 'create.png'),
    clear=os.path.join(root, 'clear.png'),
    open=os.path.join(root, 'open.png'),
    close=os.path.join(root, 'close.png'),
    save=os.path.join(root, 'save.png'),
    item1=os.path.join(root, 'item1.png'),
    item2=os.path.join(root, 'item2.png'),
    item3=os.path.join(root, 'item3.png'),
    sphere=os.path.join(root, 'sphere.png')
))

# print icons