______ ___, a_p_, so.., m.., su.., t__
____ d_t_ ______ d_t_


___ scan(ip, port
    ___
        s _ ?.?(?.A.. ?.S..
        s.settimeout(2.0)
        res _ s.connect_ex((ip, port))
        __ res __ 0:
            __ port __ 80:
                rsp _ "HEAD / HTTP/1.1\r\nhost: " + ip + "\r\n\r\n"
                s.s..(rsp.en..)
            banner _ s.r..(4096)
            msg _ "[+] Port " + st.(port) + " open\n"
            msg +_ "------------------------\n" + banner.strip.d..
            print(msg + "\n------------------------\n")
        s.c..
    ______ ?.timeout:
        banner _ "No Banner Message"
        __ port __ 53:
            banner _ ?.getoutput("nslookup -type=any -class=chaos version.bind " + ip)
        msg _ "[+] Port " + st.(port) + " open\n"
        msg +_ "------------------------\n" + banner.strip.d..
        print(msg + "\n------------------------\n")
        s.c..


___ main(args
    ___
        args.throttle _ fl..(args.throttle)
        start _ d_t_.now
        print("==================================================")
        print("Scanning " + args.IP + " Ports: " + st.(args.sport) + " - " + st.(args.eport))
        print("==================================================\n")
        ports _ ra.. args.sport, args.eport + 1)
        ___ port __ ports:
            p _ ?.Process(t.._scan, args_(args.IP, port,))
            p.start
            t__.s..(args.throttle)
        t__.s..(3)
        stop _ d_t_.now
        print("==================================================")
        print("Scan Duration: " + st.(stop - start))
        print("==================================================")
    ______ E.. __ err:
        print(st.(err))


__ __name__ __ "__main__":
    parser _ a_p_.A_P..
    parser.a_a..("IP", action_"store", help_"IP to scan", type_st.)
    parser.a_a..("sport", action_"store", nargs_"?", default_1, help_"Starting port range", type_int)
    parser.a_a..("eport", action_"store", nargs_"?", default_1024, help_"End port range", type_int)
    parser.a_a..("-t", "--throttle", action_"store", help_"throttle connection attempts",
                        nargs_"?", default_0.25, const_0.05)

    __ le.(___.argv[1:]) __ 0:
        parser.print_help
        parser.e..

    args _ parser.parse_args
    main(args)