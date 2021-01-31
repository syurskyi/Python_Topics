_____ ?

# Shto bu komanda ponjala shto mu pishem expression na Python, nado soblysti opredeljonuj sintaksis.
# Pisat' eto nado v kvadratnuh skopkah [] i v samom nachale nado napisat' klychevoe slovo - python


n = ?.tN..('ColorCorrect1')
n['saturation'].sE..('[python nuke.frame()]')

# shobu pitonskij expression bul mnogostrochnuj s vozvrachaemum znacheniem ret 

n['saturation'].sE..('''[python -execlocal x = nuke.frame()
for i in range(10):
    x+=i
ret = x]''')

# V expression vozmozno importirovat' modul. Eto dajot vozmoznost' redaktirovat' expression ne v okne expression
# a gde to v IDLE 

n['disable'].sE..('[python nuke.frame()>30]')

n1 = ?.tN..('ColorCorrect2')
n2 = ?.tN..('ColorCorrect1')

n1['saturation'].sE..('.'.j..([n2.n.., 'saturation']))