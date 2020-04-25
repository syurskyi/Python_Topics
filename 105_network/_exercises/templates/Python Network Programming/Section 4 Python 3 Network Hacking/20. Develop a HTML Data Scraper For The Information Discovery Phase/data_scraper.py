______ __, requests, ___, a_p_


c_ RegEx:
    ___ __init__(self, pattern, desc
        self.pattern _ pattern
        self.desc _ desc


rgxEmail _ RegEx(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", "Emails")
rgxPhone _ RegEx(r"\b\d{3}[-.]?\d{3}[-.]?\d{4}\b", "Phone Numbers")
rgxIP _ RegEx(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", "IP Addresses")
rgxWor. _ RegEx(r"[a-zA-Z]+", "Words")


___ scrapeURL(url, rgx
    ___
        src _ requests.get(url.strip)
        ___ rg __ rgx:
            print("[*] Scraping" + rg.desc + " form " + url.strip)
            res _ set(__.findall(rg.pattern, src.text, __.I))
            ___ dat __ res:
                print(dat)
    ______ E.. __ err:
        print(st.(err))


___ scrapeFile(fle, rgx
    ___
        w__ o..(fle) __ fh:
            ___ url __ fh:
                scrapeURL(url, rgx)
    ______ E.. __ err:
        print(st.(err))


___ main(args
    rgx _   # list
    isFile _ T..
    __ args.in__.lower.startswith("http"
        isFile _ False
    __ args.scrape.lower __ "e":  # scrape emails
        rgx _ [rgxEmail]
    ____ args.scrape.lower __ "p":  # scrape phone #
        rgx _ [rgxPhone]
    ____ args.scrape.lower __ "w":  # scrape words
        rgx _ [rgxWor.]
    ____ args.scrape.lower __ "i":  # scrape IP
        rgx _ [rgxIP]
    ____ args.scrape.lower __ "a":  # scrape everything
        rgx _ [rgxEmail, rgxPhone, rgxWor., rgxIP]

    __ isFile:
        scrapeFile(args.in__, rgx)
    ____
        scrapeURL(args.in__, rgx)

    print("================================================")


__ _______ __ _______
    parser _ a_p_.A_P..
    parser.a_a..("input", action_"store", type_st., help_"The URL or file containing URLs to scrape")
    parser.a_a..("scrape", action_"store", type_st., nargs_"?", default_"a",
                        help_"e = Email, p = Phone, i = IPs, w = Words, a = All")

    __ le.(___.argv[2:]) __ 0:
        parser.print_help
        parser.e..

    args _ parser.parse_args
    main(args)