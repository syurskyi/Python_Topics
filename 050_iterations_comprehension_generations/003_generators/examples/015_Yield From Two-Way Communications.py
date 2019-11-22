# Yield From - Two-Way Communications
#
# In the last section on generators, we started looking at yield from and how we could delegate iteration to
# another iterator.
# Alternatively we could write the same thing this way:

def squares(n):
    for i in range(n):
        yield i ** 2

def delegator(n):
    for value in squares(n):
        yield value

gen = delegator(5)
for _ in range(5):
    print(next(gen))

def delegator(n):
    yield from squares(n)


gen = delegator(5)
for _ in range(5):
    print(next(gen))


# Yield From - Two-Way Communications
# Let's start by looking at how the delegator works when a subgenerator closes by itself:
# We'll want to inspect the delegator and the subgenerator, so let's import what we'll need from the inspect module:
# Here play_song is the delegator, and song is the subgenerator. We, the Jupyter notebook, are the caller.
# As you can see, no local variables have been created in player yet - that's because it is created,
# not actually started.
# We can now get a handle to the subgenerator s:
# And we can check the state of s:
# As we can see the subgenerator is suspended.
# Let's iterate a few more times:

from inspect import getgeneratorstate, getgeneratorlocals

def song():
    yield "I'm a lumberjack and I'm OK"
    yield "I sleep all night and I work all day"

def play_song():
    count = 0
    s = song()
    yield from s
    yield 'song finished'
    print('player is exiting...')

player = play_song()
print(getgeneratorstate(player))
print(getgeneratorlocals(player))

next(player)

print(getgeneratorstate(player))
print(getgeneratorlocals(player))
s = getgeneratorlocals(player)['s']

print(getgeneratorstate(s))

print(next(player))
print(getgeneratorstate(player))
print(getgeneratorstate(s))

print(next(player))
print(getgeneratorstate(player))
print(getgeneratorstate(s))

# Yield From - Two-Way Communications
#
# Important to note here is that when the subgenerator returned, the delegator continued running normally.
#
# Let's make a tweak to our player generator to make this even more evident:

def player():
    count = 1
    while True:
        print('Run count:', count)
        yield from song()
        count += 1

p = player()
next(p), next(p)
next(p), next(p)
next(p), next(p)
