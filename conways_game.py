#!/usr/bin/env python

from random 
from sys 

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

def draw_board(board, board_size)
    # this function prints out the game board passed to it. It returns None.
    h_line = "  %s" + len(board_size) * "-" + "%s" %(left_side, right_side)
    l_side = "/"
    r_side = "\\"
    print(h_line)
    l_side = "+"
    r_side = "+"
    for y in range(int(board_size)):
        print(y+1, end=" ")
        for x in range (int(board_size)):
            print('| %s' % (board[x][y]), end=" ")
        print("|")
        if x < (int(board_size):
                    print(h_line)
        else:
             l_side = "\\"
             r_side = "/"
             print(h_line)
                
def reset_board(board, board_size):
    # clears all board spaces.
    for x in range(int(board_size)):
        for y in range (int(board_size)):
            board[x][y] = " "
                    
                    
