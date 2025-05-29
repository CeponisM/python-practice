import random # Import random for RNG

# User input number validation checking
def is_number(input):
    try:
        float(input)
        return True
    except ValueError: # if float(input) throws ValueError return false
        return False
    
print("Welcome to RNG Guesser! \n Guess the number 1-10")

rng = random.randint(0,10) # game selects number 1-10
rngGuess = None # initialize user guess variable

while rngGuess != rng: # compare input to rng
    print("Enter Guess: ")
    usrAnswer = input() # ask user for input and store in usrAnswer
    if is_number(usrAnswer): # check if userAnswer is a number
        rngGuess = float(usrAnswer) # convert user answer string answer to float
    else: # if not a number ask user to try again
        print("Enter A Number 1-10.")
    print("Try Again!!!")

print("Congratulations you correctly guessed " + str(int(rngGuess)) + "!")