import random

#Secret word picker function
def choose_word():
    words = ["plant", "crane", "slate", "brick", "ghost",
         "chair", "flame", "storm", "bread", "cloud",
         "piano", "tiger", "mouse", "horse", "light",
         "world", "quick", "frost", "grape", "shine",
         "dwarf", "train", "smile", "ocean", "candy",
         "honey", "fairy", "black", "jumbo", "proud",
         "bacon", "audio", "badge", "blame", "blind",
         "blunt", "board", "brave", "brown", "brush",
         "cabin", "camel", "charm", "chest", "clamp",
         "coral", "crown", "crust", "dance", "depth",
         "drink", "equal", "fable", "flint", "forty",
         "frame", "giant", "glove", "grind", "haunt",
         "house", "index", "joker", "knife", "lemon",
         "magic", "maple", "mango", "night", "noble",
         "opera", "paint", "pearl", "plume", "quest",
         "raven", "river", "robin", "scout", "shark",
         "snake", "spice", "sword", "table", "thumb",
         "torch", "voice", "whale", "wrist", "zebra"]
    secret_word = random.choice(words)

    return secret_word.upper()


#Get player guess and validate it.
def get_guess(previous_guesses):
    player_guess = input("Enter a five letter word: ").upper()
    while (len(player_guess) != 5) or (not player_guess.isalpha()) or (player_guess in previous_guesses):
        
        #Require each guess to contain exactly five letters.
        if (len(player_guess) != 5) or (not player_guess.isalpha()):
            print("Please enter five letters only.")
            player_guess = input("Enter a five letter word: ").upper()
        
        #Reject guesses that have already been used.
        else:
            print("You've guessed that before. Please try again.")
            player_guess = input("Enter a five letter word: ").upper()
    
    previous_guesses.append(player_guess)

    return player_guess


#Evaluate the player guess and create feedback
def evaluate_guess(player_guess, secret_word):
    feedback = []
    for i in range(5):
        if player_guess[i] == secret_word[i]:
            feedback.append("G")
        
        elif player_guess[i] in secret_word:
            feedback.append("Y")
        
        else:
            feedback.append("-")

    return feedback


#Display guess with feedback
def display_guess(player_guess, feedback):
    guess_print ="Guess:    "
    feedback_print = "Feedback: "
    for i in range(5):
        guess_print = guess_print + player_guess[i] + " "
        #Tell the player when a letter is correct, misplaced, or absent.
        feedback_print = feedback_print + feedback[i] + " "

    #Display feedback after every guess.
    print(guess_print)
    print(feedback_print)


#Compare feedback to see if player wins
def has_won(feedback):
    return feedback == ['G', 'G', 'G', 'G', 'G']
        
    
    
    