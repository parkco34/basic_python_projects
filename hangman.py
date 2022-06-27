#!/usr/bin/env python
import random
import string
import time


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

#with open("words.txt", "r") as file:
with open("most_common_words.txt", "r") as file:
    text = file.read()
    words = list(map(str, text.split()))


def get_proper_word(_words: list) -> str:
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

def hangman(_limbs: int) -> None:
    """
    HANGMAN GAME
    ----------------------------------------------------
    word_letters: (set) The letters in the actual WORD
    
    alphabet: (set) from string.acsii_UPPERCASE - All UPPERCASE
        letters of the alphabetL

    used: (set) Empty set to keep track of what the user has already guessed
    """
    
    word = get_proper_word(words).upper()
    # Letters in the WORD
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used = set()

    # USER INPUT 
   
    while len(word_letters) > 0 and _limbs > 0:

        if len(used) != 0:
            print(f"""\n
You have {_limbs} limbs left!
Letters already guessed:
                  """, ''.join(used))

        # To ensure that repeated letter in WORD are still being tracked, since
        # SET removes duplicates
        letter_display = [letter if letter in used else '-' for letter in word]
        print("Currently, your word is: ", ' '.join(letter_display))

        user_letter = input("Enter a letter to guess: ").upper()
        if user_letter in (alphabet - used):
            used.add(user_letter)

            if user_letter in word_letters:
                word_letters.remove(user_letter)    # Correct guess

            else:                                   # Incorrect guess
                _limbs -= 1

        elif user_letter in used:
            print(f"""\n
================================================================
Already used {user_letter}... Oops (˵ ͡o ͜ʖ ͡o˵)
================================================================
                  """)

        else:
            print("""\n
================================================================
You've typed an invalid character...\nLo Siento...( ͡° ͜ʖ ͡°)
================================================================
                  \n""")

    # Conclusion of Hangman Game:
    if _limbs == 0:
        print("\nLo Siento... YOU ARE DEAD! ༼ಢ_ಢ༽")
        time.sleep(3)
        print(
            f"""\n
================================================================
            The Word is: {word}
================================================================
            """
        )

    else:
        print(
            """
================================================================

 ̿̿ ̿̿ ̿̿ ̿'̿'\̵͇̿̿\з= ( ▀ ͜͞ʖ▀) =ε/̵͇̿̿/’̿’̿ ̿ ̿̿ ̿̿ ̿̿  ٩ (╬ʘ益ʘ╬) ۶ ٩ (╬ʘ益ʘ╬) ۶
(◣_(◣_(◣_◢)_◢)_◢)   ( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°) ヾ(☆▽☆) ヾ(☆▽☆)

                    !!!! CORRECT !!!!

(ノಠ益ಠ)ノ彡┻━┻ (ノಠ益ಠ)ノ彡┻━┻ (ノಠ益ಠ)ノ彡┻━┻ (ノಠ益ಠ)ノ彡┻━┻

================================================================
            """
        )


if __name__ == "__main__":
    hangman(int(input("How many LIMBS on the hangman do you want?:\n")))
    
