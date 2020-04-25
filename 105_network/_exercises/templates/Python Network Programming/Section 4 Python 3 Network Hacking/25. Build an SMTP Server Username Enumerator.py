______ so.., ___, a_p_
____ d_t_ ______ d_t_


___ scan(ip, users
    ___
        s _ ?.?(?.A.. ?.S..
        s.c..((ip, 25))
        rsp _ s.r..(1024)
        s.s..(b"HELO friend\n")
        rsp _ s.r..(1024)
        __ b"250" not __ rsp:
            print("[!] Something went wrong, exiting.")
            ___.e..(0)
        s.s..(b"MAIL FROM:nice@guy.com\n")
        rsp _ s.r..(1024)
        __ b"250" not __ rsp:
            print("[!] Something went wrong, exiting.")
            ___.e..(0)
        ___ user __ users:
            s.s..(b"RCPT TO:" + user.rs...en.. + b"\n")
            rsp _ s.r..(1024)
            __ b"250" __ rsp:
                print("[+] Valid: " + user.rs..)
        s.s..(b"QUIT\n")
        s.c..
    ______ E.. __ err:
        print(st.(err))


___ main(args
    start _ d_t_.now
    print("==================================================")
    print("Started @ " + st.(start))
    print("==================================================")
    w__ o..(args.wor.list) __ fle:
        usr _   # list
        __ args.batch !_ 0:
            ___ user __ fle:
                __ (le.(usr) + 1) !_ args.batch:
                    usr.ap..(user)
                ____
                    usr.ap..(user)
                    scan(args.ip, usr)
                    del usr[:]
            __ le.(usr) > 0:
                scan(args.ip, usr)
        ____  # No batches
            scan(args.ip, fle)
    stop _ d_t_.now
    print("==================================================")
    print("Duration: " + st.(stop - start))
    print("Completed @ " + st.(stop))
    print("==================================================")


__ __name__ __ "__main__":
    parser _ a_p_.A_P..
    parser.a_a..("ip", action_"store", help_"smtp host address")
    parser.a_a..("wordlist", action_"store", help_"wordlist of usernames")
    parser.a_a..("-b", "--batch", action_"store", nargs_'?', const_10,
                        default_0, help_"attempts per connection", type_int)

    __ le.(___.argv[2:]) __ 0:  # Show help if required arg not included
        parser.print_help
        parser.e..

    args _ parser.parse_args  # Declare argumnets object to args
    main(args)