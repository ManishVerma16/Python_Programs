import pygame
pygame.init()
gray=(119, 118, 110)
display_width=800
display_height=600

gameDisplays=pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('car game')
clock = pygame.time.Clock()
carImg = pygame.image.load('car.jpg')

def car(x, y):
    gameDisplays.blit(carImg, (x, y))

def game_loop():
    x = (display_width*0.45)
    y = (display_height*0.8)
    x_change = 0
    bumped=False
    while not bumped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bumped = True
        
        if event.type==pygame.KEYDOWN:
            if event.type == pygame.K_LEFT:
                x_change = -5
            if event.type == pygame.K_RIGH:
                x_change = 5

        gameDisplays.fill(gray)
        car(x, y)
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()