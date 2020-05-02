_____ ___, time
_____ socket
____ ? _____ QtGui
____ ? _____ ?C..
____ ?.?W.. _____ ?A.., ?D..
____ ?.?C.. _____ QCoreApplication
____ threading _____ Thread 
____ socketserver _____ ThreadingMixIn 
____ demoServer _____ *

conn_None

c_ Window(?D..
    ___  -  
        s__. - ()
        ui _ Ui_Dialog()
        ui.setupUi
        textEditMessages_ui.textEditMessages
        ui.pushButtonSend.clicked.c..(dispMessage)
        s..

    ___ dispMessage 
        text_ui.lineEditMessage.text()
        global conn
        conn.send(text.encode("utf-8"))
        ui.textEditMessages.append("Server: "+ui.lineEditMessage.text())
        ui.lineEditMessage.sT..("")

c_ ServerThread(Thread
    ___  -  ,window 
        Thread. -  
        window_window
   
    ___ run  
        TCP_IP _ '0.0.0.0'
        TCP_PORT _ 80
        BUFFER_SIZE _ 1024
        tcpServer _ socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
        tcpServer.bind((TCP_IP, TCP_PORT)) 
        threads _ []
         
        tcpServer.listen(4) 
        while T..:
            global conn
            (conn, (ip,port)) _ tcpServer.accept()
            newthread _ ClientThread(ip,port,window)
            newthread.start() 
            threads.append(newthread) 
           
        for t in threads: 
            t.join() 
 
 
c_ ClientThread(Thread 
  
    ___  -  ,ip,port,window 
        Thread. -  
        window_window
        ip _ ip
        port _ port
        
  
    ___ run  
        while T.. :              
            global conn
            data _ conn.recv(1024)
            window.textEditMessages.append("Client: "+data.decode("utf-8"))
 
__ _ ____ __ _____
    app _ ?A..(___.argv)
    window _ Window()
    serverThread_ServerThread(window)
    serverThread.start()
    window.exec()
    ___.e..(app.exec_())
