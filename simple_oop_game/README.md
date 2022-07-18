# MyGame
> The goal of this game is to escape the BASEMENT by improving your mental health in a such a way, you become strong enough to escape before the clock runs out.  Otherwise you're DEAD.

## SYNOPSIS:

"   You're trapped in a BASEMENT that's flooding with no doors.  Only a WINDOW, with which you may
escape.  You're too weak and stupid to open it right now, though...

It's a Basement that is composed
of heirarchies representing your MENTAL STATE.

   Beginning at the ABYSS level, with minimum HEALTH made up of pHYSICAL,
    MENTAL, and HENRI.  The first enemy you encounter, the Re-Sister, must be
    fought in order to go on to the next MIND STATE, and so on until you
    eventually reach the WINDOW...  There are THREE main BOSSES in which block
    you from escaping the Basement in a timely manner, and a problem to solve
    prior to freeing yourself through the Window. Between the Abyss and the
    Window, you must enter Dreams, Awake, and Revenge, evolving into CONAN, the
    only person strong enough physically and mentally to open the window."

___

*Death*: Player dies, with some "last words"

*Abyss*: Starting point of game, where you have to get beyond "level 1" before
continuing on to different MIND SETS by either READING, EXERCISING or Playing with Henri.  This is where the FIRST "DECISION" (what you decide to do to level up/down and why) is likely to KILL you or LEVEL YOU UP more than the subsequent MentalStates.

*Dreams*: MentalState where player is in a "dream state," battling with
the Leiche_ML Boss, via READING, EXERCISING, PLAYING WITH HENRI

*Awake*: Awaking from the "dream state", only to battle a stronger enemy, where
you will have to BALANCE your health components just right (might mean DRINKING
        VODKA, or something) in order to get to the WINDOW MentalState.

*Revenge*: Mental state that requires battling the MIrror after you find the SWORD and/or GENIUS, without which, you could not open the Window.

*WINDOW*: This is where the HERO (Player) escapes the BASEMENT, but only after
successfully solving a PUZZLE.

___

## EXTRACT KEY CONCEPTS and RESEARCH:
(NOUNS)

- Hero
- Leiche_ML (Mid-Level Boss)
- Basement (world)
- MentalState
- Abyss
- Dreams
- Window
- Re-Sister (Beginner Boss)
- Mirror (Final Boss)
- Death
- Engine
- Map 
- Sword
- Genius
- Puzzle

## Class Heirarchy and Object Map for Concepts:
(*What's similar to other things?*)

* Map
* Engine
* MentalState
    * Death
    * Abyss
    * Dreams
    * Awake
    * Revenge
    * Window

(*VERBS* included):

* Map
    - next_mental_state 
    - entering_mental_state

* Engine
    - play

* MentalState
    - enter
    * Death
    * Abyss
    * Dreams
    * Awake
    * Revenge
    * Window

## Pseudocode: (Skeletal and TOP-DOWN Approach)

class MentalState
    
    def enter


class Engine

    constructor(MAP_OBJECT)
    
    def play


class Death(MentalState)

    def enter


class Abyss(MentalState)

    def enter


class Dreams(MentalState)

    def enter


class Revenge(MentalState)

    def enter


class Window(MentalState)

    def enter


class Map

    constructor(MentalState_Object)

    def next_mental_state

    def open_mental_state


## Repeatand Refine:






