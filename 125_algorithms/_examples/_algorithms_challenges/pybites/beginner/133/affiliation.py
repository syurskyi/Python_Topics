original_links = [
    ('https://www.amazon.com/War-Art-Through-Creative-Battles/dp/1936891026/'
     '?keywords=war+of+art'),
    ('https://amazon.com/War-Art-Through-Creative-Battles/dp/1936891026/'
     'ref=sr_1_1'),
    ('https://www.amazon.es/War-Art-Through-Creative-Battles/dp/1936891026/'
     '?qid=1537226234'),
     'https://www.amazon.co.uk/Pragmatic-Programmer-Andrew-Hunt/dp/020161622X',
    ('https://www.amazon.com.au/Python-Cookbook-3e-David-Beazley/dp/'
     '1449340377/'),
    ('https://www.amazon.com/fake-book-with-longer-asin/dp/'
     '1449340377000/'),
]


def generate_affiliation_link(url):
    #print(url)
    #prod_id = url.split('/')
    return "http://www.amazon.com/dp/{}/?tag=pyb0f-20".format(url.split('/')[5])


for link in original_links:
    #print(link)
    print(generate_affiliation_link(link))
