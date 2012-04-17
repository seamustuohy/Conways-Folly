import pygame
import backend
def main():
    mygame = gameplay()
    mygame.game_start()

class gameplay:

    def game_start(self):
        pygame.init()
        size = 20
        self.evolver = 0
        self.game = backend.game(size)
        self.old_game = backend.game(size)
        self.board = self.game.new_board(size)
        self.old_board = self.old_game.new_board(size)
        self.temp_cells = []
        self.players = {"0":(0x000000), "1":(0xFFFFFF), "A":(0x8506A9), "B":(0xD8005F), "C":(0x87EA00), "D":(0xE5FB00)}
        self.turns = 1
        self.current_player = "A"
        active_cells = {(5,10):"A1", (15,10):"B1"}
        for x, y in active_cells.items():
            self.game.change_tile(x, y)
        self.draw_board()
        
    def next_turn(self):
        self.temp_cells = []
        if self.current_player == "A":
            "player change to B"
            self.current_player = "B"
        elif self.current_player == "B":
            "Player change to evolve"
            self.evolver = self.turns

    def evolution(self):
        self.game.evolve()
        self.evolver -= 1
        if self.evolver <= 0:
            self.current_player = "A"
            self.turns += 1
        pygame.time.wait(100)

    def notification(self, notification):
        while True:
            ev = pygame.event.poll()
            if ev.type == pygame.QUIT:
                break
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_RETURN:
                    break
            
            note_sz = self.surface_sz // 3
            note = (note_sz, note_sz, note_sz, note_sz)
            surface.fill((255,255,255), note)
            
    def click_check(self, mouse_pos):
        """ take the (x,y) position of the mouse and checks where it is on the game board and assigns a cell accordingly"""
        x,y = mouse_pos[0], mouse_pos[1]
        row = x / self.sq_sz
        col = y / self.sq_sz
        if (row, col) in self.temp_cells:
            temp_temp = []
            for i in self.temp_cells:
                if i != (row, col):
                    temp_temp.append((row, col))
            self.temp_cells = temp_temp
        elif str(self.board[row][col])[-1] == 1:
            notification("on_board")
        elif self.game.super_neighbor(self.current_player, (row, col)) == True:
            self.game.change_tile((row, col), (str(self.current_player) + "1"))
            self.temp_cells.append((row, col))
    
    def draw_board(self):
        """draw conways board"""
        n = len(self.board[0])
        self.surface_sz = 640
        self.sq_sz = self.surface_sz // n
        self.surface_sz = n * self.sq_sz
        surface = pygame.display.set_mode((self.surface_sz, self.surface_sz))
        cell_size = int(self.sq_sz / 2)
        cell_offset = cell_size
        
        while True:
            
            ev = pygame.event.poll()
            if ev.type == pygame.QUIT:
                break;
            elif ( ev.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]):
                self.click_check(pygame.mouse.get_pos()) 
            elif len(self.temp_cells) >= 6:
                self.next_turn()

                
                #is your turn over?
                # if "yes" next item in list player or evolve (p1,p2,p3,evolve(self.board)
                # if "no" temp_buffer[-1].delete and remove that last cell from board
            for row_index,row in enumerate(self.game.board):
                for col_index,cell in enumerate(row):
                    if self.old_board[row_index][col_index] != cell:
                        the_square = (row_index * self.sq_sz, col_index * self.sq_sz, self.sq_sz, self.sq_sz)
                        player_id = str(cell)[0]
                        screenc = self.players[player_id]
                        if int(str(cell)[-1]) == 1 or int(str(cell)[-1]) == "1":
                            surface.fill((0,0,0), the_square)
                            pygame.draw.circle(surface, screenc, (row_index * self.sq_sz + cell_offset, col_index * self.sq_sz + cell_offset), cell_size)
                        elif int(str(cell)[-1]) == 0 or int(str(cell)[-1]) == "0":
                            surface.fill((0,0,0), the_square)
                            pygame.draw.circle(surface, screenc, (row_index * self.sq_sz + cell_offset, col_index * self.sq_sz + cell_offset), cell_size / 6)
                        self.old_board[row_index][col_index] = cell
            pygame.display.flip()
            if self.evolver >= 1:
                self.evolution()
            score = self.game.score()
            
if __name__ == "__main__":
    main()
