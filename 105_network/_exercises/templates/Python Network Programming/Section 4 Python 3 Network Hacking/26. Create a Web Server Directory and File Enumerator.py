______ requests, ___, t__, m.., a_p_
____ d_t_ ______ d_t_


___ request(url
    ___
        agent _ {
            "User-Agent": ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) "
                           "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36")
        }
        rsp _ requests.get(url)
        __ rsp.status_code !_ 404:
            print("[+] Status " + st.(rsp.status_code) + ": " + url)
    ______ E.. __ err:
        print(st.(err))


___ scan(url, wor., ext
    turl _ "http://" + url + wor..rs..
    request(turl)
    __ ext:
        request(turl + ext)


___ main(args
    start _ d_t_.now
    print("==================================================")
    print("Started @ " + st.(start))
    print("==================================================")
    __ args.url.endswith("/") __ False: args.url +_ "/"
    w__ o..(args.wor.list) __ fle:
        ___ wor. __ fle:
            __ wor..startswith("#") __ False:
                p _ ?.Process(t.._scan, args_(args.url, wor., args.extension))
                p.start
    stop _ d_t_.now
    print("==================================================")
    print("Scan Duration: " + st.(stop - start))
    print("Completed @ " + st.(stop))
    print("==================================================")


__ __name__ __ "__main__":
    parser _ a_p_.A_P..
    parser.a_a..("url", action_"store", help_"starting url")
    parser.a_a..("wordlist", action_"store", help_"list of paths/files")
    parser.a_a..("-e", "--extension", action_"store", help_"file extension")

    __ le.(___.argv[2:]) __ 0:  # Show help if required arg not included
        parser.print_help
        parser.e..

    args _ parser.parse_args  # Declare argumnets object to args
    main(args)