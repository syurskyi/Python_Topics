import unittest
import os
import tempfile
import io

from html_pages import HtmlPagesConverter, FileAccessWrapper

class HtmlPagesTest(unittest.TestCase):
    def test_inserts_br_tags_for_linebreaks(self):
        filename = os.path.join(tempfile.gettempdir(), "afile.txt")
        f = open(filename, "w", encoding="UTF-8")
        f.write("plain text\n")
        f.close()
        converter = HtmlPagesConverter(FileAccessWrapper(filename))
        new_text = converter.get_html_page(0)
        self.assertEqual("plain text<br />", new_text)
        
    def test_quotes_escaped(self):
        converter = HtmlPagesConverter(FakeFileWrapper("text with 'quotes'"))
        new_text = converter.get_html_page(0)
        self.assertEqual("text with &#x27;quotes&#x27;<br />", new_text)

    def test_random_access_pages(self):
        converter = HtmlPagesConverter(FakeFileWrapper("page one\nPAGE_BREAK\npage two\nPAGE_BREAK\npage three"))
        page_two = converter.get_html_page(1)
        self.assertEqual("page two<br />", page_two)
         
        
class FakeFileWrapper:
    def __init__(self, text):
        self.text = text
        
    def open(self):
        return io.StringIO(self.text)