# Author: Sandra
# Assignment: Final Project for Data Structures
# Purpose: To understand stacks better, to create a game similar to the card game Hanoi which is similar the Tower of Hanoi
# Started: I modified three functions from the war game, which was the init, create_dealingPile, and the deal function
# Acknowledgements: stackoverflow which I used code from in the function redeal, this helped with the layout of the stacks

from Stack import Stack
import random
from itertools import izip_longest
import sys

class Hanoi:

    def __init__(self):
        self.dealingPile = Stack()  #these 4 variables were some of the variables from Mario's example in the war game
        self.firstStack = Stack()
        self.secStack = Stack()
        self.thirdStack = Stack()

    def create_dealingPile(self):
        """
        Creates a "dealing pile" which consists of 9 "cards" or numbers
        """
        deck = []
        for card in range(1, 10):
            deck.append(card)  # append 9 "cards" or numbers to the deck
        random.shuffle(deck)
        for i in range(len(deck)):   # used this section of code for big O analysis
            self.dealingPile.push(deck[i])
        # print deck                     # for testing purposes
        # print self.dealingPile.size()  # for testing purposes

    def deal(self):
        """
        This function "deals" out the "cards" or numbers into three different stacks and outputs the result to the screen
        for the user to see.
        """
        length = self.dealingPile.size()
        for i in range(length):    # for length of the dealingPile
            card = self.dealingPile.pop()  # pop the first number in the dealingPile
            if i%3 == 0:                     # this was how I split the 9 cards into three different stacks
                self.thirdStack.push(card)
            elif i%2 == 0:
                self.secStack.push(card)
            else:
                self.firstStack.push(card)
        # print self.firstStack.size()       #these three lines were for testing purposes
        # print self.secStack.size()
        # print self.thirdStack.size()
        for i in range(self.firstStack.size()):
            print self.firstStack.items[i],   # print each item in each stack one by one, side by side on the same line
            print " ",
            print self.secStack.items[i],
            print " ",
            print self.thirdStack.items[i]
            i+=1

    def checkUserCard(self, usr_card):
        """
        This function validates the user input for which card/number to move
        """
        numbers = []      # the list numbers will be used to check only the bottom numbers of each stack and compare it
                          # to the user's input
        if self.firstStack.size() != 0:
            numbers.append(str(self.firstStack.top()))
        if self.secStack.size() != 0:
            numbers.append(str(self.secStack.top()))
        if self.thirdStack.size() != 0:
            numbers.append(str(self.thirdStack.top()))
        if usr_card.lower() == "quit":
            print "Goodbye!"
            sys.exit(0)
        if usr_card not in numbers:
            usr_card = raw_input("Which card would you like to move (%s)? "% " ".join(numbers))
            self.checkUserCard(usr_card)    # call the function again if the user's input does not match the numbers
        else:
            return

    def checkUserStack(self, usr_stack, usr_card):
        """
        This function validates the user input for which stack to move the chosen card to
        """
        stackNum = ['1', '2', '3']   # this list will be used to compare the user's input
        if usr_stack.lower() == "quit":
            print "Goodbye!"
            sys.exit(0)
        if usr_stack not in stackNum:
            usr_stack = raw_input("Which stack would you like to move %s to (1, 2, or 3)? "%usr_card)
            self.checkUserStack(usr_stack, usr_card)    # call the function again if the user's input does not match
        else:
            return

    def moveCards(self, usr_card, usr_stack):
        """
        This function moves the card to a stack specified by the user
        """
        usr_card = int(usr_card)
        usr_stack = int(usr_stack)
        # print usr_stack   # for testing purposes
        if usr_card in self.firstStack.items:  # if the user's card is in the first stack (assuming it is a bottom card)
            popped = self.firstStack.pop()     # remove it and put it into the stack specified by the user
            if usr_stack == 1:
                self.firstStack.push(popped)
                print self.firstStack.items
            elif usr_stack == 2:
                self.secStack.push(popped)
                print self.secStack.items
            else:
                self.thirdStack.push(popped)
                print self.thirdStack.items
        elif usr_card in self.secStack.items:
            popped = self.secStack.pop()
            if usr_stack == 1:
                self.firstStack.push(popped)
                print self.firstStack.items
            elif usr_stack == 2:
                self.secStack.push(popped)
                print self.secStack.items
            else:
                self.thirdStack.push(popped)
                print self.thirdStack.items
        else:
            popped = self.thirdStack.pop()
            if usr_stack == 1:
                self.firstStack.push(popped)
                print self.firstStack.items
            elif usr_stack == 2:
                self.secStack.push(popped)
                print self.secStack.items
            else:
                self.thirdStack.push(popped)
                print self.thirdStack.items

    def redeal(self):
        """
        Function "redeals" the card after moving the cards
        """
        # layout = [self.firstStack.items, self.secStack.items, self.thirdStack.items]
        # print layout          this line and the above line were for testing purposes
        for a, b, c in izip_longest(self.firstStack.items, self.secStack.items, self.thirdStack.items, fillvalue=""):
            print "{0:1s}\t{1:1s}\t{2:1s}".format(str(a), str(b), str(c))
        # acquired the above code starting with the for loop from:
        # http://stackoverflow.com/questions/6802877/how-to-print-a-table-from-lists-with-different-lengths-in-python
        # this code creates pairs of elements in each list/stack and prints them in separate columns
            # if there is not an element to match in another list/stack, then the empty space is filled with ""

    def checkWin(self):
        """
        This function checks to see if the user won
        """
        winNum = [9, 8, 7, 6, 5, 4, 3, 2, 1]   # list is used to compare the stacks to
        if self.firstStack.size() == 9:    # first, check to see if a stack has a size of 9
            if self.firstStack.items == winNum:   # if so, then check to see if the stack is equal to winNum
                print "Congratulations! You won!"  # if it is, then the user won
                return True
        elif self.secStack.size() == 9:
            if self.secStack.items == winNum:
                print "Congratulations! You won!"
                return True
        elif self.thirdStack.size() == 9:
            if self.thirdStack.items == winNum:
                print "Congratulations! You won!"
                return True
        else:
            return False           # return false if the user has not won yet

    def playAgain(self, usr_play):
        if usr_play == "yes":
            self.create_dealingPile()
            self.deal()
