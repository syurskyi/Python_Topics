____ scapy.all ______ *
______ ___, a_p_, m.., l..
____ d_t_ ______ d_t_

?.getLogger("scapy.runtime").sL..(?.E..)
conf.verb _ 0


___ scanPort(ip, port
    srcp _ RandShort
    pkt _ sr1(IP(dst_ip) / TCP(sport_srcp, dport_port, flags_"S"))
    flag _ pkt.getlayer(TCP).flags
    __ flag __ 0x12:
        print("[+] Port " + st.(port) + " open")
        s..(IP(dst_ip) / TCP(sport_srcp, dport_port, flags_"R"))


___ main(args
    start _ d_t_.now
    args.throttle _ fl..(args.throttle)
    print("============================================================")
    print("Stealh Port Scanning " + args.IP + " for ports " + st.(args.sport)
          + " - " + st.(args.eport))
    print("Started @ " + st.(start))
    print("============================================================")
    ___ port __ ra.. in.(args.sport), in.(args.eport + 1)
        p _ ?.Process(t.._scanPort, args_(args.IP, port))
        p.start
        t__.s..(args.throttle)
    t__.s..(3)
    stop _ d_t_.now
    print("============================================================")
    print("Scan Duration: " + st.(stop - start))
    print("Completed @ " + st.(stop))
    print("============================================================")


__ __name__ __ "__main__":
    parser _ a_p_.A_P..
    parser.a_a..("IP", action_"store", help_"IP to port scan", type_st.)
    parser.a_a..("sport", action_"store", nargs_'?', default_1,
                        const_1, help_"Start Port Range", type_int)
    parser.a_a..("eport", action_"store", nargs_'?', default_1023,
                        const_1023, help_"End Port Range", type_int)
    parser.a_a..("-t", "--throttle", action_"store",
                        help_"throttle connection attempts", nargs_'?', default_0.25, const_0.25)

    __ le.(___.argv[1:]) __ 0:
        parser.parse_args
        parser.e..

    args _ parser.parse_args
    main(args)