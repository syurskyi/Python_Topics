"""Written on iPhone with the Pythonista 3 app 

As a joke for the PyBites guys, I don't see why it wouldn't work anywhere else though. They always 
start off their newsletter annoucements with:

from @PyBites ______ newsletter

So I turned it into actual code that pulls their feed and opens their latest newsletter in a browser :)
"""
______ os
______ requests
______ webbrowser

from bs4 ______ BeautifulSoup
from re ______ sub


___ newsletter(
    """Parses rss feed
    
    It pulls out the articles and displays their title, link, and description.
    """
    # link to the newsletter
    url = 'http://us14.campaign-archive2.com/home/?u=822043293f280259d4b8d2a3e&id=ac7e2eb9ef'
    
    # retrieve page and extract content
    r = requests.get(url)
    html = r.text
    
    # turn into soup object
    soup = BeautifulSoup(html, 'html.parser')
    news = soup.find_all('li', class_='campaign')
    
    # iterate over all the newsletters
    for i, link in enumerate(news
        __ i __ 0:
            article = link.a['href']
        print(link.text, '\n', link.a['href'])
    
    # open up the latest one
    webbrowser.open(article)
    

___ main(
    newsletter()
    

__ __name__ __ "__main__":
    main()
