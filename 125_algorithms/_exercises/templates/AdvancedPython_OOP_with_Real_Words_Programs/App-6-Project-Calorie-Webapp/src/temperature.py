____ selectorlib _____ Extractor
_____ requests

c_ Temperature:

    """A scraper that uses an yml file to read the xpath of a value it needs to extract
    from the timeanddate.com/weather/ url"""

    headers  {
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }
    base_url  'https://www.timeanddate.com/weather/'
    yml_path  'temperature.yaml'

    ___  -    country, city):
        country  country.r..(" ", "-")
        city  city.r..(" ", "-")

    ___ _build_url _
        """Builds the url string adding country and city"""
        url  base_url + country + "/" + city
        r_ url

    ___ _scrape _
        """Extracts a value as instructed by the yml file and returns a dictionary"""

        url  _build_url()
        extractor  Extractor.from_yaml_file(yml_path)
        r  requests.get(url, headersheaders)
        full_content  r.text
        raw_content  extractor.extract(full_content)
        r_ raw_content

    ___ get _
        """Cleans the output of _scrape"""

        scraped_content  _scrape()
        r_ f__(scraped_content['temp'].r..("°C", "").strip())

__ _______ __ _______
    temperature  Temperature(country"usa", city"san francisco")
    print(temperature.get())

