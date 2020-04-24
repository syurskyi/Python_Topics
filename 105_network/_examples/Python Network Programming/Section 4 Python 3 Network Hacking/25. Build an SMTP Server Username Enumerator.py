import socket, sys, argparse
from datetime import datetime


def scan(ip, users):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, 25))
        rsp = s.recv(1024)
        s.send(b"HELO friend\n")
        rsp = s.recv(1024)
        if b"250" not in rsp:
            print("[!] Something went wrong, exiting.")
            sys.exit(0)
        s.send(b"MAIL FROM:nice@guy.com\n")
        rsp = s.recv(1024)
        if b"250" not in rsp:
            print("[!] Something went wrong, exiting.")
            sys.exit(0)
        for user in users:
            s.send(b"RCPT TO:" + user.rstrip().encode() + b"\n")
            rsp = s.recv(1024)
            if b"250" in rsp:
                print("[+] Valid: " + user.rstrip())
        s.send(b"QUIT\n")
        s.close()
    except Exception as err:
        print(str(err))


def main(args):
    start = datetime.now()
    print("==================================================")
    print("Started @ " + str(start))
    print("==================================================")
    with open(args.wordlist) as fle:
        usr = []
        if args.batch != 0:
            for user in fle:
                if (len(usr) + 1) != args.batch:
                    usr.append(user)
                else:
                    usr.append(user)
                    scan(args.ip, usr)
                    del usr[:]
            if len(usr) > 0:
                scan(args.ip, usr)
        else:  # No batches
            scan(args.ip, fle)
    stop = datetime.now()
    print("==================================================")
    print("Duration: " + str(stop - start))
    print("Completed @ " + str(stop))
    print("==================================================")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("ip", action="store", help="smtp host address")
    parser.add_argument("wordlist", action="store", help="wordlist of usernames")
    parser.add_argument("-b", "--batch", action="store", nargs='?', const=10,
                        default=0, help="attempts per connection", type=int)

    if len(sys.argv[2:]) == 0:  # Show help if required arg not included
        parser.print_help()
        parser.exit()

    args = parser.parse_args()  # Declare argumnets object to args
    main(args)