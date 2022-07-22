#!/usr/bin/env python
from textwrap import dedent
from os.path import isdir, join, expanduser
from os import walk, listdir

def find_file(filename, dir_path=expanduser("~")):

    for path in listdir(dir_path):
        if isdir(join(dir_path, path)):
             
             for file in listdir():
                 if file == filename:
                     with open(filename) as thefile:
                        return thefile.read().split()
                        
        else:
            print(dedent("""
                         \nLo Siento...\n
                         The file you're looking was not found.\n
                         Try finding the creator of this stupid-dumb ( ͡° ͜ʖ ͡°  )
                         script maybe, ya?
                         """))

def permutations(items: list) -> int:
    n = len(items)
    unique_list = [i for i in items if items.count(i) == 1]
    counter = 1

    # Check if characters in items are all UNIQUE
    if len(unique_list) == len(list(items)):
        for i in range(1, len(unique_list)+1):
            counter *=  i

        return counter

    else:
        # Multinomial Theorem goes here
        non_unique = [i for i in range(len(items)) if items.count(i)>1]
        for item in range(1, len(items)+1):
            counter *= item

            for i in range(1, len(set(non_unique))):
                pass


def word_unjumbler(jumbled_word: str) -> list:
    result = find_file("dictionary_words.txt")
    print(result)
    return result

word_unjumbler('dog')
breakpoint()

