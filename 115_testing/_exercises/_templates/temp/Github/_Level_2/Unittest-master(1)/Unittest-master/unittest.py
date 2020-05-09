______ u__
______ requests
 
BASE_URL _ "<removed>"
DF_SECTION _ '<removed>'
 
 
c_ SearchBySymbolTest?.?
    response _ None
    
    ___ setUp
        r _ requests.get(BASE_URL + "/api/search?symbol=f")
        print BASE_URL + "/api/search?symbol=f"
        response _ r.json()
    
    ___ test_search_by_symbol
        assertTrue(isinstance(response, dict))
        assertIn("response", response, 'Missing response')
        assertIn("result", response['response'], 'Missing result')
        assertTrue(isinstance(response['response']['result'], list), "Result is not a list")
        
        for item in response['response']['result']:
			assertIn("exchange", item, 'missing exchange')
			assertIn("name", item, 'missing name')
			assertIn("symbol", item, 'missing symbol')
			assertIn("t", item, 'missing t')
			assertEquals(u'success', response['response']['status']['message'], 'no success message')
 
c_ SearchbyTermTest?.?
    response _ None
    
    ___ setUp
        r _ requests.get(BASE_URL + "/api/search?term=fe")
        print BASE_URL + "/api/search?term=fe"
        response _ r.json()
    
    ___ test_search_by_term
        assertTrue(isinstance(response, dict))
        assertIn("response", response, 'Missing response')
        assertIn("result", response['response'], 'Missing result')
        assertTrue(isinstance(response['response']['result'], list), "Result is not a list")
        
        for item in response['response']['result']:
			assertIn("exchange", item, 'missing exchange')
			assertIn("name", item, 'missing name')
			assertIn("symbol", item, 'missing symbol')
			assertIn("t", item, 'missing t')
			assertEquals(u'success', response['response']['status']['message'], 'no success message')
			
c_ SearchbyTitleTest?.?
    response _ None
    
    ___ setUp
        r _ requests.get(BASE_URL + "/api/search?title=fa")
        print BASE_URL + "/api/search?title=fa"
        response _ r.json()
    
    ___ test_search_by_title
        assertTrue(isinstance(response, dict))
        assertIn("response", response, 'Missing response')
        assertIn("result", response['response'], 'Missing result')
        assertTrue(isinstance(response['response']['result'], list), "Result is not a list")
        
        for item in response['response']['result']:
			assertIn("exchange", item, 'missing exchange')
			assertIn("name", item, 'missing name')
			assertIn("symbol", item, 'missing symbol')
			assertIn("t", item, 'missing t')
			assertEquals(u'success', response['response']['status']['message'], 'no success message')
			
c_ GetTagArticlesTest?.?
    response _ None
    
    ___ setUp
        r _ requests.get(BASE_URL + "/api/get_tag_articles?tags=Google,Facebook")
        print BASE_URL + "/api/get_tag_articles?tags=Google,Facebook"
        response _ r.json()
    
    ___ test_get_tag_articles
        assertTrue(isinstance(response, dict))
        assertIn("response", response, 'Missing response')
        assertIn("result", response['response'], 'Missing result')
        assertTrue(isinstance(response['response']['result'], list), "Result is not a list")
        
        for articles in response['response']['result']:
            for item in articles['articles']:
                assertIn("checksum", item, 'checksum')
                assertIn("created", item, 'missing created')
                assertIn("html", item, 'missing html')
                assertIn("id", item, 'missing id')
                assertIn("media", item, 'missing media')
                assertIn("source", item, 'missing source')
                assertIn("summary", item, 'missing summary')
                assertIn("tags", item, 'missing tags')
                assertIn("title", item, 'missing title')
                assertIn("url", item, 'missing url')
                
c_ MarketMoversTest?.?
    response _ None
    
    ___ setUp
        r _ requests.get(BASE_URL + "/api/market_movers/NYS?callback=")
        print BASE_URL + "/api/market_movers/NYS?callback="
        response _ r.json()
    
    ___ test_get_market_movers
        assertTrue(isinstance(response, dict))
        assertIn("response", response, 'Missing response')
        assertIn("result", response['response'], 'Missing result')
        assertTrue(isinstance(response['response']['result'], list), "Result is not a list")
        
        for item in response['response']['result']:
			assertIn("c", item, 'missin c')
			assertIn("in", item, 'missing in')
			assertIn("lu", item, 'missing lu')
			assertIn("p", item, 'missing p')
			assertIn("s", item, 'missing s')
			assertIn("v", item, 'missing v')
			assertIn("x", item, 'missing x')
			assertIn("xcntr", item, 'missing xcntr')
			assertIn("xcntrc", item, 'missing xcntrc')
			assertEquals(u'success', response['response']['status']['message'], 'no success message')
			
c_ GetChartDataTest?.?
    response _ None
    
    ___ setUp
        r _ requests.get(BASE_URL + "/api/get_chart_data?symbol=<removed>&exchange=nys")
        print BASE_URL + "/api/get_chart_data?symbol=<removed>&exchange=nys"
        response _ r.json()
    
    ___ test_get_chart_data
        assertTrue(isinstance(response, dict))
        assertIn("response", response, 'Missing response')
        assertIn("result", response['response'], 'Missing result')
        assertTrue(isinstance(response['response']['result'], dict), "Result is not a list")
        assertEquals(u'success', response['response']['status']['message'], 'no success message')
        for item in response['response']['result']['5yr']:
            assertIn("label", item, 'missin label')
            assertIn("time", item, 'missing time')
            assertIn("volume", item, 'missing volume')
            assertIn("x", item, 'missing x')
            assertIn("y", item, 'missing y')
            
        for item in response['response']['result']['today']:
            assertIn("label", item, 'missin label')
            assertIn("time", item, 'missing time')
            assertIn("volume", item, 'missing volume')
            assertIn("x", item, 'missing x')
            assertIn("y", item, 'missing y')
            
        for item in response['response']['result']['1yr']:
            assertIn("label", item, 'missin label')
            assertIn("time", item, 'missing time')
            assertIn("volume", item, 'missing volume')
            assertIn("x", item, 'missing x')
            assertIn("y", item, 'missing y')
            
if __name__ == "__main__":
    #______ sys;sys.argv = ['', 'Test.testName']
    u__.main()
			
			
			
			
			