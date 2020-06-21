#!/usr/bin/env python
# coding: utf-8

# # `set`

# ## Problem Statement: Prime Number Generator
Find all the prime numbers up to a given number.
# In[ ]:


def primes(max_num=100):
    found_primes = {2}
    for num in range(3,max_num):
        isprime = True
        for divisor in found_primes:
            if num % divisor == 0:
                isprime = False
        if isprime:
            found_primes.add(num)
    return found_primes


# In[ ]:


print(primes())


# ## set
- collection of items
- no natural sorting
- unique items
- hashability
- methods: intersect, difference, union, ... 
# #### interacting with the `set`-type

# In[ ]:


suits = {'hearts', 'diamonds', 'spades', 'clubs', }

faces = set(['ace', 'king', 'queen', 'jack', 'jack'])

numbers = set(range(2,11))


# In[ ]:


suits


# In[ ]:


faces


# In[ ]:


numbers


# In[ ]:


deck = set() # {} means "empty dictionary"

for suit in suits:
    for number in numbers:
        deck.add('{} of {}'.format(number, suit))
    for face in faces:
        deck.add('{} of {}'.format(face, suit))

deck


# In[ ]:


deck[0]


# In[ ]:


from random import choice

choice(deck)


# In[ ]:


from random import shuffle

shuffle(deck)


# In[ ]:


hand = set()

for card in deck:
    if len(hand) < 5:
        hand.add(card)
        deck.remove(card)
    
hand


# In[ ]:


hand = set()

for card in deck:
    if len(hand) < 2:
        hand.add(card)
    
for card in hand:
    deck.remove(card)
    
hand


# In[ ]:


board = set()

for _ in range(3):
    board.add(deck.pop())
    
board


# In[ ]:


board | hand


# In[ ]:


board.union(hand)


# In[ ]:


deck.add('High Joker')
deck.add('Low Joker')


# In[ ]:


'High Joker' in deck


# In[ ]:


deck.remove('High Joker')
deck.remove('Low Joker')


# In[ ]:


deck.discard('rules of five-card stud')


# In[ ]:


deck = { '{} of {}'.format(rank, suit) for rank in numbers | faces
                                       for suit in suits }

deck.update(['high Joker', 'low Joker'])

deck


# In[ ]:


from collections import namedtuple

Card = namedtuple('Card', 'suit rank')

deck = {Card(suit, rank) for rank in numbers | faces
                          for suit in suits }

deck

- straight flush
- four of a kind
- full house
- flush
- straight
- three of a kind
- two pair
- one pair
- high card
# In[ ]:


valid_straights = {set(range(n, n+5)) for n in range(2,7)}


# In[ ]:


valid_straights = {frozenset(range(n, n+5)) for n in range(2,7)}
valid_straights


# In[ ]:


valid_straights = {frozenset(range(n, n+5)) for n in range(2,7)} |                   {frozenset(['ace', 2, 3, 4, 5])              } |                   {frozenset([7, 8, 9, 10, 'jack'])            } |                   {frozenset([8, 9, 10, 'jack', 'queen'])      } |                   {frozenset([9, 10, 'jack', 'queen', 'king']) } |                   {frozenset([10, 'jack', 'queen', 'king', 'ace']) }
    
valid_straights


# In[ ]:


def rank2value(card):
    if card.rank in numbers:
        return card.rank
    
    return {'ace':   14,
            'king':  13,
            'queen': 12,
            'jack':  11,}[card.rank]


# In[ ]:


def best_card(hand):
    return max(hand, key=rank2value)


# In[ ]:


from itertools import groupby, combinations

def best_hand(hand):
    suits_in_hand = {card.suit for card in hand}
    ranks_in_hand = {frozenset(cs) for _,cs in groupby(sorted(hand, key=rank2value), key=rank2value)}
    
    high_card        = best_card(hand)
    twos_of_a_kind   = {cs for cs in ranks_in_hand if len(cs) == 2}
    threes_of_a_kind = {cs for cs in ranks_in_hand if len(cs) == 3}
    fours_of_a_kind  = {cs for cs in ranks_in_hand if len(cs) == 4}
    straights        = {cs for cs in combinations(hand, 5) if {c.rank for c in cs} in valid_straights}
        
    if len(suits_in_hand) == 1 and straights:
        return hand, 'straight flush'
    
    if fours_of_a_kind:
        return max(fours_of_a_kind, key=lambda cs: rank2value(best_card(cs))), 'four of a kind'
    
    if threes_of_a_kind and twos_of_a_kind:
        return max(threes_of_a_kind, key=lambda cs: rank2value(best_card(cs))) |                max(twos_of_a_kind,   key=lambda cs: rank2value(best_card(cs))), 'full house'
        
    if len(suits_in_hand) == 1:
        return hand, 'flush'
    
    if straights:
        return max(straights, key=lambda cs: rank2value(best_card(cs))), 'straight'
    
    if threes_of_a_kind:
        return max(threes_of_a_kind, key=lambda cs: rank2value(best_card(cs))), 'three of a kind'
    
    if len(twos_of_a_kind) == 2:
        return twos_of_a_kind.pop() | twos_of_a_kind.pop(), 'two pairs'

    if len(twos_of_a_kind) == 1:
        return twos_of_a_kind.pop(), 'one pair'
    
    return {high_card,}, 'high card'


