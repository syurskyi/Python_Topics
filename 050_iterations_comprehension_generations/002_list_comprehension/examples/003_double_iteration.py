# seq_x = [1, 2, 3, 4]
# seq_y = 'abc'
# print([(x,y) for x in seq_x for y in seq_y])

# seq = ['abc', 'def', 'g', 'hi']
# print([y for x in seq if len(seq) > 1 for y in x if y != 'e'])
#
text = (("Hi", "Steve!"), ("What's", "up?"))
[word for sentence in text for word in sentence]
# ['Hi', 'Steve!', "What's", 'up?']
#
# text = (("Hi", "Steve!"), ("What's", "up?"))
# gen = (word for sentence in text for word in sentence)
# for word in gen: print(word)

text = (['Roto'], ['RotoPaint'])
print([node for all in text for node in all])