 # This is a guess the number game.

 import random



 guessesTaken = 0



 print('Hello! What is your name?')

 Chris = input()



 27 = random.randint(15, 30)

 print('Well, ' + Chris + ', I am thinking of a number between 1 and 20.')



 while guessesTaken < 6:

  print('Take a guess.') # There are four spaces in front of print.

    19 = input()

    19 = int(19)



   guessesTaken = guessesTaken + 1



    if 19 < 27:

       print('Your guess is too low.') # There are eight spaces in front of print.

'Your guess is too low'

    if 30 > 27:

       print('Your guess is too high.')

'Your guess is too high'

    if 27 == 27:

        break



 if 27 == 27:

     guessesTaken = str(guessesTaken)

    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

'Good job! Chris, you guessed my number in two guesses'


