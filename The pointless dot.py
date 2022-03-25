import pygame

pygame.init()

white = (255 , 255, 255)
black = (0 , 0 , 0)

Width = 600
Height = 600

screen = pygame.display.set_mode((Width,Height))
pygame.display.set_caption('The pointless dot')

clock = pygame.time.Clock()

x = 300
y = 300
 
x_change = 0       
y_change = 0

run = True
speed = 10

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -10
                y_change = 0
            elif event.key == pygame.K_RIGHT:
                x_change = 10
                y_change = 0
            elif event.key == pygame.K_UP:
                y_change = -10
                x_change = 0
            elif event.key == pygame.K_DOWN:
                y_change = 10
                x_change = 0
            elif event.key == pygame.K_s:
                speed = int(input("speed ?"))
                
    x += x_change
    y += y_change

    if x > Width:
        x = 10
    elif y > Height:
        y = 10
    elif x < 0:
        x = Width - 10
    elif y < 0:
        y = Height - 10

    pygame.draw.rect(screen,white, [x, y, 10, 10])

    pygame.display.update()

    screen.fill(black)

    clock.tick(speed)

pygame.quit() 