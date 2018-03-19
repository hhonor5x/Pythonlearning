### While loops
##
### Syntax :
##    while condition:
##        statement1
##        statement2
##    else:
##        statement3
##        statementn
### Premature termination of a while loop using break
### break : As soon as the program execution flow comes to break inside a while loop ( or any other loop),the loop will be immediatly left.
### continue: continue stops the current iterration of loop and starts the next iteration by checkinig the condition.
##
### If a loop is left by a break else part is not executed.


import random
n = 20
to_be_guessed=int(n*random.random())+1

print(to_be_guessed)
guess =0

while guess != to_be_guessed :
    guess = int(input("New Number:"))
    if guess > 0:
        if guess > to_be_guessed:
            print("Number too large")
        elif guess < to_be_guessed:
            print("Number to small")
        else:
            print("Sorry that you are giving up!")
            break
else:
    print("Congratulations, You made it")
    