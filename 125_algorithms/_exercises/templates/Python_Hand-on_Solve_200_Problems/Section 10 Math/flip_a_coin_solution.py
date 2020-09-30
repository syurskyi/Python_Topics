# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Write a Python program to flip a coin 1000 times and count heads and tails.

import random
import itertools

results = {
    'heads': 0,
    'tails': 0,
}

sides = list(results.keys())

for i in range(10000):
    results[random.choice(sides)] += 1

print('Heads:', results['heads'])
print('Tails:', results['tails'])


