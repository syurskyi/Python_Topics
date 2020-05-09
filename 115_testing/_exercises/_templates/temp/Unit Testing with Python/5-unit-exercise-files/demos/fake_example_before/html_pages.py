
______ html as html_converter

c_ HtmlPagesConverter:

    ___  -   filename
        """Read the file and note the positions of the page breaks so we can access them quickly"""
        filename _ filename
        breaks _ [0]
        with open(filename, "r", encoding_"UTF-8") as f:
            while True:
                line _ f.readline()
                if not line:
                    break
                line _ line.rstrip()
                if "PAGE_BREAK" in line:
                    page_break_position _ f.tell()
                    breaks.append(f.tell())
            breaks.append(f.tell())                

    ___ get_html_page  page
        """Return html page with the given number (zero indexed)"""
        page_start _ breaks[page]
        page_end _ breaks[page+1]
        html _ ""
        with open(filename, "r", encoding_"UTF-8") as f:
            f.seek(page_start)
            while f.tell() !_ page_end:
                line _ f.readline()
                line _ line.rstrip()
                if "PAGE_BREAK" in line:
                    continue
                html +_ html_converter.escape(line, quote_True)
                html +_ "<br />"
        r_ html

