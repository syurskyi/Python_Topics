_______ __


___ fix_translation(org_text, trans_text
    """Receives original English text as well as text returned by translator.
       Parse trans_text restoring the original (English) code (wrapped inside
       code and pre tags) into it. Return the fixed translation str
    """
    fix_text = trans_text
    pattern = r'<(?P<tag>pre|code).*?>(?P<content>.*?)</(?P=tag)>'
    eng = __.finditer(pattern, org_text, __.MULTILINE | __.DOTALL)
    rus = __.finditer(pattern, trans_text, __.MULTILINE | __.DOTALL)
    ___ (e_t, r_t) __ l..(z..(eng, rus)):
        __ e_t.group('tag') __ {'code', 'pre'}:
            fix_text = fix_text.r..(r_t.group('content'), e_t.group('content'), 1)
    r.. fix_text
