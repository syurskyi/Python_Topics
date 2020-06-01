____ ?.?C.. ______ *
____ ?.?W.. ______ *
____ requests ______ Session

name _ input("Please enter your name: ")
chat_url _ "https://build-system.fman.io/chat"
server _ Session()

# GUI:
app _ ?
text_area _ ?PTE..
text_area.setFocusPolicy(__.NoFocus)
message _ QLineEdit()
layout _ QVBoxLayout()
layout.addWidget(text_area)
layout.addWidget(message)
window _ QWidget()
window.setLayout(layout)
window.s..

# Event handlers:
___ display_new_messages
    new_message _ server.get(chat_url).text
    __ new_message:
        text_area.appendPlainText(new_message)

___ send_message
    server.post(chat_url, {"name": name, "message": message.text()})
    message.clear()

# Signals:
message.returnPressed.c..(send_message)
timer _ QTimer()
timer.timeout.c..(display_new_messages)
timer.start(1000)

app.e..