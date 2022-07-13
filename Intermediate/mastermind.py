## A low level implementation of the game "Mastermind"

import random

# generates a 4 digit code
def gen_code(code_length):
    return ''.join([str(random.randint(0, 9)) for _ in range(code_length)])

# the game
def mastermind(difficulty: int= 1):
    if difficulty < 1:
        difficulty = 1
    elif difficulty > 5:
        difficulty = 5

    tries = 22 - (difficulty * 2)
    code_length = 3 + difficulty
    theCode = gen_code(code_length)
    code_digits = set(theCode)

    for _ in range(tries):
        result = ''
        userInput = input(f"Enter Your {code_length} digit guess code:")

        if len(userInput) != code_length:
            print(f"Enter only {code_length} digit(s). Please try Again.")
            continue

        if userInput == theCode:
            print(f"You guessed it in only {_+1} trys!! \nThe Answer is: ", userInput)
            break

        for i, element in enumerate(userInput):

            if element in code_digits:
                if element == theCode[i]:
                    result += 'R'
                else:
                    result += 'Y'
            else:
                result += 'B'

        print(result)

    else:
        print("You ran out of trys!!")


menu = """
Choose your difficulty level:
1 - Very Easy
2 - Easy
3 - Intermediate
4 - Hard
5 - Very Hard

Choose From [1-5]: """

if __name__ == "__main__":
    choice = int(input(menu))
    mastermind(choice)
