___ proverb(itens, qualifier=''
    phrases =  'For want of a {0} the {1} was lost.'.f..(el1, el2)
               ___ el1, el2 __ z..(itens, itens[1:])]
    qualifier += ' ' __ qualifier ____ ''
    phrases.a..('And all for the want of a {0}{1}.'.f..(qualifier,
                   itens[0]))
    r.. '\n'.j..(phrases)
