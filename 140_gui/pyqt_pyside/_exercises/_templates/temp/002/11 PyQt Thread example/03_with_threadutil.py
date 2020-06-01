____ ?.?C.. ______ *
____ ?.?W.. ______ *
____ requests ______ Session
____ th.. ______ Thread
____ threadutil ______ run_in_main_thread
____ time ______ sl..

name _ __.. ("Please enter your name: ")
chat_url _ "https://build-system.fman.io/chat"
server _ Session()

# GUI:
app _ ?
text_area _ ?PTE..
text_area.sFP..(__.NF..)
message _ ?LE..
layout _ ?VBL..
layout.aW..(text_area)
layout.aW..(message)
window _ ?W..
window.sL..(layout)
window.s..

append_message _ run_in_main_thread(text_area.aPT..)

___ fetch_new_messages
    w__ T..
        response _ server.g..(chat_url).t__
        __ response:
            append_message(response)
        sl..(.5)

___ send_message
    server.post(chat_url, {"name": name, "message": message.t__()})
    message.clear()

# Signals:
message.rP__.c..(send_message)

thread _ Thread(target_fetch_new_messages, d.._T..
thread.start()

app.e..