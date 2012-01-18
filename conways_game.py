#!/usr/bin/env python

import random
from collections import Counter
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
    """The main function that starts the game from the shell"""
    print """\n\nWelcome to Conway's Game of Doom!\n\nBefore we start I need some things.\n"""
    
    players, board = setup_game()
    history = []
    start_phase(players, board, history)
    
def setup_game():
    players = shuffle_players(request_players())
    size = request_size()
    board = build_board_matrix(size)
    print "%s will go first" %(players[0])
    print_board(board)
    return players, board

def start_phase(players, board, history):
    players, modified_board = play_phase(players, board)
    history.append(modified_board)
    print "done with that shit"
#    evolve(modified_board, len(history))

def request_players():
    num_players = int(raw_input("how many people are playing? "))
    players = []
    for player in range(num_players):
        name = raw_input("What is player %s's name? " %int(player+1))
        players.append(name)
    return players

def build_board_matrix(board_size):
    """creates empty board."""
    columns  = rows = board_size
    # creates tiles[rows[]] multi-dimensional array
    board = []
    board = [[" "] * int(columns) for i in range(rows)]
    return board

def request_size():
    """Requests game size from user."""
    while True:
        print "Would you like a 'small', medium', or 'large' game?"
        game_size = raw_input()
        small = ["s","small"]
        medium = ["m", "medium"]
        large = ["l", "large"]
        if game_size in small:
            board_size = 10
            return board_size
        elif game_size in medium:
            board_size = 20
            return board_size
        elif game_size in large:
            board_size = 25
            return board_size
        else:
            print "please enter  small, medium, or large or, s, m, or l in lowercase letters"

def shuffle_players(players):
    """randomly chooses first player and return's order"""
    random.shuffle(players,random.random)
    return players

def print_board(board):
    size = len(board)
    print "",
    for i in range(size):
        print "  " + "%02d" %(i),
    print "\n"
    for y in range(size):
        print "%02d" %(y),
        for x in range(size):
            print "[%s] " %(board[x][y]),
        print "\n"


def play_phase(players, board):
    finished_players = []
    player_num = 1
    modified_board = board
    finished = ""
    for player in players:
        player, player_num, modified_board = place_tile(player, player_num, modified_board)
        finished_players.append(player)
    print "play phase complete"
    return finished_players, modified_board



def place_tile(player, player_num, board):
    i = 1
    token = ""
    while i < 6:
        x, y, tile_type = get_space()
        if tile_type == "f":
            token = "O"
        else: token = player_num
        while board[x][y] != " ":
            print "That space is taken. Please choose again."
            x, y = get_space()
        modified_board = add_to_board(x, y, token, board)
        i += 1
    print player + ", player number " + str(player_num) + ", completed his turn."
    player_num += 1
    return player, player_num, modified_board

def get_space():
    tile_type = raw_input("Would you like an aggressive or a friendly tile?\n f = friendly, a = aggressive")
    print "and, where would you like it?"
    x = int(raw_input("what column?"))
    y = int(raw_input("what row?"))
    return x, y, tile_type

def add_to_board(x, y, player_num, board):
    board[x][y] = str(player_num)
    modified_board = board
    print_board(modified_board)
    return modified_board


def RUINED_evolve(board, turn):
    """ the evolution phase"""
    live_neighbors = []
    friends = 0
    modified_board = board
    size = len(board)
    for col in range(size):
        for row in range(size):
            this_cell = board[col][row]
            live_neighbors = []
            for k in range(-1,2):
                for l in range(-1,2):
                    try:
                        if modified_board[col + k][row +l] != " ":
                            live_neighbors.append(modified_board[col + k][row +l])
                    except IndexError: continue
                    if 1 >= len(live_neighbors) >= 4:
                        modified_board[col][row] = " "
            else:
                for i in live_neighbors:
                    if i == " " or modified_board[col][row]:
                        friends += 1
                    if 2 >= friends >=3:
                        modified_board[col][row] = " "
            friends = 0
            live_neighbors = []
    return modified_board

def new_evolve(board, turn):
    modified_board = board
    live_neighbors = 0
    size = len(board)
    for col in range(size):
        for row in range(size):
            this_cell = board[col][row]
            for k in range(-1,2):
                for l in range(-1,2):
                    try:
                        if modified_board[col + k][row +l] == ['a']:
                            live_neighbors += 1
                    except IndexError: continue
                    if this_cell == "a":
                        live_neighbors -=1
            print "%s has %s live neighbors" %(this_cell, live_neighbors)
            live_neighbors = 0
            
            
    return modified_board

def evolve(board, turn):
    modified_board = board
    for cell in board:
        neighbors = count_neighbors(cell, board)
        if board[cell] == " " and len(neighbors) == 3:
            count = Counter()
            for i in neighbors: count[i] += 1
#            if count
#            modified_board[cell] = count[0]

def count_neighbors(cell, board):
    num_neighbors = []
    neighbors = [ (cell[0]-1,cell[1]), (cell[0]-1,cell[1]-1),
                  (cell[0],cell[1]-1), (cell[0]+1,cell[1]-1),
                  (cell[0]+1,cell[1]), (cell[0]+1,cell[1]+1),
                  (cell[0],cell[1]+1), (cell[0]-1,cell[1]+1) ]
    for neighbor in neighbors:
        if neighbor in board.keys():
            num_neighbors.append(neighbor)
    return num_neighbors

def win_condition():
    """checks for a winner"""
    print "board"


if __name__ == "__main__":
    main()
