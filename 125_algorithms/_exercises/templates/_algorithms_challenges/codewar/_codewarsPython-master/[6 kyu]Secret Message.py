___ find_secret_message(paragraph):
    paragraph = ''.join([c ___ c __ paragraph.lower() __ c __ 'abcdefghijklmnopqrstuvwxyz -'])
    appear,res    # list,[]
    ___ word __ paragraph.s.. :
        __ word n.. __ appear:
            appear.a..(word)
        ____ word n.. __ res:
            res.a..(word)
    r.. ' '.join(res)


print(find_secret_message('asdf qwer zxcv. zxcv fdsa rewq. qazw asdf sxed. qwer crfv.'))