#libraries / stuff to import

import pygame
import sys
from logic.ui import UIManager

#variables outside of loop
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 360
FPS = 60

class GameEngine:
    def __init__(self):

        pygame.init() # initializing all pygame modules idk which to use yet NTD

        self.gameWindow = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SCALED | pygame.FULLSCREEN ) #single tuple arg idk why exactly, combines fullscreen and upscaling
        pygame.display.set_caption("Percolator: v0.1")

        self.gameClock = pygame.time.Clock()
        self.isRunning = True

        self.uiManager = UIManager() # instantiating ui manager

    def handle_events(self):

        for event in pygame.event.get(): #checks all user inputs

            if event.type == pygame.QUIT:
                self.isRunning = False

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: #[TEMPORARY] pressing escape key exits program as no exit button yet
                self.isRunning = False

            elif event.type == pygame.MOUSEMOTION:
                mousePos = pygame.mouse.get_pos()
                self.uiManager.handle_mouse_move(mousePos)

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mousePos = pygame.mouse.get_pos()
                self.uiManager.handle_click(mousePos)

    def run_game(self):

        while (self.isRunning == True):

            self.handle_events()
            self.gameWindow.fill((230, 226, 220)) #tuple arg again
            self.uiManager.draw(self.gameWindow) # draws cards on gameWindow
            pygame.display.flip()
            self.gameClock.tick(FPS)

        pygame.quit()
        sys.exit()
