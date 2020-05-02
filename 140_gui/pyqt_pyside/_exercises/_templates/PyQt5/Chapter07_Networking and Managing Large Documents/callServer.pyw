_____ ___, time
_____ socket
____ ? _____ QtGui
____ ? _____ ?C..
____ ?.?W.. _____ ?A.., ?D..
____ ?.?C.. _____ QCoreApplication
____ threading _____ Thread 
____ socketserver _____ ThreadingMixIn 
____ demoServer _____ *

conn=None

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
        global conn
        conn.send(text.encode("utf-8"))
        ui.textEditMessages.append("Server: "+ui.lineEditMessage.text())
        ui.lineEditMessage.sT..("")

c_ ServerThread(Thread
    ___  -  ,window 
        Thread. -  
        window=window
   
    ___ run  
        TCP_IP = '0.0.0.0'
        TCP_PORT = 80
        BUFFER_SIZE = 1024 
        tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
        tcpServer.bind((TCP_IP, TCP_PORT)) 
        threads = [] 
         
        tcpServer.listen(4) 
        while T..:
            global conn
            (conn, (ip,port)) = tcpServer.accept() 
            newthread = ClientThread(ip,port,window) 
            newthread.start() 
            threads.append(newthread) 
           
        for t in threads: 
            t.join() 
 
 
c_ ClientThread(Thread 
  
    ___  -  ,ip,port,window 
        Thread. -  
        window=window
        ip = ip 
        port = port 
        
  
    ___ run  
        while T.. :              
            global conn
            data = conn.recv(1024) 
            window.textEditMessages.append("Client: "+data.decode("utf-8"))
 
__ __name____"__main__":    
    app = ?A..(___.argv)
    window = Window()
    serverThread=ServerThread(window)
    serverThread.start()
    window.exec()
    ___.e..(app.exec_())
