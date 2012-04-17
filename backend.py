#!/usr/bin/env python
from collections import Counter

class game:
    """game class MUST be passed board size conway.board(size)"""
    
    def __init__(self, size = None):
        if size == None:
            size = 10
        self.board = self.new_board(size)
        self.players = {}
        self.turn = 0
        self.record = []

    def new_board(self, size):
        """Creates a list of rows with a cell per column in each row list"""
        col=row=int(size)
        board = [[0] * col for i in range(row)]
        return board

    def change_tile(self, location, tile):
        """Tries to add or replace a tile on the board.

        Takes the tile, as a string, and the location, as a two item list. First checks to see if tile is being removed, and if not makes sure that there is not another tile on that space.
        """
        x, y = location[0],location[1]
        current_tile = self.board[x][y]
        if str(tile)[-1] == '0': #if trying to place a blank tile
            self.board[x][y] = tile
        elif str(current_tile)[-1] == '0': #if the space is already blank
            self.board[x][y] = tile

    def evolve(self):
        """cycles thorough each cell and sends changed cells to board() to be populated"""
        changed_cells = {}
        for row_index,row in enumerate(self.board):
            for col_index,cell in enumerate(row):
                neighbors = []
                neighbors = self.get_neighbors((row_index, col_index), cell)
                evaluated = self.live_or_die(cell, neighbors)
                if cell != evaluated:
                    changed_cells[(row_index, col_index)] = evaluated
        self.build(changed_cells)

    def get_neighbors(self, location, cell):
        """gathers and values of all cells surrounding evaluated cell that are on active board (without looping around the board) in a tuple.""" 
        neighbors = []
        x, y = location [0], location [1]
        for k in range(-1,2):
            for l in range(-1,2):
                if 0 <= x + k < len(self.board[0]):
                    if 0 <= y + l < len(self.board[0]):
                        neighbors.append(self.board[x + k][y + l])
        return neighbors

    def super_neighbor(self, cell, location):
        """gathers and values of all cells surrounding evaluated cell that are on active board (without looping around the board) in a tuple and returns True if a neighbor of the same type is around and false if not.""" 
        x, y = location [0], location [1]
        for k in range(-2,3):
            for l in range(-2,3):
                if 0 <= x + k < len(self.board[0]):
                    if 0 <= y + l < len(self.board[0]):
                        neighbor = self.board[x + k][y + l]
                        if str(neighbor)[0] == str(cell)[0]:
                            return True
        return False

    def live_or_die(self, cell, neighbors):
        """compares cell to neighbors and returns final state of cell """
        count = 0
        friends = 0
#        print str(cell)
        if str(cell)[-1] == "1":
            count -= 1
            friends -= 1
        for neighbor in neighbors:
            if str(neighbor)[-1] == "1":
                    count += 1
                    if str(neighbor)[0] == str(cell)[0] or str(neighbor)[0] == "1":
                        friends += 1
#        print str(friends) + " | " + str(count)
        if str(cell)[-1] == "0":
            if count == 3:
                evolved = self.common(cell, neighbors)
                return evolved
            else:
                return cell
        if str(cell)[0] == "1":
            if 2 <= count <= 3:
                return cell
        if str(cell)[-1] == "1" and str(cell)[0] != "1":
            if 2 <= friends <= 3:
                return cell
        if str(cell)[0] != "1":
                return str(cell)[0] + str(0)    
        else:
            return "0"
        
    def common(self, cell, neighbors):
        """Counts the common neighbors around birthing cell and returns live cell based on most common neighbor""" 
        neighbors_to_count = []
        for neighbor in neighbors:
            if str(neighbor)[-1] == "1":
                neighbors_to_count.append(neighbor)
        common_list = Counter(neighbors_to_count)
        tie = False
        high_num = 0
        for cell, num in common_list.items():
            if int(num) > int(high_num):
                most_common = cell
                tie = False
            elif num == high_num:
                tie = True
            if tie == True:
                return 1
            else:
                return most_common
            
    def score(self):
        """counts all player owned cells and return dict with all player_ID's : # of marked cells """ 
        score_card = {}
        total_alive = []
        for row in self.board:
            for cell in row:
                if len(str(cell)) == 2:
                    total_alive.append(cell)
        gathered_points = Counter(total_alive)
        for player, points in gathered_points.iteritems():
            if str(player)[0] in score_card:
                score_card[str(player)[0]] += int(points)
            else:
                score_card[str(player)[0]] = int(points)
        return score_card                      
        
    def add_player(self, name):
        """Adds players to player dictionary and assigns them player_id's """
        if self.player == {}:
            self.player_id = "A"
            self.player[name] = self.player_id 
        else:
            self.player_id = chr(ord(self.player_id) + 1) #Convert Player_id to numerical code point in ASCII then add one and convert back to next higher letter.
            self.player[name] = self.player_id
            
    def build(self, changed_cells, record = True):
        """ populates changed cells  & saves board to game record"""
        for cell, loc in changed_cells.items():
            self.change_tile(cell, loc)
        if self.record == True:
            self.record.append(changed_cells)

    def check_winner(self):
        for row in  board:
            for cell in row:
                if str(cell)[0] not in players:
                    players.append(str(cell)[0])
        if len(players) == 1:
            return False
        else:
            return True
                    
