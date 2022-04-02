_______ __

c_ HtmlParser:
    """
    @param: content: content source code
    @return: a list of links
    """
    ___ parseUrls  content
        # r'': use raw string
        # [=\s]+: this block should contain `=` or blank, and at least one char here
        # ["\']: this block should contain `"` or `'`
        # [^"\'>\s]*: this block should contain any chars until `"`, `'`, `>`, or blank appears
        links = __.f..(r'href[=\s]+["\']([^"\'>\s]*)', content, __.I)
        r.. [link ___ link __ links __ link a.. n.. link.startswith('#')]
