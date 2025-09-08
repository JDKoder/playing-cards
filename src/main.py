#protypes can implement run_game to test out new functionality to be run with main to simplify testing
import sys
import time
from blackjack import run_game as run_black_jack
from highlow import run_game as run_high_low

def print_delay(message="", delay=0, line_end="\n"):
    print(message, end=line_end)
    if delay > 0:
        time.sleep(delay)

"""Application entry point"""
def main():
    #todo splash screen
    #todo game select
    skip_intro = False
    if len(sys.argv) > 1:
        skip_intro = not(sys.argv[1] == None)
    if not skip_intro:
        print_delay("I'm so glad you're here!", 3, "\r")
        print_delay("I'd love to play some card games,", 2) 
        print_delay("but it's no fun alone.", 3, "\n\n")
        print_delay("Would you enjoy a game with me?", 3)
    
    game_instructions = """
We can play:

 ( 1 ) High - Low:  Place a bet your card will be higher or lower than the dealer's card 

 ( 2 ) Blackjack:  The classic game where you try to make a hand as close to 21 without going over

 Your choice! (the number next to the game): """

    while True:
        selection = input(game_instructions)
        try:
            selection = int(selection)
        except ValueError:
            print("Sorry, but I only know what I know.", end="\n\n")
            continue
        break

    #Run main game loop
    match(selection):
        case 1:
            print_delay("High - Low! A simple and fun choice!", 2)
            run_high_low()
        case 2:
            print_delay("Blackjack!  I do love the classics!", 2)
            run_black_jack()
    print("Thank you for playing!")
main()
