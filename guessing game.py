import random
winning_number = random.randint(5,5 )
guess = int(input("Enter an integer: "))
if guess==winning_number:
    print ("you WIN!")
elif guess > winning_number:
    print ("too high")
else:
    print ("too low!")
    
