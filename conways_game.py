#!/usr/bin/env python

# import pygame

"""
Seamus Tuohy's multiplayer turn based re-interpretation of John Conway's Game of Life in Python.

A turn based game with evolving pieces and ever increasing time.
"""


LICENSE = """This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>."""

def main():
    """this causes the game_start to run with shell instead of pygame"""
    game_start("shell_board")
    
def game_start(interface = "visual_board"):
    """ sets the basic game interface and functions.

    If called from main(shell) game_ start gets player number and names and game size and passes them to shell_board function. If called any other way it starts visual_board function.
    """
    if interface == visual_board: visual_board()
    else:
        print """Welcome to Conway's Game of Doom!
\nBefore we start I need some things.\n"""
        num_players = int(raw_input("how many people are playing? "))
        players = []
        for player in range(num_players):
            name = raw_input("What is player %s's name? " %int(player+1))
            players.append(name)
#TEST            print players
        while True:
            print "Would you like a 'small', medium', or 'large' game?"
            game_size = raw_input()
            small = ["s","small"]
            medium = ["m", "medium"]
            large = ["l", "large"]
            board = []
            if game_size in small:
                for i in range(10):
                    board.append([' '] * 10)
                return shell_board(board, players, 10)
            elif game_size in medium:
                for i in range(15):
                    board.append([' '] * 15)
                return shell_board(board, players, 15)
            elif game_size in large:
                for i in range(20):
                    board.append([' '] * 20)
                return shell_board(board, players, 20)
            else:
                print "please enter  small, medium, or large or, s, m, or l in lowercase letters"

def visual_board():
    """ the visual pygame interface"""
#TEST    print "visual" 
#TEST    print pygame.ver
#ADD Get Board Size and other settings from PYGAME INTERFACE    

def shell_board(board, players, game_size):
    """ the command line interface"""
#TEST    print "shell"
#TEST    print game_size
#TEST    print players
    columns  = rows = game_size
#TEST    print columns
#TEST    print rows
# creates tiles[rows[]] multi-dimensional array
    for i in range(rows):
        for j in range(columns):
            board[i][j] = '[ ]'
    print "Welcome to Conway's game of DOOM!\n\n"
#TEST    board[4][5] = "[X]"
#    print "+"  + ("-" * (rows - 2)) + "+"
    for k in range(board):
        print str(board[i][j]) + "\n\n"

def evolve():
    """ the evolution phase"""
    print "evolve"
    
def win_condition():
    """checks for a winner"""
    print "board"


if __name__ == "__main__":
    main()
