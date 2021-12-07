_______ _______
_______ d___
_______ r__
_______ t___
____ q__ _______ Empty

_______ r..
____ lxml _______ html


c_ YahooFinancePriceScheduler(_______.T...
    ___  -  input_queue, output_queue, $$
        s__(YahooFinancePriceScheduler,   - (**kwargs)
        _input_queue = input_queue
        temp_queue = o...
        __ type(temp_queue) != list:
            temp_queue = [temp_queue]
        _output_queues = temp_queue
        s..

    ___ run
        w.... T..:
            ___
                val = _input_queue.g..timeout=10)
            ______ Empty:
                print('Yahoo scheduler queue is empty, stopping')
                ______
            __ val == 'DONE':
                ______

            yahooFinacePriceWorker = YahooFinacePriceWorker(symbol=val)
            price = yahooFinacePriceWorker.get_price()
            ___ output_queue __ _output_queues:
                output_values = (val, price, d___.d___.utcnow())
                o....p..(output_values)
            t___.s..(r__.r__())


c_ YahooFinacePriceWorkerg___
    ___  -  symbol
        _symbol = symbol
        base_url = 'https://finance.yahoo.com/quote/'
        _url = f'{base_url}{_symbol}'

    ___ get_price
        r = r...g.._url)
        __ r.status_code != 200:
            r_
        page_contents = html.fromstring(r.text)
        raw_price = page_contents.xpath('//*[@id="quote-header-info"]/div[3]/div[1]/div/span[1]')[0].text
        price = float(raw_price.replace(',', ''))
        r_ price
