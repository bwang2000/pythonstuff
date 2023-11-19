import random

def generateNumber(a):
    ''' returns an 'a' digit string of numbers between 0 and 10^a-1 '''
    return str(random.randint(pow(10,a-1),pow(10,a)+pow(10,a-1)-1))[-a:]


def playGame(a):
    '''play a game of bagels'''
    for i in range(10):
        print(f"Guess #{i+1}")
        b = str(input())
        c = ''
        if (b == a): 
            print("You got it!")
            return
        for j in a: 
            if (a[j] == b[j]): c += "Fermi"
            elif (b[j] in a): c += "Pico"
        if (c == ''): print ("Bagels")
        else: print (c)
    print (f"Sorry, you ran out of guesses. The correct answer was {a}")
    return


print ('''I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
When I say:    That means:
  Pico         One digit is correct but in the wrong position.
  Fermi        One digit is correct and in the right position.
  Bagels       No digit is correct.
I have thought up a number.
You have 10 guesses to get it.''')

number = generateNumber(3)

playGame(number)

again = input ('Do you want to play again? (yes or no)')
if (again == 'yes'):
    playGame()
else: 
    print("Thanks for Playing!")
    exit
