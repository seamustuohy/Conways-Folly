#!/usr/bin/env python
from collections import Counter

class game:
    """game class MUST be passed board size conway.board(size)"""
    def __init__(self, size = 50):
        self.board = self.build(size)
    def build(self, size):
        """Creates a list of rows with a cell per column in each row list"""
        col=row=int(size)
        board = [[0] * col for i in range(row)]
        return board
    def change_tile(self, tile, location):
        """Tries to add or replace a tile on the board.

        Takes the tile, as a string, and the location, as a two item list. First checks to see if tile is being removed, and if not makes sure that there is not another tile on that space.
        """
        x,y = location[0],location[1]
        current_tile = self.board[x][y]
        if str(tile)[-1] == '0': #if trying to place a blank tile
            self.board[x][y] = tile
        elif str(current_tile)[-1] == '0': #if the space is already blank
            self.board[x][y] = tile
        else:
            raise UserWarning('This is an illegal tile placement: ' + str(tile) + ' will not be placed at ' + str(loc))

    def evolve(self):
        """cycles thorough each cell and returns a modified board"""
        changed_cells = {}
        for row_index,row in enumerate(self.board):
            for col_index,cell in enumerate(row):
                neighbors = []
                neighbors = get_neighbors(cell, (row_index, col_index))
                evaluated = live_or_die(cell, neighbors)
                if cell != evaluated:
                    changed_cell[evaluated] = (row_index, col_index)
        for cell, loc in changed_cell():
            change_tile(cell, loc)

    def get_neighbors(self, cell, location):
        x, y = location [0], location [1]
        for k in range(-1,2):
            for l in range(-1,2):
                neighbors = []
                if 0 <= x + k <= len(self.board[0]):
                    if 0 <= y + l <= len(self.board[0]):
                        neighbors.append(self.board[x + k][y + l])
        for n in neighbors:
            if n == cell:
                neighbors.remove(n)
                break
        return neighbors


    def live_or_die(self, cell, neighbors):
        count = 0
        for neighbor in neighbors:
            if str(neighbor[-1]) == "1":
                count += 1
            if str(cell[-1]) == "0":
                if count == 3:
                    evolved = common(neighbors)
                    return evolved
                else:
                    return cell
            if str(cell[-1]) == 1:
                if 2 <= count <= 3:
                    return cell
                else:
                    if str(cell[0]) != "1":
                        return str(cell[0]) + "0"
                    else:
                        return 0
        
    def common (self, neighbors):
        neighbors_to_count = (neighbor for neighbor in neighbors if str(neighbor[:-1]) == 1)
        common_list = Counter(neighbors_to_count)
        tie = False
        high_num = 0
        for cell, count in neighbors_to_count():
            if int(count) > int(high_num):
                most_common = x
                tie = False
            elif count == high_num:
                tie = True
        if tie == True:
            return 1
        else:
            return most_common


        
        
class history:
    """takes in the saved game name, and a board from which it pulls out cells != 0 on the board, player names."""
    def __init__(self, game):
        self.archive = []
        self.archive.append(game)
    def save(self, game):
        self.archive.append(game)
