#! /usr/bin/env python
import backend
import pygame


def test_board():
    neighbor_board = backend.game(20)
    active_cells = {(0,0):"A1", (0,1):"A1", (0,2):"A1", (0,3):"A1"}
    for x, y in active_cells.items():
        print x, y
        neighbor_board.change_tile(y, x)
    old_board = backend.game(20)
    print "starting game"
    draw_board(old_board.board, neighbor_board.board)


def draw_board(old_board, the_board):
    """draw conways board"""  
    pygame.init()
    players = {"0":(0x000000), "1":(0xFFFFFF), "A":(0x8506A9), "B":(0xD8005F), "C":(0x87EA00), "D":(0xE5FB00)}
    n = len(the_board[0])
    surface_sz = 480
    sq_sz = surface_sz // n
    surface_sz = n * sq_sz
    surface = pygame.display.set_mode((surface_sz, surface_sz))
    cell_offset = cell_size = int(sq_sz / 2)
    
    while True:
        
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break;

        for row_index,row in enumerate(the_board):
            for col_index,cell in enumerate(row):
                if old_board[row_index][col_index] != cell:
                    the_square = (row_index * sq_sz, col_index * sq_sz, sq_sz, sq_sz)
                    print the_square
                    player_id = str(cell)[0]
                    screenc = players[player_id]
                    if int(str(cell)[-1]) == 1:
                        pygame.draw.circle(surface, screenc, (row_index * sq_sz + cell_offset, col_index * sq_sz + cell_offset), cell_size)
                        print cell
                    elif int(str(cell)[-1]) == 0:
                        surface.fill(screenc, the_square)
                        print cell
                    old_board[row_index][col_index] = cell
        pygame.display.flip()
        
if __name__ == "__main__":
    test_board()
    
