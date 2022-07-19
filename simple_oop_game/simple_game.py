#!/usr/bin/env python
from textwrap import dedent
from random import randint
from sys import exit


class MentalState(object):

    def enter(self):
        print("Mental States not configured yet!")
        exit(1)


class Death(MentalState):

    death_rattles = [

    """Every adversity, every failure, every heartache carries with it the
    seed of an equal or greater benefit.
    """,
    """
    What is the point of being alive if you don't at least try to do something remarkable?
    """,
    """
    That which does not kill us makes us stronger
    """,
    """
    A thinker sees his own actions as experiments and questions--as attempts to find out something. Success and failure are for him answers above all.
    """,
    """
    There are few pains so grievous as to have seen, divined, or experienced how an exceptional man has missed his way and deteriorated
    """,
    """
    Many a man fails to be a thinker simply because his memory is too good.
    """,
    """
    Success is not final, failure is not fatal: it is the courage to continue that counts.
    """,
    """
    Success is stumbling from failure to failure with no loss of enthusiasm.
    """,
    """
    My fault, my failure, is not in the passions I have, but in my lack of control of them.
    """,
    """
    All of old. Nothing else ever. Ever tried. Ever failed. No matter. Try again. Fail again. Fail better.
    """,
    """
    It is hard to fail, but it is worse never to have tried to succeed.
    """,
    """
    All men make mistakes, but a good man yields when he knows his course is wrong, and repairs the evil. The only crime is pride.
    """
    ]

    def enter(self):
        print(Death.death_rattles[randint(0, len(self.death_rattles)-1)])
        exit(1)



class Abyss(MentalState):

    def enter(self):
        print(dedent("""
         You regain consciousness only to find yourself in a cold,
         damp basement.  After looking for a way out, you realize
         the only way to escape is through the WINDOW...
         Unfortunately, you're not strong enough to pull it open!
         What's worse, even if you could open it, there's some kind
         of weird puzzle you have to solve before it can open
         completely.

         As if you weren't stressed enough, you see a puddle of water in the
                     corner.  It's MOVING!  The BASEMENT IS FLOODING!!! No time
                     to waste!  We have to figure out how to get out...

        (Heavy breathing behind you) A Re-Sister is attacking you!!!
                     \n"""))

        action = input("> ").lower()

        if action == "exercise":
            print(dedent("""
                         \nYou SWOLE UP, capable of lifting a car.  You
                         uppercut the beast in one of its four armpits and
                         round house kick the fool in the right temple
                         incompasiating it... You decapitate the S.O.B\n
                         """))
            return 'dreams'

        elif action == "read":
            print(dedent("""
                         \nYou pick up an book on Abstract Algebra and attempt
                         to read it, but the Re-Sister looks on judgmentally
                         and then devours your head clean off your
                         shoulders!\n
                         """))
            return 'death'

        elif action == 'henri':
            print(dedent("""
                         \nYou start playing with Henri using a bird toy... The
                         Creature takes the birdy away from you in jealousy and
                         begins playing with the Bengal... it thinks it has a
                         friend.  CUTE...
                         """))
            return 'superwin'

        elif action == "drink" or "gummies":
            print(dedent("""
                         \nYou turn off the lights and crack open a pint of
                         Smirnoff... Time for a stimulating movie!
                         """))
            return 'abyss'

        else:
            print("DOESN'T COMPUTE!")
            return 'abyss'


class Dreams(MentalState):

    def enter(self):
        print(dedent("""
                     \nProud with your little win, you fall deep asleep...
                     Falling into an unimaginable HELL some people call,
                     Dreaming, where a monster appears charging you!  It's a
                     damn Lieche_ML!!!! NOOOOOOOO!!!!!\nWhat's this??  She
                     challenges you to a game of WITS!!\n
                     """))
        
        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("BEEP BEEP BEEP")
            guesses += 1
            guess = input("[keypad]> ")


class Awake(MentalState):

    def enter(self):
        pass


class Revenge(MentalState):

    def enter(self):
        pass


class Window(MentalState):

    def enter(self):
        pass


class Finished(MentalState):
    
    def enter(self):
        pass


class Engine(object):
    
    def __init__(self, mental_map):
        self.mental_map = mental_map

    def play(self):
        current_mental_state = self.mental_map.open_mental_state()
        last_mental_state = self.mental_map.next_mental_state('finished')

        while current_mental_state != last_mental_state:
            next_state_name = current_mental_state.enter()
            current_mental_state =\
            self.mental_map.next_mental_state(next_state_name)

        current_mental_state.enter()

class Map(object):

    # Class Attributes
    mental_states = {
        'abyss': Abyss(),
        'dreams': Dreams(),
        'awake': Awake(),
        'revenge': Revenge(),
        'window': Window(),
        'death': Death(),
        'finished': Finished()
    }

    def __init__(self, initial_mental_state='abyss'):
        self.initial_mental_state = initial_mental_state

    def next_mental_state(self):
        pass

    def open_mental_state(self, something):
        pass


if __name__ == "__main__":
    a_game = Map()
#    breakpoint()
