#!/usr/bin/env python

import random
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
    players = shuffle_players(player_select())
    board = game_size(board_size())
    print players
    
def player_select():
    print """Welcome to Conway's Game of Doom!
\nBefore we start I need some things.\n"""
    num_players = int(raw_input("how many people are playing? "))
    players = []
    for player in range(num_players):
        name = raw_input("What is player %s's name? " %int(player+1))
        players.append(name)
    return players

def game_size(board_size):
    """creates empty board."""
    columns  = rows = board_size
    # creates tiles[rows[]] multi-dimensional array
    board = []
    for i in range(rows):
        board.append([" "] * int(columns))
    return board

def board_size():
    """Requests game size from user."""
    while True:
        print "Would you like a 'small', medium', or 'large' game?"
        game_size = raw_input()
        small = ["s","small"]
        medium = ["m", "medium"]
        large = ["l", "large"]
        if game_size in small:
            board_size = 20
            return board_size
        elif game_size in medium:
            board_size = 30
            return board_size
        elif game_size in large:
            board_size = 40
            return board_size
        else:
            print "please enter  small, medium, or large or, s, m, or l in lowercase letters"

def shuffle_players(players):
    """randomly chooses first player and return's order"""
    random.shuffle(players,random.random)
    return players
    

def evolve():
    """ the evolution phase"""
    print "evolve"
    
def win_condition():
    """checks for a winner"""
    print "board"


if __name__ == "__main__":
    main()
