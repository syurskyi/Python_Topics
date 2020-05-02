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



____ PySide.?G.. _____ QIcon
_____ os
root _ os.path.dirname(__file__)

icons _ dict(
    create_QIcon(os.path.join(root, 'create.png')),
    create_os.path.join(root, 'create.png'),
    clear_os.path.join(root, 'clear.png'),
    open_os.path.join(root, 'open.png'),
    close_os.path.join(root, 'close.png'),
    save_os.path.join(root, 'save.png'),
    item1_os.path.join(root, 'item1.png'),
    item2_os.path.join(root, 'item2.png'),
    item3_os.path.join(root, 'item3.png'),
    sphere_os.path.join(root, 'sphere.png')
)

# print icons