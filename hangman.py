#!/usr/bin/env python
import random
import re
import string

"""
If the letter guessed is in the difference between the two SETS,
the used letters and the alphabet, then add the guessed letter 
to the SET of correctly guessed letters in the WORD and subtract
the letter from the SET of letters in the actual WORD...
---------------------------------------------------------------
If user, either types an invalid character or guesses a letter already guessed,
use a print statement, and everytime the loop runs, it'll display a dash
where the user hasn't guess the correct letter and the letter iteself
where they have
---------------------------------------------------------------
Game is over when the letters in the WORD reach zero

""" 

with open("words.txt", "r") as file:
    text = file.read()
    words = list(map(str, text.split()))


def get_proper_word(_words):
    """
    Validates the Word to be used in the Hangman game
    and returns the PROPER word, UPPERCASED
    -------------------------------------------------
    INPUTS:
        _words: (list) List of words

    OUTPUTS:
        word: (str) Proper Word
    """
    
    # Remove all Special Characters except the hypen ('-')
    word = random.choice(_words)
#    # Allow Hyphens
#    remove = string.punctuation.replace('-', '')

    # No Special Characters allowed
    remove = string.punctuation
    word = word.translate(str.maketrans('', '', remove))

    return word

def user_input():
    """
    Gets user input via GUI
    ________________________________
    INPUTS:

    """

def hangman(_limbs):
    """
    HANGMAN GAME
    ----------------------------------------------------
    word_letters: (set) The letters in the actual WORD
    
    alphabet: (set) from string.acsii_UPPERCASE - All UPPERCASE
        letters of the alphabetL

    used: (set) Empty set to keep track of what the user has already guessed
    """
    
    word = get_proper_word(words)
    # Letters in the WORD
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used = set()

    # USER INPUT
    while len(word_letters) > 0 and _limbs > 0:

        print(f"""You have {_limbs} limbs left!
              \nSo far you've guessed the letters:\n
              """, ''.join(used))

        
        letter_display = [letter if letter in used else '-' for letter in word]
        print("Currently, your word is: ", ' '.join(letter_display))

        user_letter = input("Enter a letter to guess: ").upper()
        if user_letter in (alphabet - used):
            used.add(user_letter)

            if user_letter in word_letters:
                word_letters.remove(user_letter)

        elif user_letter in used:
            _limbs = _limbs - 1
            print(f"\nAlready used {user_letter}... Oops (˵ ͡o ͜ʖ ͡o˵)")

        else:
            print("\nYou've typed an invalid character...\nLo Siento...( ͡° ͜ʖ ͡°)")

    # Conclusion of Hangman Game:
    if _limbs == 0:
        print("\nLo Siento... YOU ARE DEAD! ༼ಢ_ಢ༽")

    else:
        print("YAY!! YOU GUESSED THE CORRECT WORD!  ̿̿ ̿̿ ̿̿ ̿'̿'\̵͇̿̿\з= ( ▀ ͜͞ʖ▀) =ε/̵͇̿̿/’̿’̿ ̿ ̿̿ ̿̿ ̿̿")


if __name__ == "__main__":
    hangman(int(input("How many LIMBS on the hangan do you want?:\n")))
