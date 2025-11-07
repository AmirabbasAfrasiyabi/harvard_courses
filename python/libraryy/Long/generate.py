"""choice"""
import random
from random import choice
import sys
# coin = random.choice(["heads" , "tails"])
# print(coin)

"""other solution """
# coin = choice(["heads" , "tails"])
# print(coin)

"""randint"""
# number = random.randint(1,10)
# print(number)

"""shuffle"""
# card = ["jack" , "bob" , "amir" , "ati" , "reyhan" ,"selena" , "jlo"]
# random.shuffle(card)
# for cards in card:
#     print(cards)

"""statistics"""
# import statistics
# x = statistics.mean([100,40])
# print(x)
 

"""sys"""
# if len(sys.argv) <2:
#     sys.exit("too few argument")
# elif len (sys.argv) > 2:
#     sys.exit("too many argument")

# print("hello my name is",sys.argv[1])


"""saying"""

def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye , {name}")


if __name__ == "__main__":
    main()


