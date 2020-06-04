____ ?.?G.. ______ *
____ ?.?W.. ______ *

______ __

app _ ?A..([])
app.setQuitOnLastWindowClosed(F..)

# Create the icon
icon _ ?I..(__.pa__.join("images","color.png"))

clipboard _ ?A...clipboard()
dialog _ QColorDialog()


___ copy_color_hex():
    __ dialog.e..():
        color _ dialog.currentColor()
        clipboard.sT..(color.name())
  
___ copy_color_rgb():
    __ dialog.e..():
        color _ dialog.currentColor()
        clipboard.sT..("rgb(%d, %d, %d)" % (
            color.red(), color.green(), color.blue()
        ))
  
___ copy_color_hsv():
    __ dialog.e..():
        color _ dialog.currentColor()
        clipboard.sT..("hsv(%d, %d, %d)" % (
            color.hue(), color.saturation(), color.v..
        ))

# Create the tray
tray _ QSystemTrayIcon()
tray.sI..(icon)
tray.setVisible( st.

# Create the menu
menu _ ?M..()
action1 _ ?A..("Hex")
action1.t___.c__(copy_color_hex)
menu.aA..(action1)

action2 _ ?A..("RGB")
action2.t___.c__(copy_color_rgb)
menu.aA..(action2)


action3 _ ?A..("HSV")
action3.t___.c__(copy_color_hsv)
menu.aA..(action3)

# Add the menu to the tray
tray.setContextMenu(menu)


app.e..()