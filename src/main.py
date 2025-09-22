#protypes can implement run_game to test out new functionality to be run with main to simplify testing
import sys
import time
from blackjack import run_game as run_black_jack
from highlow import run_game as run_high_low
from rich.prompt import Prompt
from console import console as c

def print_delay(message="", delay=0, line_end="\n"):
    print(message, end=line_end)
    if delay > 0:
        time.sleep(delay)

"""Application entry point"""
def main():
    c.clear()
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

 Your choice! """

    selection = Prompt.ask(game_instructions, console=c, choices=["1","2"], show_choices=True)
    c.clear()

    #Run main game loop
    match(selection):
        case "1":
            print_delay("High - Low!  Simple and fun!", 2)
            run_high_low()
        case "2":
            print_delay("Blackjack!  A classic!", 2)
            run_black_jack()
    print("Goodbye!")
main()
