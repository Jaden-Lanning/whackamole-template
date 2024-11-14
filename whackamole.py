import pygame
import random

def draw_grid(screen):
    # horizontal lines
    for i in range(1, 17):
        pygame.draw.line(screen, "black", (0, i * 32), (640, i * 32))
        #vertical lines
    for i in range(1, 21):
        pygame.draw.line(screen, "black", (i * 32, 0), (i * 32, 512))

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512)) #settings screen size
        clock = pygame.time.Clock()
        mole_x, mole_y = 0,0
        mole_rect = mole_image.get_rect(topleft=(mole_x, mole_y))

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click_x, click_y = event.pos
                    #randomizes on click
                    if mole_rect.collidepoint(click_x, click_y):
                        mole_x = random.randrange(0, 640, 32)
                        mole_y = random.randrange(0, 512, 32)
                        mole_rect.topleft = (mole_x, mole_y)
            screen.fill("light green")
            draw_grid(screen) #creates grid
            screen.blit(mole_image, mole_rect)
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()



if __name__ == "__main__":
    main()