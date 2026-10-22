#Author: Brett Rix

#Import functions
from wordle_functions import choose_word, get_guess, evaluate_guess
from wordle_functions import display_guess, has_won

play_again = True

#Welcome the player.
print()
print("Welcome to Mystery Wordle!")
while play_again == True:
    print()
    print("Guess the five-letter word!")
    print()
    print("G = correct letter and position")
    print("Y = correct letter, wrong position")
    print("- = letter is not in the word")
    print()

    #Select a secret five-letter word.
    secret_word = choose_word()

    previous_guesses = []
    player_wins = False

    #Give the player up to six guesses.
    for i in range(1,7):
        print(f"Attempt {i} of 6")
        #Require each guess to contain exactly five letters.
        #Reject guesses that have already been used.
        player_guess = get_guess(previous_guesses)
        feedback = evaluate_guess(player_guess, secret_word)
        #Display feedback after every guess.
        #Tell the player when a letter is correct, misplaced, or absent.
        print()
        display_guess(player_guess, feedback)
        print()
        #End the game when the player guesses the word or uses all six attempts.
        if has_won(feedback):
            player_wins = True
            break

    if player_wins == True:
        print("Congratulations! You solved the puzzle.")
    else:
        print("I'm sorry, you couldn't solve the puzzle.")
        #Display the secret word if the player loses.
        print(f"The secret word was: {secret_word}")

    #Ask whether the player would like to play again.
    print("Would you like to play again?")
    play_again_input = input('Press "Y" to play again, press any other key to quit. ').upper()
    if play_again_input == "Y":
        play_again = True
    else:
        play_again = False

print()
print("Thanks for playing! ;)")
print()

