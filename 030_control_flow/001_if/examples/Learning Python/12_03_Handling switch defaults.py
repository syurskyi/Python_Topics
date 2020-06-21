__author__ = 'sergejyurskyj'


branch = {'spam': 1.25,
          'ham':  1.99,
          'eggs': 0.99}

print(branch.get('spam', 'Bad choice'))

print(branch.get('bacon', 'Bad choice'))


choice = 'bacon'
if choice in branch:
    print(branch[choice])
else:
    print('Bad choice')