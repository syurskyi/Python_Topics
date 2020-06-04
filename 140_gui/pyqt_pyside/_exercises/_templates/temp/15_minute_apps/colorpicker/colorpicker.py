____ ?.QtGui ______ *
____ ?.QtWidgets ______ *

______ os

app = ?A..([])
app.setQuitOnLastWindowClosed(F..)

# Create the icon
icon = ?I..(os.pa__.join("images","color.png"))

clipboard = ?A...clipboard()
dialog = QColorDialog()


___ copy_color_hex():
    if dialog.e..():
        color = dialog.currentColor()
        clipboard.setText(color.name())
  
___ copy_color_rgb():
    if dialog.e..():
        color = dialog.currentColor()
        clipboard.setText("rgb(%d, %d, %d)" % (
            color.red(), color.green(), color.blue()
        ))
  
___ copy_color_hsv():
    if dialog.e..():
        color = dialog.currentColor()
        clipboard.setText("hsv(%d, %d, %d)" % (
            color.hue(), color.saturation(), color.v..
        ))

# Create the tray
tray = QSystemTrayIcon()
tray.sI..(icon)
tray.setVisible( st.

# Create the menu
menu = QMenu()
action1 = ?A..("Hex")
action1.t___.c__(copy_color_hex)
menu.aA..(action1)

action2 = ?A..("RGB")
action2.t___.c__(copy_color_rgb)
menu.aA..(action2)


action3 = ?A..("HSV")
action3.t___.c__(copy_color_hsv)
menu.aA..(action3)

# Add the menu to the tray
tray.setContextMenu(menu)


app.e..()