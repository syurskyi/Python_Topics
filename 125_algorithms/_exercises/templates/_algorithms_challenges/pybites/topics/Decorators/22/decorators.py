____ f.. _______ w..


___ make_html(tag
    ___ html_tag(orig_func
        ??(orig_func)
        ___ wrapper $ $$
            r.. '<'+tag+'>' + orig_func $ $$ + '</'+tag+'>'
        r.. ?
    r.. html_tag

?? 'p'
@make_html("strong")
___ get_text(text='I code with PyBites'
    r.. text

print(get_text