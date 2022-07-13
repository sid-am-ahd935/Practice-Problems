"""
The Infinite Monkey Theorum states that if a monkey was given a typewriter and an infinite amount of time,
Eventually the monkey could write some of the lines of the great acts of Shakespeare.

The score would then be set to determine how much of the works of Shakespeare was written by the monkey.
"""

import random

# function to generate a random string
def generateOne(strlen):

    alphabets = "abcdefghijklmnopqrstuvwxyz "
    sentence = ""

    for i in range(strlen):
        sentence += alphabets[random.randrange(27)]

    return sentence


def generateOneBySmartMonkey(strlen, prevString, remarksString: "prevString where incorrect letters are dashes and only correct letters are there"):
    pass


#### This would be my implementation when there is a little change in this program for making things when monkey has space to write more than goalstring; then this would become a sliding window problem
# # function to determine the score of the generated string
# def long_score(goalString, monkeyString):
#     # goalString is the message that will be compared with the monkey's writings
#     # monkeyString is the writings of the monkey named Python; It should be always greater than equal to the goalString
#     len_goal = len(goalString)
#     len_monkey = len(monkeyString)
#     goal_chars = set

#     match = 0
#     i = 0

#     """
#     Window Sliding Algorithm Here To Score The Monkey String...
#     """

#     return match / len_goal



# function to determine the score of the generated string
def score(goalString, monkeyString):
    # goalString is the message that will be compared with the monkey's writings
    # monkeyString is the writings of the monkey named Python
    numScore = 0
    assert len(goalString) == len(monkeyString)

    for a, b in zip(goalString, monkeyString):
        if a == b:
            numScore += 1

    return numScore / len(goalString)


def main():
    # goalString = input("Enter your desired sentence:\n")
    goalString = "Not too long"
    # monkeyStrlen = len(goalString) * 1000
    monkeyStrlen = len(goalString)
    monkeyString = generateOne(monkeyStrlen)

    best = 0
    newScore = score(goalString, monkeyString)
    print("Starting monkey...")

    while newScore<1:
        if newScore > best:
            print(monkeyString)
            best = newScore

        monkeyString = generateOne(len(goalString))
        newScore = score(goalString, monkeyString)


if __name__ == "__main__":
    main()