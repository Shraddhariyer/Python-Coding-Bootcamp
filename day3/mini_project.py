#Number Guessing Game
#using for loop
print("GUESS THE NUMBER CHALLENGE!!\n")
print("You'll have 5 chances to guess the number between (1-20)\n")
secret=8
for i in range(5):
    guess=int(input("Guess a number:"))
    if guess==secret:
        print("You guessed it correct, You won.")
        break
    else:
        print("Wrong guess, try again..")
else:
    print("You couldn't guess the number. You lose.")
#using while loop
print("GUESS THE NUMBER CHALLENGE!!\n")
print("You'll have 5 chances to guess the number between (1-20)\n")
secret=10
count=1
while count<=5:
    guess=int(input("Guess a number:"))
    if guess==secret:
        print("You guessed it correct, You won.")
        break
    else:
        print("Wrong guess, try again..")
    count+=1#count=count+1
else:
    print("You couldn't guess the number. You lose.")