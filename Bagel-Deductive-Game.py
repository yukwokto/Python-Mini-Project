from random import shuffle
# set the maximum guess of the game
MAX_GUESS = 10
# set the number of digits of the number
MAX_DIGIT = 3


def main():
    # Introduction
    print(f'''
###################################################################################################
#   Bagel Detective Game by Kwok To Yu                                                            #
#                                                                                                 #
#   A number guessing game allows player to guess a {MAX_DIGIT}-digit numbers.                              #
#   Each player has {MAX_GUESS} chances to guess the correct number.                                       #
#                                                                                                 #
#   The digit of the number is non-repetitive, zero is not included.                              #
#   After each round of guessing, a response to the answer is given:                              #
#                                                                                                 #
#   Response 1: Pico  => One digit is included in the guess, but it is in the wrong position      #
#   Response 2: Fermi => One digit is correct and in the right position                           #
#   Response 3: Bagel => No digit is correct.                                                     #
#                                                                                                 #
###################################################################################################

Now the game begins! 

A {MAX_DIGIT}-digit number is generated.
''')
    # generate a non-repetive 3-digit number
    answer = numberGenerator()
    round = 1
    
    while round <= MAX_GUESS:
        print(f'Round {round}')
        guess = input("Enter a number: ")
        response = getReponse(guess, answer)
        
        if response == "correct":
            print("Correct! You WON!")
            break
        
        else:
            print(f"{response}")
            print()
            round += 1
        
    print(f'The number is {answer}')
        

# return a response according to the player guess
def getReponse(guess, answer):
    # if the guess is completely correct
    if guess == answer:
        return "correct"
    
    # if one or more digits guess are in the right order 
    for i in range(MAX_DIGIT):
        if guess[i] == answer[i]:
            return "Fermi"
    
    # if one digit is included but not in the right order
    else:
        for c in guess:
            if c in answer:
                return "Pico"
            
    # if none of the digit is correct
    return "Bagel"


# create a non-repetitive-digit number
def numberGenerator():
    numList = list('123456789')
    shuffle(numList)
    num = ""
    for i in range(MAX_DIGIT):
        num += numList[i]
    return num    


if __name__ == '__main__':
    main()
