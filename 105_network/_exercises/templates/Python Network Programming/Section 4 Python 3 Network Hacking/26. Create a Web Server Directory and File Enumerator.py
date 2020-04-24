import requests, sys, time, multiprocessing, argparse
from datetime import datetime


def request(url):
    try:
        agent = {
            "User-Agent": ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) "
                           "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36")
        }
        rsp = requests.get(url)
        if rsp.status_code != 404:
            print("[+] Status " + str(rsp.status_code) + ": " + url)
    except Exception as err:
        print(str(err))


def scan(url, word, ext):
    turl = "http://" + url + word.rstrip()
    request(turl)
    if ext:
        request(turl + ext)


def main(args):
    start = datetime.now()
    print("==================================================")
    print("Started @ " + str(start))
    print("==================================================")
    if args.url.endswith("/") == False: args.url += "/"
    with open(args.wordlist) as fle:
        for word in fle:
            if word.startswith("#") == False:
                p = multiprocessing.Process(target=scan, args=(args.url, word, args.extension))
                p.start()
    stop = datetime.now()
    print("==================================================")
    print("Scan Duration: " + str(stop - start))
    print("Completed @ " + str(stop))
    print("==================================================")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url", action="store", help="starting url")
    parser.add_argument("wordlist", action="store", help="list of paths/files")
    parser.add_argument("-e", "--extension", action="store", help="file extension")

    if len(sys.argv[2:]) == 0:  # Show help if required arg not included
        parser.print_help()
        parser.exit()

    args = parser.parse_args()  # Declare argumnets object to args
    main(args)