# #imports
import pygame
from constants import *
from player import *

# Main game 
def main():
    #  initilize imported pygame modules
    pygame.init()

    # create game clock
    clock = pygame.time.Clock()
    dt = 0

    # Create groups
    updatable = pygame.sprite.Group()
    drawable = my_group = pygame.sprite.Group()

    # Add to groups
    Player.containers = (updatable, drawable)

    # Create player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    #  console print stuff at launch
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # start gui
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # start of loop
    while True:
        # Makes windows close button work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #  set screen to black
        screen.fill(000000)

        # rotate player +
        updatable.update(dt)

        # draw player +
        for each in drawable:
            each.draw(screen)

        # update screen
        pygame.display.flip()

        #update gametime
        dt = clock.tick(60) / 1000
                
# Start main if executed, not imported
if __name__ == "__main__":
    main()
