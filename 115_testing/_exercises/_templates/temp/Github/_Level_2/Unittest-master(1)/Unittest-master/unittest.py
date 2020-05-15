______ u__
______ requests
 
BASE_URL _ "<removed>"
DF_SECTION _ '<removed>'
 
 
c_ SearchBySymbolTest?.?
    response _ N..
    
    ___ setUp
        r _ requests.get(BASE_URL + "/api/search?symbol=f")
        print BASE_URL + "/api/search?symbol=f"
        response _ r.j__()
    
    ___ test_search_by_symbol
        aT..(isi..(response, dict))
        aI..("response", response, 'Missing response')
        aI..("result", response['response'], 'Missing result')
        aT..(isi..(response['response']['result'], li..), "Result is not a list")
        
        ___ item __ response['response']['result']:
			aI..("exchange", item, 'missing exchange')
			aI..("name", item, 'missing name')
			aI..("symbol", item, 'missing symbol')
			aI..("t", item, 'missing t')
			assertEquals(u'success', response['response']['status']['message'], 'no success message')
 
c_ SearchbyTermTest?.?
    response _ N..
    
    ___ setUp
        r _ requests.get(BASE_URL + "/api/search?term=fe")
        print BASE_URL + "/api/search?term=fe"
        response _ r.j__()
    
    ___ test_search_by_term
        aT..(isi..(response, dict))
        aI..("response", response, 'Missing response')
        aI..("result", response['response'], 'Missing result')
        aT..(isi..(response['response']['result'], li..), "Result is not a list")
        
        ___ item __ response['response']['result']:
			aI..("exchange", item, 'missing exchange')
			aI..("name", item, 'missing name')
			aI..("symbol", item, 'missing symbol')
			aI..("t", item, 'missing t')
			assertEquals(u'success', response['response']['status']['message'], 'no success message')
			
c_ SearchbyTitleTest?.?
    response _ N..
    
    ___ setUp
        r _ requests.get(BASE_URL + "/api/search?title=fa")
        print BASE_URL + "/api/search?title=fa"
        response _ r.j__()
    
    ___ test_search_by_title
        aT..(isi..(response, dict))
        aI..("response", response, 'Missing response')
        aI..("result", response['response'], 'Missing result')
        aT..(isi..(response['response']['result'], li..), "Result is not a list")
        
        ___ item __ response['response']['result']:
			aI..("exchange", item, 'missing exchange')
			aI..("name", item, 'missing name')
			aI..("symbol", item, 'missing symbol')
			aI..("t", item, 'missing t')
			assertEquals(u'success', response['response']['status']['message'], 'no success message')
			
c_ GetTagArticlesTest?.?
    response _ N..
    
    ___ setUp
        r _ requests.get(BASE_URL + "/api/get_tag_articles?tags=Google,Facebook")
        print BASE_URL + "/api/get_tag_articles?tags=Google,Facebook"
        response _ r.j__()
    
    ___ test_get_tag_articles
        aT..(isi..(response, dict))
        aI..("response", response, 'Missing response')
        aI..("result", response['response'], 'Missing result')
        aT..(isi..(response['response']['result'], li..), "Result is not a list")
        
        ___ articles __ response['response']['result']:
            ___ item __ articles['articles']:
                aI..("checksum", item, 'checksum')
                aI..("created", item, 'missing created')
                aI..("html", item, 'missing html')
                aI..("id", item, 'missing id')
                aI..("media", item, 'missing media')
                aI..("source", item, 'missing source')
                aI..("summary", item, 'missing summary')
                aI..("tags", item, 'missing tags')
                aI..("title", item, 'missing title')
                aI..("url", item, 'missing url')
                
c_ MarketMoversTest?.?
    response _ N..
    
    ___ setUp
        r _ requests.get(BASE_URL + "/api/market_movers/NYS?callback=")
        print BASE_URL + "/api/market_movers/NYS?callback="
        response _ r.j__()
    
    ___ test_get_market_movers
        aT..(isi..(response, dict))
        aI..("response", response, 'Missing response')
        aI..("result", response['response'], 'Missing result')
        aT..(isi..(response['response']['result'], li..), "Result is not a list")
        
        ___ item __ response['response']['result']:
			aI..("c", item, 'missin c')
			aI..("in", item, 'missing in')
			aI..("lu", item, 'missing lu')
			aI..("p", item, 'missing p')
			aI..("s", item, 'missing s')
			aI..("v", item, 'missing v')
			aI..("x", item, 'missing x')
			aI..("xcntr", item, 'missing xcntr')
			aI..("xcntrc", item, 'missing xcntrc')
			assertEquals(u'success', response['response']['status']['message'], 'no success message')
			
c_ GetChartDataTest?.?
    response _ N..
    
    ___ setUp
        r _ requests.get(BASE_URL + "/api/get_chart_data?symbol=<removed>&exchange=nys")
        print BASE_URL + "/api/get_chart_data?symbol=<removed>&exchange=nys"
        response _ r.j__()
    
    ___ test_get_chart_data
        aT..(isi..(response, dict))
        aI..("response", response, 'Missing response')
        aI..("result", response['response'], 'Missing result')
        aT..(isi..(response['response']['result'], dict), "Result is not a list")
        assertEquals(u'success', response['response']['status']['message'], 'no success message')
        ___ item __ response['response']['result']['5yr']:
            aI..("label", item, 'missin label')
            aI..("time", item, 'missing time')
            aI..("volume", item, 'missing volume')
            aI..("x", item, 'missing x')
            aI..("y", item, 'missing y')
            
        ___ item __ response['response']['result']['today']:
            aI..("label", item, 'missin label')
            aI..("time", item, 'missing time')
            aI..("volume", item, 'missing volume')
            aI..("x", item, 'missing x')
            aI..("y", item, 'missing y')
            
        ___ item __ response['response']['result']['1yr']:
            aI..("label", item, 'missin label')
            aI..("time", item, 'missing time')
            aI..("volume", item, 'missing volume')
            aI..("x", item, 'missing x')
            aI..("y", item, 'missing y')
            
__ _____ __ ______
    #______ sys;sys.argv = ['', 'Test.testName']
    ?.?
			
			
			
			
			