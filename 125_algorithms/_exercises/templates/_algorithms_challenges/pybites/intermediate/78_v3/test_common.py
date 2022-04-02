_______ p__

____ common _______ common_languages


?p__.f..()
___ programmers
    r.. d..(bob= 'JS', 'PHP', 'Python', 'Perl', 'Java' ,
                tim= 'Python', 'Haskell', 'C++', 'JS' ,
                sara= 'Perl', 'C', 'Java', 'Python', 'JS' ,
                paul= 'C++', 'JS', 'Python' )


___ test_common_languages(programmers
    expected =  'JS', 'Python'
    actual = common_languages(programmers)
    ... s..(l..(actual)) __ expected


___ test_adding_programmer_without_js(programmers
    programmers 'sue'  =  'Scala', 'Python'
    expected =  'Python'
    actual = common_languages(programmers)
    ... l..(actual) __ expected


___ test_adding_programmer_without_js_nor_python(programmers
    programmers 'fabio'  =  'PHP'
    expected    # list
    actual = common_languages(programmers)
    ... l..(actual) __ expected


___ test_common_languages_adding_new_common_language(programmers
    programmers 'bob' .a..('C++')
    programmers 'sara' .a..('C++')
    expected =  'C++', 'JS', 'Python'
    actual = common_languages(programmers)
    ... s..(l..(actual)) __ expected