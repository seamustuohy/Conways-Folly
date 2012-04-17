import os, sys
import pygame
import backend
import game_board
from pygame.locals import *


class conway_main:
    """The controlling function of Conway's Folley: initializes and builds"""

    def __init__(self, width = 680, height = 780):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Conway's Folley")
        c_game = backend.game()
    def main_loop(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE: sys.exit(0)
            self.screen.fill(0,0,0)
            pygame.display.flip()


        
if __name__ == "__main__":
    MainWindow = conway_main()
    MainWindow.main_loop()
    
