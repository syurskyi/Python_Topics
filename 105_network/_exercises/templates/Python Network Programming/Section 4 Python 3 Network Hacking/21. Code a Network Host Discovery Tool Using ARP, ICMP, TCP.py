______ m.., ___, netaddr, a_p_, l..
____ scapy.all ______ *
____ d_t_ ______ d_t_

?.getLogger("scapy.runetime").sL..(?.E..)
conf.verb _ 0


c_ const:
    ARP _ 0
    PING _ 1
    TCP _ 2


___ arpScan(subnet
    ans, unans _ srp(Ether(dst_"ff:ff:ff:ff:ff:ff") / ARP(pdst_subnet), timeout_2)
    ___ snd, rcv __ ans:
        print(rcv.sprintf(r"[ARP] Online: %ARP.psrc% - %Ether.src%"))


___ ping(ip
    reply _ sr1(IP(dst_st.(ip)) / ICMP, timeout_3)
    __ reply is not None:
        print("[PING] Online: " + st.(ip))


___ tcp(ip
    port _ 53
    srcp _ RandShort
    pkt _ sr1(IP(dst_st.(ip)) / TCP(sport_srcp, dport_port, flags_"S"), timeout_5)
    __ pkt is not None:
        flag _ pkt.getlayer(TCP).flags
        __ flag __ 0x12:  # syn,ack
            print("[TCP] Online:" + st.(ip) + " - replied with syn,ack")
            s..(IP(dst_st.(ip)) / TCP(sport_srcp, dport_port, flags_"R"))
        ____ flag __ 0x14:  # RST
            print("[TCP] Online: " + st.(ip) + " - replied with rst,ack")


___ scan(subnet, typ
    jobs _   # list
    ___ ip __ subnet:
        __ typ __ const.PING:
            p _ ?.Process(t.._ping, args_(ip,))
            jobs.ap..(p)
            p.start
        ____
            p _ ?.Process(t.._tcp, args_(ip,))
            jobs.ap..(p)
            p.start

    ___ j __ jobs:
        j.j..


___ main(args
    subnet _ netaddr.IPNetwork(args.subnet)
    start _ d_t_.now
    print("==================================================")
    print("Scanning " + st.(subnet[0]) + " to " + st.(subnet[-1]))
    print("Started @ " + st.(start))
    print("==================================================")

    __ args.scantype __ const.ARP:
        arpScan(args.subnet)
    ____ args.scantype __ const.PING:
        scan(subnet, const.PING)
    ____ args.scantype __ const.TCP:
        scan(subnet, const.TCP)
    ____
        arpScan(args.subnet)
        scan(subnet, const.PING)
        scan(subnet, const.TCP)

    stop _ d_t_.now
    print("==================================================")
    print("Scan Duration: " + st.(stop - start))
    print("Completed @ " + st.(stop))
    print("==================================================")


__ _______ __ _______
    parser _ a_p_.A_P..
    parser.a_a..("subnet", action_"store", help_"Subnet to scan for hosts", type_st.)
    parser.a_a..("scantype", action_"store", nargs_"?", default_3,
                        help_"Type of scan: [0 = Arp, 1 = Ping, 2 = TCP, 3 = ALL]", type_int)

    __ le.(___.argv[1:]) __ 0:
        parser.print_help
        parser.e..

    args _ parser.parse_args
    main(args)