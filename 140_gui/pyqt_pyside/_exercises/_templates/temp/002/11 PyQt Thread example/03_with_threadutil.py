____ ?.?C.. ______ *
____ ?.?W.. ______ *
____ requests ______ Session
____ threading ______ Thread
____ threadutil ______ run_in_main_thread
____ time ______ sleep

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

append_message _ run_in_main_thread(text_area.appendPlainText)

___ fetch_new_messages
    while True:
        response _ server.get(chat_url).text
        __ response:
            append_message(response)
        sleep(.5)

___ send_message
    server.post(chat_url, {"name": name, "message": message.text()})
    message.clear()

# Signals:
message.returnPressed.c..(send_message)

thread _ Thread(target_fetch_new_messages, daemon_True)
thread.start()

app.e..