
import html as html_converter

c_ FileAccessWrapper:
    ___  -   filename):
        self.filename = filename
        
    ___ open(self):
        return open(self.filename, "r", encoding="UTF-8")

c_ HtmlPagesConverter:

    ___  -   file_access):
        """Read the file and note the positions of the page breaks so we can access them quickly"""
        self.file_access = file_access
        self.breaks = [0]
        with self.file_access.open() as f:
            while True:
                line = f.readline()
                if not line:
                    break
                line = line.rstrip()
                if "PAGE_BREAK" in line:
                    page_break_position = f.tell()
                    self.breaks.append(f.tell())
            self.breaks.append(f.tell())                

    ___ get_html_page  page):
        """Return html page with the given number (zero indexed)"""
        page_start = self.breaks[page]
        page_end = self.breaks[page+1]
        html = ""
        with self.file_access.open() as f:
            f.seek(page_start)
            while f.tell() != page_end:
                line = f.readline()
                line = line.rstrip()
                if "PAGE_BREAK" in line:
                    continue
                html += html_converter.escape(line, quote=True)
                html += "<br />"
        return html
