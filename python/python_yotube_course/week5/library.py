from random import choice
import random

#choice
coin1 = random . choice(['heads', 'tails'])
# print(coin1)

#randint
coin2 = random . randint(1,10)
# print(coin2)


#shuffle
from random  import shuffle

music = ["sogati" , "morge sahar" , "owge asemane"]
random.shuffle(music)

# print(music)
# for _ in music:
#     print(_)


#statistics

import statistics
# print(statistics.geometric_mean([100,90,80,50,40,90]))

#sys

import sys
# try:
#     print(f"hello world , {sys.argv[1]}")
# except IndexError:
#     print("Too few argument")

"""other example"""

# print(sys.argv)
#
# if len(sys.argv)>2:
#     sys.exit("Too many argument")
# elif len(sys.argv)<2:
#     sys.exit("Too few argument")
#
# print(f"hello {sys.argv[1]}")


"""say hello to five user"""

# print(sys.argv)
# if len(sys.argv)<2:
#     sys.exit("Too few argument!")
# for arg in sys.argv[1:]:
#     print(f"hello {arg}")


