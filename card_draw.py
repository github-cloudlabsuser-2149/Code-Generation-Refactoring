# Intentionally flawed Python program

# importing modules
import itertools
import random

deck = list(itertools.product(range(1, 14), ['Spade', 'Heart', 'Diamond', 'Club']))

# shuffle the cards
random.shuffle(deck)

# draw five cards
for i in range(5):
    print(deck[i][0], "of", deck[i][1])
