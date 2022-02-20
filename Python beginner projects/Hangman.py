import random

from words import words
import string # from python, for the alphabet, this function set(string.ascii_uppercase)

lives = 6
def get_valid_words(words):
    word = random.choice(words) # randomly chooses something from the list
    while "-" in word or "" in word:
        word = random.choice(words)
    return word

def hangman():
    word = get_valid_words(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        print("You have", lives, "lives left and you have used these letters: ', ' ".join(used_letters))

        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word: ', ' ".join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            user_letter.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1 #takes away a life if wrong
                print("letter is not in word")

        elif user_letter in used_letters:
            print("You have already used that character. Try again")
        else:
            print("Invalid character. Please try again")
    if lives == 0:
        print("You died, sorry. The world was", word)
    else:
        print("You guessed the word", word, "!!" )


hangman()