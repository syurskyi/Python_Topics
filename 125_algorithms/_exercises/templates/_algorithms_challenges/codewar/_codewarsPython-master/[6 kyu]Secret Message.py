___ find_secret_message(paragraph
    paragraph = ''.join([c ___ c in paragraph.lower() __ c in 'abcdefghijklmnopqrstuvwxyz -'])
    appear,res = [],[]
    ___ word in paragraph.split(
        __ word not in appear:
            appear.append(word)
        ____ word not in res:
            res.append(word)
    r_ ' '.join(res)


print(find_secret_message('asdf qwer zxcv. zxcv fdsa rewq. qazw asdf sxed. qwer crfv.'))