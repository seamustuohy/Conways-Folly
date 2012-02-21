#!/usr/bin/env python


class board:
    """board class MUST be passed board size conway.board(size)"""
    def __init__(self, size = 50):
        self.aboard = self.build(size)
    def build(self, size):
        """Creates a list of rows with a cell per column in each row list"""
        col=row=int(size)
        aboard = [[0] * col for i in range(row)]
        return aboard
    def change_tile(self, tile, location):
        """Tries to add or replace a tile on the board.

        Takes the tile, as a string, and the location, as a two item list. First checks to see if tile is being removed, and if not makes sure that there is not another tile on that space.
        """
        x,y = location[0],location[1]
        current_tile = self.aboard[x][y]
        if str(tile)[-1] == '0': #if trying to place a blank tile
            self.aboard[x][y] = tile
        elif str(current_tile)[-1] == '0': #if the space is already blank
            self.aboard[x][y] = tile
        else:
            return "failure"
    def evolve(self):
        """cycles thorough each cell and returns a modified board"""
        changed_board = list(self.aboard)
        for row_index,row in enumerate(self.aboard):
            for col_index,cell in enumerate(row):
                neighbors = []
                neighbors = get_neighbors(row_index, col_index)
                if str(cell)[-1] == '0': #If cell is empty
                    changed_board[row_index][col_index] = reproduce(cell, neighbors)
                else:
                    changed_board[row_index][col_index] = eval_life(cell, neighbors)
        self.aboard = changed_board
        
    def static_board(self, fuck):
        fuck = list(self.aboard)
        return fuck
    
class history:
    """what was supposed to be easy is seemingly quite hard. FUCKING LISTS!"""
    def __init__(self, game):
        self.archive = []
        self.archive.append(game)
    def save(self, game):
        self.archive.append(game)
