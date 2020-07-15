import nuke

# Shto bu komanda ponjala shto mu pishem expression na Python, nado soblysti opredeljonuj sintaksis.
# Pisat' eto nado v kvadratnuh skopkah [] i v samom nachale nado napisat' klychevoe slovo - python


n = nuke.toNode('ColorCorrect1')
n['saturation'].setExpression('[python nuke.frame()]')

# shobu pitonskij expression bul mnogostrochnuj s vozvrachaemum znacheniem ret 

n['saturation'].setExpression('''[python -execlocal x = nuke.frame()
for i in range(10):
    x+=i
ret = x]''')

# V expression vozmozno importirovat' modul. Eto dajot vozmoznost' redaktirovat' expression ne v okne expression
# a gde to v IDLE 

n['disable'].setExpression('[python nuke.frame()>30]')

n1 = nuke.toNode('ColorCorrect2')
n2 = nuke.toNode('ColorCorrect1')

n1['saturation'].setExpression('.'.join([n2.name(), 'saturation']))