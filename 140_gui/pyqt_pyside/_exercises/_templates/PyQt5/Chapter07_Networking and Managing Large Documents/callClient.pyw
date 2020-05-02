_____ ___

____ ?.?W.. _____ ?A.., ?D..

_____ socket
____ threading _____ Thread
____ socketserver _____ ThreadingMixIn

____ demoClient _____ *

tcpClientA=None

c_ Window(?D..
    ___  -
        s__. - ()
        ui = Ui_Dialog()
        ui.setupUi
        textEditMessages=ui.textEditMessages
        ui.pushButtonSend.clicked.c..(dispMessage)
        s..


    ___ dispMessage
        text=ui.lineEditMessage.text()
        ui.textEditMessages.append("Client: "+ui.lineEditMessage.text())
        tcpClientA.send(text.encode())
        ui.lineEditMessage.sT..("")

c_ ClientThread(Thread
    ___  -  ,window
        Thread. -  
        window=window
  
    ___ run
       host = socket.gethostname() 
       port = 80
       BUFFER_SIZE = 1024
       global tcpClientA
       tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
       tcpClientA.c..((host, port))
        
       while T..:
           data = tcpClientA.recv(BUFFER_SIZE)
           window.textEditMessages.append("Server: "+data.decode("utf-8"))
       tcpClientA.close() 
            
        
__ __name____"__main__":    
    app = ?A..(___.argv)
    window = Window()
    clientThread=ClientThread(window)
    clientThread.start()
    window.exec()
    ___.e..(app.exec_())
