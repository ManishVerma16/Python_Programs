import pygame
pygame.init()
gray=(119, 118, 110)
display_width=800
display_height=600

gameDisplays=pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('car game')
clock = pygame.time.Clock()

def game_loop():
    bumped=False
    while not bumped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bumped = True
        
        gameDisplays.fill(gray)
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()