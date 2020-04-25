______ __, a_p_, so.., so..server, bin__cii

c_ tcpServer(socketserver.B__eR..Handler
    ___ handle(self
        data _ self.request.r..(512).strip
        __ data.startswith(b"send:"
            fle _ data.sp..(b":")[1]
            print("Receiving File: " + fle.d..)
            w__ o..(st.(fle.d..("utf-8")), 'wb') __ f:
                w__ data:
                    data _ bytearray(self.request.r..(512).strip)
                    __ le.(data)  2 __ 0:
                        f.w..(bin__cii.unhexlify(data))
                    ____
                        f.w..(bin__cii.unhexlify(data.ap..(0)))
        print ("File Received.\n-----------------------------------")

___ startServer(args
    server _ socketserver.T_S_(("", args.port), tcpServer)
    print("[Server Started]")
    server.serve_forever

___ startClient(args
    sock _ ?.?(?.A.. ?.S..
    sock.c..((args.ip, args.port))
    pa__, fle _ __.pa__.sp..(args.file)
    print("Sending file: " + args.file)
    sock.s_a..(b"send:" + bytes(fle, "utf-8"))
    w__ o..(args.file, __) __ f:
        data _ f.r..(512)
        w__ (data
            sock.s_a..(bin__cii.hexlify(data))
            data _ f.r..(512)
    sock.c..
    print("File sent: " + args.file)


___ main(args
    __ (args.client
        startClient(args)
    ____ (args.server
        startServer(args)

__ __name__ __ "__main__":
    parser _ a_p_.A_P..
    parser.a_a..("-c", "--client", action_"store", help_"start client", type_st.,
    nargs_'?', default_False, const_T..)
    parser.a_a..("-s", "--server", action_"store", help_"start server", type_st.,
    nargs_'?', default_False, const_T..)
    parser.a_a..("-i", "--ip", action_"store", help_"remote server ip", type_st.)
    parser.a_a..("-p", "--port", action_"store", help_"remote server port", type_int)
    parser.a_a..("-f", "--file", action_"store", help_"file to send", type_st.)

    args _ parser.parse_args # Declare argumnets object to args
    __ (not args.client an. not args.server
        parser.print_help
        print ("\n\nYou must specify --client or --server")
        parser.e..
    main(args)