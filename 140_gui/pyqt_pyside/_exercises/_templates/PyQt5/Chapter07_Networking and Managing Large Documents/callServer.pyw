_____ ___, time
_____ s..
____ ? _____ ?G..
____ ? _____ ?C..
____ ?.?W.. _____ ?A.., ?D..
____ ?.?C.. _____ QCoreApplication
____ th.. _____ T..
____ s_s_ _____ TMI..
____ demoServer _____ *

conn_None

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
        g.. conn
        conn.send(t...e..("utf-8"))
        ?.tE__Messages.ap..("Server: "+?.lineEditMessage.t..())
        ?.lineEditMessage.sT..("")

c_ ServerThread(T..
    ___  -  ,window 
        T... -
        window_window
   
    ___ run  
        TCP_IP _ '0.0.0.0'
        TCP_PORT _ 80
        BUFFER_SIZE _ 1024
        tcpServer _ ?.?(?.A_N.., ?.SOCK_STREAM)
        tcpServer.setsockopt(?.SOL_SOCKET, ?.SO_REUSEADDR, 1)
        tcpServer.bind((TCP_IP, TCP_PORT)) 
        threads _ []
         
        tcpServer.listen(4) 
        w__ T..:
            g.. conn
            (conn, (ip,port)) _ tcpServer.accept
            newthread _ ClientThread(ip,port,window)
            newthread.s..
            threads.ap..(newthread)
           
        ___ t in threads:
            t.join 
 
 
c_ ClientThread(T..
  
    ___  -  ,ip,port,window 
        T... -
        window_window
        ip _ ip
        port _ port
        
  
    ___ run  
        w__ T.. :
            g.. conn
            data _ conn.recv(1024)
            window.tE__Messages.ap..("Client: "+data.d..("utf-8"))
 
__ _ ____ __ _____
    app _ ?A..
    window _ Window
    serverThread_ServerThread(window)
    serverThread.s..
    window.exec
    ___.e.. ?.e
