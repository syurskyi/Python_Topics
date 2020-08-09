#! /urs/bin/env python3

______ requests
from bs4 ______ BeautifulSoup

__ __name__ __ '__main__':
    url = 'http://www.nytimes.com'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    headings = soup.find_all("h2", {"class": "story-heading"})
    i = 1
    for heading in headings:
        __ heading.findAll("a"
            # .strip() removes leading/trailing whitespace
            print(str(i) + " " + heading.a.text.strip() + "\n")
        ____
            print(str(i) + " " + heading.text.strip() + "\n")
        i+=1
