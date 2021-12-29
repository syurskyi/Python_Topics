___ find_secret_message(paragraph):
    paragraph = ''.join([c for c in paragraph.lower() __ c in 'abcdefghijklmnopqrstuvwxyz -'])
    appear,res = [],[]
    for word in paragraph.split():
        __ word not in appear:
            appear.append(word)
        elif word not in res:
            res.append(word)
    return ' '.join(res)


print(find_secret_message('asdf qwer zxcv. zxcv fdsa rewq. qazw asdf sxed. qwer crfv.'))