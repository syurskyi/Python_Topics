_______ p__

____ common _______ common_languages


?p__.f..()
___ programmers
    r.. d..(bob= 'JS', 'PHP', 'Python', 'Perl', 'Java' ,
                tim= 'Python', 'Haskell', 'C++', 'JS' ,
                sara= 'Perl', 'C', 'Java', 'Python', 'JS' ,
                paul= 'C++', 'JS', 'Python' )


___ test_common_languages(programmers
    e.. =  'JS', 'Python'
    a.. common_languages(programmers)
    ... s..(l..(a.. __ e..


___ test_adding_programmer_without_js(programmers
    programmers 'sue'  =  'Scala', 'Python'
    e.. =  'Python'
    a.. common_languages(programmers)
    ... l..(a..) __ e..


___ test_adding_programmer_without_js_nor_python(programmers
    programmers 'fabio'  =  'PHP'
    e..    # list
    a.. common_languages(programmers)
    ... l..(a..) __ e..


___ test_common_languages_adding_new_common_language(programmers
    programmers 'bob' .a..('C++')
    programmers 'sara' .a..('C++')
    e.. =  'C++', 'JS', 'Python'
    a.. common_languages(programmers)
    ... s..(l..(a.. __ e..