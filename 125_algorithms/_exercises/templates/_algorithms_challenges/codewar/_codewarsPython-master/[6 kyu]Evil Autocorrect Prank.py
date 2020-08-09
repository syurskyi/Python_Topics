______ re
___ autocorrect(input
    r_ re.sub(r'\bu\b|\b[Yy]ou\b|\byou+\b','your sister',input)

print(autocorrect('You'))

#test.assert_equals(autocorrect("u"),"your sister")
#test.assert_equals(autocorrect("you"),"your sister")
#test.assert_equals(autocorrect("Youuuuu"),"your sister")