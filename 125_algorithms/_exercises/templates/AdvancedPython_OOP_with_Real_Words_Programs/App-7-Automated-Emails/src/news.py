_____ requests


c_ NewsFeed:
    """Representing multiple news titles and links as a single string
    """
    base_url  "http://newsapi.org/v2/everything?"
    api_key  "INSERT YOUR API KEY HERE"

    ___  -    interest, from_date, to_date, language'en'):
        interest  interest
        from_date  from_date
        to_date  to_date
        language  language

    ___ get _
        url  _build_url()

        articles  _get_articles(url)

        email_body  ''
        ___ article __ articles:
            email_body  email_body + article['title'] + "\n" + article['url'] + "\n\n"

        r_ email_body

    ___ _get_articles   url):
        response  requests.get(url)
        content  response.json()
        articles  content['articles']
        r_ articles

    ___ _build_url _
        url  f"{base_url}" \
              f"qInTitle={interest}&" \
              f"from={from_date}&" \
              f"to={to_date}&" \
              f"language={language}&" \
              f"apiKey={api_key}"
        r_ url


__ __name__ __ "__main__":
    news_feed  NewsFeed(interest'nasa', from_date'2020-11-12', to_date'2020-11-13', language'en')
    print(news_feed.get())
