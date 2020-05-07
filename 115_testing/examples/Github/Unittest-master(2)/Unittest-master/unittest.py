import unittest
import requests
 
BASE_URL = "<removed>"
DF_SECTION = '<removed>'
 
 
class SearchBySymbolTest(unittest.TestCase):
    response = None
    
    def setUp(self):
        r = requests.get(BASE_URL + "/api/search?symbol=f")
        print BASE_URL + "/api/search?symbol=f"
        self.response = r.json()
    
    def test_search_by_symbol(self):
        self.assertTrue(isinstance(self.response, dict))
        self.assertIn("response", self.response, 'Missing response')
        self.assertIn("result", self.response['response'], 'Missing result')
        self.assertTrue(isinstance(self.response['response']['result'], list), "Result is not a list")
        
        for item in self.response['response']['result']:
			self.assertIn("exchange", item, 'missing exchange')
			self.assertIn("name", item, 'missing name')
			self.assertIn("symbol", item, 'missing symbol')
			self.assertIn("t", item, 'missing t')
			self.assertEquals(u'success', self.response['response']['status']['message'], 'no success message')
 
class SearchbyTermTest(unittest.TestCase):
    response = None
    
    def setUp(self):
        r = requests.get(BASE_URL + "/api/search?term=fe")
        print BASE_URL + "/api/search?term=fe"
        self.response = r.json()
    
    def test_search_by_term(self):
        self.assertTrue(isinstance(self.response, dict))
        self.assertIn("response", self.response, 'Missing response')
        self.assertIn("result", self.response['response'], 'Missing result')
        self.assertTrue(isinstance(self.response['response']['result'], list), "Result is not a list")
        
        for item in self.response['response']['result']:
			self.assertIn("exchange", item, 'missing exchange')
			self.assertIn("name", item, 'missing name')
			self.assertIn("symbol", item, 'missing symbol')
			self.assertIn("t", item, 'missing t')
			self.assertEquals(u'success', self.response['response']['status']['message'], 'no success message')
			
class SearchbyTitleTest(unittest.TestCase):
    response = None
    
    def setUp(self):
        r = requests.get(BASE_URL + "/api/search?title=fa")
        print BASE_URL + "/api/search?title=fa"
        self.response = r.json()
    
    def test_search_by_title(self):
        self.assertTrue(isinstance(self.response, dict))
        self.assertIn("response", self.response, 'Missing response')
        self.assertIn("result", self.response['response'], 'Missing result')
        self.assertTrue(isinstance(self.response['response']['result'], list), "Result is not a list")
        
        for item in self.response['response']['result']:
			self.assertIn("exchange", item, 'missing exchange')
			self.assertIn("name", item, 'missing name')
			self.assertIn("symbol", item, 'missing symbol')
			self.assertIn("t", item, 'missing t')
			self.assertEquals(u'success', self.response['response']['status']['message'], 'no success message')
			
class GetTagArticlesTest(unittest.TestCase):
    response = None
    
    def setUp(self):
        r = requests.get(BASE_URL + "/api/get_tag_articles?tags=Google,Facebook")
        print BASE_URL + "/api/get_tag_articles?tags=Google,Facebook"
        self.response = r.json()
    
    def test_get_tag_articles(self):
        self.assertTrue(isinstance(self.response, dict))
        self.assertIn("response", self.response, 'Missing response')
        self.assertIn("result", self.response['response'], 'Missing result')
        self.assertTrue(isinstance(self.response['response']['result'], list), "Result is not a list")
        
        for articles in self.response['response']['result']:
            for item in articles['articles']:
                self.assertIn("checksum", item, 'checksum')
                self.assertIn("created", item, 'missing created')
                self.assertIn("html", item, 'missing html')
                self.assertIn("id", item, 'missing id')
                self.assertIn("media", item, 'missing media')
                self.assertIn("source", item, 'missing source')
                self.assertIn("summary", item, 'missing summary')
                self.assertIn("tags", item, 'missing tags')
                self.assertIn("title", item, 'missing title')
                self.assertIn("url", item, 'missing url')
                
class MarketMoversTest(unittest.TestCase):
    response = None
    
    def setUp(self):
        r = requests.get(BASE_URL + "/api/market_movers/NYS?callback=")
        print BASE_URL + "/api/market_movers/NYS?callback="
        self.response = r.json()
    
    def test_get_market_movers(self):
        self.assertTrue(isinstance(self.response, dict))
        self.assertIn("response", self.response, 'Missing response')
        self.assertIn("result", self.response['response'], 'Missing result')
        self.assertTrue(isinstance(self.response['response']['result'], list), "Result is not a list")
        
        for item in self.response['response']['result']:
			self.assertIn("c", item, 'missin c')
			self.assertIn("in", item, 'missing in')
			self.assertIn("lu", item, 'missing lu')
			self.assertIn("p", item, 'missing p')
			self.assertIn("s", item, 'missing s')
			self.assertIn("v", item, 'missing v')
			self.assertIn("x", item, 'missing x')
			self.assertIn("xcntr", item, 'missing xcntr')
			self.assertIn("xcntrc", item, 'missing xcntrc')
			self.assertEquals(u'success', self.response['response']['status']['message'], 'no success message')
			
class GetChartDataTest(unittest.TestCase):
    response = None
    
    def setUp(self):
        r = requests.get(BASE_URL + "/api/get_chart_data?symbol=<removed>&exchange=nys")
        print BASE_URL + "/api/get_chart_data?symbol=<removed>&exchange=nys"
        self.response = r.json()
    
    def test_get_chart_data(self):
        self.assertTrue(isinstance(self.response, dict))
        self.assertIn("response", self.response, 'Missing response')
        self.assertIn("result", self.response['response'], 'Missing result')
        self.assertTrue(isinstance(self.response['response']['result'], dict), "Result is not a list")
        self.assertEquals(u'success', self.response['response']['status']['message'], 'no success message')
        for item in self.response['response']['result']['5yr']:
            self.assertIn("label", item, 'missin label')
            self.assertIn("time", item, 'missing time')
            self.assertIn("volume", item, 'missing volume')
            self.assertIn("x", item, 'missing x')
            self.assertIn("y", item, 'missing y')
            
        for item in self.response['response']['result']['today']:
            self.assertIn("label", item, 'missin label')
            self.assertIn("time", item, 'missing time')
            self.assertIn("volume", item, 'missing volume')
            self.assertIn("x", item, 'missing x')
            self.assertIn("y", item, 'missing y')
            
        for item in self.response['response']['result']['1yr']:
            self.assertIn("label", item, 'missin label')
            self.assertIn("time", item, 'missing time')
            self.assertIn("volume", item, 'missing volume')
            self.assertIn("x", item, 'missing x')
            self.assertIn("y", item, 'missing y')
            
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
			
			
			
			
			