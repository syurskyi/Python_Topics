_____ ___, time
_____ socket
____ ? _____ ?G..
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
        ui _ ?
        ?.sU..
        tE__Messages_?.tE__Messages
        ?.pushButtonSend.c___.c..(dispMessage)
        s..

    ___ dispMessage 
        text_?.lineEditMessage.t..()
        global conn
        conn.send(t...encode("utf-8"))
        ?.tE__Messages.ap..("Server: "+?.lineEditMessage.t..())
        ?.lineEditMessage.sT..("")

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
        w__ T..:
            global conn
            (conn, (ip,port)) _ tcpServer.accept()
            newthread _ ClientThread(ip,port,window)
            newthread.start() 
            threads.ap..(newthread)
           
        ___ t in threads:
            t.join() 
 
 
c_ ClientThread(Thread 
  
    ___  -  ,ip,port,window 
        Thread. -  
        window_window
        ip _ ip
        port _ port
        
  
    ___ run  
        w__ T.. :
            global conn
            data _ conn.recv(1024)
            window.tE__Messages.ap..("Client: "+data.decode("utf-8"))
 
__ _ ____ __ _____
    app _ ?A..
    window _ Window()
    serverThread_ServerThread(window)
    serverThread.start()
    window.exec()
    ___.e.. ?.e
