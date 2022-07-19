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
        pass

class Dreams(MentalState):

    def enter(self):
        # Change this to something more interesting and fun
        print(dedent("""
 \n
Proud with your little win, you fall deep asleep...
Falling into an unimaginable HELL some people call
Dreaming...\n where a monster appears charging you!  It's a
damn Lieche_ML!!!! NOOOOOOOO!!!!!\nWhat's this??  She
challenges you to a game of WITS!!\n\n
==================================
Guess the Two-DIgit number:\n
==================================
                     """))
        pass        

class Awake(MentalState):

    def enter(self):
        print("""\n
              ===========================
              This be the Awake state...
              ===========================
              \n""")


class Revenge(MentalState):

    def enter(self):
        print("""
              \n===========================
              This be the Revenge Class...
                ===========================
              \n
              """)


class Window(MentalState):

    def enter(self):
        print("""
              \n
                ===========================
              This be the Window class
                ===========================
              \n""")


class Finished(MentalState):
    
    def enter(self):
        print("""
              \n
                ===========================
              This bet he Finished class
                ===========================
              \n
              """)


class Engine(object):
    
    def __init__(self, mental_map):
        self.mental_map = mental_map

    def play(self):
        pass


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

    def __init__(self, mental_state='abyss'):
        self.mental_state = mental_state

    # Map class stores each mental_state in a Dict
    def next_mental_state(self, mental_state_name): 
        pass

    def open_mental_state(self):
        pass

if __name__ == "__main__":
    a_game = Map()
    engine = Engine(a_game)
    engine.play()





