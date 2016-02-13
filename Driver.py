# Author: Sandra
# Assignment: Final Project in Data Structures
# Purpose: To understand stacks better, to create a game similar to the card game Hanoi which is similar the Tower of Hanoi
# Acknowledgements: stackoverflow which I used code from in the function redeal, this helped with the layout of the stacks

from Hanoi import Hanoi
import sys

def main():
    print "Welcome to the card game Hanoi.\nThe object of this game is to move all the cards into a single stack with" \
          " 9 being the top card and 1 being the bottom card.\nThe rules are simple: You can only move one card at a" \
          " time. You can only move cards from the bottom of each stack. You cannot move a higher value card onto a" \
          " lower value card.\nYou can quit the game anytime by entering the word 'quit'.\n"    # instructions on how to play
    play = raw_input("Would you like to play Hanoi (yes or no)? ")
    win = False
    playAgain = 'yes'
    while playAgain == 'yes':
        if play == "no":
            print("Goodbye!")
            sys.exit(0)
            
        else:
            game = Hanoi()
            game.create_dealingPile()
            game.deal()
            
            while win == False:
                print ""
                user_card = raw_input("Which card would you like to move? ")
                game.checkUserCard(user_card)
                user_stack = raw_input("Which stack would you like to move " + user_card + " to (1, 2, or 3)? ")
                game.checkUserStack(user_stack, user_card)
                game.moveCards(user_card, user_stack)
                game.redeal()
                check = game.checkWin()
                
                if check:
                    win = True
                    again = raw_input("Would you like to play again (yes or no)? ")
                    
                    if again == "no":
                        print "I hope you enjoyed playing Hanoi."
                        sys.exit(0)
                    
                    elif again == "yes":
                        win = False
                        game.playAgain(again)
        
        #else:
            #print ("Goodbye!")
            #quit()

main()
