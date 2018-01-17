import pygame
from pygame.locals import *
## Constants
(WIN_W, WIN_H) = (800, 600) # Window Width and Height

def main():
    pygame.init() # Initialize pygame modules
    screen = pygame.display.set_mode((WIN_W,WIN_H)) # Create Screen
    pygame.display.set_caption("Truck Pirates Ahoy v0.0.1") # Set Window Title

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    font = pygame.font.Font(None, 36)
    text = font.render("Hello There", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    textpos.centery = background.get_rect().centery
    background.blit(text, textpos)

    screen.blit(background, (0,0))
    pygame.display.flip() # This is necessary to draw to the screen
    
    done = False 
    while not done: # Main Loop
        for e in pygame.event.get(): # Gets event e from queue returned by get()
            if e.type == pygame.QUIT: # End loop if quit event is detected
                done = True

        screen.blit(background, (0,0))
        pygame.display.flip() # This is necessary to draw to the screen

    pygame.quit() # Exit program when loop terminates

if __name__ == '__main__': main()
