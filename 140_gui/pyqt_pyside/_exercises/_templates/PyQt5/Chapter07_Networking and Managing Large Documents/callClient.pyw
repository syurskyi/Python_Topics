_____ ___

____ ?.?W.. _____ ?A.., ?D..

_____ socket
____ threading _____ Thread
____ socketserver _____ ThreadingMixIn

____ demoClient _____ *

tcpClientA_None

c_ Window(?D..
    ___  -
        s__. -
        ui _ ?
        ?.sU..
        tE__Messages_?.tE__Messages
        ?.pushButtonSend.c___.c..(dispMessage)
        s..


    ___ dispMessage
        text_?.lineEditMessage.t..
        ?.tE__Messages.ap..("Client: "+?.lineEditMessage.t..())
        tcpClientA.send(t...encode())
        ?.lineEditMessage.sT..("")

c_ ClientThread(Thread
    ___  -  ,window
        Thread. -  
        window_window
  
    ___ run
       host _ socket.gethostname
       port _ 80
       BUFFER_SIZE _ 1024
       global tcpClientA
       tcpClientA _ socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       tcpClientA.c..((host, port))
        
       w__ T..:
           data _ tcpClientA.recv(BUFFER_SIZE)
           window.tE__Messages.ap..("Server: "+data.decode("utf-8"))
       tcpClientA.c..
            
        
__ _ ____ __ _____
    app _ ?A..
    window _ Window
    clientThread_ClientThread(window)
    clientThread.start
    window.exec
    ___.e.. ?.e
