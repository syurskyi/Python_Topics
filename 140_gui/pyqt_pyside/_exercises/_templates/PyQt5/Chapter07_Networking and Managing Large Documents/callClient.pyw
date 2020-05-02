_____ ___

____ ?.?W.. _____ ?A.., ?D..

_____ socket
____ threading _____ Thread
____ socketserver _____ ThreadingMixIn

____ demoClient _____ *

tcpClientA_None

c_ Window(?D..
    ___  -
        s__. - ()
        ui _ Ui_Dialog()
        ui.sU..
        tE__Messages_ui.tE__Messages
        ui.pushButtonSend.c___.c..(dispMessage)
        s..


    ___ dispMessage
        text_ui.lineEditMessage.t..()
        ui.tE__Messages.ap..("Client: "+ui.lineEditMessage.t..())
        tcpClientA.send(t...encode())
        ui.lineEditMessage.sT..("")

c_ ClientThread(Thread
    ___  -  ,window
        Thread. -  
        window_window
  
    ___ run
       host _ socket.gethostname()
       port _ 80
       BUFFER_SIZE _ 1024
       global tcpClientA
       tcpClientA _ socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       tcpClientA.c..((host, port))
        
       while T..:
           data _ tcpClientA.recv(BUFFER_SIZE)
           window.tE__Messages.ap..("Server: "+data.decode("utf-8"))
       tcpClientA.close() 
            
        
__ _ ____ __ _____
    app _ ?A..(___.argv)
    window _ Window()
    clientThread_ClientThread(window)
    clientThread.start()
    window.exec()
    ___.e..(app.e