# In[ ]:


get_ipython().run_cell_magic('time', '', '\nfrom itertools import combinations\n\nexample_hands = {}\n\nfor hand in combinations(deck, 5):\n    cards, hand_type = best_hand(hand)\n    if hand_type not in example_hands:\n        example_hands[hand_type] = cards, hand')


# In[ ]:


for hand_type in example_hands:
    print(hand_type)
    print('=' * len(hand_type))
    matched_cards, all_cards = example_hands[hand_type]
    for card in all_cards:
        print('  ', '*' if card in matched_cards else ' ', '{} of {}'.format(card.rank, card.suit))

.clear
.difference
.difference_update
.intersection
.intersection_update
.symmetric_difference
.symmetric_difference_update
# In[ ]:


animals = {'dog', 'cat', 'bird'}
animals


# In[ ]:


animals.clear()
animals


# In[ ]:


while animals:
    animals.pop()


# In[ ]:


{'dog', 'cat', 'bird'} - {'horse'}


# In[ ]:


{'dog', 'cat', 'bird'}.difference('cat')


# In[ ]:


{'dog', 'cat', 'bird'}.difference(['cat'])


# In[ ]:


{'dog', 'cat', 'bird', 'horse'}.symmetric_difference({'dog', 'horse', 'giraffe'})


# In[ ]:


{'dog', 'cat', 'bird', 'horse'} ^ {'dog', 'horse', 'giraffe'}


# In[ ]:


{'dog', 'cat', 'bird', 'horse'}.intersection({'dog', 'horse', 'giraffe'})


# In[ ]:


{'dog', 'cat', 'bird', 'horse'} & {'dog', 'horse', 'giraffe'}


# In[ ]:


animals = {'dog', 'cat', 'bird'}
animals.intersection_update({'bird', 'horse'})
animals


# In[ ]:


animals = {'dog', 'cat', 'bird'}
animals &= {'bird', 'horse'}
animals


# In[ ]:


animals = {'dog', 'cat', 'bird'}
animals.difference_update({'bird', 'horse'})
animals


# In[ ]:


animals = {'dog', 'cat', 'bird'}
animals -= {'bird', 'horse'}
animals


# In[ ]:


animals = {'dog', 'cat', 'bird'}
animals.update({'bird', 'horse'}) # think `union_update`
animals


# In[ ]:


animals = {'dog', 'cat', 'bird'}
animals |= {'bird', 'horse'}
animals


# In[ ]:


animals = {'dog', 'cat', 'bird'}
animals.symmetric_difference_update({'bird', 'horse'})
animals


# In[ ]:


animals = {'dog', 'cat', 'bird'}
animals ^= {'bird', 'horse'}
animals


# ## Problem Statement: Prime Number Generator
Find all the prime numbers up to a given number.
# In[132]:


def primes(max_num=100):
    found_primes = {2}
    for num in range(3, max_num):
        # determine if the number is prime
        pass
    return found_primes


# In[133]:


def primes(max_num=100):
    found_primes = {2}
    for num in range(3,max_num):
        isprime = True
        for divisor in found_primes:
            if num % divisor == 0:
                isprime = False
        if isprime:
            found_primes.add(num)
    return found_primes


# In[134]:


print(primes())


# In[135]:


def primes(max_num=100):
    found_primes = set()
    for num in range(2,max_num):
        if not any(num % divisor == 0 for divisor in found_primes):
            found_primes.add(num)
    return found_primes


# In[136]:


print(primes())


# In[137]:


def primes(max_num=100):
    numbers = set(range(2,max_num))
    nonprimes = set()
    for num in numbers:
        for x in range(num, max_num // num + 1):
            nonprimes.add(num * x)
    return numbers - nonprimes


# In[138]:


print(primes())


# In[139]:


def primes(max_num=100):
    numbers = set(range(2,max_num))
    nonprimes = set()
    for num in numbers:
        nonprimes.update(num * x for x in range(num, max_num // num + 1))
    return numbers - nonprimes


# In[140]:


print(primes())


# In[141]:


def primes(max_num=100):
    numbers = set(range(2,max_num))
    for num in range(2, max_num):
        for x in range(num, max_num // num + 1):
            numbers.discard(num * x)
    return numbers


# In[142]:


print(primes())


# [An Introduction to Prime Number Sieves: ftp://ftp.cs.wisc.edu/pub/techreports/1990/TR909.pdf](ftp://ftp.cs.wisc.edu/pub/techreports/1990/TR909.pdf)

# In[143]:


from itertools import count

def primes():
    found_primes = {2}
    yield 2
    for num in count(3):
        isprime = True
        for divisor in found_primes:
            if num % divisor == 0:
                isprime = False
        if isprime:
            found_primes.add(num)
            yield num


# In[ ]:


# list(primes())


# In[145]:


from itertools import islice

print(set(islice(primes(),0,10)))


# In[156]:


from itertools import count

def primes():
    multiples = {}
    for num in count(2):
        print (multiples)
        if num in multiples:
            for x in multiples[num]:
                multiples.setdefault(num+x, set()).add(x)
            del multiples[num]
        else: # prime !
            multiples[num * num] = {num}
            yield num


# In[157]:


from itertools import islice

print(list(islice(primes(),0,10)))

