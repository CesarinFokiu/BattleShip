import pygame
pygame.init()
screen = pygame.display.set_mode([1385, 980])
clock = pygame.time.Clock()

done = False

backgroung = pygame.image.load("playa.JPG").convert()
barco1 = pygame.image.load("barco.PNG").convert()
barco1.set_colorkey([0, 0, 0])
letras = pygame.image.load("letras.PNG").convert()
letras.set_colorkey([0, 0, 0])

cordX = 0
cordY = 99
cordX2 = 1383
cordY2 = 24

speedX = 3
speddy = 3
speedX2 = 3
speddy2 = 3

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    cordX += speedX
    if(cordX2 > 1385):
        speedX2 *= -1

    mousePosition = pygame.mouse.get_pos()
    print(mousePosition)
    x = mousePosition[0]
    y = mousePosition[1]

    screen.blit(backgroung, [0, 0])
    screen.blit(barco1, [cordX, cordY])
    screen.blit(letras, [cordX2, cordY2])

    pygame.display.flip()
    clock.tick(60)

pygame.quit()